from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.base,name="base"), #http://localhost:8000/blog
    url(r'^me_index/$', views.me_index,name="me_index"), #http://localhost:8000/blog
    url(r'^me_new/$',views.me_new, name="me_new"),  #http://localhost:8000/blog/new/ 뷰에있는 포스트뉴에 있는 걸가져올거야
    url(r'^(?P<me_id>\d+)/$', views.me_detail, name="me_detail"), #http://localhost:8000/blog/1
    url(r'^(?P<me_id>\d+)/edit/$', views.me_edit, name="me_edit"), #http://localhost:8000/blog/edit
    url(r'^(?P<me_id>\d+)/delete/$', views.me_delete, name="me_delete"), #http://localhost:8000/blog/edit

    url(r'^ask_new/$',views.ask_new, name="ask_new"),  #http://localhost:8000/blog/new/ 뷰에있는 포스트뉴에 있는 걸가져올거야
    url(r'^ask_index/$',views.ask_index, name="ask_index"),        
    url(r'^ask_(?P<ask_id>\d+)/$', views.ask_detail, name="ask_detail"), #http://localhost:8000/blog/1
    url(r'^ask_(?P<ask_id>\d+)/edit/$', views.ask_edit, name="ask_edit"), #http://localhost:8000/blog/edit
    url(r'^ask_(?P<ask_id>\d+)/delete/$', views.ask_delete, name="ask_delete"), #http://localhost:8000/blog/edit
    url(r'^ask_(?P<ask_id>\d+)/comment/$', views.add_comment_to_ask, name="add_comment_to_ask"), #http://localhost:8000/blog/me/123/comment
    url(r'^comment_(?P<comment_id>\d+)/delete/$', views.comment_delete, name="comment_delete"), #http://localhost:8000/blog/me/123/comment

]
#ask index