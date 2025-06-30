from django.db import models

class Stakeholder(models.Model):
    # Basic Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    
    # Additional Fields from Excel
    partnership_model = models.CharField(max_length=100, blank=True)
    relation_model = models.CharField(max_length=100, blank=True)
    relevance_priority = models.CharField(max_length=50, blank=True)
    stakeholder_segment = models.CharField(max_length=100, blank=True)
    stakeholder_sub_sector = models.CharField(max_length=100, blank=True)
    technology_expertise = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    annual_turnover = models.CharField(max_length=100, blank=True)
    number_of_employees = models.IntegerField(null=True, blank=True)
    projected_market_entry = models.CharField(max_length=50, blank=True)
    engagement_status = models.CharField(max_length=50, blank=True)
    outreach_manager = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    contact_role = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    potential_relationships = models.TextField(blank=True)
    actual_relationships = models.TextField(blank=True)
    potential_activities = models.TextField(blank=True)
    actual_activities = models.TextField(blank=True)
    tools_collaterals = models.TextField(blank=True)
    expected_outcomes = models.TextField(blank=True)

    def __str__(self):
        return self.name