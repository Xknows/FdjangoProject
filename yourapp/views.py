from django.shortcuts import render
from store.models import Product


def sayHi(request):
    # simple
    # someThingForTest = Product.objects.filter(unitPrice__range=(0,10))
    # someThingForTest = Product.objects.filter(title__istartswith='Coffee')
    # someThingForTest = Product.objects.filter(lastUpdate__year=2021)
    # complex
    # someThingForTest = Product.objects.filter(inventory__lt=10, unitPrice__gt=20)
    # someThingForTest = Product.objects.filter(Q(inventory__lt=10) | Q(unitPrice__gt=20) )
    someThingForTest = Product.objects.filter(
        Q(inventory__lt=10) & ~Q(unitPrice__gt=20))
    return render(request, 'hello.html', {'products': list(someThingForTest)})
