from django.contrib import admin
from vendor.models import Vendor


# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user','vendor_name', 'vendor_licence', 'is_approved', 'create_at', 'modified_at')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_approved',)
    

    

admin.site.register(Vendor,VendorAdmin)