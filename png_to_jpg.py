
#!/usr/bin/env python
from glob import glob                                                           
import cv2 
from tqdm import tqdm
from multiprocessing import Pool
import time
from tqdm import *

#read files and make list with all .pngs in directory
pngs = glob('./*.png')

#convert the image and write it do drive
def _foo(j):
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)

if __name__ == '__main__':
    #6 threads parallelized map loop
    with Pool(processes=6) as p:
         with tqdm(total=len(pngs)) as pbar:
            for i, _ in enumerate(p.imap_unordered(_foo, pngs)):
                pbar.update()
