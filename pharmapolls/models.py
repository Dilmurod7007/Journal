from ckeditor.fields import RichTextField
from django.db import models


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
    count_author = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Jurnal(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    downloadview = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    pdf_file = models.FileField(upload_to='media')
    keyword = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='organization_subdivision')
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    facs_number = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/', blank=True)

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

    def __str__(self):
        return self.name


class Conference(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    email = models.EmailField()
    date = models.DateField()
    sponsor = models.CharField(max_length=250)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Seminar(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    link = models.URLField()
    linkbutton = models.CharField(max_length=50)
    phon_number = models.CharField(max_length=13)
    date = models.DateField()
    sponsor = models.CharField(max_length=250)
    archive = models.BooleanField(default=False)

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
    videourl = models.URLField()
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

    def __str__(self):
        return self.title


class Webcontact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.phone
