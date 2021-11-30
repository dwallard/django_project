from django.contrib import admin

# Register your models here.

from .models import Booking, Album, Contact, Artist


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']
    readonly_fields = ["created_at","contact","album","contacted"]
    def has_add_permission(self, request):
        return False


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

class BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ] # list columns
    extra = 0
    readonly_fields = ["created_at", "album","contacted"]
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    def has_add_permission(self, request, Obj):
        return False
   

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,] # list of bookings made by a contact
   

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]


