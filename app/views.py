from django.shortcuts import render
from django.db import models
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from .models import *
import random


# Create your views here.
def get_tag_list(req):
    cate = list(models.QuerySet(Cate).all().values_list('cate',flat=True))
    idx = random.randrange(len(cate))
    cate_selection = cate[idx]
    sub = list(models.QuerySet(Sub).filter(cate=cate_selection).values_list('sub',flat=True))
    sub_selection = sub[random.randrange(len(sub))]
    taging_image_query = models.QuerySet(Image_list).filter(sub=sub_selection,correct__lt=0)
    taging_image = list(taging_image_query.values_list('image_path',flat=True))
    taging_id = list(taging_image_query.values_list('id',flat=True))
    if len(taging_image) < 10:
        n = len(taging_image)
    else:
        n = 10
    random_list = random.sample(range(len(taging_image)),k=n)
    correct_image_list = list(models.QuerySet(Image_list).filter(sub=sub_selection,correct=1).values_list('image_path',flat=True))
    correct_image = correct_image_list[random.randrange(len(correct_image_list))]

    res_image_list = []
    res_id_list = []
    


    for  i,idx in enumerate(random_list):
        res_image_list.append(taging_image[idx])
        res_id_list.append(taging_id[idx])
    
    d = {
        'res_image_list':res_image_list,
        'res_id_list':res_id_list,
        'correct_image':correct_image
    }
    return JsonResponse(d)


#def get_runking_list(req):

#def get_runking_my(req):

#def get_gatya(req):

@csrf_exempt
def post_tag_info(req):
    image_idx = int(req.POST.get('image_idx'))
    image_correct = int(req.POST.get('correct'))
    user_id = int(req.POST.get('id'))
    image_obj = models.QuerySet(Image_list).filter(id=image_idx).first()
    image_obj.correct = image_correct
    image_obj.save()

    user = models.QuerySet(User).get(id=user_id)
    runking = models.QuerySet(Runking).filter(User=user).first()
    runking.point +=1


    return HttpResponse('image info update') 

def post_user_info(req):
    user_name = req.POST.get('user_name')
    user = User(userName=user)
    user.save()
    id = models.QuerySet(User).all().aggregate(Max('id'))
    id = id['id__max']
    user = models.QuerySet(User).get(id=id)
    runking = Runking(User=user)
    return HttpResponse(id)