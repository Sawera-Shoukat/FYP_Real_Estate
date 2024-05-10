from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user
            login(request, user)

            # Get the URL of the profile photo
            profile_photo_url = None
            if user.profile_photo:
                profile_photo_url = request.build_absolute_uri(user.profile_photo.url)

            # Return user data including role and profile photo URL
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'profile_photo_url': profile_photo_url
            })
        else:
            return JsonResponse({'error': 'Incorrect username or password.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        profile_photo = data.get('profile_photo')
        email = data.get('email')

        # Create user
        user = CustomUser.objects.create_user(username=username, password=password,
                                              profile_photo=profile_photo, email=email)

        # Save user
        user.save()

        return JsonResponse({'message': 'User created successfully.'})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully.'})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer