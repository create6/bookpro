from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns=[

]

#1,创建对象
router =DefaultRouter()
#2,注册视图集
router.register(r'book',views.BookModelView,base_name='vbook')
#3,添加至列表url
urlpatterns += router.urls
print(router.urls)

'''[
<RegexURLPattern vbook-list ^book/$>,
<RegexURLPattern vbook-list ^book\.(?P<format>[a-z0-9]+)/?$>,
<RegexURLPattern vbook-detail ^book/(?P<pk>[^/.]+)/$>,
<RegexURLPattern vbook-detail ^book/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>,
<RegexURLPattern api-root ^$>,
<RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>
]'''