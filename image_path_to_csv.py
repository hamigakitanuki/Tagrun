import csv
import os
import glob
with open('image_list.csv','w') as f:
    writer = csv.writer(f)
    idx = 0
    for i,cate in enumerate(list(os.listdir('media'))):
        for j,sub in enumerate(list(os.listdir('media/'+cate))):
            for k,color in enumerate(list(os.listdir('media/'+cate+'/'+sub))):
                item_list = glob.glob('media/'+cate+'/'+sub+'/'+color+'/*.jpg')
                for y,filename in enumerate(item_list):
                    if y == 0:
                        writer.writerow([idx,filename,cate,sub,1])
                    else:
                        writer.writerow([idx,filename,cate,sub,-1])
                    idx = idx + 1
                    
                