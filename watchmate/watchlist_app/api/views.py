from watchlist_app.models import Content, StreamingPlatform
from watchlist_app.api.serializers import ContentSerializer, PlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class ContentListAPIView(APIView):
    def get(self, request):
        content = Content.objects.all()
        serializer = ContentSerializer(content, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class ContentDetailsAPIView(APIView):
    def get(self, request, pk):
        content = Content.objects.get(pk=pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        serializer = ContentSerializer(Content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        content = Content.objects.get(pk=pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamingPlatformAPIView(APIView):
    def get(self, request, pk):
        try:    
            platform =  StreamingPlatform.objects.get(pk=pk)
            serializer = PlatformSerializer(platform)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response(data=serializer.errors) 
        
    def post(self, request):
        serializer = PlatformSerializer(StreamingPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors)
        
    def put(self, request, pk):
        serializer  =  PlatformSerializer(StreamingPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors)
    
    
    
# @api_view(['GET', 'POST'])
# def Content_list(request):
#     if request.method == "GET":
#         Contents = Content.objects.all()
#         serializer = ContentSerializer(Contents, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = ContentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def Content_details(request, pk):
#     try:
#         Content = Content.objects.get(pk=pk)
#     except:
#         return Response(data={"Error":'Page not found'}, status=status.HTTP_404_NOT_FOUND)    
    
#     if request.method == 'GET':
#         serializer = ContentSerializer(Content)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = ContentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         Content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

        