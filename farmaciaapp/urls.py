"""
URL configuration for farmaciaapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions
from django.conf.urls.static import static
=======
>>>>>>> 1394ab79238923f51650b24bdac26a562cd444f8


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),
]
<<<<<<< HEAD


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Project Base v1",
        default_version="v1",
        description="Base Django",
        terms_of_service="https://raw.githubusercontent.com/Marcelo1180/django-base-backend/main/LICENSE",
        contact=openapi.Contact(email="arteagamarcelo@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        path(
            "swagger<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

=======
>>>>>>> 1394ab79238923f51650b24bdac26a562cd444f8
