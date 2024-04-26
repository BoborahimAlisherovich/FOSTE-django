from django.urls import path
from .views import home_view,contact_view,client_view,blog_view,base_view,about_view,services_view



urlpatterns = [
    path('',home_view, name="home-page"),
    path('blog/',blog_view,  name="blog-page"),
    path('client/',client_view, name="client-page"),
    path('contact/', contact_view, name="cantact-page"),
    path('base/', base_view, name="base-page"),
    path('about/', about_view, name="about-page"),
    path('services/', services_view, name="services-page"),
    
    
]
