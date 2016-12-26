from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
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
            return ValueError


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


class ResultView(View):
    def dispatch(self, request, *args, **kwargs):
        res = super(ResultView, self).dispatch(request, args, kwargs)
        pk = kwargs.get("pk")
        if pk:
            # place your code here
            teamwork_mark = TeamworkMark.objects.filter(id=pk)
            self.full_mark = 123213

        return res

    def get_context_data(self, **kwargs):
        res = super(ResultView, self).get_context_data()

        res.update({
            "fill_mark": self.full_mark
        })

        return res
