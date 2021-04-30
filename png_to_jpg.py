
#!/usr/bin/env python
from glob import glob                                                           
import cv2 
from tqdm import tqdm

pngs = glob('./*.png')

for j in tqdm(pngs):
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)
