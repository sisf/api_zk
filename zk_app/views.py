from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import Gust,Movie,Reservation,Music,query_musics_by_args
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GustSerializer,MovieSerializer,ReservationSerializer,MusicSerializer
from rest_framework import status,filters,viewsets

from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def list(self, request, **kwargs):
        try:
            music = query_musics_by_args(**request.query_params)
            serializer = MusicSerializer(music['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = music['draw']
            result['recordsTotal'] = music['total']
            result['recordsFiltered'] = music['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

            # [Get] api/music/
            # def list(self, request, **kwargs):
            #     try:
            #         music = Music.objects.all()[0:50000]
            #         serializer = MusicSerializer(music, many=True)
            #
            #         return Response(serializer.data, status=status.HTTP_200_OK, template_name=None, content_type=None)
            #
            #     except Exception as e:
            #         return Response(e.message, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
            #

@api_view(['GET','POST'])
def FBV_LIST(request):
    #GET
    if request.method == 'GET':
        guests = Gust.objects.all()
        serializer = GustSerializer(guests, many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method == 'POST':
        serializer = GustSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request, pk):
    try:
        guest = Gust.objects.get(pk=pk)
    except Gust.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #GET
    if request.method == 'GET':
        serializer = GustSerializer(guest)
        return Response(serializer.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = GustSerializer(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)