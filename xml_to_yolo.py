# -*- coding: utf-8 -*-    33333
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = ["Washing Machine", "Roller"]  # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open('Annotations_E/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    print('root', root.tag)
    w = 1280
    h = 720
    for obj in root.iter('formData'):
        if obj.find('difficult'):
            difficult = float(obj.find('difficult').text)
        else:
            difficult = 0
        # difficult = obj.find('Difficult').text
        cls = obj.find('labelName').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        b = (float(obj.find('x1').text), float(obj.find('x2').text), float(obj.find('y1').text),
             float(obj.find('y2').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
for image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    image_ids = open('ImageSets/Main/%s.txt' % (image_set)).read().strip().split()

    if not os.path.exists('dataSet_path/'):
        os.makedirs('dataSet_path/')

    list_file = open('dataSet_path/%s.txt' % (image_set), 'w')
    # 这行路径不需更改，这是相对路径
    for image_id in image_ids:
        list_file.write('/home/hik/zhangyuxin19/Yolov5_StrongSORT_OSNet-master/yolov5/tongDATA/Images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
