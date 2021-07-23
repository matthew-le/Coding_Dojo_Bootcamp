from django.db import models
import re 

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
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
        return errors
    def login_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        if len(postData['email']) < 1:
            errors['email'] = 'email cannot be blank'
        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 characters'
        return errors

class WishManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['item']) < 3:
            errors['item'] = 'A wish must consist of at least 3 characters!'
        if len(postData['desc']) < 3:
            errors['desc'] = 'A description must be provided!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


    def __repr__(self):
        return f"<Show Information: {self.first_name} ({self.id})>"

class Wish(models.Model):
    item = models.CharField(max_length=255)
    desc = models.TextField()
    granted = models.BooleanField()
    creator = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE, null=True)
    users_who_liked = models.ManyToManyField(User, related_name='wishes_user_liked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()