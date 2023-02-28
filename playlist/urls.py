from django.urls import path
from . import views

app_name="playlist"
urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    #path("download",views.download,name="download")
    #path("Prog",views.Prog)
    #adding path to download function in views callable by playlist:download, with filename argument
    path("download/<str:filename>",views.download,name="download")
    
]