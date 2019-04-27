from django_filters import filters
from django_filters import FilterSet
from .models import CodeModel


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順)'



class ItemFilter(FilterSet):
    tags = filters.CharFilter(label='タグ',lookup_expr='contains')
    title = filters.CharFilter(label='タイトル',look_expr='contains')



    order_by = MyOrderingFilter(
            fields = (
            ('tags','tags'),
            ('title','title'),
            ),
            field_labels = {
            'tags':'タグ',
            'title':'タイトル',
            },
            label='並び順'
    )
    class Meta:
        model = CodeModel
        fields = ('title','tags','name')
