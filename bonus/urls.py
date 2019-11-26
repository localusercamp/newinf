from . import views
from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

urlpatterns = [
    path("", views.testrequest),
    path("user-diagram-value/", views.GetDiagramValues),
    path(
        "user-bonus-transactions/",
        views.UserBonusTransactionList.as_view(),
        name="bonus-api-user_bonus_transaction-list",
    ),
    path("api-token-auth/", obtain_jwt_token),
    path("api-token-refresh/", refresh_jwt_token),
]
