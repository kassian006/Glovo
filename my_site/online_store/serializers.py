from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'user_name']

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StoreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImage
        fields = '__all__'


class StoreListSerializer(serializers.ModelSerializer):
    store_category = CategoryListSerializer(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    total_good = serializers.SerializerMethodField()
    store_images = StoreImageSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['store_name', 'store_images', 'store_category', 'avg_rating','total_people', 'total_good']

    def get_avg_rating(self, obj):
       return obj.get_avg_rating()

    def get_total_people(self, obj):
       return obj.get_total_people()

    def get_total_good(self, obj):
       return obj.get_total_good()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'category', 'address', 'owner']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Contact_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Info
        fields = ['contact']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['product_name','product_images', 'price', 'store']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['product_name','product_images', 'price', 'store', 'description', 'quantity']


class ComboProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboProduct
        fields = ['combo_name', 'combo_image', 'store', 'combo_price']


class ComboProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboProduct
        fields = ['combo_name', 'combo_image', 'store', 'combo_price', 'description']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['products']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client', 'products', 'status', 'delivery_address', 'courier', 'created_date']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ComboProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboProduct
        fields = ['combo_name', 'combo_image', 'combo_price', 'store', 'description']


class CourierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['user', 'current_orders']


class CourierDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['user', 'status_courier', 'current_orders']


class StoreReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    client = UserReviewSerializer()

    class Meta:
        model = StoreReview
        fields = ['client', 'rating', 'comment', 'created_date']


class CourierReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierReview
        fields = '__all__'

class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    owner = UserProfileSimpleSerializer(read_only=True, )
    store_contact = Contact_InfoSerializer(read_only=True, many=True)
    products = ProductListSerializer(read_only=True, many=True)
    combo_products = ComboProductListSerializer(read_only=True, many=True)
    store_review = StoreReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        fields = [
            'store_name', 'store_image', 'category', 'description',
            'owner', 'address', 'store_contact', 'products',
            'combo_products', 'store_review'
        ]

