# WaveCT-AIN_base_version
# （Style Transfer for Medical Image）

## Getting Started
### Dependency
- PyTorch >= 0.4.1
- Check the requirements.txt
```bash
pip install -r requirements.txt
```


### Arguments

* `--content`: FOLDER-PATH-TO-CONTENT-IMAGES
* `--style`: FOLDER-PATH-TO-STYLE-IMAGES
* `--output`: FOLDER-PATH-TO-OUTPUT-IMAGES
* `--image_size`: output image size
* `-a`: all transfer
* `-d`: decoder transfer
* `-e`: encoder transfer
* `-s`: skip transfer   



### Introduction

* Pretrained models can be found in the `./model_checkpoints`
* Content and style images can be found in the`./examples`
*  `./transfer.py` is the transfer code


- Test the model:

```bash
CUDA_VISIBLE_DEVICES=5 python transfer.py --content ./examples/content --style ./examples/style --output ./outputs/ --verbose --image_size 512 -d
```

The test results will be saved to `./outputs` by default.  

### Result

![](http://m.qpic.cn/psc?/V12kySKV4IhBFe/45NBuzDIW489QBoVep5mcSeUxtbMpqAb1lwsxHoL*q7TE8pwUHUwnBsOVrpMRuLg1Lmm3vTzx2RU7Q435WCVSbtieqZ3ibA0mS6YXnR5I5g!/b&bo=TQNSAQAAAAADJx8!&rf=viewer_4)



Please cite:


Liu, Zhendong, et al. "Remove appearance shift for ultrasound image segmentation via fast and universal style transfer." 2020 IEEE 17th International Symposium on Biomedical Imaging (ISBI). IEEE, 2020.


