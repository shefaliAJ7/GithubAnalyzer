"""djreact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.views import generic
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/',include('dashboard.urls')),
    url(r'^about/$',views.about),
    url(r'^help/',views.help),
    url(r'^views2/',generic.TemplateView.as_view(template_name='view2.html')),
    url(r'^$',generic.TemplateView.as_view(template_name='view1.html')),
    url(r'^user/', include('user_account.urls')),
]
