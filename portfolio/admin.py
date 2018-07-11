from django.contrib import admin
from .models import Portfolio


#Admin Dashboard add content
admin.site.site_title='Klondike-X'
admin.site.site_header = 'Klonike-X Admin Dashboard'
admin.site.index_title = 'Welcome to Klondike-X Dashboard'



#Admin Dashboard categories/forms
admin.site.register(Portfolio)
