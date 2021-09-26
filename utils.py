# -*-coding:utf-8 -*-

import os
import datetime
import ipdb
import numpy as np
from PIL import Image
from torchvision import transforms
from torchvision.utils import save_image


class Timer:
    def __init__(self, msg='Elapsed time: {}', verbose=True):
        self.msg = msg
        self.start_time = None
        self.verbose = verbose

    def __enter__(self):
        self.start_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.verbose:
            print(self.msg.format(datetime.datetime.now() - self.start_time))


def open_image(image_path, image_size=None):
    image = Image.open(image_path)  # (700,525)
    _transforms = []
    if image_size is not None:
        image = transforms.Resize(image_size)(image)
        # _transforms.append(transforms.Resize(image_size))
    w, h = image.size  # (911,512)
    _transforms.append(transforms.CenterCrop((h // 16 * 16, w // 16 * 16)))
    _transforms.append(transforms.ToTensor())
    transform = transforms.Compose(_transforms)
    return transform(image).unsqueeze(0)

def adain(content_features, style_features):
    # [64, 180, 528][64, 360, 496]
    style_mean = style_features.mean((2, 3), keepdim=True)
    style_std = style_features.std((2, 3), keepdim=True) + 1e-6
    content_mean = content_features.mean((2, 3), keepdim=True)
    content_std = content_features.std((2, 3), keepdim=True) + 1e-6
    target_feature = style_std * (content_features - content_mean) / content_std + style_mean
    return target_feature


def mkdir(dname):
    if not os.path.exists(dname):
        os.makedirs(dname)
    else:
        assert os.path.isdir(dname), 'alread exists filename {}'.format(dname)
