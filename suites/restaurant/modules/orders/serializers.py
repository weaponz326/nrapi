from rest_framework import serializers

from .models import Order, OrderItem
from modules.customers.serializers import CustomerSerializer
from modules.tables.serializers import TableSerializer
from modules.menu.serializers import MenuItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'account',
            'table',
            'customer',
            'customer_name',
            'order_code',
            'order_date',
            'order_type',
            'order_status',
            'order_total',
        ]

class OrderDepthSerializer(serializers.ModelSerializer):
    table = TableSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'account',
            'table',
            'customer',
            'customer_name',
            'order_code',
            'order_date',
            'order_type',
            'order_status',
            'order_total',
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'created_at',
            'order',
            'menu_item',
            'quantity',
        ]

class OrderItemDepthSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'created_at',
            'order',
            'menu_item',
            'quantity',
        ]
