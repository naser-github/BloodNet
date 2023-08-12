from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import BloodGroup

from .models import Division
from .models import District
from .models import Thana

User = get_user_model()

class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ['name']


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'division_id', 'division_name', 'status']

    def division_id(self, obj):
        return obj.division.id

    def division_name(self, obj):
        return obj.division.name


class ThanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district_id', 'district_name',
                    'division_id', 'division_name', 'status']

    def district_id(self, obj):
        return obj.district.id

    def district_name(self, obj):
        return obj.district.name

    def division_id(self, obj):
        return obj.district.division.id

    def division_name(self, obj):
        return obj.district.division.name


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email', 'phone', 'blood_group_name', 'can_donate', 'is_active']
#
#     def blood_group_name(self, obj):
#         return obj.blood_group.name
#
#
admin.site.register(User)

admin.site.register(Thana, ThanaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Division, DivisionAdmin)

admin.site.register(BloodGroup, BloodGroupAdmin)
