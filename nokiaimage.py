#%%

from PIL import Image
import numpy as np


# %%
name_im1 = "pico8_font.png"
name_im2 = "pico8_fontnew.png"


# %%
target_rgb_dark = (67,82,61)
target_rgb_light = (199,240,216)

def recolor_image(im, target):
    im.putalpha(1)
    array_im = np.array(im)
    array_im[:,:,3] = array_im[:,:,2]
    for _, cc in enumerate(target):
        array_im[:,:,_] = array_im[:,:,_]*(1/255)*cc
    im_new = Image.fromarray(array_im)
    return im_new


# %%
if __name__ == "__main__":
    import sys

    name_im1 = sys.argv[1]
    name_im2 = sys.argv[2]
    if sys.argv[3] == "light":
        targ = target_rgb_light
    else:
        targ = target_rgb_dark

    im1 = Image.open(name_im1)

    im2 = recolor_image(im1, targ)

    im2.save(name_im2)
