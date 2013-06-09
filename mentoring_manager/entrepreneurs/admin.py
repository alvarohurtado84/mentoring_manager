from django.contrib import admin

from entrepreneurs.models import Entrepreneur
from entrepreneurs.models import Startup

class StartupInline(admin.TabularInline):
    model = Startup
    
class EntrepreneurAdmin(admin.ModelAdmin):
    inlines = [ StartupInline, ]

admin.site.register(Entrepreneur, EntrepreneurAdmin)
admin.site.register(Startup)
