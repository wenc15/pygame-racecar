from PIL import Image
with Image.open('R-C.jpg') as img:
    rotated_img = img.rotate(270)
        # 假设我们想将图像缩小到原来的一半大小
    width, height = rotated_img.size
    new_width = width // 4
    new_height = height // 4
    rotated_img = rotated_img.resize((new_width, new_height))

rotated_img.show()

rotated_img.save('rotated_player.jpg')