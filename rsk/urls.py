from django.urls import path
from rsk import views
app_name="rsk"


urlpatterns = [
    path('index/',views.index,name="index"),
    path('first/',views.first,name="first"),
    path('second/',views.second,name="second"),
    path('third/',views.third,name="third"),
    path('fourth/',views.fourth,name="fourth"),
    path('urls_data/<name>',views.urls_data,name="urls_data"),
    path('urls_data1/<ab>',views.urls_data1,name="urls_data1"),
    path('urls_data2/<c>/<d>',views.urls_data2,name="urls_data2"),
    path('urls_data3/<greater>',views.urls_data3,name="urls_data3"),
    path('urls_data4/<string>',views.urls_data4,name="urls_data4")
]