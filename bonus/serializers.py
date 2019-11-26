from rest_framework import serializers
from .models import *

# class BonusTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BonusTransaction
#         fields = ['id', 'user', 'account_payment', 'value', 'note'] #'date_created', 'date_updated']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone']# 'date_created', 'date_updated']


class BonusTransactionSerializer(serializers.ModelSerializer):
    supplier_service = serializers.SerializerMethodField()
    date_created = serializers.DateTimeField()

    class Meta:
        model = BonusTransaction
        fields = ["id", "user", "value", "note", "date_created", "supplier_service"]

    def get_supplier_service(self, obj):  # supplier_service serialize
        result_dict = {}
        try:
            for item in AccountPaymentService.objects.filter(
                account_payment=obj.account_payment.id
            ):
                result_dict[item.supplier_name] = item.service_name
        except Exception:
            pass
        if result_dict:
            return result_dict
        else:
            return None


# class DiagrammSerializer(serializers.ModelSerializer):
#     earned = serializers.SerializerMethodField()
#     spent = serializers.SerializerMethodField()
#     balance = serializers.SerializerMethodField()

#     class Meta:
#         fields = ['earned', 'spent', 'balance']

#     def get_earned(self):
#         pass
