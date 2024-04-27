from django.db import models

# Create your models here.

class SimpleEnquiry(models.Model):
    """
    Simple enquiry model - get in touch with us type form
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class FullEnquiry(models.Model):
    """
    Full enquiry model - full enquiry form. Contains much more information
    about the child in question.
    """

    # Child's details
    child_name = models.CharField(max_length=255)
    child_date_of_birth = models.DateField()
    child_gender = models.CharField(max_length=10)
    child_primary_language = models.CharField(max_length=255)
    child_secondary_languages = models.CharField(max_length=255)

    child_strengths = models.TextField()
    child_interests = models.TextField()
    child_things_important = models.TextField()

    # Enquirer's details
    enquirer_name = models.CharField(max_length=255)
    enquirer_relationship = models.CharField(max_length=255)
    enquirer_email = models.EmailField(max_length=255) 
    enquirer_phone = models.CharField(max_length=10)
    enquirer_primary_language = models.CharField(max_length=255)
    enquirer_secondary_languages = models.CharField(max_length=255)

    # Primary support 1 details
    primary_support_1_name = models.CharField(max_length=255)
    primary_support_1_address = models.TextField()
    primary_support_1_phone = models.CharField(max_length=10)
    primary_support_1_email = models.EmailField(max_length=255)
    primary_support_1_relationship = models.CharField(max_length=255)

    # Primary support 2 details
    primary_support_2_name = models.CharField(max_length=255)
    primary_support_2_address = models.TextField()
    primary_support_2_phone = models.CharField(max_length=10)
    primary_support_2_email = models.EmailField(max_length=255)
    primary_support_2_relationship = models.CharField(max_length=255)

    # Goals
    expression = models.BooleanField()
    reception = models.BooleanField()
    articulation = models.BooleanField()
    social = models.BooleanField()
    participation = models.BooleanField()
    mealtimes = models.BooleanField()
    stuttering = models.BooleanField()
    other_goals = models.TextField()

    # When did you notice your child needed help
    noticed_help_needed = models.TextField()

    # Medical history
    diagnosis_primary = models.CharField(max_length=255)
    diagnoses_secondary = models.CharField(max_length=255)
    additional_info = models.TextField()

    # other therapies
    occupational = models.BooleanField()
    psychology = models.BooleanField()
    speech_other = models.BooleanField()
    physio = models.BooleanField()
    other_therapies = models.TextField()

    # Family history
    family_history = models.TextField()

    # education & day care info
    day_care_name = models.CharField(max_length=255)
    day_care_contact = models.TextField()

    school_name = models.CharField(max_length=255)
    school_contact = models.TextField()
    school_year = models.IntegerField()
    teacher = models.CharField(max_length=255)

    # Therapy services
    home_therapy = models.BooleanField()
    school_therapy = models.BooleanField()
    support_to_access_activity = models.BooleanField()
    parent_coaching = models.BooleanField()

    # Preferred days for therapy
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()

    # Funding
    private = models.BooleanField()
    ndis_self_managed = models.BooleanField()
    ndis_plan_managed = models.BooleanField()

    # NDIS info
    ndis_number = models.CharField(max_length=255)
    plan_manager_name = models.CharField(max_length=255)
    plan_manager_email = models.EmailField(max_length=255)