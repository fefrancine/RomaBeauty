from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Telefone, User
from core.serializers import TelefoneSerializer, UserSerializer


class CadastroAPIView(APIView):
    def post(self, request):
        telefone = request.data.pop('telefone')
        serializerUser = UserSerializer(data=request.data)
        serializerUser.is_valid(raise_exception=True)

        user = serializerUser.save()

        serializerTelefone = TelefoneSerializer(data={'user': user.id, 'telefone': telefone})
        serializerTelefone.is_valid(raise_exception=True)
        serializerTelefone.save()

        return Response({"message": "Cadastro realizado com sucesso!"}, status=status.HTTP_201_CREATED)
