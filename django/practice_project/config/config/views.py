from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['home_desc'] = 'This is just to demonstrate content injection'
        return context