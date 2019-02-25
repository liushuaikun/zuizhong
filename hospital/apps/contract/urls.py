"""hospital URL Configuration

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

from django.urls import path
from . import views

app_name="contract"

urlpatterns = [
    path('show/',views.contractshow.as_view(),name="contractshow"),
    path('contractadd/', views.contractadd.as_view(), name="contractadd"),
    path('contractupdate/', views.contractupdate.as_view(), name="contractupdate"),
    path('contractdelete/', views.contractdelete.as_view(), name="contractdelete"),
    path('quit/', views.quit.as_view(), name="quit"),

]
