from rest_framework import pagination
from rest_framework.response import Response
# from rest_framework.pagination import PaginationSerializer


class Pagination(pagination.PageNumberPagination):
	page_size_query_param = "page[size]"

	def get_paginated_response(self, data):
		return Response({
			'links': {
				'next': self.get_next_link(),
				'previous': self.get_previous_link()
			},
			'count': self.page.paginator.count,
			'num_pages': self.page.paginator.num_pages,
			'results': data,
			'current_page': self.page.number,
		})