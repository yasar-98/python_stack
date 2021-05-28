from django.db import models
import re	# the regex module

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Letters_REGEX = re.compile(r'^[a-zA-Z]+$')

        if len(postData['first_name']) < 2 or not Letters_REGEX.match(postData['first_name']):    # test whether a field matches the pattern            
                errors["first_name"] = " first_name should be at least 2 letters"
        if len(postData['last_name']) < 2 or not Letters_REGEX.match(postData['last_name']):    # test whether a field matches the pattern            
                errors["last_name"] = " last_name should be at least 2 letters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = " passwordd should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    passwd= models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager()   

class Post(models.Model):
    post_message= models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager()   

class Comment(models.Model):
    comment_message= models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)    
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager()   


class Car(models.Model):
    name = models.CharField(max_length=255)
    model= models.IntegerField()
    clients= models.ManyToManyField(User,related_name="cars")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

def create_user(first_name,last_name,email,passwd):
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,passwd=passwd)

def get_user(email):
    users= User.objects.filter(email=email)
    if len(users)>0:
        return users[0]
    return None

def get_users_cars(id):
    user= User.objects.get(id=id)
    return user.cars.all()