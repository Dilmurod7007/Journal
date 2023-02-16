from . import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import generics, permissions
from . import models
from django.contrib.auth import logout
from . import paginations
import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Count
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.core.exceptions import PermissionDenied
from django.db.models import Sum





class OrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.all().order_by('-id')
    serializer_class = serializers.OrganizationSerializer
    pagination_class = paginations.PaginateBy15


class PopOrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.filter(top=True).order_by('number_table')
    serializer_class = serializers.OrganizationSerializer


class OrganizationDetail(generics.RetrieveAPIView):
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
    queryset = models.Jurnal.objects.filter(archive=False).order_by('-id')
    serializer_class = serializers.JurnalSerializer
    pagination_class = paginations.PaginateBy12


class PopularJurnalList(generics.ListAPIView):
    queryset = models.Jurnal.objects.filter(archive=False).order_by('-downloadview')[:12]
    serializer_class = serializers.JurnalSerializer


class JurnalDetail(generics.RetrieveAPIView):
    queryset = models.Jurnal.objects.filter(archive=False)
    serializer_class = serializers.JurnalDetailSerializer


class SubdivisionList(ListCreateAPIView):
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class SubdivisionDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class StatyaList(generics.ListAPIView):
    queryset = models.Statya.objects.filter(archive=False).order_by('-downloadview')[:12]
    serializer_class = serializers.StatyaSerializer
    pagination_class = paginations.PaginateBy12
    

class StatisticsApiView(generics.ListAPIView):
    queryset = models.Jurnal.objects.all()
    serializer_class = serializers.StatyaSerializer

    def get(self, request, *args, **kwargs):
        context = {'request': request}
        journals = models.Jurnal.objects.filter(archive=False).count()
        authors = models.Author.objects.all().count()
        organizations = models.Organization.objects.all().count()
        seminars = models.Seminar.objects.filter(archive=False).count()

        payload = {
            'journals': journals,
            'authors': authors,
            'organizations': organizations,
            'seminars': seminars,
        }
        return Response(payload, status=status.HTTP_200_OK)


class ConferenceList(ListCreateAPIView):
    queryset = models.Conference.objects.filter(archive=False)
    serializer_class = serializers.ConferenceSerializer


class ConferenceDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Conference.objects.filter(archive=False)
    serializer_class = serializers.ConferenceSerializer


class PlanningConferenceApiView(generics.ListAPIView):
    queryset = models.Conference.objects.filter(archive=False)
    serializer_class = serializers.ConferenceSerializer

    def get(self, request):
        today = datetime.datetime.today()
        ended = models.Conference.objects.filter(Q(date__lt=today))
        ended.update(archive=True)
        conference = models.Conference.objects.filter(archive=False).order_by('date')[:12]
        serializer = serializers.ConferenceSerializer(conference, many=True)
        return Response(serializer.data)


class SeminarList(ListCreateAPIView):
    queryset = models.Seminar.objects.filter(archive=False)
    serializer_class = serializers.SeminarSerializer

    def get(self, request):
        today = datetime.datetime.today()
        ended = models.Seminar.objects.filter(Q(date__lt=today))
        ended.update(archive=True)
        seminar = models.Seminar.objects.filter(archive=False).order_by('date')
        serializer = serializers.SeminarSerializer(seminar, many=True)
        return Response(serializer.data)


class SeminarDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Seminar.objects.filter(archive=False)
    serializer_class = serializers.SeminarSerializer


class VideoList(generics.ListAPIView):
    queryset = models.Video.objects.all().order_by('-id')
    serializer_class = serializers.VideoSerializer


class VideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class Video_GalleryList(ListCreateAPIView):
    queryset = models.Video_Gallery.objects.all()
    serializer_class = serializers.Video_GallerySerializer


class Video_GalleryDetail(RetrieveUpdateDestroyAPIView):
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
                response1 = models.Jurnal.objects.filter(archive=False, name_uz__contains=string)
                response2 = models.Jurnal.objects.filter(archive=False, name_ru__contains=string)
                response3 = models.Jurnal.objects.filter(archive=False, name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 2:
                response = models.Jurnal.objects.filter(archive=False, date__contains=string)
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 3:
                response1 = models.Jurnal.objects.filter(archive=False, keyword_uz__contains=string)
                response2 = models.Jurnal.objects.filter(archive=False, keyword_ru__contains=string)
                response3 = models.Jurnal.objects.filter(archive=False, keyword_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 4:
                response1 = models.Jurnal.objects.filter(archive=False, organization__name_uz__contains=string)
                response2 = models.Jurnal.objects.filter(archive=False, organization__name_ru__contains=string)
                response3 = models.Jurnal.objects.filter(archive=False, organization__name_en__contains=string)
                response = response1 | response2 | response3
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            elif param2 == 5:
                response = models.Jurnal.objects.filter(archive=False, journal_article__name__contains=string)
                serializer = serializers.JurnalSearchSerializer(response, many=True)
            else:
                return Response(payload, status=status.HTTP_303_SEE_OTHER)   
        elif param1 == 3:
            if param2 == 2:
                response = models.Statya.objects.filter(date__contains=string, archive=False)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 3:
                response = models.Statya.objects.filter(keyword__contains=string, archive=False)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 5:
                response = models.Statya.objects.filter(name__contains=string, archive=False)
                serializer = serializers.StatyaSearchSerializer(response, many=True)
            elif param2 == 6:
                response1 = models.Statya.objects.filter(author__name_uz__contains=string, archive=False)
                response2 = models.Statya.objects.filter(author__name_ru__contains=string, archive=False)
                response3 = models.Statya.objects.filter(author__name_en__contains=string, archive=False)
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
            elif param2 == 5:
                response = models.Author.objects.filter(article_author__name__contains=string)
                serializer = serializers.AuthorSearchSerializer(response, many=True)
            else:
                return Response(payload, status=status.HTTP_303_SEE_OTHER)   
        else:
            return Response(payload, status=status.HTTP_303_SEE_OTHER)   

            
        return Response(serializer.data)




class UserLoginAPIView(APIView):
    queryset = models.User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        error_message = _("Siz ro'yxatdan o'tmagansiz, Iltimos ro'yxatdan o'ting!!!")
        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            return Response({'error_message': error_message}, status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)[0]
        if user.check_password(password) is False:
            raise ValidationError({"message": _("Noto'g'ri parol kiritdingiz")})
        if user:
            if user.is_active:
                return Response({
                    'email': email,
                    'token': token.key,
                    'user_type': user.organization.name
                })
            else:
                raise ValidationError({'error_message': _('Hisob faol emas')})
        else:
            raise ValidationError({'error_message': _('Hisob mavjud emas')})


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    queryset = models.User.objects.all()


class UserLogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        logout(request)
        return Response({'success_message': _('Siz hisobdan muvaffaqiyatli chiqdingiz!!!')})


class UserDashboardAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.User.objects.all()
    serializer_class = serializers.NewsSerializer

    def get(self, request, *args, **kwargs):
        organization = self.request.user.organization
        journals = models.Jurnal.objects.filter(organization=organization, archive=False)
        article = models.Statya.objects.filter(jurnal__in=journals)
        conference = models.Conference.objects.filter(organization=organization)
        seminar = models.Seminar.objects.filter(organization=organization)

        payload = {
        "statistics": {
            'journals': journals.count(),
            'journal_views': journals.aggregate(Sum('views'))['views__sum'],
            'journal_downloadviews': journals.aggregate(Sum('downloadview'))['downloadview__sum'],
            'article': article.count(),
            'article_views': article.aggregate(Sum('views'))['views__sum'],
            'article_downloadviews': article.aggregate(Sum('downloadview'))['downloadview__sum'],
            'conference': conference.filter(archive=False).count(),
            'conference_views': conference.aggregate(Sum('views'))['views__sum'],
            'conference_all': conference.count(),
            'seminar': seminar.filter(archive=False).count(),
            'seminar_views': seminar.aggregate(Sum('views'))['views__sum'],
            'seminar_all': seminar.count(),
            },
        "contacts": {
            'organization_id': self.request.user.organization.id,
            'organization_uz': self.request.user.organization.name_uz,
            'organization_ru': self.request.user.organization.name_ru,
            'organization_en': self.request.user.organization.name_en,
            'adress_uz': organization.adress,
            'adress_ru': organization.adress,
            'adress_en': organization.adress,
            'phone_number': organization.phon_number,
            'website': organization.website,
            'ISSN': organization.issn,   
        }}

        return Response(payload, status=status.HTTP_200_OK)


class UserJournalListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.JurnalSerializer
    pagination_class = paginations.PaginateBy6

    def get_queryset(self):
        return models.Jurnal.objects.filter(organization=self.request.user.organization, archive=False).order_by('-id')



class UserJournalListForSearchAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserJournalListSerializer

    def get_queryset(self):
        return models.Jurnal.objects.filter(organization=self.request.user.organization, archive=False).order_by('-id')


class UserJournalCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.JurnalUpdateCreateSerializer
        


class UserJournalDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        queryset = models.Jurnal.objects.filter(archive=False)
        return queryset

    def destroy(self, request, *args, **kwargs):
        journals = models.Jurnal.objects.filter(organization=self.request.user.organization, archive=False) or None
        instance = self.get_object()
        if not instance in journals:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')
        instance.archive = True
        instance.save()
        serializer = serializers.JurnalSerializer(instance)
        return Response(serializer.data)



class UserJournalUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.JurnalUpdateCreateSerializer
    queryset = models.Jurnal.objects.filter(archive=False)

    def get_queryset(self):
        queryset = models.Jurnal.objects.filter(archive=False)
        return queryset 


    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user.organization != obj.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')
        serializer.save()




class UserArticleListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.StatyaSerializer
    pagination_class = paginations.PaginateBy6

    def get_queryset(self):
        journals = models.Jurnal.objects.filter(organization=self.request.user.organization)
        return models.Statya.objects.filter(jurnal__in=journals, archive=False).order_by('-id')


class UserArticleForSearchListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ArticleListForSearchSerializer

    def get_queryset(self):
        journals = models.Jurnal.objects.filter(organization=self.request.user.organization)
        article = models.Statya.objects.filter(jurnal__in=journals, archive=False).order_by('-id')
        return article


class UserArticleDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Statya.objects.filter(archive=False)
    serializer_class = serializers.StatyaSerializer


class UserArticleCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ArticleUpdateCreateSerializer





class UserArticleUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ArticleUpdateCreateSerializer
    queryset = models.Statya.objects.filter(archive=False)

    def get_queryset(self):
        queryset = models.Statya.objects.filter(archive=False)
        return queryset 


    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user.organization != obj.jurnal.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')
        serializer.save()


class UserArticleDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        queryset = models.Statya.objects.filter(archive=False)
        return queryset

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.organization != obj.jurnal.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')

        print("What the fuck")
        obj.archive = True
        obj.save()
        serializer = serializers.StatyaSerializer(obj)
        return Response(serializer.data)




class UserConferenceListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ConferenceSerializer
    pagination_class = paginations.PaginateBy6

    def get_queryset(self):
        return models.Conference.objects.filter(organization=self.request.user.organization, archive=False)


class UserConferenceCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ConferenceSerializer
    queryset = models.Conference.objects.first()



class UserConferenceUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ConferenceSerializer

    def get_queryset(self):
        return models.Conference.objects.filter(organization=self.request.user.organization, archive=False)


class UserConferenceDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Conference.objects.filter(archive=False)
    serializer_class = serializers.ConferenceSerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.organization != obj.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')

        obj.archive = True
        obj.save()
        serializer = serializers.ConferenceSerializer(obj)
        return Response(serializer.data)







class UserSeminarListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SeminarSerializer
    pagination_class = paginations.PaginateBy6

    def get_queryset(self):
        return models.Seminar.objects.filter(organization=self.request.user.organization, archive=False)


class UserSeminarCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SeminarSerializer
    
    def get_queryset(self):
        return models.Seminar.objects.filter(organization=self.request.user.organization, archive=False)


class UserSeminarUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SeminarSerializer

    def get_queryset(self):
        return models.Seminar.objects.filter(organization=self.request.user.organization, archive=False)


class UserSeminarDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Seminar.objects.filter(archive=False)
    serializer_class = serializers.SeminarSerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.organization != obj.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')

        obj.archive = True
        obj.save()
        serializer = serializers.SeminarSerializer(obj)
        return Response(serializer.data)





class UserAuthorCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer



class UserAuthorForSearchAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.AuthorForUserSearchSerializer

    def get_queryset(self):
        return models.Author.objects.all().order_by('-id')



class UserOrganizationUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.OrganizationSerializer

    def get_queryset(self):
        return models.Organization.objects.filter(id=self.request.user.organization.id)



class UserSubdivisionCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class UserSubdivisionUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SubdivisionSerializer

    def get_queryset(self):
        return models.Subdivision.objects.filter(id=self.request.user.organization.id)




class UserSubdivisionDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SubdivisionSerializer
    queryset = models.Subdivision.objects.all()

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.organization != obj.organization:
            raise PermissionDenied('Foydalanuvchiga ruxsat etilmagan!')

        obj.delete()
        serializer = serializers.SubdivisionSerializer(obj)
        return Response(serializer.data)


