from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response

# from .authenticator import JWToken
# from .mixins import RestrictedViewMixin
from .models import Category, Product
from .serializers import CategoriesSerializer, ProductsSerializer


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    def update(self, request):
        pass
    
    def delete(self, request):
        pass


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def update(self, request):
        pass

    def delete(self, request):
        pass



@api_view(['GET'])
def getproduct(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductsSerializer(products, many=False)

    return Response(serializer.data)


# TODO:: make it get category items
@api_view(['GET'])
def getcategory(request, pk):
    categories = Category.objects.get(id=pk)
    serializer = CategoriesSerializer(categories, many=False)

    return Response(serializer.data)


# class DummyView(RestrictedViewMixin, APIView):
#     def get(self, request):
#         content = {"details": "Hello, this is a restricted end point"}

#         return Response(content)
