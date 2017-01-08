from django.http import Http404
from django.views.generic import DetailView
from django.views.generic import ListView

from core.mixins import AccessMixin
from core.models import User
from marks.forms import WeightCreateForm, ProfessionalismMarkCreateForm, ControlMarkCreateForm, \
    CommunicationMarkCreateForm, ClientOrientationMarkCreateForm, EfficiencyMarkCreateForm, EvolutionMarkCreateForm, \
    TeamworkMarkCreateForm, LeadershipMarkCreateForm


class Main360System(DetailView, AccessMixin):
    model = User
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        res = super(Main360System, self).get_context_data()

        res.update({
            "weight_form": WeightCreateForm,
            "professionalism_mark": ProfessionalismMarkCreateForm,
            "control_mark": ControlMarkCreateForm,
            "communication_mark": CommunicationMarkCreateForm,
            "client_orientation_mark": ClientOrientationMarkCreateForm,
            "efficiency_mark": EfficiencyMarkCreateForm,
            "evolution_mark": EvolutionMarkCreateForm,
            "leadership_mark": LeadershipMarkCreateForm,
            "teamwork_mark": TeamworkMarkCreateForm,
        })

        return res
