import pyrealsense2 as rs
import numpy as np
import cv2

# 创建管道和配置
pipeline = rs.pipeline()
config = rs.config()

# 启用RGB流
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

# 启动设备
profile = pipeline.start(config)

try:
    while True:
        # 获取帧
        frames = pipeline.wait_for_frames()
        
        # 提取RGB帧
        color_frame = frames.get_color_frame()
        
        if not color_frame:
            continue
            
        # 转换为numpy数组
        color_image = np.asanyarray(color_frame.get_data())
        
        # 显示RGB图像
        cv2.imshow('RGB Image', color_image)
        
        # 按Q保存并退出
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            # 保存为无损PNG
            cv2.imwrite("color_image.png", color_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            break
            
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
