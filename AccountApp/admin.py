from django.contrib import admin
from .models import User,Doctor,Patient,Specialty
from django.contrib.auth.admin import UserAdmin
from AppointmentApp.models import Appointment

# Register your models here.

#admin.site.register(User)
#admin.site.register(Doctor)
#admin.site.register(Patient)
#admin.site.register(Specialty)

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0
    readonly_fields = ("appointment_date", "doctor", "status", "duration_minutes", "reason")
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False
        
@admin.register(Specialty)
class Specialty (admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering=('name',)

@admin.register(Doctor)
class Specialty (admin.ModelAdmin):
    list_display=('last_name','first_name','license_number','phone')
    search_fields=('specialties',)
    ordering=('last_name',)

@admin.register(Patient)
class Specialty (admin.ModelAdmin):
    list_display=('last_name','first_name','phone')
    search_fields=('last_name','first_name','national_id')
    ordering=('last_name',)
    inlines = [AppointmentInline]

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets= UserAdmin.add_fieldsets+ (
    ( 'Informations personnelles' , {'fields': ('first_name', 'last_name','email')}),)




        
     

# Register your models here.
