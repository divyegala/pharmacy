from django.contrib import admin

# Register your models here.
from models import Staff,Medicines,Nonmedicine,Doctor, Location

admin.site.register(Staff)
admin.site.register(Medicines)
admin.site.register(Nonmedicine)
admin.site.register(Doctor)
admin.site.register(Location)
