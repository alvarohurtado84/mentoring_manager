from django.contrib import admin

from mentors.models import Mentor
from entrepreneurs.models import Entrepreneur
from entrepreneurs.models import Startup
from people.models import Person

class EntrepreneurInline(admin.TabularInline):
    model = Entrepreneur
    
class MentorInline(admin.StackedInline):
    model = Mentor
    
class PersonAdmin(admin.ModelAdmin):
    inlines = [ MentorInline, EntrepreneurInline, ]
    list_display = ('user', 'is_mentor', 'is_entrepreneur', )


admin.site.register(Person, PersonAdmin)
