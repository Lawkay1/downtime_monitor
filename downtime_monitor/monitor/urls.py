from django.urls import path 
from . import views 

urlpatterns = [

    path('create/', views.WebsiteView.as_view(), name = 'create-site' ),
    path('addmail/<int:weburl_id>/', views.EmailView.as_view(), name='addmail'),
    
]