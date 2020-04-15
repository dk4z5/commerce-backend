from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

#class CustomPagination(LimitOffsetPagination):
class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    #def get_paginated_response(self, data):
        #return Response(data)