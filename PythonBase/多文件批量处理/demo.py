# 处理一个文件夹中的所有文件
import os.path as osp
import glob

path = r'F:\Download\dataset\auto\bdd100k_images\bdd100k\images\100k\train'
Images_path = glob.glob(path + "/*" + ".jpg")        # 读取所有文件名形成list

for Image_path in Images_path:  # os.path.split()  输出路径和文件名， os.path.splitext(basename) 输出middlename 和 扩展名
    dirname, basename = osp.split(Image_path)       # dirname: F:\Download\dataset\auto\bdd100k_images\bdd100k\images\100k\train, basename : fe189115-8dabb5b1.jpg
    middlename, filetype = osp.splitext(basename)   # middlename: fe189115-8dabb5b1, filetype : .jpg
    print("dirname: {0}, basename : {1}".format(dirname, basename))
    print("middlename: {0}, filetype : {1}".format(middlename, filetype))
