import cv2
import os

path = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(path, '/output/')
videoname = 'test.mp4'
fullpath = path + "/output/" + videoname

try : 
    if not os.path.exists(outpath):
        os.makedirs(outpath)
except OSError:
    if  os.path.exists(outpath):
        print('Error: Creating directory of data')
        exit()





listimage = os.listdir(path+'/im')

img = []

f = 0
for i in listimage:
    i = path+'/im/'+i
    img.append(i)
    f += 1
if f == 0:
    print('Error: No image found')
    exit()

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()

video = cv2.VideoWriter(fullpath, cv2_fourcc, 24, size)

for i in range(len(img)):
    video.write(cv2.imread(img[i]))

video.release()
