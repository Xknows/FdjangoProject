from django.shortcuts import render
from store.models import Product


def sayHi(request):
    # someThingForTest = Product.objects.filter(unitPrice__range=(0,10))
    # someThingForTest = Product.objects.filter(title__istartswith='Coffee')
    someThingForTest = Product.objects.filter(lastUpdate__year=2021)
    return render(request, 'hello.html',{'products':list(someThingForTest)})
