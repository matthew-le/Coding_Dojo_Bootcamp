from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        curr_date = datetime.today() - relativedelta(years=13)
        new_date = datetime.strptime(postData['birthday'], '%Y-%m-%d')
        if users: 
            errors['existing_user'] = 'email already tied to existing account'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = ("Invalid email address!")
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
        users = User.objects.filter(email=postData['email'])
        if len(postData['email']) < 1:
            errors['email'] = 'email cannot be blank'
        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 characters'

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'Title needs to be at least one character'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description needs to be at least 5 characters'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255, null= 'TRUE')
    birthday = models.DateField(null='TRUE')
    created_at = models.DateTimeField(auto_now_add=True, null='TRUE')
    updated_at = models.DateTimeField(auto_now=True, null='TRUE')
    objects = UserManager()


    def __repr__(self):
        return f"<Show Information: {self.first_name} ({self.id})>"

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    users_who_favorited = models.ManyToManyField(User, related_name='books_user_favorited')
    created_at = models.DateTimeField(auto_now_add=True, null='TRUE')
    updated_at = models.DateTimeField(auto_now=True, null='TRUE')
    objects = BookManager()