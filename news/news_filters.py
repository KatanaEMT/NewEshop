from .models import New
import django_filters
from .news_forms import DatePicker


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Заголовок"
    )
    article = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Описание"
    )

    views_qty = django_filters.RangeFilter(
        field_name='views_qty',
    )

    class Meta:
        model = New
        fields = [
            'title', 'article',
            'category',
            'views_qty',
        ]