from . import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from . import models
from . import paginations
import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Count
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class OrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.all().order_by('-id')
    serializer_class = serializers.OrganizationSerializer
    pagination_class = paginations.PaginateBy15


class PopOrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.filter(top=True).order_by('number_table')
    serializer_class = serializers.OrganizationSerializer


class OrganizationDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class AuthorList(generics.ListAPIView):
    queryset = models.Author.objects.all().annotate(articles=Count('article_author')).order_by('-id')
    serializer_class = serializers.AuthorSerializer
    pagination_class = paginations.PaginateBy20


class AuthorDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorDetailSerializer


class JurnalList(generics.ListAPIView):
    queryset = models.Jurnal.objects.all()#Jurnal listni date bo'yicha qilish kere
    serializer_class = serializers.JurnalSerializer
    pagination_class = paginations.PaginateBy12


class PopularJurnalList(generics.ListAPIView):
    queryset = models.Jurnal.objects.all().order_by('-downloadview')[:12]
    serializer_class = serializers.JurnalSerializer


class JurnalDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Jurnal.objects.all()
    serializer_class = serializers.JurnalDetailSerializer


class SubdivisionList(ListCreateAPIView):
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class SubdivisionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class StatyaList(generics.ListAPIView):
    queryset = models.Statya.objects.all().order_by('-downloadview')[:12]
    serializer_class = serializers.StatyaSerializer
    pagination_class = paginations.PaginateBy12
    

class StatisticsApiView(generics.ListAPIView):
    queryset = models.Jurnal.objects.all()
    serializer_class = serializers.StatyaSerializer

    def get(self, request, *args, **kwargs):
        context = {'request': request}
        journals = models.Jurnal.objects.all().count()
        authors = models.Author.objects.all().count()
        organizations = models.Organization.objects.all().count()
        seminars = models.Seminar.objects.all().count()

        payload = {
            'journals': journals,
            'authors': authors,
            'organizations': organizations,
            'seminars': seminars,
        }
        return Response(payload, status=status.HTTP_200_OK)


class ConferenceList(ListCreateAPIView):
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer


class ConferenceDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer


class PlanningConferenceApiView(generics.ListAPIView):
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer

    def get(self, request):
        today = datetime.datetime.today()
        ended = models.Conference.objects.filter(Q(date__lt=today))
        ended.update(archive=True)
        conference = models.Conference.objects.filter(archive=False).order_by('date')[:12]
        serializer = serializers.ConferenceSerializer(conference, many=True)
        return Response(serializer.data)


class SeminarList(ListCreateAPIView):
    queryset = models.Seminar.objects.all()
    serializer_class = serializers.SeminarSerializer

    def get(self, request):
        today = datetime.datetime.today()
        ended = models.Seminar.objects.filter(Q(date__lt=today))
        ended.update(archive=True)
        seminar = models.Seminar.objects.filter(archive=False).order_by('date')
        serializer = serializers.SeminarSerializer(seminar, many=True)
        return Response(serializer.data)


class SeminarDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Seminar.objects.all()
    serializer_class = serializers.SeminarSerializer


class VideoList(generics.ListAPIView):
    queryset = models.Video.objects.all().order_by('-id')
    serializer_class = serializers.VideoSerializer


class VideoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class Video_GalleryList(ListCreateAPIView):
    queryset = models.Video_Gallery.objects.all()
    serializer_class = serializers.Video_GallerySerializer


class Video_GalleryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Video_Gallery.objects.all()
    serializer_class = serializers.Video_GallerySerializer


class NewsList(ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class ContactCreate(ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class FaqList(generics.ListAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class BannerList(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class WebcontactList(generics.ListAPIView):
    queryset = models.Webcontact.objects.all()
    serializer_class = serializers.WebcontactSerializer



class SearchAPIView(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer

    def get(self, request, param1, param2, string):
        payload = {
            'error': "notog'ri informatsia kiritildi",
        }

        if param1 == 1:
            if param2 == 4:
                response1 = models.Organization.objects.filter(name_uz__contains=string)
                response2 = models.Organization.objects.filter(name_ru__contains=string)
                response3 = models.Organization.objects.filter(name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.OrganizationSearchSerializer(response, many=True)
            elif param2 == 8:
                response = models.Organization.objects.filter(phon_number__contains=string)
                serializer = serializers.OrganizationSearchSerializer(response, many=True) 
            elif param2 == 9:
                response = models.Organization.objects.filter(issn__contains=string)
                serializer = serializers.OrganizationSearchSerializer(response, many=True)
            elif param2 == 10:
                response1 = models.Organization.objects.filter(adress_uz__contains=string)
                response2 = models.Organization.objects.filter(adress_en__contains=string)
                response3 = models.Organization.objects.filter(adress_ru__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.OrganizationSearchSerializer(response, many=True)
            else:
                return Response(payload, status=status.HTTP_303_SEE_OTHER)   
        elif param1 == 2:
            if param2 == 1:
                response1 = models.Jurnal.objects.filter(name_uz__contains=string)
                response2 = models.Jurnal.objects.filter(name_ru__contains=string)
                response3 = models.Jurnal.objects.filter(name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 2:
                response = models.Jurnal.objects.filter(date__contains=string)
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 3:
                response1 = models.Jurnal.objects.filter(keyword_uz__contains=string)
                response2 = models.Jurnal.objects.filter(keyword_ru__contains=string)
                response3 = models.Jurnal.objects.filter(keyword_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 4:
                response1 = models.Jurnal.objects.filter(organization__name_uz__contains=string)
                response2 = models.Jurnal.objects.filter(organization__name_ru__contains=string)
                response3 = models.Jurnal.objects.filter(organization__name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 5:
                response = models.Jurnal.objects.filter(journal_article__name__contains=string)
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            else:
                return Response(payload, status=status.HTTP_303_SEE_OTHER)   
        elif param1 == 3:
            if param2 == 2:
                response = models.Statya.objects.filter(date__contains=string)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 3:
                response = models.Statya.objects.filter(keyword__contains=string)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 5:
                response = models.Statya.objects.filter(name__contains=string)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 6:
                response1 = models.Statya.objects.filter(author__name_uz__contains=string)
                response2 = models.Statya.objects.filter(author__name_ru__contains=string)
                response3 = models.Statya.objects.filter(author__name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.StatyaSearchSerializer(response, many=True) 
            else:   
                return Response(payload, status=status.HTTP_303_SEE_OTHER)       
        elif param1 == 4:
            if param2 == 7:
                response1 = models.Author.objects.filter(name_uz__contains=string)
                response2 = models.Author.objects.filter(name_ru__contains=string)
                response3 = models.Author.objects.filter(name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.AuthorSearchSerializer(response, many=True)
            if param2 == 5:
                response = models.Author.objects.filter(article_author__name__contains=string)
                serializer = serializers.AuthorSearchSerializer(response, many=True)
            else:
                return Response(payload, status=status.HTTP_303_SEE_OTHER)   
        else:
            return Response(payload, status=status.HTTP_303_SEE_OTHER)   

            
        return Response(serializer.data)

