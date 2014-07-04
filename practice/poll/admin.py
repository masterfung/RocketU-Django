from django.contrib import admin
from poll.models import Poll, Choice

class ChoiceInline(admin.TabularInline): #tabular is table
    model = Choice #gives three
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] #adds more choices panels

    list_filter = ['pub_date'] #cool filter on the admin panel
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)