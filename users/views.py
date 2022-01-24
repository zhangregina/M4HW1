from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    if request.method == 'POST':        #выдаёт нам токен
        # username = request.data['username']
        # password = request.data['password']
        user = authenticate(**request.data) #(username:"admin",password: "123")
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'user not found :c'}, status=404)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        User.objects.create_user(username=username, password=password) #простой пользователь, который не будет заходить в админку
        return Response(data={'The user is created'}, status=201)
