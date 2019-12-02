from . import views
import cv2

def main(piyo):
    photo = '3_3.jpg'
    # print(photoname)
    # src = cv2.imread(photo, cv2.IMREAD_COLOR)
    # cv2.namedWindow("src", cv2.WINDOW_NORMAL)
    # cv2.imshow("src",src)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()    
    # img = cv2.imread('original.jpg')
    # gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    # hoge = 10969
    piyo += '4'
    # gray = 0
    return piyo

if __name__ == '__main__':
    piyo = main(piyo)