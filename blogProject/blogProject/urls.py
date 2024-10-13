"""
URL configuration for blogProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include('blog.urls')),
    path('list/',views.list),
    path('evenodd/',views.evenodd,name='evenodd'),
    path('operations/', views.operations, name='operations'),
    path('operations_input/', views.operations_input, name='operations'),
    path('factorial/', views.factorial, name='factorial'),





]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
