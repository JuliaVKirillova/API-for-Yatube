from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
        PostSerializer, 
        CommentSerializer, 
        GroupSerializer, 
        FollowSerializer,
    )
from .models import (
        Post, 
        Comment,
        Follow,
        Group,
    )   
from .permissions import IsOwnerOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs.get('post_id'))



class APIFollow(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class APIGroup(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

