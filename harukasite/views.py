from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class NewsView(TemplateView):
    template_name = 'news.html'

class BiographyView(TemplateView):
    template_name = 'biography.html'