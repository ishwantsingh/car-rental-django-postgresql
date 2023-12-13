# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

from django.db import models

class IdmCard(models.Model):
    card_number = models.CharField(max_length=30, primary_key=True)
    card_type = models.CharField(max_length=30)
    payment = models.ForeignKey('IdmPayment', on_delete=models.CASCADE)

class IdmClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=20)
    rate_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    over_mileage_fee = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.ForeignKey('IdmOffice', on_delete=models.CASCADE)
    rental = models.ForeignKey('IdmRentalAgr', on_delete=models.CASCADE)

class IdmCorpCoup(models.Model):
    coupon_id = models.CharField(max_length=20, primary_key=True)
    corp_coupon_id = models.IntegerField()
    aff_company_name = models.CharField(max_length=30)
    discount_percentage = models.IntegerField()
    discount = models.ForeignKey('IdmDiscount', on_delete=models.CASCADE)

class IdmCorporate(models.Model):
    # customer_id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField()
    registration_num = models.CharField(max_length=20)
    company_name = models.CharField(max_length=30)
    customer = models.ForeignKey('IdmCustomer', on_delete=models.CASCADE)

class IdmCustomer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField()
    driver_license_num = models.CharField(max_length=30)
    customer_type = models.CharField(max_length=1, choices=[('C', 'Corporate'), ('I', 'Individual')])
    rental = models.ForeignKey('IdmRentalAgr', on_delete=models.CASCADE)
    coupon = models.ForeignKey('IdmDiscount', on_delete=models.CASCADE)

class IdmDiscount(models.Model):
    coupon_id = models.CharField(max_length=20, primary_key=True)
    coupon_code = models.CharField(max_length=20)
    disc_description = models.CharField(max_length=20)
    coupon_type = models.CharField(max_length=1, choices=[('C', 'Corporate'), ('I', 'Individual')])

class IdmIndCoup(models.Model):
    coupon_id = models.CharField(max_length=20, primary_key=True)
    indv_coupon_id = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    discount_percentage = models.IntegerField()
    discount = models.ForeignKey('IdmDiscount', on_delete=models.CASCADE)

class IdmIndividual(models.Model):
    # customer_id = models.IntegerField(primary_key=True)
    individual_id = models.IntegerField()
    insurance_company_name = models.CharField(max_length=20)
    insurance_policy_num = models.CharField(max_length=20)
    customer = models.ForeignKey('IdmCustomer', on_delete=models.CASCADE)

class IdmInvoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    invoice_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.CharField(max_length=10)

class IdmOffice(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street_name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    building_number = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)

class IdmPayment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateField()
    invoice = models.ForeignKey('IdmInvoice', on_delete=models.CASCADE)

class IdmRentalAgr(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    start_odometer = models.CharField(max_length=10)
    end_odometer = models.CharField(max_length=10)
    daily_odometer_limit = models.CharField(max_length=10)
    unlimited_mileage = models.CharField(max_length=1)
    invoice = models.ForeignKey('IdmInvoice', on_delete=models.CASCADE)
    coupon = models.ForeignKey('IdmDiscount', on_delete=models.CASCADE)
    pickup_loc = models.ForeignKey('IdmOffice', on_delete=models.CASCADE, related_name='pickup_location')
    dropoff_loc = models.ForeignKey('IdmOffice', on_delete=models.CASCADE, related_name='dropoff_location')

class IdmVehicles(models.Model):
    vin = models.CharField(max_length=30, primary_key=True)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.DateField()
    license_plate_number = models.CharField(max_length=30)
    vehicle_class = models.ForeignKey('IdmClass', on_delete=models.CASCADE)
    capacity = models.IntegerField()
    mileage = models.DecimalField(max_digits=7, decimal_places=2)
    fuel_type = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30)