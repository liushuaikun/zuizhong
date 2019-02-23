from django.urls import path
from . import views

app_name="adjust"

urlpatterns = [
    path('addprice',views.Addprice.as_view()),
    path('show',views.Show.as_view()),
    path('update',views.Updateadjustprice.as_view()),
    path('delete',views.Delete.as_view())
]