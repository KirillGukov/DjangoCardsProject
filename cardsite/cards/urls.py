from multiprocessing.resource_tracker import register

from django.urls import path, re_path, register_converter
from . import views
from . import converters



register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.CardsHome.as_view(), name='home'),
    path('load_image/', views.load_image, name='load_image'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.PostsCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),

]
