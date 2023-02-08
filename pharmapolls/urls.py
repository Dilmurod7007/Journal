from django.urls import path
from . import views


urlpatterns = [
    path("organizations/", views.OrganizationList.as_view()),  #used
    path("popular_organizations/", views.PopOrganizationList.as_view()),  #used
    path("organization/<int:pk>/", views.OrganizationDetail.as_view()), #used
    path("authors/", views.AuthorList.as_view()), #used
    path("author/<int:pk>/", views.AuthorDetail.as_view()), #used
    path("journals/", views.JurnalList.as_view()),  #used
    path("journal/<int:pk>/", views.JurnalDetail.as_view()), #used
    path("popular_journals/", views.PopularJurnalList.as_view()),  #used
    path("subdivisions/", views.SubdivisionList.as_view()),
    path("subdivision/<int:pk>/", views.SubdivisionDetail.as_view()),
    path("articles/", views.StatyaList.as_view()),  #used
    path("conferences/", views.ConferenceList.as_view()),
    path("conference/<int:pk>/", views.ConferenceDetail.as_view()),
    path("conference_soon/", views.PlanningConferenceApiView.as_view()),  #used
    path("seminars/", views.SeminarList.as_view()),
    path("seminar/<int:pk>/", views.SeminarDetail.as_view()),
    path("statistics/", views.StatisticsApiView.as_view()),  #used
    path("videos/", views.VideoList.as_view()), #used
    path("video/<int:pk>/", views.VideoDetail.as_view()),
    path("video_gallery/", views.Video_GalleryList.as_view()),
    path("video_gallery/<int:pk>/", views.Video_GalleryDetail.as_view()),
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>/", views.NewsDetail.as_view()),
    path("contact_create/", views.ContactCreate.as_view()),
    path("faq/", views.FaqList.as_view()),
    path("banner/", views.BannerList.as_view()),
    path("webcontact/", views.WebcontactList.as_view()),
    path('filter/<int:param1>/<int:param2>/<str:string>/', views.SearchAPIView.as_view()),
    path('auth/login/', views.UserLoginAPIView.as_view(), name='login'),
    path('auth/register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('auth/logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('user/dashboard/', views.UserDashboardAPIView.as_view(), name='user_dashboard'),
    path('user/journal_list/', views.UserJournalListAPIView.as_view(), name="user_journals"),
    path('user/journal_create/', views.UserJournalCreateAPIView.as_view(), name="journal_create"),
    path('user/journal_delete/<int:pk>/', views.UserJournalDeleteAPIView.as_view(), name='journal_delete'),
    path('user/journal_update/<int:pk>/', views.UserJournalUpdateAPIView.as_view(), name='journal_update'),
    path('user/article_list', views.UserArticleListAPIView.as_view(), name="user_article"),
    path('user/conference_list/', views.UserConferenceListAPIView.as_view(), name='user_conference'),
    path('user/seminar_list/', views.UserSeminarListAPIView.as_view(), name='user_seminar'),


]
