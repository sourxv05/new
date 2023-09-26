from .import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
        path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
     path('genlist/',views.tasklist.as_view(),name='genlist'),
    path('detview/<int:pk>/',views.detailview.as_view(),name='detview'),
     path('editview/<int:pk>/',views.updateview.as_view(),name='editview'),
     path('deleteview/<int:pk>/',views.deletelist.as_view(),name='deleteview')


]
