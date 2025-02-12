from django.contrib import admin, messages
from .models import Posts, Category


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']


    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, posts: Posts):
        return f"Содержит {len(posts.content)} символов"


    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Posts.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей")


    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Posts.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

