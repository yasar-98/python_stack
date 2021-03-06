from django.db import models
import re	# the regex module
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Letters_REGEX = re.compile(r'^[a-zA-Z]+$')
        user_birthday = datetime.strptime(postData['birthday'], '%Y-%m-%d')

        if len(postData['first_name']) < 2 or not Letters_REGEX.match(postData['first_name']):    # test whether a field matches the pattern            
                errors["first_name"] = "Blog first_name should be at least 2 letters"
        if len(postData['last_name']) < 2 or not Letters_REGEX.match(postData['last_name']):    # test whether a field matches the pattern            
                errors["last_name"] = "Blog last_name should be at least 2 letters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "Blog passwordd should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if user_birthday > datetime.today() - relativedelta(years=13):
            errors["release_date"] = "User must be at least 13"
        return errors

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    passwd= models.CharField(max_length=255)
    birthday= models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager()   



class Car(models.Model):
    name = models.CharField(max_length=255)
    model= models.IntegerField()
    clients= models.ManyToManyField(User,related_name="cars")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

def create_user(first_name,last_name,email,birthday,passwd):
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,birthday=birthday,passwd=passwd)

def get_user(email):
    users= User.objects.filter(email=email)
    if len(users)>0:
        return users[0]
    return None

def get_users_cars(id):
    user= User.objects.get(id=id)
    return user.cars.all()