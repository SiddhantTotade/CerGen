from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/api/", include("cergen_auth.urls")),
    path("graphql/", include("cert_gen_sen_app_backend.urls")),
    path("app/api/", include("cert_gen_sen_app_backend.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
