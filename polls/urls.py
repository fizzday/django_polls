from django.conf.urls import url
from . import views,views_interface


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # polls interface
    # ex : /polls/questions/
    url(r'^questions/$', views_interface.questions, name='questions'),
    # ex : /polls/question_option/
    url(r'^question_option/$', views_interface.question_option, name='question_option'),
    # ex : /polls/question_result/
    url(r'^question_result/$', views_interface.question_result, name='question_result'),
    # ex : /polls/question_vote/
    url(r'^question_vote/$', views_interface.question_vote, name='question_vote'),
]
