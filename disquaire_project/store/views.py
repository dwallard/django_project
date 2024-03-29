from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Contact, Booking
from django.db import transaction, IntegrityError
from .forms import ContactForm, ParagraphErrorList 

# Create your views here.

def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]   
    context = {'albums':albums}
    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums': albums
    }
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            contact = Contact.objects.filter(email=email)
            try:
                with transaction.atomic():
                    if not contact.exists():
                        # If a contact is not registered, create a new one.
                        contact = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contact.first()
                    # If no album matches the id, it means the form must have been tweaked
                    # so returning a 404 is the best solution.
                    album = get_object_or_404(Album, id=album_id)
                    booking = Booking.objects.create(
                        contact=contact,
                        album=album
                    )
                # Make sure no one can book the album again.
                album.available = False
                album.save()
                context = {
                    'album_title': album.title
                }
                return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        # GET method. Creat a new form to be used in the template.
        form = ContactForm()
      
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'store/search.html', context)