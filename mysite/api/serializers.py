from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogPost model, converting model instances to JSON format.
    """
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']
