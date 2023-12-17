import cv2
import os
from datetime import datetime

# 打开摄像头（通常摄像头设备文件路径为'/dev/video0'）
cap = cv2.VideoCapture(0)

# 指定照片保存路径
photo_dir = "/home/YHS/Desktop/Colaps/picture"

while True:
    # 读取摄像头的每一帧
    ret, frame = cap.read()

    # 在窗口中显示帧
    cv2.imshow('Camera', frame)

    # 按下 's' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

    # 按下 'c' 键拍照
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # 获取当前系统本地时间
        current_time = datetime.now()

        # 使用当前时间生成文件名
        timestamp = current_time.strftime("%Y%m%d_%H%M%S")
        photo_path = os.path.join(photo_dir, f"photo_{timestamp}.jpg")

        # 保存照片
        cv2.imwrite(photo_path, frame)
        print(f"Photo saved as {photo_path}")

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
