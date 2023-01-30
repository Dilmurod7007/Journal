from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title = "Farmwikipedia",
        discription = "BU farmasevtikaga oid ilmiy maqolalar jamlanmansi",
        default_version = 'v1',
        terms_of_service = 'https://www.google.com/policies/terms/',
        contact = openapi.Contact(email='ramziddin_jurabek.uz@mail.ru'),
        license=openapi.License(name='Pharm'),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("pharmapolls.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += i18n_patterns(
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

