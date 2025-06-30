from django import forms
from .models import Stakeholder

class StakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = (
            # Basic Information
            'name', 'email', 'phone', 'organization', 'role', 'notes',
            # Additional Fields
            'partnership_model', 'relation_model', 'relevance_priority',
            'stakeholder_segment', 'stakeholder_sub_sector', 'technology_expertise',
            'location', 'annual_turnover', 'number_of_employees',
            'projected_market_entry', 'engagement_status', 'outreach_manager',
            'contact_person', 'contact_role', 'contact_number', 'contact_email',
            'website', 'potential_relationships', 'actual_relationships',
            'potential_activities', 'actual_activities', 'tools_collaterals',
            'expected_outcomes'
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add placeholders and classes to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter stakeholder name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['organization'].widget.attrs['placeholder'] = 'Enter organization name'
        self.fields['role'].widget.attrs['placeholder'] = 'Enter role/position'
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Set choices for dropdown fields based on Excel data
        self.fields['stakeholder_segment'].widget = forms.Select(choices=[
            ('', 'Select Segment'),
            ('Government & Regulatory', 'Government & Regulatory'),
            ('Academic Institutions', 'Academic Institutions'),
            ('Private Sector & OEMs', 'Private Sector & OEMs'),
            ('Development Institutions', 'Development Institutions'),
            ('Innovation Ecosystem', 'Innovation Ecosystem'),
            ('Media & Influencers', 'Media & Influencers'),
            ('General Public', 'General Public'),
        ])
        
        self.fields['engagement_status'].widget = forms.Select(choices=[
            ('', 'Select Status'),
            ('Engaged', 'Engaged'),
            ('Not engaged', 'Not engaged'),
            ('In progress', 'In progress'),
        ])
        
        self.fields['relevance_priority'].widget = forms.Select(choices=[
            ('', 'Select Priority'),
            ('1', '1 - Highest'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5 - Lowest'),
        ])
        
        # Make text areas larger
        for field_name in ['notes', 'potential_relationships', 'actual_relationships', 
                          'potential_activities', 'actual_activities', 'tools_collaterals', 
                          'expected_outcomes']:
            self.fields[field_name].widget.attrs['rows'] = 3