from django.urls import path
from. import views

urlpatterns = [
    path('',views.news.as_view(),name = "news"),
    path('create/',views.PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('<int:pk>',views.NewsDetail.as_view(),name = 'news_details'),
    path('create', views.PostUpdateView.as_view(), name='post_update'),
    path('delete', views.PostDeleteView.as_view(), name='post_delete'),


]