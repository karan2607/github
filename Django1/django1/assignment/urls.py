from django.urls import path
from assignment import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.form_view, name="login"),
    path('signup/', views.signup, name="signup"),
]