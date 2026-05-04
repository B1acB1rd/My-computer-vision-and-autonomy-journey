import os
from PIL import Image
from pylab import *
def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.jpeg')]

def imresize(im, sz):
    """Resize an image from array using PIL"""
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))