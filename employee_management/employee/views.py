from django.views import generic
from .forms import SearchForm
from .models import Employee


class IndexView(generic.ListView):
    model = Employee
    paginate_by = 5     # 何件でページを切り替えるかを指定

    def get_context_data(self):
        # テンプレートに渡す辞書の作成
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)  # 基の辞書に、formを追加
        return context

    def get_queryset(self):
        # テンプレートへ渡す「employee_list」を作成する
        form = SearchForm(self.request.GET)
        form.is_valid()     # これをしないと、cleaned_dataができない！

        # 全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        # 部署の選択があれば、部署で絞り込み(filter)
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)
        return queryset
