from rest_framework import serializers
from . import models
from django.db.models import Sum


class SubdivisionSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'facs_number', 'email', 'website', 'logo', )
        model = models.Subdivision



class OrganizationSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', )
        model = models.Organization





class OrganizationSerializer(serializers.ModelSerializer):
    subdivisions = SubdivisionSerializer(many=True, source='organization_subdivision')

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'facs_number', 'email', 'website',
                  'image', 'logo', 'issn', 'top', 'number_table', 'subdivisions')
        model = models.Organization


class AuthorSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en')
        model = models.Author




class AuthorSerializer(serializers.ModelSerializer):
    count_download = serializers.CharField(write_only=True)
    count_article = serializers.CharField(write_only=True)

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'surname_uz', 'surname_ru', 'surname_en', 'family_name_uz', 'family_name_ru', 'family_name_en', 'description_uz', 'description_ru', 'description_en', 'work_uz', 'work_ru', 'work_en', 'count_author', 'count_download', 'count_article', 'image')
        model = models.Author

    def to_representation(self, instance):
        article = models.Statya.objects.filter(author__id=instance.id).aggregate(Sum('downloadview'))
        count_article = models.Statya.objects.filter(author__id=instance.id).count()
        data = super().to_representation(instance)
        data['count_download'] = article["downloadview__sum"]
        data['count_article'] = str(count_article)
        return data


class StatyaSerializer(serializers.ModelSerializer):
    jurnal = serializers.StringRelatedField()
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'author', 'name', 'jurnal', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', )
        model = models.Statya


class StatyaforAuthorSerializer(serializers.ModelSerializer):
    jurnal = serializers.StringRelatedField()
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'author', 'name', 'jurnal', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', )
        model = models.Statya


class AuthorDetailSerializer(serializers.ModelSerializer):
    count_download = serializers.CharField(write_only=True)
    count_article = serializers.CharField(write_only=True)
    articles = StatyaforAuthorSerializer(many=True, source='article_author')

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'surname_uz', 'surname_ru', 'surname_en', 'family_name_uz', 'family_name_ru', 'family_name_en', 'description_uz', 'description_ru', 'description_en', 'work_uz', 'work_ru', 'work_en', 'count_author', 'count_download', 'count_article', 'articles', 'image')
        model = models.Author

    def to_representation(self, instance):
        article = models.Statya.objects.filter(author__id=instance.id).aggregate(Sum('downloadview'))
        count_article = models.Statya.objects.filter(author__id=instance.id).count()
        data = super().to_representation(instance)
        data['count_download'] = article["downloadview__sum"]
        data['count_article'] = str(count_article)
        return data


class JurnalDetailSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    articles = StatyaSerializer(many=True, source='journal_article')

    class Meta:
        fields = ('id','organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword_uz', 'keyword_ru', 'keyword_en', 'image', 'articles', )
        model = models.Jurnal



class JurnalSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()


    class Meta:
        fields = ('id','organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword', 'image' )
        model = models.Jurnal



class ConferenceSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        fields = ('id', 'organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'date', 'sponsor_uz', 'sponsor_ru', 'sponsor_en', 'email','archive' )
        model = models.Conference
    



class SeminarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'link', 'linkbutton_uz', 'linkbutton_ru', 'linkbutton_en', 'phon_number', 'date', 'sponsor_uz', 'sponsor_ru', 'sponsor_en', 'archive', )
        model = models.Seminar



class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'photo', 'organization', 'views', 'date', )
        model = models.Video


class Video_GallerySerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        fields = ('id', 'video', 'videourl', 'title', )
        model = models.Video_Gallery


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'date', 'photo', 'views', )
        model = models.News



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number', 'email', 'message', 'organization', 'lavozim', )
        model = models.Contact


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question_uz', 'question_ru', 'question_en', 'answer_uz', 'answer_ru', 'answer_en',)
        model = models.Faq




class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title_uz', 'title_ru', 'title_en', 'subtitle_uz', 'subtitle_ru', 'subtitle_en', 'button_uz', 'button_ru', 'button_en', 'video_banner', 'link', 'login_text')
        model = models.Banner


class WebcontactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('phone', 'email', 'address_uz', 'address_ru', 'address_en', 'facebook', 'instagram', 'telegram', 'youtube')
        model = models.Webcontact

