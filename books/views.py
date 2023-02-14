from books.models import Book
from books.serializers import BookSerializer

from rest_framework import (
    viewsets,
    permissions
)



class BookViewSet(viewsets.ModelViewSet):
    """ Api endpoint for Book models """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
