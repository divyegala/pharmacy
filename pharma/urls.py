from django.conf.urls import url, include
from . import views

app_name = 'pharma'

urlpatterns = [

    # /pharma/
    url(r'^$', views.index, name='index'),

    # /pharma/doctor/
    url(r'^doctor/$', views.doctor, name='doctor'),

    # /pharma/medicine/
    url(r'^medicine/$', views.medicine, name='medicine'),

    # /pharma/nonmedicine/
    url(r'^nonmedicine/$', views.nonmedicine, name='nonmedicine'),

    # /pharma/staff/
    url(r'^staff/$', views.staff, name='staff'),

    # /pharma/docs/Andheri
    url(r'^docs/(?P<site>[a-zA-Z]+)/$', views.dispdocs, name='dispdocs'),

    # /pharma/meds/Andheri
    url(r'^meds/(?P<site>[a-zA-Z]+)/$', views.dispmeds, name='dispmeds'),

    # /pharma/nonmeds/Andheri
    url(r'^nonmeds/(?P<site>[a-zA-Z]+)/$', views.dispnonmeds, name='dispnonmeds'),

    # /pharma/staff/Andheri
    url(r'^staff/(?P<site>[a-zA-Z]+)/$', views.dispstaff, name='dispstaff'),
# url(r'^staff/$', views.staff, name='staff'),

    url(r'^get_doctor/$', views.get_doctor),

    url(r'^get_medicine/$', views.get_medicine),

    url(r'^get_non_medicine/$', views.get_non_medicine),

    url(r'^get_staff/$', views.get_staff),

]