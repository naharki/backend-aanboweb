from django.urls import path
from .view import views
from .view import employee_views
from .view import leader_view
from .view import notice_view


urlpatterns = [
    path("office/", views.Office_profile_create.as_view(), name="Office-list"),
    path('office/add/', views.Office_profile_create.as_view(), name='add- office'),
    path('office/<id>/', views.Office_profile_update_destroy.as_view(), name="update"),

# Employee urls 
    path('employee/', employee_views.Employee_list.as_view(), name="employee list"),
    path('employee/add', employee_views.Employee_create.as_view(), name="employee add"),
    path('employee/<id>/', employee_views.Employee_update_destroy.as_view(), name="update"),

    #leaders urls 
    path('leader/', leader_view.Leader_list.as_view(), name="leader-list"),
    path('leader/add', leader_view.Leader_create.as_view(), name="Leader add"),
    path('leader/<id>/', leader_view.Leader_update_destroy.as_view(), name="update"),

    # notice urls 
    path('notice/', notice_view.Notice_list.as_view(), name="notice-list"),
    path('notice/add', notice_view.Notice_create.as_view(), name="Notice add"),
    path('notice/<id>/', notice_view.Notice_update_destroy.as_view(), name="update")
]
