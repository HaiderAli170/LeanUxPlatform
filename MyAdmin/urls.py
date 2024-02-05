from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.AdminLogin,name="AdminLogin"),
    path("AdminDashboard/",views.AdminDashboard,name="AdminDashboard"),
    path("assignTask/",views.AssignTask,name="assignTask"),
    path("viewRequest/",views.ViewRequest,name="viewRequest"),
    path("viewRequestDetails/<int:contact_id>/",views.ViewRequestDetails,name="viewRequestDetails"),
    path("manageEvaluator/",views.ManageEvaluator,name="manageEvaluator"),
    path("adminlogout/",views.Adminlogout,name="adminlogout"),
    path('delete_request/<int:contact_id>/', views.delete_request, name='delete_request'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create_new_evaluator/', views.CreateNewEvaluator, name='CreateNewEvaluator'),
    path('RegistrationSuccessful/', views.RegistrationSuccessful, name='RegistrationSuccessful'),
    path('forward_data/<int:contact_id>/', views.Forward_data, name='forward_data'),
    path("displayForwardRequest/<int:contact_id>/",views.forward_request,name="displayForwardRequest"),
    path('edit_user<int:user_id>/', views.editUser, name='edit_user'),
    path('manageEvaluator/', views.ManageEvaluator, name='manageEvaluator'),
    path('forwardSuccess/', views.forwardSuccess, name='forwardSuccess'),
    path('feedback/', views.feedback, name='feedback'),
    path('delete_forwarded_data/<int:data_id>/', views.delete_forwarded_data, name='delete_forwarded_data'),
]
