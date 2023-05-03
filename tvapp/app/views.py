from django.shortcuts import render
from .models import TVShow
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ShowSerializer, ShowDetailSerializer, ShowOtherSerializer
from django.db.models import Avg


class ShowListView(APIView):
    def get(self, request):
        shows = TVShow.objects.all().order_by('-rating')
        data = ShowSerializer(shows, many=True).data
        avg_rating = TVShow.objects.all().aggregate(Avg('rating'))
        total = TVShow.objects.all().count()
        return Response({
            'total': total,
            # 'average_rating': average,
            'average_rating': avg_rating['rating__avg'],
            'shows': data
        })

        # if id:
        #     tv_show = get_object_or_404(TVShow, id=id)
        #     serializer = self.serializer_class(tv_show)
        #     return Response(serializer.data)
        # else:
        #     tv_shows = TVShow.objects.all()
        #     serializer = self.serializer_class(tv_shows, many=True)
        #     avg_rating = TVShow.objects.all().aggregate(Avg('rating'))
        #     return Response({'TV shows': serializer.data, 'average_rating': avg_rating['rating__avg']})
    def post(self, request):
        serializer = ShowOtherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            show = serializer.save()
            return Response({
            "status": 0,
            "message": "New show added",
            "id": show.id
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    

    


    
   

      

class ShowDetailView(APIView):
    serializer_class = ShowDetailSerializer
    def get(self, request, id):

        show = get_object_or_404(TVShow, id=id)
        serializer = ShowDetailSerializer(show)
        return Response(serializer.data)
    
    def put(self, request, id):
        show = get_object_or_404(TVShow, id=id)
        serializer = ShowDetailSerializer(show, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 0,
                "message": "show updated",
            })

    def patch(self, request, id):
        show = get_object_or_404(TVShow, id=id)
        serializer = ShowOtherSerializer(show, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
              "status": 0,
              "message": "Show modified"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP)
    
    def delete(self, request, id):
        show = get_object_or_404(TVShow, id=id)
        show.delete()
        return Response({
          "status": 0,
          "message": "Show deleted"
        }, status=status.HTTP_200_OK)
# class ShowCreateView(APIView):
#     serializer_class = ShowCreateSerializer
#     def post(self, request):
#         serializer = ShowCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             show = serializer.save()
#             return Response({
#               "status": 0,
#               "message": "New show added",
#               "id": show.id
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ShowUpdateView(APIView):
#     serializer_class = ShowUpdateSerializer
#     def put(self, request, id):
#         show = get_object_or_404(TVShow, id=id)
#         serializer = ShowUpdateSerializer(show, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "status": 0,
#                 "message": "show updated",
#             })
# class ShowPatchView(APIView):
#     serializer_class = ShowPatchSerializer
#     def patch(self, request, id):
#         show = get_object_or_404(TVShow, id=id)
#         serializer = ShowPatchSerializer(show, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#               "status": 0,
#               "message": "Show modified"
#             }, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP)
# class ShowDeleteView(APIView):
#     serializer_class = ShowSerializer
#     def delete(self, request, id):
#         show = get_object_or_404(TVShow, id=id)
#         show.delete()
#         return Response({
#           "status": 0,
#           "message": "Show deleted"
#         }, status=status.HTTP_204_NO_CONTENT)


