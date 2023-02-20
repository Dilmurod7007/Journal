from rest_framework import pagination

class PaginateBy12(pagination.PageNumberPagination):
    page_size = 12
    max_page_size = 50
    page_query_param = 'p'


class PaginateBy6(pagination.PageNumberPagination):
    page_size = 6
    max_page_size = 50
    page_query_param = 'p'



class PaginateBy16(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'   


class PaginateBy15(pagination.PageNumberPagination):
    page_size = 15
    max_page_size = 50
    page_query_param = 'p'



class PaginateBy20(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 50
    page_query_param = 'p'

