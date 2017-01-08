from django.contrib import admin

from interview.models import Evaluating, Interview


class EvaluatingAdmin(admin.ModelAdmin):
    exclude = ['already_estimated_users']

admin.site.register(Evaluating, EvaluatingAdmin)
admin.site.register(Interview)
