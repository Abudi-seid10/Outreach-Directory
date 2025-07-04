# Generated by Django 4.2.23 on 2025-06-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='actual_activities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='actual_relationships',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='annual_turnover',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='contact_role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='engagement_status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='expected_outcomes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='number_of_employees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='outreach_manager',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='partnership_model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='potential_activities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='potential_relationships',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='projected_market_entry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='relation_model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='relevance_priority',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='stakeholder_segment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='stakeholder_sub_sector',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='technology_expertise',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='tools_collaterals',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
