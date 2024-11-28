from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
from .models import Category, Channel, Creator
from .serializers import CategorySerializer, ChannelSerializer, CreatorSerializer, CreatorWriteSerializer, UserSerializer, GroupSerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['post'])
    def add_categoy(self, request, pk=None):
        creator = self.get_object()
        category_id = request.data.get('category_id')
        try:
            category = Category.objects.get(pk=category_id)
            creator_category, created = CreatorCategory.objects.get_or_create(creator=creator, category=category)
            if created:
                return Response(CreatirCategorySerializer(creatir_category).data, status=status.HTTP_201_CREATED)
            else:
                return Responbse({'detail':'Category already linked to creator.'})
        except Category.DoesNotExist:
            return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    def get_serializer_class(self):
        # Usar o serializer de escrita para métodos POST/PUT
        if self.action in ['create', 'update', 'partial_update']:
            return CreatorWriteSerializer
        return CreatorSerializer

    @action(detail=True, methods=['get'])
    def channels(self, request, pk=None):
        # Endpoint para listar os canais de um criador específico
        creator = self.get_object()
        channels = creator.channels.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint para edicao e visualizalçao de usuarios
    """
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]