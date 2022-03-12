from django.urls import include, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
<<<<<<< HEAD
from django.conf.urls.static import static
from django.conf import settings
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> eb083f2d3446faa244defd00c9e248739cdd5246

schema_view = get_schema_view(
    openapi.Info(
        title="PROJECT DRAFT API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authenticate.urls')),
    path('question/',include('question.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
<<<<<<< HEAD
]
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> eb083f2d3446faa244defd00c9e248739cdd5246
