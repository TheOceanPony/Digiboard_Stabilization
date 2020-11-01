import pylab
import numpy as np
from skimage import io


img_still = io.imread("img/still.png")
img_disp  = io.imread("img/disp_-2left.png")

disp_range = 5

best_score = float("inf")
best_disp = None

for disp in range(-disp_range, disp_range, 1):
    
    diff = img_still - np.roll(img_disp, disp, axis=1)
    
    temp_score = np.sum(diff)
    if best_score > temp_score:
        best_score = temp_score
        best_disp = disp
        


img_reconstr = np.roll(img_disp, best_disp, axis=1)
io.imsave("img/result_diff.png", img_still - img_reconstr)

print(f"Best score : {best_score}, with disp {best_disp}")