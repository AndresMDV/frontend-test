import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic


class ProductListView(generic.TemplateView):
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        product_filter = request.GET.get("filter", None)
        products = json.loads(open("products.json").read())["products"]

        if product_filter:
            try:
                products = [
                    product
                    for product in products
                    if product["filterId"] == int(product_filter)
                ]

            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON payload"}, status=400)

        if request.headers.get("HX-Request"):
            return render(
                request,
                "list.html",
                {
                    "products": products,
                },
            )
        return render(
            request,
            "home.html",
            {
                "products": products,
            },
        )
