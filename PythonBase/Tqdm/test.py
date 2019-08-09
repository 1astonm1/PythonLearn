from tqdm import  tqdm
import glob
import cv2
# 读取文件夹里所有图片
Image_file_path = r'F:\Download\dataset\auto\bdd100k_images\bdd100k\images\100k\train'
Image_files = glob.glob(Image_file_path+"/*"+".jpg")

# 把要处理的list在循环时放在tqdm()里面就可以了
for Image_file in tqdm(Image_files):
    img = cv2.imread(Image_file)
