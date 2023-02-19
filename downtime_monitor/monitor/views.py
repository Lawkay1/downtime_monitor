from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import generics, status
from .models import Website, Emails
from .serializers import WebsiteSerializer, EmailSerializer
from rest_framework.response import Response
from .utils import get_status_and_date
from drf_yasg.utils import swagger_auto_schema
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from django.shortcuts import render

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
            
        
            user = request.user
            web_model = get_object_or_404(Website, pk = weburl_id)
             
            #Validate, the user can only access logs of their website
            if user == web_model.user_id:

                logs=get_status_and_date(web_id=weburl_id, tail_index= 144, step= 6)

                data = { 
                    'website': weburl_id,
                    'site_logs': logs
                    }

                return Response(data=data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    

        
         

    
def status_visuals(request): 

    data = get_status_and_date(web_id=1, tail_index= 144, step= 6)
    date = data['date'].tolist()
    status = transform_data(data['status'].tolist())
    web_model = get_object_or_404(Website, pk = 1)
    
    #print(date.tolist())
    #print(status.tolist())
    #date = [1,2,4,5,6,7] 
    #status = [2,3,5,6,7,7]
    print(status)
    print(date)
    '''
p = figure(x_range=fruits, height=350, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
'''

    plot = figure(title="Website Status", x_axis_label='Date', y_axis_label='Status', x_range=date)
    plot.vbar(x=date, top=status, width=3)
    #plot.line(date, status, line_width=2)
    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0
    #show(plot)

    script, div = components(plot, CDN)

    return render(request, 'status.html', {'script': script, 'div': div, 'website':web_model})

def transform_data(status_list): 
    new_list=[]
    for s in status_list: 
        if s=='UP':
            s=1
            
        else:
            s= 0
        new_list.append(s)
    return new_list