from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(["GET", "POST"])
def product_list(request: Request) -> Response:
    if request.method == "GET":
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)  # type: ignore
        if serializer.is_valid():
            serializer.save()  # type: ignore
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    raise BaseException("unreachable")
