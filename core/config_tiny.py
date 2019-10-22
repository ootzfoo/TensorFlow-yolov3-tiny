#! /usr/bin/env python
# coding=utf-8
# ================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : config.py
#   Author      : YunYang1994
#   Created date: 2019-02-28 13:06:54
#   Description :
#
# ================================================================

from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by: from config import cfg

cfg = __C

# YOLO options
__C.YOLO = edict()

# Set the class name
__C.YOLO.CLASSES = "./data/classes/voc.names"
__C.YOLO.ANCHORS = "./data/anchors/tiny_anchors.txt"
__C.YOLO.MOVING_AVE_DECAY = 0.9
__C.YOLO.STRIDES = [16, 32]
__C.YOLO.ANCHOR_PER_SCALE = 3
__C.YOLO.IOU_LOSS_THRESH = 0.5
__C.YOLO.UPSAMPLE_METHOD = "deconv"
__C.YOLO.ORIGINAL_WEIGHT = ""
__C.YOLO.DEMO_WEIGHT = ""

# Train options
__C.TRAIN = edict()

__C.TRAIN.ANNOT_PATH = "./data/dataset/voc_train.txt"
__C.TRAIN.BATCH_SIZE = 30
__C.TRAIN.INPUT_SIZE = [320, 352, 384, 416, 448, 480, 512]
__C.TRAIN.DATA_AUG = True
__C.TRAIN.LEARN_RATE_INIT = 1e-3
__C.TRAIN.LEARN_RATE_END = 1e-6
__C.TRAIN.WARMUP_EPOCHS = 2
__C.TRAIN.FISRT_STAGE_EPOCHS = 40
__C.TRAIN.SECOND_STAGE_EPOCHS = 60
__C.TRAIN.INITIAL_WEIGHT = ""

# TEST options
__C.TEST = edict()

__C.TEST.ANNOT_PATH = "./data/dataset/voc_test.txt"
__C.TEST.BATCH_SIZE = 16
__C.TEST.INPUT_SIZE = 416
__C.TEST.DATA_AUG = False
__C.TEST.WRITE_IMAGE = False
__C.TEST.WRITE_IMAGE_PATH = "./data/detection/"
__C.TEST.WRITE_IMAGE_SHOW_LABEL = True
__C.TEST.WEIGHT_FILE = ""
__C.TEST.SHOW_LABEL = True
__C.TEST.SCORE_THRESHOLD = 0.3
__C.TEST.IOU_THRESHOLD = 0.45
