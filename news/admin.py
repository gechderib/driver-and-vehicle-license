from django.contrib import admin
from .models import News, OfficeDirection, UserObligation, TicketAnnouncement
# Register your models here.

class NewsAdmin(admin.ModelAdmin):

 list_display = (
  'id',
  'title',
  'content',
  'created_at',
  'updated_at'
 )

class OfficeDirectionAdmin(admin.ModelAdmin):
  list_display = (
  'id',
  'name',
  'start_room',
  'end_room',
  'description',
  )
 

class UserObligationdmin(admin.ModelAdmin):
  list_display = (
  'id',
  'content',
 )
  

class Ticketdmin(admin.ModelAdmin):
  list_display = (
  'id',
  'current_ticket_number',
  'last_ticket_number',
  'updated_at'
 )
admin.site.register(News, NewsAdmin)
admin.site.register(OfficeDirection,OfficeDirectionAdmin)
admin.site.register(UserObligation,UserObligationdmin)
admin.site.register(TicketAnnouncement,Ticketdmin)

