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
    path("video_gallery/<int:pk>/", views.VideoGalleryListAPIView.as_view()), #used
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>/", views.NewsDetail.as_view()),
    path("contact_create/", views.ContactCreate.as_view()),
    path("faq/", views.FaqList.as_view()),
    path("banner/", views.BannerList.as_view()),
    path("webcontact/", views.WebcontactList.as_view()),
    path('filter/<int:param1>/<int:param2>/<str:string>/', views.SearchAPIView.as_view(), name='search'),
    path('auth/login/', views.UserLoginAPIView.as_view(), name='login'),
    # path('auth/register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('auth/logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('user/dashboard/', views.UserDashboardAPIView.as_view(), name='user_dashboard'),
    path('user/journal_list/', views.UserJournalListAPIView.as_view(), name="user_journals"),
    path('user/journal_list_for_search/', views.UserJournalListForSearchAPIView.as_view(), name='user_journal_for_search'),
    path('user/journal_create/', views.UserJournalCreateAPIView.as_view(), name="user_journal_create"),
    path('user/journal_update/<int:pk>/', views.UserJournalUpdateAPIView.as_view(), name='user_journal_update'),
    path('user/journal_delete/<int:pk>/', views.UserJournalDeleteAPIView.as_view(), name='user_journal_delete'),
    path('user/article_list', views.UserArticleListAPIView.as_view(), name="user_article"),
    path('user/article/<int:pk>', views.UserArticleDetailAPIView.as_view(), name='user_article_detail'),
    path('user/article_list_for_search/', views.UserArticleForSearchListAPIView.as_view(), name='user_article_for_search'),
    path('user/article_create/', views.UserArticleCreateAPIView.as_view(), name="user_article_create"),
    path('user/article_update/<int:pk>/', views.UserArticleUpdateAPIView.as_view(), name="user_article_update"),
    path('user/article_delete/<int:pk>/', views.UserArticleDeleteAPIView.as_view(), name="user_article_delete"),
    path('user/conference_list/', views.UserConferenceListAPIView.as_view(), name='user_conference'),
    path('user/conference_create/', views.UserConferenceCreateAPIView.as_view(), name='user_conference_create'),
    path('user/conference_update/<int:pk>/', views.UserConferenceUpdateAPIView.as_view(), name='user_conference_update'),
    path('user/conference_delete/<int:pk>/', views.UserConferenceDeleteAPIView.as_view(), name='user_conference_delete'),
    path('user/seminar_list/', views.UserSeminarListAPIView.as_view(), name='user_seminar'),
    path('user/seminar_create/', views.UserSeminarCreateAPIView.as_view(), name='user_seminar_create'),
    path('user/seminar_update/<int:pk>/', views.UserSeminarUpdateAPIView.as_view(), name='user_seminar_update'),
    path('user/seminar_delete/<int:pk>/', views.UserSeminarDeleteAPIView.as_view(), name='user_seminar_delete'),
    path('user/author_create/', views.UserAuthorCreateAPIView.as_view(), name='user_author_create'),
    path('user/author_for_search/', views.UserAuthorForSearchAPIView.as_view(), name='user_author_for_search'),
    path('user/organization_update/<int:pk>/', views.UserOrganizationUpdateAPIView.as_view(), name='user_organization_update'),
    path('user/subdivision_create/', views.UserSubdivisionCreateAPIView.as_view(), name='user_subdivision_create'),
    path('user/subdivision_update/<int:pk>/', views.UserSubdivisionUpdateAPIView.as_view(), name='user_subdivision_update'),
    path('user/subdivision_delete/<int:pk>/', views.UserSubdivisionDeleteAPIView.as_view(), name='user_subdivision_delete'),
    path('user/search/<int:param>/<str:string>/', views.UserSearchAPIView.as_view(), name='user_search'),
    # path('user/full_search/<int:param>/<str:string>/', views.UserFullSearchAPIView.as_view(), name='user_full_search'),

]
