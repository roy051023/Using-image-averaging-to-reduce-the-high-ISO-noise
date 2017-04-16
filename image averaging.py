# 匯入library
from PIL import Image

# 讀三張圖片
im1 = Image.open('_MG_3744.JPG')
im2 = Image.open('_MG_3745.JPG')
im3 = Image.open('_MG_3746.JPG')

# 把圖片變數放入陣列
image = [im1, im2, im3]

# 取得圖片長寬
size = im1.size

# new 一個新圖
output = Image.new("RGB", (size[0], size[1]))

# 用迴圈把每張圖的像素相加並除總張數，且放到新圖
for i in range(0, size[0]):
	for j in range(0, size[1]):
		R = 0
		G = 0
		B = 0
		for k in range(0, len(image)):
			temp = image[k].getpixel((i,j))
			R += temp[0]
			G += temp[1]
			B += temp[2]

		R = R / len(image)
		G = G / len(image)
		B = B / len(image)
		output.putpixel((i,j),(int(R),int(G),int(B)))

# 儲存圖片
output.save("output.jpg")
