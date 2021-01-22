from django.urls import path
from events import views

urlpatterns = [
    path("eventanalytics/topevents", views.EventOperationsClientViewTopEvent.as_view()),
    path("eventanalytics/filterevents", views.EventOperationsClientViewFilterEvent.as_view()),
    path("eventanalytics/countevents", views.EventOperationsClientViewCountEvent.as_view()),
    path("eventanalytics/removeduplicateevent", views.EventOperationsClientViewRemoveDuplicateEvent.as_view()),
    path("eventanalytics/patternmatching", views.PatternOperationsClientViewMatchPatternsOverEvents.as_view()),
]
