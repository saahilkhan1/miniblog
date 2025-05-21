from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Blog, Like, Comment
from .serializer import *

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    print('request.data',request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status':'Account has been created.','token': token.key})
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    print('get user deatils ',user)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        print('token',token)
        return Response({'status':'login_success','token': token.key},status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def post_list_create(request):
    if request.method == 'GET':
        posts = Blog.objects.all()
        serializer = BlogSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print('___level 1________________',request.data)
        print('___level 2________________',request.user)
        if not request.user or not request.user.is_authenticated:
            return Response({"detail": "Authentication required for POST"}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_edit_delete_post(request, pk):
    try:
        post = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if post.author != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = BlogSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if post.author != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = BlogSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Updated done','response':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if post.author != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response({'status':'Post has been deleted'},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def like_post(request, pk):
    try:
        print('____level 1____________',pk)
        post = Blog.objects.get(pk=pk)
        print('____level 2____________',post)
    except Blog.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        like = Like.objects.get(user=request.user, post=post)
        print('____level 3____________',like)
        if like.like_post:
            like.like_post = False
            like.save()
            return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        else:
            like.like_post = True
            like.save()
            return Response({'message': 'Liked'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        Like.objects.create(user=request.user, post=post, like_post=True)
        return Response({'message': 'Liked'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def comment_post(request, pk):
    try:
        post = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
