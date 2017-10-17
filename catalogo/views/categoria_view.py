from ..models.categoria import Categoria
from rest_framework import serializers, viewsets


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.filter(nombre__contains="K")
