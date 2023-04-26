
import xml.etree.ElementTree as ET
import os
from os import getcwd


sets = ['train', 'val', 'test']
classes = ["垃圾类漂浮物", "植物类漂浮物", "其他类漂浮物"]  # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)
# def sta(image_id,g,z,q):
g = 0
z = 0
q = 0
wd = getcwd()
for image_set in sets:
    image_ids = open('ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    # 这行路径不需更改，这是相对路径
    for image_id in image_ids:
        in_file = open('Annotations/%s.xml' % (image_id), encoding='UTF-8')
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            if obj.find('difficult'):
                difficult = float(obj.find('difficult').text)
            else:
                difficult = 0
            # difficult = obj.find('Difficult').text
            cls = obj.find('name').text
            print(cls)
            if cls in classes:
                if cls == '垃圾类漂浮物':
                    g = g + 1
                elif cls == '植物类漂浮物':
                    z = z + 1
                elif cls == '其他类漂浮物':
                    q = q + 1
            elif cls not in classes or int(difficult) == 1:
                continue
print("垃圾类漂浮物：", g, "\n植物类漂浮物:", z, "\n其他类漂浮物:", q)



