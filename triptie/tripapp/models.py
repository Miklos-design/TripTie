from django.db import models

# Create your models here.

# ready to edit

# table for users
class users(models.Model):
    userEmail = models.EmailField()
    userPassword = models.CharField()



    
# table for user profile 


class userProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    Gender_Choices = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    userEmail = models.EmailField()
    userPassword = models.CharField()
    userAvatar = models.ImageField()
    userID = models.IntegerField()
    userAge = models.IntegerField()
    userGender = models.CharField(max_length = 1, choices = Gender_Choices)
    userBio = models.CharField()

# table for posting a trip on the app

class postTrip(models.Model):
    visibility_choices = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    tripID = models.IntegerField()
    userID = models.IntegerField()
    title = models.CharField()
    visibility = models.CharField(max_length=7, choices=visibility_choices)
    cityName = models.CharField()
    startDate = models.DateField()
    endDate = models.DateField()

# table for posting a picture on the app

class postPicture(models.Model):
    tripID = models.IntegerField()
    pictureURL = models.URLField()

# table of giving likes to the post

class likeTable(models.Model):
    userID = models.IntegerField()
    tripID = models.IntegerField()
    createdTime = models.TimeField()

# table for commenting on the post

class postComment(models.Model):
    userID = models.IntegerField()
    tripID = models.IntegerField()
    createdTime = models.TimeField()
    comment = models.CharField()




