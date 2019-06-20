from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.db import DatabaseError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    #1,调用系统方法处理异常
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        #以下为自定义异常
        #判断是否是数据库异常
        if isinstance(exc,DatabaseError):
            response =Response("数据库异常",status=status.HTTP_400_BAD_REQUEST)
        else:
            response =Response("系统异常",status=status.HTTP_400_BAD_REQUEST)
    return response