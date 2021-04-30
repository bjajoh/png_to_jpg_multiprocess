
#!/usr/bin/env python
from glob import glob                                                           
import cv2 
from tqdm import tqdm
from multiprocessing import Pool
import time
from tqdm import *

pngs = glob('./*.png')

#for j in tqdm(pngs):
#    img = cv2.imread(j)
#    cv2.imwrite(j[:-3] + 'jpg', img)

def _foo(j):
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)

if __name__ == '__main__':
    with Pool(processes=6) as p:
         with tqdm(total=len(pngs)) as pbar:
            for i, _ in enumerate(p.imap_unordered(_foo, pngs)):
                pbar.update()
