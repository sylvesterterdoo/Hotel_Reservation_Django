from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import HotelSerializers
from app.models import Hotels

def home(request):
    return HttpResponse("<h1>hello world</h1>")

@api_view(['GET', 'POST'])
def gethotels(request):

    if request.method == 'GET':
        hotels_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(
            {
               "hotel_list" : hotelSerializer.data
            }
        )
    if request.method == 'POST':
        request_data = request.data
        serialize_request_data = HotelSerializers(data=request_data)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Added Successfully"})


class HotelsList(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializers