from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializer import BookInfoModelSerializer,HeroInfoModelSerializer
from .models import BookInfo,HeroInfo
from rest_framework.throttling import AnonRateThrottle
from rest_framework import filters  #注意
from redis import RedisError
from django.db import DatabaseError

#自定义分页类,改写
class MyPageNumber(PageNumberPagination):
    #1,设置页面名称
    page_size_query_param = "page_size"
    #2,设置最大显示个数，更多自定义属性详见PageNumberPagination 源码
    max_page_size=6
    '''http://api.example.org/accounts/?page=4&page_size=100'''


class BookModelView(ModelViewSet):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()

    #局部认证
    # authentication_classes = (SessionAuthentication)
    # permission_classes = (AllowAny,)

    #3,局部限流, AnonRateThrottle#限制匿名用户
    # throttle_classes = (AnonRateThrottle,)
    # 4,设置可选限流
    # throttle_scope = 'downloads'
    #5分页
    # pagination_class = LimitOffsetPagination
    """
        A limit/offset based style. For example:
        http://api.example.org/accounts/?limit=100
        http://api.example.org/accounts/?offset=400&limit=100
        """

    # pagination_class = PageNumberPagination
    #6,自定义分页
    pagination_class = MyPageNumber #调用上面自定义分页类
    '''
        http://api.example.org/accounts/?page=4
        http://api.example.org/accounts/?page=4&page_size=100'''
    #7,过滤设置
    #DEMO:  http://example.com/api/products?category=clothing&in_stock=True
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('id', 'btitle')
    #8,排序   ?ordering=id
    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('id', 'bread','bcomment')
    #9,异常处理(API类异常，其他异常)



#三级视图--英雄
class HeroModelView(ModelViewSet):


    serializer_class = HeroInfoModelSerializer
    queryset = HeroInfo.objects.all()
    throttle_scope = 'uploads'

    # pagination_class = PageNumberPagination
    pagination_class = MyPageNumber
    # 8,排序   ?ordering=id
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'hbook')


class TestView(APIView):

    def get(self,request):
        # 9.1抛出API异常
        raise APIException('api异常')
        # raise DatabaseError('error')
        # raise RedisError('redis error')

        return Response("hello")
