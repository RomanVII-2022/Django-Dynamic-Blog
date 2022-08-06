from django.contrib import admin
from .models import Post, Subscriber, MailMessage, Contact

# Register your models here.
admin.site.register(Post)
admin.site.register(Subscriber)
admin.site.register(MailMessage)
admin.site.register(Contact)