from django.shortcuts import render
from store.models import Product, OrderItem, Order


def sayHi(request):
    # simple
    # someThingForTest = Product.objects.filter(unitPrice__range=(0,10))
    # someThingForTest = Product.objects.filter(title__istartswith='Coffee')
    # someThingForTest = Product.objects.filter(lastUpdate__year=2021)
    # complex
    # someThingForTest = Product.objects.filter(inventory__lt=10, unitPrice__gt=20)
    # someThingForTest = Product.objects.filter(Q(inventory__lt=10) | Q(unitPrice__gt=20) )
    # for avoid duplicates distinct()

    # # to get title of all products
    # someThingForTest = Product.objects.values('title')
    # # to get title of products have been ordered
    # someThingForTest = Product.objects.filter(id__in =OrderItem.objects.values('product_id').distinct()).order_by('title')

    # to get product.collection.title one way is 
    # someThingForTest = Product.objects.all()
    ## better way: because of less queries means just query to related tables
    someThingForTest = Product.objects.select_related('collection')
    
    ## query to get 5 last customers first name and their order item id
    someThingForTest = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placedAt')[:5]

    return render(request, 'hello.html', {'orders': list(someThingForTest)})
