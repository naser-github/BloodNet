from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class Division(models.Model):
    name = models.CharField(unique=True, max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(unique=True, max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Thana(models.Model):
    name = models.CharField(unique=True, max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BloodGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40, null=True, unique=True, db_index=True)
    address = models.TextField(max_length=200, null=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)

    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True)
    can_donate = models.BooleanField(default=True)

    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class DonationHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    donation_date = models.DateField()

    # def __str__(self):
    #     return self.date


class Hospital(models.Model):
    name = models.CharField(unique=True, max_length=100)
    address = models.TextField(null=True, max_length=300)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, null=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    contact_no = models.CharField(max_length=40)
    is_published = models.BooleanField(default=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)
