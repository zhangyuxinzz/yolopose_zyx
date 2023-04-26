# encoding:utf-8     111111
import os
import xml.etree.ElementTree as ET

count = 0
list_xml = []
dict = {"洗衣机": "Washing Machine",
        "洗衣机桶槽": "Roller"
        }

openPath = "/home/hik/zhangyuxin19/Yolov5_StrongSORT_OSNet-master/yolov5/tongDATA/Annotations_xml"
savePath = "/home/hik/zhangyuxin19/Yolov5_StrongSORT_OSNet-master/yolov5/tongDATA/Annotations_E"
fileList = os.listdir(openPath)         # 得到进程当前工作目录中的所有文件名称列表
for fileName in fileList:               # 获取文件列表中的文件
    if fileName.endswith(".xml"):       # 只看xml文件
        print("filename=:", fileName)
        tree = ET.parse(os.path.join(openPath, fileName))
        root = tree.getroot()
        print("root-tag=:", root.tag)   # ',root-attrib:', root.attrib, ',root-text:', root.text)
        for child in root: # 第一层解析
            if child.tag == "formData":   # 找到object标签
                print(child.tag)
                for sub in child:
                    if sub.tag == "labelName":
                        print("标签名字:", sub.tag, ";文本内容:", sub.text)
                        if sub.text not in list_xml:
                            list_xml.append(sub.text)
                        if sub.text in list(dict.keys()):
                            sub.text = dict[sub.text]
                            print(sub.text)
                            count = count + 1
        tree.write(os.path.join(savePath, fileName))
    print("=" * 20)

print(count)
for i in list_xml:
    print(i)
