from django.db import models

# Create your models here.
class Patient_info(models.Model):
    Male = 'M'
    Female = 'F'
    Gender_Choices = (
        (Male, 'Male'),
           (Female, 'Female'),
           )
    hospitalNo = models.CharField(max_length=120, blank=True, null=True, unique=True )
    surname = models.CharField(max_length=120, blank=True, null=True)
    othernames = models.CharField(max_length=120, blank=True, null=True)
    data_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=False, choices =  Gender_Choices)
    email = models.CharField(max_length=120, blank=True, null=True, unique= True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    #updated_on = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    occupation = models.CharField(max_length=120, blank=True, null=True)
    state_of_origin = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    tribe = models.CharField(max_length=120, blank=True, null=True)
    religion = models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural ="Patient_info"

    def __self__(self):
        return self.surname
class patient_pic(models.Model):
    personal_info = models.OneToOneField(Patient_info, on_delete=models.CASCADE)
    image = models.ImageField()
    class Meta:
        verbose_name_plural ="patient_pic"
class Rank(models.Model):
    personal_info = models.OneToOneField(Patient_info, on_delete=models.CASCADE)
    name_of_service = models.CharField(max_length=120, blank=True, null=True)
    rank_name =models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural ="Rank"

class Address(models.Model):
    personal_info = models.ForeignKey(Patient_info, on_delete=models.CASCADE)
    street_no = models.CharField(max_length=120, blank=True, null=True)
    street_name = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    lga = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural ="Address"
    def __self__(self):
        return self.street_no
    
class Next_of_kin(models.Model):
    personal_info = models.OneToOneField(Patient_info, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=120, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    relationship = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural ="Next_of_kin"
    def __self__(self):
        return self.fullName
class Unit(models.Model):
    personal_info = models.ForeignKey(Patient_info, on_delete=models.CASCADE)
    Command = models.CharField(max_length=120, blank=True, null=True)
    presentUnit = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural ="Unit"
    def __self__(self):
        return self.presentUnit