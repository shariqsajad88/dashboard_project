from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import DataPoint
from .serializers import DataPointSerializer
from django.shortcuts import render
class DataPointList(generics.ListAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
# dashboard_app/views.py
# dashboard_app/views.py
# dashboard_app/views.py
from django.http import JsonResponse
from .models import DataPoint

def data_points_view(request):
    data_points = list(DataPoint.objects.values())
    return JsonResponse(data_points, safe=False)



def dashboard_view(request):
    return render(request, 'dashboard_app/dashboard.html')
