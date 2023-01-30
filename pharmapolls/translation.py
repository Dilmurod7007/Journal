from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'adress', )


@register(models.Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'family_name', 'description', 'work', )


@register(models.Jurnal)
class JurnalTranslationOptions(TranslationOptions):
    fields = ('author', 'organization', 'name', 'description', 'keyword',)


@register(models.Subdivision)
class SubdivisionTranslationOptions(TranslationOptions):
    fields = ('organization', 'name', 'description', 'adress', )


@register(models.Conference)
class ConferenceTranslationOptions(TranslationOptions):
    fields = ('organization', 'name', 'description', 'adress', 'sponsor',)


@register(models.Seminar)
class SeminarTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'linkbutton', 'sponsor',)


@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(models.Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer', )


@register(models.Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button',)


@register(models.Webcontact)
class WebcontactTranslationOptions(TranslationOptions):
    fields = ('address', )

