from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from watchlist.api.serializers import (ContentSerializer, PlatformSerializer,
                                       ReviewSerializer)
from watchlist.models import Content, Review, StreamingPlatform


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


class StreamPlatformViewset(viewsets.ViewSet):
    """
    implementation of viewsets
    """
    def list(self, request):
        queryset = StreamingPlatform.objects.all()
        serializer = PlatformSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
        
    def retreive(self, request, pk):
        queryset = StreamingPlatform.objects.all()
        content = get_object_or_404(queryset, pk=pk)
        serializer = PlatformSerializer(content)
        return Response(serializer.data)
    
    
###Using APIView
# class StreamingPlatformAPIView(APIView):
#     def get(self, request):
#         try:    
#             platform =  StreamingPlatform.objects.all()
#             serializer = PlatformSerializer(platform, many=True, context={'request': request})
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response(data={"error":str(e)}) 
        
#     def post(self, request):
#         serializer = PlatformSerializer(StreamingPlatform, data=request.data)  
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors)


# class StreamingPlatformDetailsApiView(APIView):
#     def get(self, request, pk):
#         try:    
#             platform =  StreamingPlatform.objects.get(pk=pk)
#             serializer = PlatformSerializer(platform, context={'request': request})
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response(data={"error":str(e)}) 
        
#     def put(self, request, pk):
#         serializer  =  PlatformSerializer(StreamingPlatform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors)
        
#     def delete(self, request, pk):
#         platform = StreamingPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(pk=pk)


#Using generic apiview
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset =  Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(content=content, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("Already reviewed!!")
        
        serializer.save(content=content, review_user=review_user)
        

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset= Review.objects.all()
    serializer_class = ReviewSerializer


####Using mixins
# class ReviewList(mixins.ListModelMixin, 
#                  mixins.CreateModelMixin, 
#                  generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
        
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)



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
    

        