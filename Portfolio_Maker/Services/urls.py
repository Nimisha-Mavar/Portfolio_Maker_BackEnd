from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('Personal_data',views.Personal,name="Personal_data"),
    path('Education_data',views.Education_data,name="Education_data"),
    path('Experience_data',views.Experience_data,name="Experience_data"),
    path('Project_data',views.Project_data,name="Project_data"),
    path('Skill_data',views.Skill_data,name="Skill_data"),
    path('Award_data',views.Award_data,name="Award_data"),
    path('Social_data',views.Social_data,name="Social_data"),
    path('Data_display',views.Data_display,name="Data_display"),
    #for delete
    path('Education_del/<int:id>',views.Education_del,name="Education_del"),
    path('Experience_del',views.Experience_del,name="Experience_del"),
    path('Project_del',views.Project_del,name="Project_del"),
    path('Skill_del',views.Project_del,name="Project_del"),
    path('Award_del',views.Award_del,name="Award_del"),
    path('Social_del',views.Social_del,name="Social_del"),
    #for ready template
    path('Ready',views.Ready_page,name="Ready"),
    #for get portfolio url
    path('Get_url',views.Get_url,name="Get_url"),
]
