from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

# Create your models here.
class MessageManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors['content'] = 'Message needs to be at least one character'
        return errors

class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors['content'] = 'Comment needs to be at least one character'
        return errors


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
        return errors
    def edit_validator(self, postData, user_id):
        errors = {}
        curr_date = datetime.today() - relativedelta(years=13)
        new_date = datetime.strptime(postData['birthday'], '%Y-%m-%d')
        users = User.objects.filter(email=postData['email'])
        # user_tie_to_email = users[0]
        if users: 
            my_user = User.objects.get(id=user_id)
            # if my_user.email != user_tie_to_email:
            if my_user.email != users[0].email:
                errors['email'] = 'email is already in user'
            else: 
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
        else: 
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

class Message(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name='messages_user_liked')
    created_at = models.DateTimeField(auto_now_add=True, null='TRUE')
    updated_at = models.DateTimeField(auto_now=True, null='TRUE')
    objects = MessageManager()

class Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE, null='TRUE')
    users_who_liked = models.ManyToManyField(User, related_name='comments_user_liked')
    created_at = models.DateTimeField(auto_now_add=True, null='TRUE')
    updated_at = models.DateTimeField(auto_now=True, null='TRUE')
    objects = CommentManager()