"""
URL configuration for wowbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('api/item/<int:item_id>/', get_item, name='get_item'),
# ]

from myapp.views import (
    signup, cars, category, booking, LoginView,  get_idm_card_data, get_idm_class_data, get_idm_corp_coup_data,
    get_idm_corporate_data, get_idm_customer_data, get_idm_discount_data,
    get_idm_ind_coup_data, get_idm_individual_data, get_idm_invoice_data,
    get_idm_office_data, get_idm_payment_data, get_idm_rental_agr_data,
    get_idm_vehicles_data, index, view_vehicle_classes
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomeView.as_view(), name='home'),
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'), #this and the method below are two different ways of doing the same thing

    # path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('cars/', cars, name='cars'),
    path('category/', category, name='category'),
    path('booking/', booking, name='booking'),

    path('cars/<str:class_name>/', view_vehicle_classes, name='view_vehicle_classes'),

    path('get-idm-card-data/', get_idm_card_data, name='get_idm_card_data'),
    path('get-idm-class-data/', get_idm_class_data, name='get_idm_class_data'),
    path('get-idm-corp-coup-data/', get_idm_corp_coup_data, name='get_idm_corp_coup_data'),
    path('get-idm-corporate-data/', get_idm_corporate_data, name='get_idm_corporate_data'),
    path('get-idm-customer-data/', get_idm_customer_data, name='get_idm_customer_data'),
    path('get-idm-discount-data/', get_idm_discount_data, name='get_idm_discount_data'),
    path('get-idm-ind-coup-data/', get_idm_ind_coup_data, name='get_idm_ind_coup_data'),
    path('get-idm-individual-data/', get_idm_individual_data, name='get_idm_individual_data'),
    path('get-idm-invoice-data/', get_idm_invoice_data, name='get_idm_invoice_data'),
    path('get-idm-office-data/', get_idm_office_data, name='get_idm_office_data'),
    path('get-idm-payment-data/', get_idm_payment_data, name='get_idm_payment_data'),
    path('get-idm-rental-agr-data/', get_idm_rental_agr_data, name='get_idm_rental_agr_data'),
    path('get-idm-vehicles-data/', get_idm_vehicles_data, name='get_idm_vehicles_data'),
    # Add more URLs for other tables if needed
    # path('idm_cards/', idm_card_list, name='idm_card_list'),
    # path('idm_classes/', idm_class_list, name='idm_class_list'),
    # path('idm_corp_coups/', idm_corp_coup_list, name='idm_corp_coup_list'),
    # path('idm_corporates/', idm_corporate_list, name='idm_corporate_list'),
    # path('idm_customers/', idm_customer_list, name='idm_customer_list'),
    # path('idm_discounts/', idm_discount_list, name='idm_discount_list'),
    # path('idm_ind_coups/', idm_ind_coup_list, name='idm_ind_coup_list'),
    # path('idm_individuals/', idm_individual_list, name='idm_individual_list'),
    # path('idm_invoices/', idm_invoice_list, name='idm_invoice_list'),
    # path('idm_offices/', idm_office_list, name='idm_office_list'),
    # path('idm_payments/', idm_payment_list, name='idm_payment_list'),
    # path('idm_rental_agrs/', idm_rental_agr_list, name='idm_rental_agr_list'),
    # path('idm_vehicles/', idm_vehicles_list, name='idm_vehicles_list'),
]
