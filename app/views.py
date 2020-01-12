from django.shortcuts import render
from django.db import models
from django.http.response import JsonResponse
from .models import *
import random


# Create your views here.
def get_tag_list(req):
    cate = list(models.QuerySet(Cate).all().values_list('cate',flat=True))
    print(cate)
    idx = random.randrange(len(cate))
    cate_selection = cate[idx]
    sub = list(models.QuerySet(Sub).filter(cate=cate_selection).values_list('sub',flat=True))
    print(sub)
    sub_selection = sub[random.randrange(len(sub))]
    print(sub_selection)
    taging_image_query = models.QuerySet(Image_list).filter(sub=sub_selection,correct__lt=0)
    taging_image = list(taging_image_query.values_list('image_path',flat=True))
    taging_id = list(taging_image_query.values_list('id',flat=True))
    print(taging_image)
    random_list = random.sample(range(len(taging_image)),k=10)
    correct_image_list = list(models.QuerySet(Image_list).filter(sub=sub_selection,correct=1).values_list('image_path',flat=True))
    correct_image = correct_image_list[random.randrange(len(correct_image_list))]
    print(correct_image)
    res_image_list = []
    res_id_list = []
    


    for  i,idx in enumerate(random_list):
        res_image_list.append(taging_image[idx])
        res_id_list.append(taging_image[idx])
    
    d = {
        'res_image_list':res_image_list,
        'res_id_list':res_id_list,
        'correct_image':correct_image
    }
    return JsonResponse(d)


#def get_runking_list(req):

#def get_runking_my(req):

#def get_gatya(req):

#def post_tag_info(req):
