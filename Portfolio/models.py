from django.db import models


class Enquiry(models.Model):
    first_name = models.CharField('First name', default="", max_length=50)
    last_name = models.CharField('Last name', default="", max_length=50)
    email = models.CharField("Phone number", default="", max_length=50)
    company = models.CharField('High school', default="", max_length=50)

    def __str__(self):
        return self.company
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_company(self):
        return self.company
