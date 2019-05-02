from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django.db.models import Q
from .serializers import SmsSerializer, UserRegSerializer
from .models import VerifyCode
from random import choice
from utils import AliYun

# Create your views here.
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user

        except Exception as e:
            print(e)
            return None


class SmsCodeViewSet(CreateModelMixin,viewsets.GenericViewSet):
    '''
    手机验证码
    '''
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        code = self.generate_code()
        params = "{\"code\":\"" + code + "\"}"
        sms_status = AliYun.send_verify_sms(mobile, params)

        if sms_status["Code"] == 'OK':
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "mobile": sms_status["Message"]
            }, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户相关页面
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
