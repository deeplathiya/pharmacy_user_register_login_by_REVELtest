from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CustomerSerializer


# Create your views here.

@api_view(http_method_names=["GET"])
def Health(request):
    return Response({
        "message": "Health Checked Successfully",
    }, status=200)


@api_view(http_method_names=["POST"])
@permission_classes(permission_classes=(permissions.AllowAny, ))
def register(request):
    try:
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User is Registered Successfully",
        }, status=201)
    except Exception as e:
        return Response({
            "message": e.__str__(),
        }, status=400)


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            response = super(LoginView, self).post(request, format=None)
            if response.status_code >= 400:
                return Response({
                    "message": "Invalid credential",
                }, status=401)
            return response
        except Exception as e:
            return Response({
                "message": "Invalid credential",
            }, status=401)


@api_view(http_method_names=["GET"])
@permission_classes(permission_classes=(permissions.IsAuthenticated, ))
def getAll(request):
    return Response({
        "message": "Successfully Accessed"
    })
