from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("appointment_date","patient","doctor","status","duration_minutes","has_prescription",)
    list_filter = ("status", "appointment_date", "doctor")
    search_fields = ("patient__last_name","patient__first_name","doctor__last_name","doctor__first_name","reason",)
    ordering = ("-appointment_date",)
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("patient", "doctor")

    @admin.display(boolean=True, description="Ordonnance")
    def has_prescription(self, obj):
        return bool(obj.prescription)

# Register your models here.
