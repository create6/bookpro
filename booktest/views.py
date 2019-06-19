
from rest_framework.viewsets import ModelViewSet
from .serializer import BookInfoModelSerializer
from .models import BookInfo

class BookModelView(ModelViewSet):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()
