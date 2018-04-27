from django.contrib import admin
from .models import Question, Choice, Comment, Voted


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class CommentInline(admin.TabularInline):
    model = Comment


class QuestionInline(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['date_pub']}),
    ]
    inlines = [ChoiceInline, CommentInline]
    list_display = ('question_text', 'date_pub', 'user')
    list_filter = ['date_pub']
    search_fields = ['question_text']


class VotedAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('User', {'fields': ['user']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Voted, VotedAdmin)
