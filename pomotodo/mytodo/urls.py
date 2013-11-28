from django.conf.urls import include,url,patterns
from mytodo import views


urlpatterns=patterns('',
		url(r'^$',views.ListProjectView.as_view(),name='index'),
	)