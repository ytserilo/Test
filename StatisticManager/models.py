from django.db import models

# Create your models here.
class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user_id = models.IntegerField(unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    ip_address = models.CharField(max_length=15, unique=True)

class UserStatistic(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField()

    page_views = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
