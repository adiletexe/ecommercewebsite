from .models import Categories

def categories_link(request):
    links = Categories.objects.all
    return dict(links=links)