from django.db import models
from datetime import datetime
from django.utils import timezone

class Info(models.Model):
    photo = models.ImageField(upload_to='upload/', default='upload/no_img.png', null=True)
    first_name = models.CharField('First name', default="", max_length=50)
    last_name = models.CharField('Last name', default="", max_length=50)
    address = models.TextField('Address', default="", max_length=255)
    about_me = models.TextField('About me', default="", max_length=300)
    interest = models.TextField('Interest', default="", max_length=300)
    phone_number = models.CharField("Phone number", default="", max_length=10)
    high_school = models.CharField('High school', default="", max_length=50)
    high_school_gpa = models.FloatField('High school gpa', default=0.00, max_length=4)
    university = models.CharField('University', default="", max_length=30)
    department = models.CharField('Department', default="", max_length=30)
    faculty = models.CharField('Faculty', default="", max_length=30)
    university_gpa = models.FloatField('University gpa', default=0.00, max_length=4)

    def __str__(self):
        return self.first_name
    
    def get_photo(self):
        return self.photo
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address
    
    def get_about_me(self):
        return self.about_me
    
    def get_interest(self):
        return self.interest
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_high_school(self):
        return self.high_school
    
    def get_high_school_gpa(self):
        return self.high_school_gpa
    
    def get_university(self):
        return self.university
    
    def get_department(self):
        return self.department
    
    def get_faculty(self):
        return self.faculty
    
    def get_unversity_gpa(self):
        return self.unversity_gpa