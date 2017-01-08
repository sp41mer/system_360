from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django.views import View

from interview.models import Interview


class AccessMixin(View):
    def dispatch(self, request, *args, **kwargs):
        now = timezone.now().date()
        selection = Interview.objects.filter(Q(start_date__lte=now) & Q(end_date__gte=now)).first()

        if not selection:
            raise Http404

        self.eval_user = selection.users_to_eval.filter(eval_user=self.request.user).first()

        pk = kwargs.get('pk', None)
        user_ids_to_exclude = self.eval_user.already_estimated_users.all().values_list('id', flat=True)
        if pk and pk not in [str(el) for el in self.eval_user.estimated_users.exclude(id__in=user_ids_to_exclude).values_list('id', flat=True)]:
                raise Http404

        if self.eval_user:
            return super(AccessMixin, self).dispatch(request)
        else:
            raise Http404
