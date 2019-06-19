from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializer import BookInfoModelSerializer
from .models import BookInfo

class BookModelView(ModelViewSet):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()

    #局部认证
    # authentication_classes = (SessionAuthentication)
    # permission_classes = (AllowAny,)