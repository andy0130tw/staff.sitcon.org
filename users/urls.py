from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
        url(r'^$', views.list, name='list'),
        url(r'^reg$', views.reg_list_token, name='reg_list_token'),
        url(r'^reg/add$', views.reg_add_token, name='reg_add_token'),
        url(r'^reg/edit/(?P<token>[0-9A-Za-z]+)$', views.reg_edit_token, name='reg_edit_token'),
        url(r'^reg/form/(?P<token>[0-9A-Za-z]+)$', views.reg_form, name='reg_form'),
        url(r'^login$', views.login, name='login'),
        url(r'^logout$', views.logout, name='logout'),
        url(r'^new$', views.create, name='create'),
        url(r'^contacts$', views.contacts, name='contacts'),
        url(r'^contacts/export(?:/(?P<format>[0-9A-Za-z]+))?$', views.export, name='export'),
        url(r'^password/change$', views.change_password, name='change_password'),
        url(r'^password/reset$', views.reset_password, name='reset_password'),
        url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)$', views.reset_password_confirm, name='reset_password_confirm'),
        url(r'^me$', views.me, name='me'),
        url(r'^(?P<username>[0-9A-Za-z_@\+\.\-]+)$', views.profile, name='profile'),
        url(r'^(?P<username>[0-9A-Za-z_@\+\.\-]+)/edit$', views.edit, name='edit'),
        url(r'^(?P<username>[0-9A-Za-z_@\+\.\-]+)/edit/fancy$', views.edit, name='edit fancy', kwargs={'fancy': True}),
		url(r'^(?P<username_or_pk>[0-9A-Za-z_@\+\.\-]+)/photo$', views.photo.general, name='photo_general'),
		url(r'^(?P<username_or_pk>[0-9A-Za-z_@\+\.\-]+)/photo/small$', views.photo.small, name='photo_small'),
		url(r'^(?P<username_or_pk>[0-9A-Za-z_@\+\.\-]+)/photo/medium$', views.photo.medium, name='photo_medium'),
    )
