from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import House

class HouseListView(View):
    def get(self, request):
        houses = House.objects.all()
        return render(request, 'index.html', {'houses': houses})

class HouseDetailView(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        return render(request, 'detail.html', {'house': house})

class HouseCreateView(View):
    def get(self, request):
        return render(request, 'create_house.html')

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        built_at = request.POST.get('built_at')
        rooms = request.POST.get('rooms')
        area = request.POST.get('area')
        desc = request.POST.get('desc')

        house = House.objects.create(
            title=title,
            price=price,
            built_at=built_at,
            rooms=rooms,
            area=area,
            desc=desc
        )
        house.save()
        return redirect('index')

class HouseUpdateView(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        return render(request, 'update_house.html', {'uy': house})

    def post(self, request, pk):
        house = get_object_or_404(House, id=pk)
        house.title = request.POST['title']
        house.price = request.POST['price']
        house.built_at = request.POST['built_at']
        house.rooms = request.POST['rooms']
        house.area = request.POST['area']
        house.desc = request.POST['desc']

        house.save()
        return redirect('index')

class HouseDeleteView(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        house.delete()
        return redirect('index')
