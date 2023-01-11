from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import generics, status
from .models import Website, Emails
from .serializers import WebsiteSerializer, EmailSerializer
from rest_framework.response import Response


# Create your views here.
'''
class WebsiteView(generics.CreateAPIView):
    
    #This class creates a view that enables only authenticated users
    #to create a website with an associated mail
    
    #permission_classes = (IsAuthenticated,)
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #serializer.validated_data['user'] = request.user 
        self.perform_create(serializer)      
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
'''

class WebsiteView(generics.GenericAPIView):
    serializer_class =WebsiteSerializer    
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            
            serializer.save(user_id=request.user)
            

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class EmailView(generics.GenericAPIView):
    print(1)
    serializer_class= EmailSerializer
    permission_classes= [IsAuthenticated]
    
    def post(self, request, weburl_id):
        data=request.data  
         
        weburl_id= get_object_or_404(Website, pk=weburl_id)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(website_id=weburl_id)        

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
            
