from django.contrib import admin
from .models import Post, Comment, Categoria, Tag
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug' ,'introducao', 'status','created_on','categoria')
    list_filter = ("status","categoria")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(Categoria, admin.ModelAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
