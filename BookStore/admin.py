from django.contrib import admin
from BookStore.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Cart)