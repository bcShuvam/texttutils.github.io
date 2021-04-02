"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from . import Exercise1
# from . import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index', Exercise1.facebook_url,name='index'),
#     path('home',views.home,name='home'),
#     path('about',views.about,name='about')
# ]

###################################################################################################

# from . import viewsPipeline2
# from . import layingPipeline2
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', viewsPipeline2.index1,name="index1"),
#     path('removepunc', viewsPipeline2.removepunc,name="rempunc"),
#     path('capitalizefirst', viewsPipeline2.capfirst,name="capfirst"),
#     path('newlineremove', viewsPipeline2.removenewline,name="removenewline"),
#     path('spaceremover', viewsPipeline2.spaceremove,name="spaceremove"),
#     path('charcount', viewsPipeline2.charcount,name="charcount")
# ]

#####################################################################################################

# from . import viewsTemplates3
#
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',viewsTemplates3.index,name="index"),
# ]

#####################################################################################################

# from . import viewsHomepage4
#
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',viewsHomepage4.index,name="index"),
#     path('analyze',viewsHomepage4.analyze,name='analyze')
#     # path('removepunc',viewsHomepage4.removepunc,name="rempun"),
#     # path('capitalizefirst',viewsHomepage4.removepunc,name="capfirst"),
#     # path('newlinerremove',viewsHomepage4.removepunc,name="newlineremove"),
#     # path('spaceremove',viewsHomepage4.removepunc,name="spaceremove"),
#     # path('charcount',viewsHomepage4.removepunc,name="charcount"),
# ]

from django.contrib import admin
from django.urls import path
from . import viewsHomepage4

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', viewsHomepage4.index, name='index'),
   path('analyze', viewsHomepage4.analyze, name='analyze')
]

