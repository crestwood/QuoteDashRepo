from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if not postData['first_name'].isalpha():
            errors['first_name'] = 'First name contains non-alpha characters.'
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name should be at least 3 characters.'
        if len(postData['first_name']) >= 255:
            errors['first_name'] = 'First name should be less than 255 characters.'
        if not postData['last_name'].isalpha():
            errors['last_name'] = 'Last name contains non-alpha characters.'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name should be at least 3 characters.'
        if len(postData['last_name']) >= 255:
            errors['last_name'] = 'Last name should be less than 255 characters.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        if User.objects.filter(email = postData['email']):
            errors['email'] = 'Email already exists.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match.'
        return errors

    def editvalidator(self, postData):
        errors = {}
        if not postData['first_name'].isalpha():
            errors['first_name'] = 'First name contains non-alpha characters.'
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name should be at least 3 characters.'
        if len(postData['first_name']) >= 255:
            errors['first_name'] = 'First name should be less than 255 characters.'
        if not postData['last_name'].isalpha():
            errors['last_name'] = 'Last name contains non-alpha characters.'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name should be at least 3 characters.'
        if len(postData['last_name']) >= 255:
            errors['last_name'] = 'Last name should be less than 255 characters.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        if User.objects.filter(email = postData['email']):
            errors['email'] = 'Email already exists.'
        return errors








class QuoteManager(models.Manager):
    def quoteValidator(self,postData):
        errors = {}
        if len(postData['author']) > 20:
            errors['author'] = 'Authors name should be at least 4, but less than 20 characters long.'
        if len(postData['author']) < 3:
            errors['author'] = 'Authors name should be at least 3, but less than 20 characters long.'
        if len(postData['quote']) >= 255:
            errors['quote'] = 'Quote should be at least 10, but less than 255 characters long.'
        if len(postData['quote']) < 10:
            errors['quote'] = 'Quote should be at least 10, but less than 255 characters long.'
        # if Item.objects.filter(name = postData['item_name']):
        #     errors['item_name'] = 'Item already exists.'
        return errors


class User(models.Model): #has to be capitals
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now = True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    objects = UserManager()

    def __repr__(self):
        return "<User object: {} | {}>".format(self.first_name,self.last_name)

class Quotes(models.Model): #has to be capitals
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name = 'creates')
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now = True) 
    liked_by = models.ManyToManyField(User, related_name="likes")
    likecount =  models.IntegerField(null=True)

    objects = QuoteManager()
    def __repr__(self):
        return "<Quotes object: {} | {} | {}>".format(self.quote,self.posted_by,self.liked_by)
