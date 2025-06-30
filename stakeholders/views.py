from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
import csv
import io
from .models import Stakeholder
from .forms import StakeholderForm

def stakeholder_list(request):
    stakeholders = Stakeholder.objects.all()
    return render(request, 'stakeholders/stakeholder_list.html', {'stakeholders': stakeholders})

def stakeholder_detail(request, pk):
    stakeholder = get_object_or_404(Stakeholder, pk=pk)
    return render(request, 'stakeholders/stakeholder_detail.html', {'stakeholder': stakeholder})

def stakeholder_new(request):
    if request.method == "POST":
        form = StakeholderForm(request.POST)
        if form.is_valid():
            stakeholder = form.save()
            return redirect('stakeholder_detail', pk=stakeholder.pk)
    else:
        form = StakeholderForm()
    return render(request, 'stakeholders/stakeholder_edit.html', {'form': form})

def stakeholder_edit(request, pk):
    stakeholder = get_object_or_404(Stakeholder, pk=pk)
    if request.method == "POST":
        form = StakeholderForm(request.POST, instance=stakeholder)
        if form.is_valid():
            stakeholder = form.save()
            return redirect('stakeholder_detail', pk=stakeholder.pk)
    else:
        form = StakeholderForm(instance=stakeholder)
    return render(request, 'stakeholders/stakeholder_edit.html', {'form': form})

def stakeholder_delete(request, pk):
    stakeholder = get_object_or_404(Stakeholder, pk=pk)
    stakeholder.delete()
    return redirect('stakeholder_list')

def export_stakeholders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stakeholders.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'Name', 'Email', 'Phone', 'Organization', 'Role', 'Notes',
        'Partnership Model', 'Relation Model', 'Relevance / Priority',
        'Stakeholder Segment', 'Stakeholder Sub-sector', 'Stakeholder Technology Expertise',
        'Stakeholder Location', 'Stakeholder Annual Turnover (USD)', 'Stakeholder Number of Employees',
        'Projected Year of Market Entry', 'Engagement Status', 'Ark Vertical Outreach Manager',
        'Stakeholder Contact Person', 'Stakeholder Contact Role', 'Stakeholder Contact Number',
        'Stakeholder Contact Email', 'Stakeholder Website', 'Potential Stakeholder Relationship(s)',
        'Actual Stakeholder Relationship(s)', 'Potential Engagement Activities',
        'Actual Engagement Activities', 'Tools & Collaterals', 'Expected Outcomes'
    ])
    
    stakeholders = Stakeholder.objects.all()
    for stakeholder in stakeholders:
        writer.writerow([
            stakeholder.name, stakeholder.email, stakeholder.phone, stakeholder.organization, 
            stakeholder.role, stakeholder.notes, stakeholder.partnership_model, stakeholder.relation_model,
            stakeholder.relevance_priority, stakeholder.stakeholder_segment, stakeholder.stakeholder_sub_sector,
            stakeholder.technology_expertise, stakeholder.location, stakeholder.annual_turnover,
            stakeholder.number_of_employees, stakeholder.projected_market_entry, stakeholder.engagement_status,
            stakeholder.outreach_manager, stakeholder.contact_person, stakeholder.contact_role,
            stakeholder.contact_number, stakeholder.contact_email, stakeholder.website,
            stakeholder.potential_relationships, stakeholder.actual_relationships,
            stakeholder.potential_activities, stakeholder.actual_activities,
            stakeholder.tools_collaterals, stakeholder.expected_outcomes
        ])
    
    return response

def import_stakeholders_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        # Check if it's a CSV file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return redirect('import_stakeholders_csv')
        
        # Process the file
        try:
            # Read the file
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            
            # Get the header row to map columns
            reader = csv.reader(io_string, delimiter=',')
            header = next(reader)
            
            # Create a mapping of column names to indices
            column_mapping = {}
            for i, column in enumerate(header):
                clean_column = column.strip().lower()
                if 'name' in clean_column and 'contact' not in clean_column:
                    column_mapping['name'] = i
                elif 'email' in clean_column and 'contact' not in clean_column:
                    column_mapping['email'] = i
                elif 'phone' in clean_column and 'contact' not in clean_column:
                    column_mapping['phone'] = i
                elif 'organization' in clean_column:
                    column_mapping['organization'] = i
                elif 'role' in clean_column and 'contact' not in clean_column:
                    column_mapping['role'] = i
                elif 'notes' in clean_column:
                    column_mapping['notes'] = i
                elif 'partnership model' in clean_column:
                    column_mapping['partnership_model'] = i
                elif 'relation model' in clean_column:
                    column_mapping['relation_model'] = i
                elif 'relevance' in clean_column or 'priority' in clean_column:
                    column_mapping['relevance_priority'] = i
                elif 'segment' in clean_column:
                    column_mapping['stakeholder_segment'] = i
                elif 'sub-sector' in clean_column or 'subsector' in clean_column:
                    column_mapping['stakeholder_sub_sector'] = i
                elif 'technology' in clean_column and 'expertise' in clean_column:
                    column_mapping['technology_expertise'] = i
                elif 'location' in clean_column:
                    column_mapping['location'] = i
                elif 'turnover' in clean_column:
                    column_mapping['annual_turnover'] = i
                elif 'employees' in clean_column:
                    column_mapping['number_of_employees'] = i
                elif 'market entry' in clean_column:
                    column_mapping['projected_market_entry'] = i
                elif 'engagement status' in clean_column:
                    column_mapping['engagement_status'] = i
                elif 'outreach manager' in clean_column:
                    column_mapping['outreach_manager'] = i
                elif 'contact person' in clean_column:
                    column_mapping['contact_person'] = i
                elif 'contact role' in clean_column:
                    column_mapping['contact_role'] = i
                elif 'contact number' in clean_column:
                    column_mapping['contact_number'] = i
                elif 'contact email' in clean_column:
                    column_mapping['contact_email'] = i
                elif 'website' in clean_column:
                    column_mapping['website'] = i
                elif 'potential' in clean_column and 'relationship' in clean_column:
                    column_mapping['potential_relationships'] = i
                elif 'actual' in clean_column and 'relationship' in clean_column:
                    column_mapping['actual_relationships'] = i
                elif 'potential' in clean_column and 'activities' in clean_column:
                    column_mapping['potential_activities'] = i
                elif 'actual' in clean_column and 'activities' in clean_column:
                    column_mapping['actual_activities'] = i
                elif 'tools' in clean_column or 'collaterals' in clean_column:
                    column_mapping['tools_collaterals'] = i
                elif 'expected' in clean_column and 'outcomes' in clean_column:
                    column_mapping['expected_outcomes'] = i
            
            # Process each row
            success_count = 0
            error_count = 0
            
            for row in reader:
                # Skip empty rows
                if not any(row):
                    continue
                    
                # Ensure we have at least name and email
                if 'name' in column_mapping and 'email' in column_mapping and \
                   len(row) > max(column_mapping['name'], column_mapping['email']):
                    
                    # Create a defaults dictionary with all available fields
                    defaults = {'name': row[column_mapping['name']]}
                    
                    # Add all other fields if they exist in the mapping and row
                    field_mapping = {
                        'phone': 'phone',
                        'organization': 'organization',
                        'role': 'role',
                        'notes': 'notes',
                        'partnership_model': 'partnership_model',
                        'relation_model': 'relation_model',
                        'relevance_priority': 'relevance_priority',
                        'stakeholder_segment': 'stakeholder_segment',
                        'stakeholder_sub_sector': 'stakeholder_sub_sector',
                        'technology_expertise': 'technology_expertise',
                        'location': 'location',
                        'annual_turnover': 'annual_turnover',
                        'number_of_employees': 'number_of_employees',
                        'projected_market_entry': 'projected_market_entry',
                        'engagement_status': 'engagement_status',
                        'outreach_manager': 'outreach_manager',
                        'contact_person': 'contact_person',
                        'contact_role': 'contact_role',
                        'contact_number': 'contact_number',
                        'contact_email': 'contact_email',
                        'website': 'website',
                        'potential_relationships': 'potential_relationships',
                        'actual_relationships': 'actual_relationships',
                        'potential_activities': 'potential_activities',
                        'actual_activities': 'actual_activities',
                        'tools_collaterals': 'tools_collaterals',
                        'expected_outcomes': 'expected_outcomes'
                    }
                    
                    for csv_field, model_field in field_mapping.items():
                        if csv_field in column_mapping and len(row) > column_mapping[csv_field]:
                            # Handle special case for number_of_employees which is an integer field
                            if csv_field == 'number_of_employees':
                                try:
                                    value = row[column_mapping[csv_field]].strip()
                                    if value:
                                        defaults[model_field] = int(value)
                                except ValueError:
                                    # If conversion fails, skip this field
                                    pass
                            else:
                                defaults[model_field] = row[column_mapping[csv_field]]
                    
                    try:
                        # Use email as unique identifier
                        email = row[column_mapping['email']]
                        if email:  # Only process if email is not empty
                            _, created = Stakeholder.objects.update_or_create(
                                email=email,
                                defaults=defaults
                            )
                            if created:
                                success_count += 1
                            else:
                                # Updated an existing record
                                success_count += 1
                    except Exception as row_error:
                        error_count += 1
                else:
                    error_count += 1
            
            if success_count > 0:
                messages.success(request, f'Successfully imported {success_count} stakeholders.')
            if error_count > 0:
                messages.warning(request, f'Could not import {error_count} rows due to missing or invalid data.')
            if success_count == 0 and error_count == 0:
                messages.warning(request, 'No data was imported. Please check your CSV file format.')
                
        except Exception as e:
            messages.error(request, f'Error importing file: {str(e)}')
        
        return redirect('stakeholder_list')
    
    return render(request, 'import_stakeholders.html')