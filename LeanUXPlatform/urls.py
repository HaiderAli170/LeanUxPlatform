"""
URL configuration for LeanUXPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from LeanUXPlatform import views
admin.site.site_header = "Lean UX Platform"
admin.site.site_title = "Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path('Djadmin/', admin.site.urls),
    path('admin/', include('MyAdmin.urls')),
    path("", include('Customer.urls')),
    path('evaluator/',include('Evaluator.urls')),
    # path('generate_pdf/', views.generate_pdf, name='generate_pdf'),



    
]
