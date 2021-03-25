from django.urls import path
from events import views

urlpatterns = [
    path("eventAnalytics/topevents", views.EventOperationsClientViewTopEvent.as_view()),
    path("eventAnalytics/filterEvents", views.EventOperationsClientViewFilterEvent.as_view()),
    path("eventAnalytics/countEvents", views.EventOperationsClientViewCountEvent.as_view()),
    path("eventAnalytics/removeDuplicateEvents", views.EventOperationsClientViewRemoveDuplicateEvent.as_view()),
    path("eventAnalytics/matchEventPattern", views.PatternOperationsClientViewMatchPatternsOverEvents.as_view()),
]
