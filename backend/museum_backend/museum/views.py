from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Group
from .serializers import PersonListSerializer, PersonDetailSerializer, GroupWithPersonsSerializer

class PersonListView(generics.ListAPIView):
    """API для получения списка всех людей"""
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer

class PersonDetailView(generics.RetrieveAPIView):
    """API для получения детальной информации о человеке"""
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer
    lookup_field = 'id'

class GroupListView(generics.ListAPIView):
    """API для получения списка всех групп с людьми"""
    queryset = Group.objects.prefetch_related('persons').all()
    serializer_class = GroupWithPersonsSerializer

@api_view(['GET'])
def api_root(request):
    """Корневой endpoint API"""
    return Response({
        'people_list': request.build_absolute_uri('/api/people/'),
        'person_detail': request.build_absolute_uri('/api/people/1/'),
        'groups_list': request.build_absolute_uri('/api/groups/'),
    })