from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bet, Line

@admin.register(Bet) 
class BetAdmin(SummernoteModelAdmin):    
    list_display = ('punter', 'stake', 'settled_amount', 'updated_on')
    search_fields = ['punter', 'status']
    list_filter = ('punter', 'created_on', 'status')


# Register your models here.
admin.site.register(Line)