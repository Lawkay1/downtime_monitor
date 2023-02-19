from django.urls import path 
from . import views 

urlpatterns = [

    path('create/', views.WebsiteView.as_view(), name = 'create-site' ),
    path('addmail/<int:weburl_id>/', views.EmailView.as_view(), name='addmail'),
    path('logs/<int:weburl_id>/', views.LogsView.as_view(), name = 'logsview'),
    path('status_visuals/', views.status_visuals, name='status_visuals')
    
]