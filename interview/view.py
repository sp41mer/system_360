from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView

from core.models import User
from interview.models import Interview


class EstimateUserListView(ListView):
    model = User

    def dispatch(self, request, *args, **kwargs):
        selection = Interview.objects.filter(start_date__gte=timezone.now()).first()
        self.eval_user = selection.users_to_eval.filter(eval_user=self.request.user).first()

        if self.eval_user:
            res = super(EstimateUserListView, self).dispatch(request)
            return res
        else:
            return Http404

    def get_context_data(self, **kwargs):
        context = super(EstimateUserListView, self).get_context_data()
        context['object_list'] = self.eval_user.estimated_users.all()
        return context
