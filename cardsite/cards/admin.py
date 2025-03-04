from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Posts, Category


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'images', 'post_image', 'cat', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_image']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    list_display = ('title', 'post_image', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    save_on_top = True


    @admin.display(description='Изображение', ordering='content')
    def post_image(self, posts: Posts):
        if posts.images:
            return mark_safe(f"<img src='{posts.images.url}' width=50>")
        else:
            return "Без изображения"


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

