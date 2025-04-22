from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.db.models import Q
from core.models import Post
from core.serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def search_posts(request):
    query = request.query_params.get('q', '').strip()
    if not query:
        return Response({"error": "Search query parameter 'q' is required"}, status=400)
    
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).order_by('-created_at')
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)