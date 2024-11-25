from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(CommentReaction)


