from django.shortcuts import render , redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	form = CarForm()
	if request.method == "POST":
		form = CarForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, ' add  success.')
			return redirect('car-list')
	context = {
			"form":form,
			}
	#messages.success(request, 'create car success.')
	return render(request, 'create.html', context)




def car_update(request, car_id):
	#Complete Me
	car_obj = Car.objects.get(id=car_id)
	form = CarForm(instance=car_obj)
	if request.method == "POST":
		form = CarForm(request.POST,request.FILES, instance=car_obj)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your car was updated success.')
			return redirect('car-list')
	context = {
			"car_obj": car_obj,
			"form":form,
			}
	#messages.set_level(request, messages.WARNING)

	#CRITICAL = 50
	#messages.add_message(request, CRITICAL, 'A serious error occurred.')
	return render(request, 'update.html', context)




def car_delete(request, car_id):
	#Complete Me
	car_obj = Car.objects.get(id=car_id)
	car_obj.delete()
	messages.success(request, ' delete  success.')
	return redirect('car-list')
	#return render(...)
