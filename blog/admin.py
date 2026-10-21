from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'slug', 'image', 'published_at')
	raw_id_fields = ('author', 'tags', 'likes')

class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
	raw_id_fields = ('author', 'post')
	list_display = ('id', 'text', 'published_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)