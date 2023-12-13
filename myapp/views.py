from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from .models import Item

# def get_item(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     data = {'name': item.name, 'description': item.description}
#     return JsonResponse(data)

from django.shortcuts import render
from django.http import JsonResponse
from .models import (
    IdmCard, IdmClass, IdmCorpCoup, IdmCorporate, IdmCustomer, IdmDiscount,
    IdmIndCoup, IdmIndividual, IdmInvoice, IdmOffice, IdmPayment, IdmRentalAgr, IdmVehicles
)
from django.views.generic import TemplateView

# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'index.html'


def index(request):
    # Retrieve data from your models
    idm_customers = IdmCustomer.objects.all()
    idm_offices = IdmOffice.objects.all()
    idm_vehicles = IdmVehicles.objects.all()
    idm_rental_agreements = IdmRentalAgr.objects.all()
    idm_classes = IdmClass.objects.all()
    idm_corp_coups = IdmCorpCoup.objects.all()
    idm_corporates = IdmCorporate.objects.all()
    idm_discounts = IdmDiscount.objects.all()
    idm_ind_coups = IdmIndCoup.objects.all()
    idm_individuals = IdmIndividual.objects.all()
    idm_invoices = IdmInvoice.objects.all()
    idm_payments = IdmPayment.objects.all()

    # Pass the data to the template
    context = {
        'idm_customers': idm_customers,
        'idm_offices': idm_offices,
        'idm_vehicles': idm_vehicles,
        'idm_rental_agreements': idm_rental_agreements,
        'idm_classes': idm_classes,
        'idm_corp_coups': idm_corp_coups,
        'idm_corporates': idm_corporates,
        'idm_discounts': idm_discounts,
        'idm_ind_coups': idm_ind_coups,
        'idm_individuals': idm_individuals,
        'idm_invoices': idm_invoices,
        'idm_payments': idm_payments,
        # Add other data as needed
    }

    # Render the HTML template with the data
    return render(request, 'index.html', context)



class LoginView(TemplateView):
    template_name = 'login.html'

# def login(request):
#     return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def cars(request):
    return render(request, 'cars.html')

def category(request):
    # Retrieve data from your models
    idm_vehicles = IdmVehicles.objects.all()
    idm_classes = IdmClass.objects.all()

    # Pass the data to the template
    context = {
        'idm_vehicles': idm_vehicles,
        'idm_classes': idm_classes,
        # Add other data as needed
    }

    # Render the HTML template with the data
    return render(request, 'category.html', context)

# def view_economy_classes(request, class_name):
#     # Filter vehicles based on the class name
#     economy_vehicles = IdmVehicles.objects.filter(vehicle_class__class_name=class_name)

#     # Pass the filtered vehicles to the template
#     context = {'economy_vehicles': economy_vehicles}
#     return render(request, 'cars.html', context)

def view_vehicle_classes(request, class_name):
    # Filter vehicles based on the class name
    filtered_vehicles = IdmVehicles.objects.filter(vehicle_class__class_name=class_name)
    # image_filenames = ['car-1.jpg', 'car-2.jpg', 'car-3.jpg', 'car-4.jpg']  # Replace with your actual filenames
    # Pass the filtered vehicles to the template
    context = {'filtered_vehicles': filtered_vehicles, 'class_name': class_name, 
    # 'image_filenames': image_filenames
    }
    return render(request, 'cars.html', context)
# def category(request):
#     return render(request, 'category.html')

def booking(request):
    return render(request, 'booking.html')


def get_idm_card_data(request):
    data = list(IdmCard.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_class_data(request):
    data = list(IdmClass.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_corp_coup_data(request):
    data = list(IdmCorpCoup.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_corporate_data(request):
    data = list(IdmCorporate.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_customer_data(request):
    data = list(IdmCustomer.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_discount_data(request):
    data = list(IdmDiscount.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_ind_coup_data(request):
    data = list(IdmIndCoup.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_individual_data(request):
    data = list(IdmIndividual.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_invoice_data(request):
    data = list(IdmInvoice.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_office_data(request):
    data = list(IdmOffice.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_payment_data(request):
    data = list(IdmPayment.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_rental_agr_data(request):
    data = list(IdmRentalAgr.objects.values())
    return JsonResponse(data, safe=False)

def get_idm_vehicles_data(request):
    data = list(IdmVehicles.objects.values())
    return JsonResponse(data, safe=False)
#4444
# def idm_card_list(request):
#     idm_cards = IdmCard.objects.all()
#     data = {'idm_cards': list(idm_cards.values())}
#     return JsonResponse(data)

# def idm_class_list(request):
#     idm_classes = IdmClass.objects.all()
#     data = {'idm_classes': list(idm_classes.values())}
#     return JsonResponse(data)

# def idm_corp_coup_list(request):
#     idm_corp_coups = IdmCorpCoup.objects.all()
#     data = {'idm_corp_coups': list(idm_corp_coups.values())}
#     return JsonResponse(data)

# def idm_corporate_list(request):
#     idm_corporates = IdmCorporate.objects.all()
#     data = {'idm_corporates': list(idm_corporates.values())}
#     return JsonResponse(data)

# def idm_customer_list(request):
#     idm_customers = IdmCustomer.objects.all()
#     data = {'idm_customers': list(idm_customers.values())}
#     return JsonResponse(data)

# def idm_discount_list(request):
#     idm_discounts = IdmDiscount.objects.all()
#     data = {'idm_discounts': list(idm_discounts.values())}
#     return JsonResponse(data)

# def idm_ind_coup_list(request):
#     idm_ind_coups = IdmIndCoup.objects.all()
#     data = {'idm_ind_coups': list(idm_ind_coups.values())}
#     return JsonResponse(data)

# def idm_individual_list(request):
#     idm_individuals = IdmIndividual.objects.all()
#     data = {'idm_individuals': list(idm_individuals.values())}
#     return JsonResponse(data)

# def idm_invoice_list(request):
#     idm_invoices = IdmInvoice.objects.all()
#     data = {'idm_invoices': list(idm_invoices.values())}
#     return JsonResponse(data)

# def idm_office_list(request):
#     idm_offices = IdmOffice.objects.all()
#     data = {'idm_offices': list(idm_offices.values())}
#     return JsonResponse(data)

# def idm_payment_list(request):
#     idm_payments = IdmPayment.objects.all()
#     data = {'idm_payments': list(idm_payments.values())}
#     return JsonResponse(data)

# def idm_rental_agr_list(request):
#     idm_rental_agrs = IdmRentalAgr.objects.all()
#     data = {'idm_rental_agrs': list(idm_rental_agrs.values())}
#     return JsonResponse(data)

# def idm_vehicles_list(request):
#     idm_vehicles = IdmVehicles.objects.all()
#     data = {'idm_vehicles': list(idm_vehicles.values())}
#     return JsonResponse(data)