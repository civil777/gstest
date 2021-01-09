from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render, redirect
#from django.urls import reverse
from . import models, forms

class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        #return redirect(reverse("core:home"))
        raise Http404()

class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        name = request.GET.get("name")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                item_type = form.cleaned_data.get("item_type")
                price = form.cleaned_data.get("price")
                인증_회원 = form.cleaned_data.get("인증_회원")

                filter_args = {}

                if name != "여기에+물품을+검색하세요":
                    filter_args["name__startswith"] = name


                if item_type is not None:
                    filter_args["item_type"] = item_type

                if price is not None:
                    filter_args["price__lte"] = price

                if 특가_상품 is True:
                    filter_args["특가_상품__superhost"] = True

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})
