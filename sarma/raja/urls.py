from django.urls import path
from.import views

urlpatterns = [
    path("",views.hi,name = "Home-page"),
    path("insert",views.data,name="insert"),
    #path('showpage/',views.showpage,name='showpage'),
]