from rest_framework import serializers
from watchlist_app.models import Content, StreamingPlatform


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"
    
    #Validations
    # def validate(self, data):
    #     """
    #     Object based validation
    #     """
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and description should be different.")
    #     return 
    
    def validate_name(self, value):
        """
        Field based validation
        """
        if len(value)<2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
           
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        exclude = ['created']
        

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
