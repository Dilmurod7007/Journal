from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from pharma import settings

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    organization = models.ForeignKey("Organization", on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(_('Yaratilgan sana'), auto_now_add=True)
    updated_at = models.DateTimeField(_('O\'zgartirilgan sana'), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)





class Organization(models.Model):
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    facs_number = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    issn = models.CharField(max_length=150)
    top = models.BooleanField(default=False)
    number_table = models.IntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    description = RichTextField()
    work = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/authors/', blank=True, null=True)
    count_author = models.IntegerField(default=0)
    downloadview = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Jurnal(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    downloadview = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    pdf_file = models.FileField(upload_to='media')
    keyword = models.CharField(max_length=250)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='organization_subdivision', blank=True, null=True)
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    facs_number = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/', blank=True)
    issn = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    position = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.name


class Statya(models.Model):
    lang = (
        ("UZ", "UZ"),
        ("RU", "RU"),
        ("EN", "EN"),
    )

    author = models.ManyToManyField(Author, related_name="article_author")
    jurnal = models.ForeignKey(Jurnal, on_delete=models.CASCADE, related_name="journal_article")
    name = models.CharField(max_length=250)
    language = models.CharField(max_length=2, choices=lang,default="UZ")
    downloadfile = models.FileField(upload_to='media')
    downloadview = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date = models.DateField()
    keyword = models.CharField(max_length=250)
    archive = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Conference(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    email = models.EmailField()
    date = models.DateField()
    sponsor = models.CharField(max_length=250, blank=True, null=True)
    archive = models.BooleanField(default=False)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Seminar(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=500)
    fio = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextField()
    link = models.URLField()
    linkbutton = models.CharField(max_length=50)
    phon_number = models.CharField(max_length=13)
    date = models.DateField()
    sponsor = models.CharField(max_length=250, blank=True, null=True)
    archive = models.BooleanField(default=False)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=250)
    organization = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/', blank=True)
    views = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.title


class Video_Gallery(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    videourl = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='images/', blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phon_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    organization = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=150)
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = RichTextField()

    def __str__(self):
        return self.question


class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button = models.CharField(max_length=20)
    video_banner = models.FileField(upload_to='media', blank=True, null=True)
    link = models.URLField(max_length=200)
    login_text = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Webcontact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    facebook = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.phone



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




