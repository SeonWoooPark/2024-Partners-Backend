from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse

from .forms import ShortLinkForm
from .models import ShortLinkModel

def index(request):
    return render(request, "url_main.html")

def url_create(request):
    if request.method == "POST":
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            if len(ShortLinkModel.objects.filter(origin_url=url.origin_url)) == 0:
                url.hash_value = hash(url.origin_url)
                url.short_url = f"localhost:8000/short-links/{url.hash_value}"
                url.create_date = timezone.now()
                url.save()
                context = {'short_url': url.short_url, 'origin_url': url.origin_url}

                return render(request, 'url_create.html', context)
            else:
                exist_model = ShortLinkModel.objects.filter(origin_url=url.origin_url)[0]
                context = {'short_url': exist_model.short_url, 'origin_url': exist_model.origin_url}

                return render(request, 'url_create.html', context)
    else:
        short_url = "none"
    context = {'short_url': "none"}

    return render(request, 'url_create.html', context)


def url_redirect(request, hash_value):
    # url = get_object_or_404(ShortLinkModel, pk=hash_value)
    url = ShortLinkModel.objects.filter(hash_value=hash_value)
    if len(url) == 0:
        return HttpResponse("해당 Short URL이 존재하지 않습니다.")

    origin_url = "https://" + url[0].origin_url
    return redirect(origin_url)
