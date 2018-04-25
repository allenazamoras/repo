from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['date_pub']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'date_pub', 'user')
    list_filter = ['date_pub']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
