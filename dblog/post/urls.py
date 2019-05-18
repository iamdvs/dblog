from . import views

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    path('',views.index,name="index"),
    path('createpost/',views.create_post,name="createpost"),
    path('<int:post_id>',views.description,name="description"),
    
]


