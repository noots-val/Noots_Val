from django.views.generic import ListView
from .models import Assertion
from .models import Objective


class AssertionIndexView(ListView):
    template_name = "assertion_index.html"
    model = Assertion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objective_list"] = Objective.objects.all()
        return context
