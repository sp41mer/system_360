from django.views.generic import CreateView

from marks.forms import WeightCreateForm, ProfessionalismMarkCreateForm, ControlMarkCreateForm, \
    ClientOrientationMarkCreateForm, CommunicationMarkCreateForm, EfficiencyMarkCreateForm, EvolutionMarkCreateForm, \
    TeamworkMarkCreateForm, LeadershipMarkCreateForm
from marks.models import Weight, ClientOrientationMark, ControlMark, CommunicationMark, ProfessionalismMark, \
    EfficiencyMark, EvolutionMark, LeadershipMark, TeamworkMark


class WeightCreateView(CreateView):
    model = Weight
    form_class = WeightCreateForm
    template_name_suffix = "_create_form"


class ProfessionalismMarkCreateView(CreateView):
    model = ProfessionalismMark
    form_class = ProfessionalismMarkCreateForm
    template_name_suffix = "_create_form"


class ControlMarkCreateView(CreateView):
    model = ControlMark
    form_class = ControlMarkCreateForm
    template_name_suffix = "_create_form"


class CommunicationMarkCreateView(CreateView):
    model = CommunicationMark
    form_class = CommunicationMarkCreateForm
    template_name_suffix = "_create_form"


class ClientOrientationMarkCreateView(CreateView):
    model = ClientOrientationMark
    form_class = ClientOrientationMarkCreateForm
    template_name_suffix = "_create_form"


class EfficiencyMarkCreateView(CreateView):
    model = EfficiencyMark
    form_class = EfficiencyMarkCreateForm
    template_name_suffix = "_create_form"


class EvolutionMarkCreateView(CreateView):
    model = EvolutionMark
    form_class = EvolutionMarkCreateForm
    template_name_suffix = "_create_form"


class LeadershipMarkCreateView(CreateView):
    model = LeadershipMark
    form_class = LeadershipMarkCreateForm
    template_name_suffix = "_create_form"


class TeamworkMarkCreateView(CreateView):
    model = TeamworkMark
    form_class = TeamworkMarkCreateForm
    template_name_suffix = "_create_form"


