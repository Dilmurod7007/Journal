from rest_framework import pagination

class PaginateBy12(pagination.PageNumberPagination):
    page_size = 12
    max_page_size = 50
    page_query_param = 'p'




class PaginateBy20(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 50
    page_query_param = 'p'

