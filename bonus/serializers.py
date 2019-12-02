from rest_framework import serializers
from .models import *


class AccountPaymentServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPaymentService
        fields = ["supplier_name", "service_name"]

class AccountPaymentSerializer(serializers.ModelSerializer):
    account_payment_services = serializers.SerializerMethodField()

    class Meta:
        model = AccountPayment
        fields = ["account_payment_services"]
    
    def get_account_payment_services(self, obj):
        serializer = AccountPaymentServiceSerializer(obj.accountpaymentservice_set.all(), many=True)
        return serializer.data

class BonusTransactionSerializer(serializers.ModelSerializer):
    # supplier_service = serializers.SerializerMethodField()
    date_created = serializers.DateTimeField()
    account_payment = AccountPaymentSerializer()

    class Meta:
        model = BonusTransaction
        fields = ["id", "user", "value", "note", "date_created", 'account_payment']#"supplier_service"]

    # def get_supplier_service(self, obj):  # supplier_service serialize
    #     result_dict = {}
    #     try:
    #         for item in AccountPaymentService.objects.filter(
    #             account_payment=obj.account_payment.id
    #         ):
    #             result_dict[item.supplier_name] = item.service_name
    #     except Exception:
    #         pass
    #     if result_dict:
    #         return result_dict
    #     else:
    #         return None
