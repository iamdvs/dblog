from . import views
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name="index"),
    path('createpost/',views.create_post,name="createpost"),
    path('<int:post_id>',views.description,name="description"),
    path('manage/',views.manage,name="manage"),
    path('manage/<int:post_id>',views.manageDelete,name="delete"),
    path('manage/edit/<int:post_id>',views.editPost,name="editPost"),
    
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 





