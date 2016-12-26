from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from marks.forms import WeightCreateForm, ProfessionalismMarkCreateForm, ControlMarkCreateForm, \
    ClientOrientationMarkCreateForm, CommunicationMarkCreateForm, EfficiencyMarkCreateForm, EvolutionMarkCreateForm, \
    TeamworkMarkCreateForm, LeadershipMarkCreateForm
from marks.models import Weight, ClientOrientationMark, ControlMark, CommunicationMark, ProfessionalismMark, \
    EfficiencyMark, EvolutionMark, LeadershipMark, TeamworkMark


class SuccessMixin(CreateView):
    success_url = reverse_lazy("core:test")
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id', None)
        if user_id:
            form.instance.who_rated = self.request.user
            form.instance.rated_user = User.objects.filter(id=user_id).first()
            return super(SuccessMixin, self).form_valid(form)
        else:
            return


class WeightCreateView(SuccessMixin):
    model = Weight
    form_class = WeightCreateForm


class ProfessionalismMarkCreateView(SuccessMixin):
    model = ProfessionalismMark
    form_class = ProfessionalismMarkCreateForm


class ControlMarkCreateView(SuccessMixin):
    model = ControlMark
    form_class = ControlMarkCreateForm


class CommunicationMarkCreateView(SuccessMixin):
    model = CommunicationMark
    form_class = CommunicationMarkCreateForm


class ClientOrientationMarkCreateView(SuccessMixin):
    model = ClientOrientationMark
    form_class = ClientOrientationMarkCreateForm


class EfficiencyMarkCreateView(SuccessMixin):
    model = EfficiencyMark
    form_class = EfficiencyMarkCreateForm


class EvolutionMarkCreateView(SuccessMixin):
    model = EvolutionMark
    form_class = EvolutionMarkCreateForm


class LeadershipMarkCreateView(SuccessMixin):
    model = LeadershipMark
    form_class = LeadershipMarkCreateForm


class TeamworkMarkCreateView(SuccessMixin):
    model = TeamworkMark
    form_class = TeamworkMarkCreateForm


