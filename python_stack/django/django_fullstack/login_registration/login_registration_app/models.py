from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        curr_date = datetime.today() - relativedelta(years=13)
        new_date = datetime.strptime(postData['birthday'], '%Y-%m-%d')
        if users: 
            errors['existing_user'] = 'email already tied to existing account'
        if len(postData['first_name']) < 2:
            errors['first_name'] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "last name should be at least 2 characters"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'password does not match confirmation password'
        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 characters'
        if new_date > curr_date:
            errors['birthday'] = 'User must be at least 13 to register'
        return errors
    def login_validator(self, postData):
        errors = {}
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255, null= 'TRUE')
    birthday = models.DateField(null='TRUE')
    objects = UserManager()

    def __repr__(self):
        return f"<Show Information: {self.first_name} ({self.id})>"
