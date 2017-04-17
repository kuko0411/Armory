from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Item)
admin.site.register(ItemData)
admin.site.register(EquipmentData)
admin.site.register(Passivity)
admin.site.register(ItemPassivity)
admin.site.register(ItemDataPassivity)