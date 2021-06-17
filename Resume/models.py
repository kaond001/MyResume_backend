from django.db import models
# from django.contrib .auth.models import User


class Contact(models.Model):
    full_name = models.CharField(max_length=60)
    area = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, default='')
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

class Testimonials(models.Model):
    message = models.CharField(max_length=255)
    user = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

class Skills(models.Model):
    skill_name = models.CharField(max_length=255)
    percentage = models.CharField(max_length=60)
    color_code = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    institute_name = models.CharField(max_length=255)
    programm = models.CharField(max_length=60)
    Year_of_graduate = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

class Home(models.Model):
    heading = models.CharField(max_length=60)
    summary = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

class Media(models.Model):
    icon = models.CharField(max_length=60)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)