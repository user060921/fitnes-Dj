from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register_page, name="register_page"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('programms/', views.programms_page, name="programms"),
    path('programm_detail/<slug:slug>/', views.programm_detail_page, name="programm_detail"),
    path('articles/', views.articles_page, name="articles"),
    path('article_detail/<slug:slug>/', views.article_detail_page, name="article_detail"),
    path('profile/', views.profile_page, name="profile"),
    path('reset_password/', views.reset_password_page, name="reset_password"),
    path('check_like/', views.check_like, name="check_like"),
    path('favorite/', views.favorite_page, name="favorite"),
    path('search_programm/', views.search_programm, name="search_programm"),
]