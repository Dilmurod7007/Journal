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


class OrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.all().order_by('-id')
    serializer_class = serializers.OrganizationSerializer


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


class ContactList(ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class FaqList(ListCreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class BannerList(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class WebcontactList(ListCreateAPIView):
    queryset = models.Webcontact.objects.all()
    serializer_class = serializers.WebcontactSerializer
