from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.evaluatorLogin),
    path("dashboard",views.Dashboard),
    path("dashboard/",views.Dashboard,name="dashboard"),
    path("logout/",views.logoutUser,name="logout"),
    # path("face", views.face_recognition),
    path("profile/", views.showprofile,name="profile"),
    path('gazedata/',views.GazeData, name='gazedata'),
    path("projects/", views.showProject,name="Projects"),
    # path('capture/', views.face_recognition, name='capture'),
    path('face_recognition/', views.face_recognition, name='face_recognition'),
    path('face/<int:forwarded_data_id>/', views.face, name='face'),
    path('show_chart/', views.show_chart, name='show_chart'),
    path('send_email/', views.send_email, name='send_email'),
    path('view_forwarded_request/', views.view_forwarded_request, name='view_forwarded_request'),
    path('notifications/', views.view_notifications, name='view_notifications'),
    path('startProject/', views.StartProject, name='startProject'),
    # path('generate_heatmap/', views.generate_heatmap, name='generate_heatmap'),
    # path('receive_gaze_data/', views.receive_gaze_data, name='receive_gaze_data'),
    path('view_gaze_data/', views.view_gaze_data, name='view_gaze_data'),
    path('reportForm/', views.reportSelection, name='reportForm'),
    path('heuristicReport/', views.reportdetailform, name='heuristicReport'),
    path('cloud/', views.cloud, name='cloud'),
    path('reportForm/evaluator/generate_pdf_report/', views.generate_pdf_report, name='generate_pdf_report'),
    path('heuristicReport/evaluator/generate_ux_report/', views.generate_pdf, name='generate_pdf'),
    path('save_video/', views.save_video, name='save_video'),
    path('generate_bar_chart/', views.generate_bar_chart, name='generate_bar_chart'),
    
    

]
