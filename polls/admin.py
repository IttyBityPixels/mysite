from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
