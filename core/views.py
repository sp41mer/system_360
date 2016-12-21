from django.views.generic import TemplateView


class Fish(TemplateView):
    template_name = 'index.html'
