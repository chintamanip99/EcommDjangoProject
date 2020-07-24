from django.contrib import admin
from django.urls import path
from .views import TransactionDeleteWithoutChangeView,CreateTransaction,send_email,TransactionListView,TransactionCreateView,TransactionDeleteView,TransactionUpdateView,TransactionDetailView
app_name="cart"
urlpatterns = [
	# path("",TransactionCreateView.as_view(),name="create_transaction"),
	path("<int:lo>/",CreateTransaction.as_view(),name="create_transaction1"),
    path("list/",TransactionListView.as_view(),name="display_transaction_list"),
    path("delete/<int:lo>",TransactionDeleteView.as_view(),name="delete_transaction"),
    path("delete2/<int:lo>",TransactionDeleteWithoutChangeView.as_view(),name="delete_transaction2"),
    path("update/<int:lo>",TransactionUpdateView.as_view(),name="update_transaction"),
    # path("list/<int:lo>",TransactionDetailView.as_view(),name="display_a_transaction"),
    # path("email/",send_email,name="sendemail")
]