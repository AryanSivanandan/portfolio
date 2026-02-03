from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Project, Experience
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # ✅ REQUIRED

        context["projects"] = Project.objects.order_by("-featured", "-id")
        context["experiences"] = Experience.objects.all()
        context["form"] = ContactForm()

        return context


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "partials/contact_success.html")

    return render(request, "partials/contact_form.html", {"form": form})
