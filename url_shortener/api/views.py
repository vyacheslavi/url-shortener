from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


from .serializers import TokenURLSerializer, UserTokenSerializer
from .models import TokenURL


class TokenURLViewSet(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    model = TokenURL
    queryset = TokenURL.objects.all()
    serializer_class = TokenURLSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TokenURL.objects.filter(owner=user)

    def post(self, request: Request) -> Response:
        serializer = TokenURLSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid(raise_exception=True):
            token, status_code = serializer.create(
                validated_data=serializer.validated_data,
            )
            return Response(TokenURLSerializer(token).data, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTokenListAPIView(
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserTokenSerializer
    queryset = User.objects.filter(is_active=True)
