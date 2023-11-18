from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, State, City, student

def controls(request):
    countries = Country.objects.all()

    context = {
        'countries': countries,
    }

    return render(request, 'index.html', context)

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'state_name')
    return JsonResponse({'states': list(states)})

def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'city_name')
    return JsonResponse({'cities': list(cities)})



def add_data(request):
        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        data = student.objects.create(name = name, email = email, country = country, state = state, city = city)
        return render(request, "index.html")



# store name in database in logic
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Country, State, City, student

# def controls(request):
#     countries = Country.objects.all()

#     context = {
#         'countries': countries,
#     }

#     return render(request, 'index.html', context)

# def get_states(request):
#     country_id = request.GET.get('country_id')
#     states = State.objects.filter(country_id=country_id).values('id', 'state_name')
#     return JsonResponse({'states': list(states)})

# def get_cities(request):
#     state_id = request.GET.get('state_id')
#     cities = City.objects.filter(state_id=state_id).values('id', 'city_name')
#     return JsonResponse({'cities': list(cities)})

# def add_data(request):
#     name = request.POST['name']
#     email = request.POST['email']
#     country_id = request.POST['country']
#     state_id = request.POST['state']
#     city_id = request.POST['city']
    
#     country_name = Country.objects.get(id=country_id).country_name
#     state_name = State.objects.get(id=state_id).state_name
#     city_name = City.objects.get(id=city_id).city_name

#     data = student.objects.create(
#         name=name,
#         email=email,
#         country=country_name,
#         state=state_name,
#         city=city_name
#     )
    
#     return render(request, "index.html")