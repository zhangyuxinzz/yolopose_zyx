import os
import shutil

source_path = os.path.abspath(r'E:\8月工作资料\0水面物体检测大作业\数据集\标准校验集\9a8a67b02a6211ed8b9b246e96909081_20220902095751\Images')  # 源文件夹
target_path = os.path.abspath(r'E:\8月工作资料\0水面物体检测大作业\yolov5-master\WDData\detectImages')  # 目标文件夹

if not os.path.exists(target_path):  # 目标文件夹不存在就新建
    os.makedirs(target_path)

if os.path.exists(source_path):  # 源文件夹存在才执行
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)

    for root, dirs, files in os.walk(source_path):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, target_path)
            print(src_file)

print('复制完成')

