from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path

from app.config.application import DEBUG
from app.config.web import STATIC_ROOT, STATIC_URL

urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
