from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema', get_schema_view(title='API Schema', description='Guide for API'), name='api_schema'),
    path("admin/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path('swagger/', TemplateView.as_view(
        template_name='swaggerui.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),
    path("api/", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
