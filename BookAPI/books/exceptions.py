from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

# Custom exception cho Book Not Found
class BookNotFoundException(Exception):
    pass

# Custom exception handler
def custom_exception_handler(exc, context):
    if isinstance(exc, BookNotFoundException):
        return Response(
            {"error": "Book not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response
