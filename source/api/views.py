from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Friend


class AddView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, pk=None):
        print(request)
        profile = get_object_or_404(User, pk=pk)
        frds, create = Friend.objects.get_or_create(user=request.user, friend=profile)
        if create:
            return Response({'pk': pk})
        else:
            return Response(status=403)


class RemoveView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def delete(self, request, pk=None):
        friend = get_object_or_404(User, pk=pk)
        friends = Friend.objects.filter(friend=friend)
        friends.delete()
        return Response({'pk': pk})