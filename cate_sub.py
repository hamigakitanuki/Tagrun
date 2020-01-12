import csv
import os
import glob
with open('cate_list.csv','w') as f:
    with open('sub_list.csv','w') as sf:
        cate_writer = csv.writer(f)
        sub_writer = csv.writer(sf)
        k=0
        for i,cate in enumerate(list(os.listdir('download'))):
            cate_writer.writerow([i,cate])
            for j,sub in enumerate(list(os.listdir('download/'+cate))):
                sub_writer.writerow([k,cate,sub])
                k = k+1
                    
                