from django.conf.urls import url
from . import views as v

urlpatterns = [
    # post views

    url(r'^$', v.posts_list, name='posts_list'),
    url(r'^post_detail/(?P<post_id>\d+)/$', v.post_detail, name='post_detail'),
    url(r'^login/$', v.log_in, name='login'),
    url(r'^logout/$', v.log_out, name='logout'),
    url(r'^create_new_post/$', v.create_new_post, name='create_new_post'),
    url(r'^registration/$', v.registration, name='registration'),

]