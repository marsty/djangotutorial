from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    def get_page_size(self,request):
        if request.query_params.get("page_size"):
            page_size = int(request.query_params.get("page_size",0))
            if page_size < 0:
                return self.page_size
            return page_size
        return  self.page_size

