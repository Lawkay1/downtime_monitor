from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import generics, status
from .models import Website, Emails
from .serializers import WebsiteSerializer, EmailSerializer
from rest_framework.response import Response
from .utils import get_status_and_date
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class WebsiteView(generics.GenericAPIView):
    '''
#This class creates a view that enables only authenticated usersto create a website
    '''
    serializer_class =WebsiteSerializer    
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Add a website you want to monitor")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            
            serializer.save(user_id=request.user)
            

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class EmailView(generics.GenericAPIView):
    '''
    This class enables users 
    '''
    serializer_class= EmailSerializer
    permission_classes= [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Add Emails to a website")
    def post(self, request, weburl_id):
        data=request.data  
         
        weburl_id= get_object_or_404(Website, pk=weburl_id)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(website_id=weburl_id)        

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
            
class LogsView(generics.GenericAPIView): 
    '''
    This class enables users to get the last 144 logs generated in steps of 6 
    '''
    permission_classes= [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get Your Server Logs")
    def get(self, request, weburl_id):
            
        try:
            
            logs=get_status_and_date(web_id=weburl_id, tail_index= 144, step= 6)

            data = { 
                'website': weburl_id,
                'site_logs': logs
                }

            return Response(data=data,status=status.HTTP_200_OK)
        
        except Exception: 

            return Response(status=status.HTTP_400_BAD_REQUEST)

        
         

    
