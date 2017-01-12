from django.db.models import Avg
from django.db.models import Q
from django.utils import timezone
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

from core.mixins import AccessMixin
from core.models import User
from interview.models import Interview
from marks.forms import WeightCreateForm, ProfessionalismMarkCreateForm, ControlMarkCreateForm, \
    ClientOrientationMarkCreateForm, CommunicationMarkCreateForm, EfficiencyMarkCreateForm, EvolutionMarkCreateForm, \
    TeamworkMarkCreateForm, LeadershipMarkCreateForm
from marks.models import Weight, ClientOrientationMark, ControlMark, CommunicationMark, ProfessionalismMark, \
    EfficiencyMark, EvolutionMark, LeadershipMark, TeamworkMark


list_of_marks = [
    ProfessionalismMark, ControlMark, 
    CommunicationMark, ClientOrientationMark, EfficiencyMark, 
    EvolutionMark, LeadershipMark, TeamworkMark
]

class SuccessCreateView(CreateView):
    success_url = reverse_lazy("interview:estimate_list")
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id', None)
        if user_id:
            form.instance.who_rated = self.request.user
            form.instance.rated_user = User.objects.filter(id=user_id).first()
            return super(SuccessCreateView, self).form_valid(form)
        else:
            return ValueError


class WeightCreateView(SuccessCreateView):
    model = Weight
    form_class = WeightCreateForm


class ProfessionalismMarkCreateView(SuccessCreateView):
    model = ProfessionalismMark
    form_class = ProfessionalismMarkCreateForm


class ControlMarkCreateView(SuccessCreateView):
    model = ControlMark
    form_class = ControlMarkCreateForm


class CommunicationMarkCreateView(SuccessCreateView):
    model = CommunicationMark
    form_class = CommunicationMarkCreateForm


class ClientOrientationMarkCreateView(SuccessCreateView):
    model = ClientOrientationMark
    form_class = ClientOrientationMarkCreateForm


class EfficiencyMarkCreateView(SuccessCreateView):
    model = EfficiencyMark
    form_class = EfficiencyMarkCreateForm


class EvolutionMarkCreateView(SuccessCreateView):
    model = EvolutionMark
    form_class = EvolutionMarkCreateForm


class LeadershipMarkCreateView(SuccessCreateView):
    model = LeadershipMark
    form_class = LeadershipMarkCreateForm


class TeamworkMarkCreateView(SuccessCreateView):
    model = TeamworkMark
    form_class = TeamworkMarkCreateForm

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id', None)
        if user_id:
            now = timezone.now().date()
            selection = Interview.objects.filter(Q(start_date__lte=now) & Q(end_date__gte=now)).first()

            if not selection:
                raise Http404

            already_estimated_users = selection.users_to_eval.filter(eval_user=self.request.user).first().already_estimated_users
            estimated_user = User.objects.filter(id=user_id).first()
            already_estimated_users.add(estimated_user)
        return super(TeamworkMarkCreateView, self).form_valid(form)

#TODO: Optimize that shit
class ResultView(TemplateView):
    template_name = 'marks/result_view.html'
    def get_context_data(self, **kwargs):
        res = super(ResultView, self).get_context_data(**kwargs)
        pk = kwargs.get("pk")
        user = res.get('view').request.user.id
        if pk:
            self.user = User.objects.filter(id=pk).first()
            now = timezone.now().date()
            selection = Interview.objects.filter(Q(start_date__lte=now) & Q(end_date__gte=now)).first()

            weight_query = Weight.objects.filter(Q(rated_user=pk) & 
                                                 Q(date_create__lte=selection.end_date) & 
                                                 Q(date_create__gte=selection.start_date) &
                                                 Q(who_rated=user))
            
            professionalism_mark_query = ProfessionalismMark.objects.filter(Q(rated_user=pk) & 
                                                 Q(date_create__lte=selection.end_date) & 
                                                 Q(date_create__gte=selection.start_date) &
                                                 Q(who_rated=user))
            professionalism_mark = professionalism_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            professionalism_mark_count = len(
                ProfessionalismMark._meta.get_fields(include_parents=False,include_hidden=False))-2
            professionalism_mark_weight = weight_query.aggregate(
                Avg('professionalism')).get('professionalism__avg')
            control_mark_query = ControlMark.objects.filter(Q(rated_user=pk) &
                                                            Q(date_create__lte=selection.end_date) &
                                                            Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            control_mark = control_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            control_mark_weight = weight_query.aggregate(
                Avg('control')).get('control__avg')
            control_mark_count = len(
                ControlMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            commnication_mark_query = CommunicationMark.objects.filter(Q(rated_user=pk) &
                                                                       Q(date_create__lte=selection.end_date) &
                                                                       Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            communication_mark = commnication_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            communication_mark_weight = weight_query.aggregate(
                Avg('communication')).get('communication__avg')
            communication_mark_count = len(
                CommunicationMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            client_orientation_mark_query = ClientOrientationMark.objects.filter(Q(rated_user=pk) &
                                                                                 Q(date_create__lte=selection.end_date) &
                                                                                 Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            client_orientation_mark = client_orientation_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            client_orientation_weight = weight_query.aggregate(
                Avg('client_orientation')).get('client_orientation__avg')
            client_orientation_mark_count = len(
                ClientOrientationMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            efficiency_mark_query = EfficiencyMark.objects.filter(Q(rated_user=pk) &
                                                                  Q(date_create__lte=selection.end_date) &
                                                                  Q(date_create__gte=selection.start_date) &
                                                                  Q(who_rated=user))
            efficiency_mark = efficiency_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            efficiency_mark_weight = weight_query.aggregate(
                Avg('efficiency')).get('efficiency__avg')
            efficiency_mark_count = len(
                EfficiencyMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            evolution_mark_query = EvolutionMark.objects.filter(Q(rated_user=pk) &
                                                                Q(date_create__lte=selection.end_date) &
                                                                Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            evolution_mark = evolution_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            evolution_mark_weight = weight_query.aggregate(
                Avg('evolution')).get('evolution__avg')
            evolution_mark_count = len(
                EvolutionMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            leadership_mark_query = LeadershipMark.objects.filter(Q(rated_user=pk) &
                                                                  Q(date_create__lte=selection.end_date) &
                                                                  Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            leadership_mark = leadership_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            leadership_mark_weight = weight_query.aggregate(
                Avg('leader')).get('leader__avg')
            leadership_mark_count = len(
                LeadershipMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2
            teamwork_mark_query = TeamworkMark.objects.filter(Q(rated_user=pk) &
                                                              Q(date_create__lte=selection.end_date) &
                                                              Q(date_create__gte=selection.start_date)&
                                                 Q(who_rated=user))
            teamwork_mark = teamwork_mark_query.aggregate(Avg('sum_of_all')).get('sum_of_all__avg')
            teamwork_mark_weight = weight_query.aggregate(
                Avg('teamwork')).get('teamwork__avg')
            teamwork_mark_count = len(
                TeamworkMark._meta.get_fields(include_parents=False, include_hidden=False)) - 2

            self.prof_kpi = self.calculate_mark(professionalism_mark_weight, professionalism_mark, professionalism_mark_count)
            self.control_kpi = self.calculate_mark(control_mark_weight, control_mark, control_mark_count)
            self.communication_kpi = self.calculate_mark(communication_mark_weight, communication_mark, communication_mark_count)
            self.client_orientation_kpi = self.calculate_mark(client_orientation_weight, client_orientation_mark, client_orientation_mark_count)
            self.efficeincy_kpi = self.calculate_mark(efficiency_mark_weight, efficiency_mark, efficiency_mark_count)
            self.evolution_kpi = self.calculate_mark(evolution_mark_weight, evolution_mark, evolution_mark_count)
            self.leadership_kpi = self.calculate_mark(leadership_mark_weight, leadership_mark, leadership_mark_count)
            self.teamwork_kpi = self.calculate_mark(teamwork_mark_weight, teamwork_mark, teamwork_mark_count)

        res.update({
            "user": self.user,
            "prof_kpi": self.prof_kpi,
            "control_kpi": self.control_kpi,
            "communication_kpi": self.communication_kpi,
            "client_orientation_kpi": self.client_orientation_kpi,
            "efficeincy_kpi": self.efficeincy_kpi,
            "evolution_kpi": self.evolution_kpi,
            "leadership_kpi": self.leadership_kpi,
            "teamwork_kpi": self.teamwork_kpi
        })
        return res

    def calculate_mark(self,weight,mark,number):
        marks_and_weights = weight*mark
        max_mark = weight*number*10
        kpi = marks_and_weights/float(max_mark)
        return kpi

