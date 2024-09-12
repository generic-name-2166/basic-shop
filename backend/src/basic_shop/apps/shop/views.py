from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer


@csrf_exempt
def product_list(request: HttpRequest):
    if request.method == "GET":
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)  # type: ignore
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # type: ignore
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request: HttpRequest, pk: int):
    try:
        snippet = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)  # type: ignore
        serializer = ProductSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()  # type: ignore
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
