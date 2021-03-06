import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


# Create your models here.


class JobonicUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class JobonicUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    company = models.ForeignKey('jobonicEntity.Entity', default=None, blank=True, null=True, on_delete=models.SET_NULL)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    uuid_info = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_activated = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_joined = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = JobonicUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    # def clean(self):
    #     super(JobonicUser, self).clean()
    #     self.email = self.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(JobonicUser, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    phone = models.CharField(unique=True, max_length=15)
    birth_date = models.DateField(blank=True, null=True)
    # user_type = models.CharField(max_length=15, choices=[('Admin', 'Administrator'), ('Recruit', 'Recruiter'), ('seeker', 'Job Seeker')], default='seeker')
    phone = models.CharField(max_length=11, blank=True)
    facebook = models.CharField(max_length=70, blank=True)
    twitter = models.CharField(max_length=70, blank=True)
    linkedIn = models.CharField(max_length=70, blank=True)
    score = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)




