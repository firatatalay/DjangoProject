from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>/', views.deletecomment, name='deletecomment'),
    path('contents/', views.contents, name='contents'),
    path('addcontent/', views.addcontent, name='addcontent'),
    path('editcontent/<int:id>/', views.editcontent, name='editcontent'),
    path('deletecontent/<int:id>/', views.deletecontent, name='deletecontent'),
    path('addimagecontent/<int:id>/', views.addimagecontent, name='addimagecontent'),
    path('places/', views.places, name='places'),
    path('addplace/', views.addplace, name='addplace'),
    path('editplace/<int:id>/', views.editplace, name='editplace'),
    path('deleteplace/<int:id>/', views.deleteplace, name='deleteplace'),
    path('addimageplace/<int:id>/',views.addimageplace, name='addimageplace'),
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]