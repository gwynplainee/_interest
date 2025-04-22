from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Post, UserFollowing, Comment, Like


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            raise serializers.ValidationError("Username and password are required")
        return data

class UserFollowingSerializer(serializers.Serializer):
    following_user_id = serializers.IntegerField()

    def validate(self, data):
        request = self.context.get('request')
        following_user_id = data.get('following_user_id')
        
        if request.user.id == following_user_id:
            raise serializers.ValidationError("Cannot follow yourself")
        
        try:
            following_user = User.objects.get(id=following_user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if UserFollowing.objects.filter(
            user=request.user, following_user_id=following_user_id
        ).exists():
            raise serializers.ValidationError("Already following this user")
        
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        following_user = User.objects.get(id=validated_data['following follow_user_id'])
        return UserFollowing.objects.create(
            user=request.user,
            following_user=following_user
        )

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    board_title = serializers.ReadOnlyField(source='board.title', allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'user', 'board', 'board_title', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        return Post.objects.create(user=request.user, **validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance.user != request.user:
            raise serializers.ValidationError("You can only update your own posts")
        return super().update(instance, validated_data)

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Board
        fields = ['id', 'title', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        return Board.objects.create(user=request.user, **validated_data)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        return Comment.objects.create(user=request.user, **validated_data)

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        request = self.context.get('request')
        post = data.get('post')
        if Like.objects.filter(user=request.user, post=post).exists():
            raise serializers.ValidationError("You already liked this post")
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        return Like.objects.create(user=request.user, **validated_data)

class UserSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'post_count', 'follower_count']

    def get_post_count(self, obj):
        return obj.posts.count()

    def get_follower_count(self, obj):
        return obj.followers.count()
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'username': {'required': False, 'allow_blank': True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        username = validated_data.get('username') or validated_data['email'].split('@')[0]
        user = User.objects.create_user(
            username=username,
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            raise serializers.ValidationError("Email and password are required")
        return data