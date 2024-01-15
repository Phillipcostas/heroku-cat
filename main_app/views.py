from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cat, Feeding, Toy
from .serializers import CatSerializer, FeedingSerializer, ToySerializer

class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the cat-collector api home route!'}
    return Response(content)

class CatList(generics.ListCreateAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer
  lookup_field = 'id'

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    cat_id = self.kwargs['cat_id']
    return Feeding.objects.filter(cat_id=cat_id)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    cat_id = self.kwargs['cat_id']
    return Feeding.objects.filter(cat_id=cat_id)

class ToyList(generics.ListCreateAPIView):
  queryset = Toy.objects.all()
  serializer_class = ToySerializer

class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Toy.objects.all()
  serializer_class = ToySerializer
  lookup_field = 'id'