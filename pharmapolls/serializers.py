import datetime
from rest_framework import serializers
from . import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
import json


class SubdivisionSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'facs_number', 'email', 'website', 'logo', 'image', 'issn')
        model = models.Subdivision
        read_only_fields = ['organization', ]
        order_by = ['position', ]


    def create(self, validated_data):
        subdivision = models.Subdivision.objects.create(**validated_data)
        subdivision.organization = self.context['request'].user.organization
        subdivision.save()
        return subdivision


    def update(self, instance, validated_data):

        for i in validated_data:
            setattr(instance, i, validated_data[i])
        
        instance.save()
        return instance




class OrganizationSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'phon_number', 'issn', 'adress')
        model = models.Organization





class OrganizationSerializer(serializers.ModelSerializer):
    subdivisions = serializers.SerializerMethodField()
    subdivision_position = serializers.CharField(write_only=True)

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'facs_number', 'email', 'website',
                  'image', 'logo', 'issn', 'top', 'number_table', 'subdivisions', 'subdivision_position')
        model = models.Organization
        read_only_fields = ['top', 'number_table']



    def get_subdivisions(self, instance):
        subdivisions = models.Subdivision.objects.filter(organization=instance).order_by('position')
        return SubdivisionSerializer(subdivisions, many=True, read_only=True, context={"request": self.context.get("request")}).data


    def update(self, instance, validated_data):
        subdivision_position = json.loads(validated_data.get('subdivision_position'))
        for i in subdivision_position['subdivision_position']:
            subdivision = models.Subdivision.objects.get(id=i['id'], organization=self.context['request'].user.organization)
            subdivision.position = i['position']
            subdivision.save()

        for i in validated_data:
            setattr(instance, i, validated_data[i])
        instance.save()
        return instance




class AuthorSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en')
        model = models.Author




class AuthorSerializer(serializers.ModelSerializer):
    count_download = serializers.CharField(write_only=True, required=False)
    count_article = serializers.CharField(write_only=True, required=False)

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'surname_uz', 'surname_ru', 'surname_en', 'family_name_uz', 'family_name_ru', 'family_name_en', 'description_uz', 'description_ru', 'description_en', 'work_uz', 'work_ru', 'work_en', 'count_author', 'count_download', 'count_article', 'image', 'created_by')
        model = models.Author

    def to_representation(self, instance):
        article = models.Statya.objects.filter(author__id=instance.id).aggregate(Sum('downloadview'))
        count_article = models.Statya.objects.filter(author__id=instance.id).count()
        data = super().to_representation(instance)
        data['count_download'] = article["downloadview__sum"]
        data['count_article'] = str(count_article)
        return data

    def create(self, validated_data):
        author = models.Author.objects.create(**validated_data)
        author.created_by = self.context['request'].user
        author.save()
        return author



class AuthorForUserSearchSerializer(serializers.ModelSerializer):
    fio_uz = serializers.SerializerMethodField()
    fio_ru = serializers.SerializerMethodField()
    fio_en = serializers.SerializerMethodField()


    def get_fio_uz(self, obj):
        return f'{obj.name_uz} {obj.surname_uz} {obj.family_name_uz}'

    def get_fio_ru(self, obj):
        return f'{obj.name_ru} {obj.surname_ru} {obj.family_name_ru}'    

    def get_fio_en(self, obj):
        return f'{obj.name_en} {obj.surname_en} {obj.family_name_en}'      

    class Meta:
        model = models.Author
        fields = ['id', 'fio_uz', 'fio_ru', 'fio_en']



class StatyaSearchSerializer(serializers.ModelSerializer):
    author = AuthorSearchSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'author', 'name', 'date', 'keyword', )
        model = models.Statya


class ArticleListForSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statya
        fields = ['id', 'name_uz', 'name_ru', 'name_en']




class ArticleForeignKeySerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        organization = self.context['request'].user.organization
        return models.Jurnal.objects.filter(organization=organization)


class ArticleUpdateCreateSerializer(serializers.ModelSerializer):
    jurnal = ArticleForeignKeySerializer()
    author_ids = serializers.CharField(write_only=True)
    # date = serializers.CharField(write_only=True)
    # author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = ['name_uz', 'name_ru', 'name_en', 'date', 'language', 'keyword', 'jurnal', 'downloadfile', 'author_ids']
        model = models.Statya
        extra_kwargs = {'name': {'required': False}} 


    def update(self, instance, validated_data):
        try:
            author = validated_data.pop("author_ids")
            author = author.split(',')
            instance.author.clear()
            print(author)
            for i in author:
                instance.author.add(i)
                
            
        except:
            pass

        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")
        # instance.date = new_date
        for i in validated_data:
            setattr(instance, i, validated_data[i])
        
        instance.save()
        return instance

    def create(self, validated_data):
        language = validated_data.pop("language")
        journal = validated_data.get("jurnal")
        author = validated_data.pop("author_ids")

        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")


        article_data={
        "name_uz":validated_data.pop('name_uz'), 
        "name_ru":validated_data.pop('name_ru'),
        "name_en":validated_data.pop('name_en'),
        "date": validated_data.pop("date"),
        "language": language,
        "keyword": validated_data.pop('keyword'),
        "jurnal": journal,
        "downloadfile": validated_data.pop('downloadfile'),
        } 

        article = models.Statya.objects.create(**article_data)
        author = author.split(',')
        for i in author:
            article.author.add(i)

        return article



class StatyaSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)
    jurnal_uz = serializers.StringRelatedField(source='jurnal.name_uz')
    jurnal_ru = serializers.StringRelatedField(source='jurnal.name_ru')
    jurnal_en = serializers.StringRelatedField(source='jurnal.name_en')


    class Meta:
        fields = ('id', 'author', 'name_uz', 'name_ru', 'name_en', 'jurnal_uz', 'jurnal_ru', 'jurnal_en', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', 'archive')
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



class UserJournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jurnal
        fields = ['id', 'name_uz', 'name_ru', 'name_en']



class JurnalSearchSerializer(serializers.ModelSerializer):
    organization = OrganizationSearchSerializer()

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'date', 'keyword', 'organization')
        model = models.Jurnal



class JurnalUpdateCreateSerializer(serializers.ModelSerializer):
    # date = serializers.CharField(write_only=True)


    class Meta:
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'pdf_file', 'keyword_uz', 'keyword_ru', 'keyword_en', 'image', 'date']
        model = models.Jurnal
        extra_kwargs = {'name': {'required': False}} 

    def update(self, instance, validated_data):
        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")
        # instance.date = new_date

        for i in validated_data:
            setattr(instance, i, validated_data[i])
        instance.save()
        return instance

    def create(self, validated_data):
        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")
        journal_data={
        "name_uz":validated_data.pop('name_uz'), 
        "name_ru":validated_data.pop('name_ru'),
        "name_en":validated_data.pop('name_en'),
        "description_uz":validated_data.pop("description_uz"),
        "description_ru":validated_data.pop("description_ru"),
        "description_en":validated_data.pop("description_en"),
        "pdf_file":validated_data.pop("pdf_file"),
        "keyword_uz":validated_data.pop("keyword_uz"),
        "keyword_ru":validated_data.pop("keyword_ru"),
        "keyword_en":validated_data.pop("keyword_en"),
        "image":validated_data.pop("image"),
        "date": validated_data.pop("date"),
        "organization": self.context['request'].user.organization
        } 

        journal = models.Jurnal.objects.create(**journal_data)


        return journal



class JurnalSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()


    class Meta:
        fields = ('id','organization', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword', 'image' )
        model = models.Jurnal



class ConferenceSearchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en')
        model = models.Conference





class ConferenceSerializer(serializers.ModelSerializer):
    organization_uz = serializers.StringRelatedField(source='organization.name_uz')
    organization_ru = serializers.StringRelatedField(source='organization.name_ru')
    organization_en = serializers.StringRelatedField(source='organization.name_en')


    class Meta:
        fields = ('id', 'organization_uz', 'organization_ru', 'organization_en', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en', 'adress_uz', 'adress_ru', 'adress_en', 'phon_number', 'date', 'sponsor_uz', 'sponsor_ru', 'sponsor_en', 'email','archive', 'views' )
        model = models.Conference
        read_only_fields = ['sponsor_uz', 'sponsor_ru', 'sponsor_en', 'views', 'archive', 'organization']


    def create(self, validated_data):
        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")
        conference_data={
        "name_uz":validated_data.pop('name_uz'), 
        "name_ru":validated_data.pop('name_ru'),
        "name_en":validated_data.pop('name_en'),
        "description_uz":validated_data.pop("description_uz"),
        "description_ru":validated_data.pop("description_ru"),
        "description_en":validated_data.pop("description_en"),
        "adress_uz":validated_data.pop("adress_uz"),
        "adress_ru":validated_data.pop("adress_ru"),
        "adress_en":validated_data.pop("adress_en"),
        "phon_number":validated_data.pop("phon_number"),
        "date":validated_data.pop("date"),
        "email":validated_data.pop("email"),
        "organization": self.context['request'].user.organization
        } 

        seminar = models.Conference.objects.create(**conference_data)
        return seminar




class SeminarSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', )
        model = models.Seminar





class SeminarSerializer(serializers.ModelSerializer):
    organization_uz = serializers.StringRelatedField(source='organization.name_uz')
    organization_ru = serializers.StringRelatedField(source='organization.name_ru')
    organization_en = serializers.StringRelatedField(source='organization.name_en')

    class Meta:
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'organization_uz', 'organization_ru', 'organization_en', 'fio_uz', 'fio_ru', 'fio_en', 'description_uz', 'description_ru', 'description_en', 'link', 'linkbutton_uz', 'linkbutton_ru', 'linkbutton_en', 'phon_number', 'date', 'sponsor_uz', 'sponsor_ru', 'sponsor_en', 'archive', 'views')
        model = models.Seminar
        read_only_fields = ['sponsor_uz', 'sponsor_ru', 'sponsor_en', 'views', 'archive', 'description_uz', 'description_ru', 'description_en']

    def create(self, validated_data):
        # date = datetime.datetime.strptime(validated_data.pop("date"), '%d.%m.%Y').date()
        # new_date = date.strftime("%Y-%d-%m")
        seminar_data={
        "name_uz":validated_data.pop('name_uz'), 
        "name_ru":validated_data.pop('name_ru'),
        "name_en":validated_data.pop('name_en'),
        "link":validated_data.pop("link"),
        "linkbutton_uz":validated_data.pop("linkbutton_uz"),
        "linkbutton_ru":validated_data.pop("linkbutton_ru"),
        "linkbutton_en":validated_data.pop("linkbutton_en"),
        "phon_number":validated_data.pop("phon_number"),
        "fio_uz":validated_data.pop("fio_uz"),
        "fio_ru":validated_data.pop("fio_ru"),
        "fio_en":validated_data.pop("fio_en"),
        "date":validated_data.pop("date"),
        "organization": self.context['request'].user.organization
        } 

        seminar = models.Seminar.objects.create(**seminar_data)
        return seminar




class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'photo', 'organization_uz', 'organization_ru', 'organization_en', 'views', 'date', )
        model = models.Video


class VideoGallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'video', 'videourl', 'title_uz', 'title_ru', 'title_en' )
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





class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=32, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        fields = ('email', 'organization', 'password', 'password2')

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError(_('Parollar mos kelmadi, Iltimos qayta urinib ko\'ring!!!'))
        else:
            user = super(UserRegisterSerializer, self).create(validated_data)
            user.set_password(password)
            user.is_active = True
            user.user_type = 1
            user.save()
            return user








