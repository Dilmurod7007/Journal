from django.contrib import admin
from . import models
from .models import Organization, Author, Jurnal, Subdivision, Statya, Conference, News, Faq, Banner, Webcontact
from modeltranslation.admin import TranslationAdmin


class VidioInline(admin.StackedInline):
    model = models.Video_Gallery


class VideoGallerys(admin.ModelAdmin):

    inlines = [VidioInline]


@admin.register(models.Conference)
class ConferanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'archive']



@admin.register(models.Seminar)
class ConferanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'archive']


class OrganizationAdmin(TranslationAdmin):
    model = Organization


class AuthorAdmin(TranslationAdmin):
    model = Author


class JurnalAdmin(TranslationAdmin):
    model = Jurnal
    list_display = ['id', 'name', 'organization']


class ArticleAdmin(TranslationAdmin):
    model = Statya
    list_display = ['id', 'name', 'jurnal', 'date']


class SubdivisionAdmin(TranslationAdmin):
    model = Subdivision


class NewsAdmin(TranslationAdmin):
    model = News


class FaqAdmin(TranslationAdmin):
    model = Faq


class BannerAdmin(TranslationAdmin):
    model = Banner


class WebcontactAdmin(TranslationAdmin):
    model = Webcontact


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email',  'is_active']



admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Jurnal, JurnalAdmin)
admin.site.register(models.Statya, ArticleAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Subdivision, SubdivisionAdmin)
admin.site.register(models.Video, VideoGallerys,)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Banner, BannerAdmin)
admin.site.register(models.Faq, FaqAdmin)
admin.site.register(models.Webcontact, WebcontactAdmin)



