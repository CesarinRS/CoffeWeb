from .models import Link

def context(request):
    contxt = {}
    links = Link.objects.all()
    for link in links:
        contxt[link.key] = link.url
    return contxt