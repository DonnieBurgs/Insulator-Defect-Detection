import os

path = "./data/VOCdevkit/VOC2007/TestJPEGImages/"
test_list = os.listdir(path)
n = 0
for image_name in test_list:
    n += 1
    print("------This is the No.%d image.------" % n)
    image_name = path + image_name
    os.system("python demo_isolate.py --prefix model_0606/e2e --epoch 10 --image "
              + image_name)
    if n == 101:
        break
