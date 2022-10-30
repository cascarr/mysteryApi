from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

import requests

# I have used the Item and Mystery classes only on the ItemDetail class .


class MysteryClass(object):

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a concert":
                if item.quality > 0:
                    if item.name != "Sulfuras":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras":
                                item.quality = item.quality - 1
                        else:
                            item.quality = item.quality - item.quality
                    else:
                        if item.quality < 50:
                            item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) 



class ItemView(APIView):
    """
    List all items, or create a new item
    """

    serializ = ProductSerializer

    def get(self, request, *args, **kwargs):
        items = Product.objects.all()
        data_s = self.serializ(items, many=True)
        return Response(data_s.data)

    def post(self, request, *args, **kwargs):
        data_s = self.serializ(data=request.data)
        if data_s.is_valid():
            data_s.save()
            return Response(data_s.data, status=status.HTTP_201_CREATED)
        return Response(data_s.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView, Item, MysteryClass):
    """
    Retrieve, and update
    """

    serializ = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        data_s = self.serializ(item)
        return Response(data_s.data)

    def put(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        
        cl_item = [Item(item.name, item.sell_in, item.quality)]
        chck_mysteryclass = MysteryClass(cl_item)
        chck_mysteryclass.update()

        if chck_mysteryclass:
            data_s = self.serializ(item, data=request.data)
        
        if data_s.is_valid():
            data_s.save()
            return Response(data_s.data)
        return Response(data_s.errors, status=status.HTTP_400_BAD_REQUEST)

# function to call the index template
def home(request):
    get_data = requests.get('http://127.0.0.1:8000/items/')
    data_sved = get_data.json()
    context = {
        'response': data_sved
    }

    return render(request, 'index.html', context)