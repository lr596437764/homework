from rest_framework.routers import SimpleRouter

from News.views import  *
urlpatterns=[


]
router=SimpleRouter()
router.register(r"API/Food",Foods_View)