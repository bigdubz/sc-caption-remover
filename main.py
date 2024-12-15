from PIL import Image
import numpy as np
import os


# find the bar
# change the bar - done
# stonks


# color of bar = rgba(0, 0, 0, 0.6)
# color of bar on edge pixels rgba(0, 0, 0, 0.99)
# 1 - 0.6 = 0.4, / 0.4 = * 5/2 = * 5 * 0.5 = * 2.5
ALPHA_INVERSE = 2.5
ALPHA_INVERSE_EDGE = 1.00790513835

# RGB(blended) = RGB(original) * 0.4

def read_image(im_path: str):
    pix = np.array(Image.open(im_path))

    bar_start = 1469
    bar_end = 1581

    pix = unblend_bar(pix, bar_start, bar_end);
    result = Image.fromarray(pix)
    result.save('TEST.png')

def unblend_color(blended, alpha) -> tuple[int, int, int, int]:
    return (min(blended[0] * alpha, 255),
            min(blended[1] * alpha, 255),
            min(blended[2] * alpha, 255),
            255)
    
def unblend_bar(pix, start_i, end_i):
    width = len(pix[0])
    f = 1 / (end_i - start_i) * 100
    pr = 0
    for i in range(start_i, end_i):

        # print progress
        prc = int((i-start_i)*f)
        if prc != pr:
            pr = prc
            print(f"{pr}%")

        for j in range(width):
            r, g, b, a = unblend_color(pix[i, j], ALPHA_INVERSE)

            try:
                pix[i, j] = (r, g, b, a)

            except:
                pix[i, j] = (r, g, b)
    
    print("100%")

    return pix


read_image("i.jpg")
