# --------------------------------------------------------
# Written by JianFeng Liu, based on python
# json file transform to xml file automatically
# --------------------------------------------------------
import xmltodict  # 他是一个支持从xml转换到python的dict互相转换的模块
import json
import os

# json to xml
def jsonToXml(json_str):
    xml_str = xmltodict.unparse({'Annotations': json_str}, encoding='utf-8')  # 将字典转换为xml字符串
    return xml_str

def json_to_xml(json_path,xml_path):
    if(os.path.exists(xml_path)==False):
        os.makedirs(xml_path)
    dir = os.listdir(json_path)
    for file in dir:
        file_list=file.split(".")
        with open(os.path.join(json_path, file), 'r') as load_f:
            load_dict = json.load(load_f)  # json.load()函数读取json文件，可以直接读取到这个文件中的所有内容，并且读取的结果返回为python的dict对象。
        json_result = jsonToXml(load_dict)
        f = open(os.path.join(xml_path,file_list[0]+".xml"), 'w', encoding="UTF-8")
        f.write(json_result)
        f.close()

if __name__ == '__main__':

    json_path = "/home/hik/zhangyuxin19/Yolov5_StrongSORT_OSNet-master/yolov5/tongDATA/Annotations"  #该目录为存放json文件的路径  ps:目录中只能存放json文件
    xml_path = "/home/hik/zhangyuxin19/Yolov5_StrongSORT_OSNet-master/yolov5/tongDATA/Annotations_xml"   #该目录为放xml文件的路径
    json_to_xml(json_path,xml_path)