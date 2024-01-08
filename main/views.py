from django.shortcuts import render
from django.views import View
from .models import Score
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.

max_output=10

class Main(View):

    def get(self,request):
        if("maze_name" not in request.GET):
            return HttpResponse("not a valid request")

        scores=Score.objects.filter(maze_name=request.GET["maze_name"]).order_by("time")
        output={}
        cnt=0
        for i in scores:
            cnt+=1
            if(cnt>max_output):
                break
            output[i.username]=i.time
        
        return JsonResponse(output)
    def post(self,request):
        print(request.POST["time"])
        if("username" not in request.POST or "time" not in request.POST or "map_name" not in request.POST):
            return HttpResponse("not a valid request")
        
        username=request.POST["username"]
        time=request.POST["time"]
        map_name=request.POST["map_name"]


        search_result=Score.objects.filter(username=username,maze_name=map_name)
        if(len(search_result)==0):
            Score.objects.create(username=username,maze_name=map_name,time=time)
        else:
            search_result[0].time=time
            search_result[0].save()

        return HttpResponse("uploaded successfuly")
        






