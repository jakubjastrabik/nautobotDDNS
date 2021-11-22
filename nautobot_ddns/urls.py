from django.urls import path

from . import views
# from .views import ExtraDNSNameCreateView, ExtraDNSNameDeleteView, ExtraDNSNameEditView, IPAddressDNSNameRecreateView

urlpatterns = [
    path("ip-addresses/<uuid:ipaddress_pk>/recreate/", views.IPAddressDNSNameRecreateView.as_view(), name='ipaddress_dnsname_recreate'),
    path("ip-addresses/<uuid:ipaddress_pk>/extra/create/", views.ExtraDNSNameCreateView.as_view(), name='extradnsname_create'),
    path("ip-addresses/<uuid:ipaddress_pk>/extra/<int:pk>/edit/", views.ExtraDNSNameEditView.as_view(), name='extradnsname_edit'),
    path("ip-addresses/<uuid:ipaddress_pk>/extra/<int:pk>/delete/", views.ExtraDNSNameDeleteView.as_view(), name='extradnsname_delete'),
]
