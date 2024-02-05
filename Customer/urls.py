from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header = "Lean UX Platform"
admin.site.site_title = "Admin"
admin.site.index_title = "Admin"
urlpatterns = [
    path("", views.Home,name='home'),
    path("contact", views.show_form),
    path('contact/', views.ContactUs,name='contactUs'),
    path('viewData/', views.view_saved_data, name='view_saved_data'),
]
