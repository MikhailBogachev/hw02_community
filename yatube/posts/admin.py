from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Класс кастомизации модели Post"""

    list_display: tuple[str] = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable: tuple[str] = ('group',)
    search_fields: tuple[str] = ('text',)
    list_filter: tuple[str] = ('pub_date',)
    empty_value_display: str = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Класс кастомизации модели Post"""

    list_display: tuple[str] = ('pk', 'title', 'description',)
    search_fields: tuple[str] = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
