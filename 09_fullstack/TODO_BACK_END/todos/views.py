from django.shortcuts import get_object_or_404


from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
# from rest_framework.permissions import IsAuthenticated # login_required
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication # login via JWT    이거 두개는 지금 안쓴다~ 
from .models import Todo
from .serializers import TodoSerializer  # serializer 가 json 으로 내보내는거다. 

@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.POST)  # request.POST => form-data 만 잡음. 
    if serializer.is_valid():
        serializer.save()
        # serializer.data => { 'id':1, 'user_id':1, 'title':'밥먹기', 'completed':false }
        return Response(serializer.data)  # serializers.py 의 fields 애들이 나간다. (json 으로 )
    return Response(status=400, data=serializers.errors)


@api_view(['PATCH', 'DELETE'])
def update_delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'PATCH':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)