from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CreatingUsers(BaseUserManager):
    def create_user(self, username, firstname, secondname, email, password=None):
        if not username:
            raise ValueError('User must have username')
        if not email:
            raise ValueError('User must have email')
        if not firstname:
            raise ValueError('User must have at least first name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            secondname=secondname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, firstname, secondname, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            secondname=secondname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Accounts(AbstractBaseUser):
    username = models.CharField(max_length=40, unique= True)
    firstname = models.CharField(max_length=40)
    secondname = models.CharField(max_length=40)
    email = models.EmailField(max_length=150, unique=True)
    phonenumber = models.CharField(max_length=20, unique=True)

    #parameters
    date_signed = models.DateTimeField(auto_now_add=True)
    date_logged = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_isactive = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'secondname', 'username']

    objects = CreatingUsers()

    def __str__(self):
        return  self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True