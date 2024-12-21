##重命名当前文件夹下的图片

##按顺序从1开始命名图片名称
import os


def rename_images_in_folder():
    # 获取当前目录下的所有文件和文件夹
    files = os.listdir('.')

    # 用于存储图片文件的原始名称
    image_files = []

    # 遍历所有文件，找出图片文件
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(file)

            # 对图片文件按名称排序（如果需要的话）
    image_files.sort()

    # 对图片文件进行编号
    for i, file in enumerate(image_files, start=1):
        # 构建新文件名
        # 输出形式为1.jpg 2.jpg 3.jpg ...10.jpg
        new_name = f"{i}.jpg"  ##其他需求可修改此处代码

        ##根据需求进行修改，注意 {i:02d} 格式
        ##        ##设置输出形式为 01.jpg 02.jpg 03.jpg ...10.jpg
        ##        new_name = f"{i:02d}.jpg"

        ##        ##设置输出形式为 001.jpg 002.jpg 003.jpg ...010.jpg,..100.jpg
        ##        new_name = f"{i:03d}.jpg"

        # 如果有必要，可以保留原扩展名
        # new_name = f"{i}.{file.split('.')[-1]}"

        # 重命名文件
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")


if __name__ == "__main__":
    rename_images_in_folder()

