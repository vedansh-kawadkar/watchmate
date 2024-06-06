from rest_framework import serializers
from watchlist.models import Content, StreamingPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True) #nested serializer
    platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = Content
        exclude = ['created']
    
    # def validate_name(self, value):
    #     """
    #     Field based validation. used as validate_<field_name>
    #     """
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
           
class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    '''
    nested serializer.
    '''
    content = ContentSerializer(many=True, read_only=True) #use name defined in related_name field of foreign key
    
    # content = serializers.StringRelatedField(many=True, read_only=True) #use name defined in related_name field of foreign key
    
    class Meta:
        model = StreamingPlatform
        fields = "__all__"        
        

# class PlatformSerializer(serializers.ModelSerializer):
#     # content = ContentSerializer(many=True, read_only=True) #use name defined in related_name field of foreign key
#     content = serializers.StringRelatedField(many=True, read_only=True) #use name defined in related_name field of foreign key
    
#     class Meta:
#         model = StreamingPlatform
#         fields = "__all__"    





# def name_length(value):
#     if len(value)<3:
#         return serializers.ValidationError("Name is too short!")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length]) #value validators
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         """ 
#         create new value
#         """
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update each value individually
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     #Validations
#     def validate(self, data):
#         """
#         Object based validation
#         """
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different.")
#         return 
    
#     def validate_name(self, value):
#         """
#         Field based validation
#         """
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value
