import pyautogui
import cv2
import numpy as np


def find_image_location(photo_path, threshold=0.8):
    """
    根据给定的图片路径，在屏幕上查找该图片的位置。

    参数:
    photo_path (str): 要查找的图片的路径。
    threshold (float): 匹配的阈值，默认值为 0.8。值越高，匹配越严格。

    返回:
    tuple: 如果找到匹配，返回图片的位置 (x, y)（中心坐标），否则返回 None。
    """
    # 获取当前屏幕截图
    screenshot = pyautogui.screenshot()

    # 将截图转换为 numpy 数组
    screenshot = np.array(screenshot)

    # 转换为灰度图，因为模板匹配需要灰度图
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # 加载目标图片（模板图片）
    template = cv2.imread(photo_path, 0)  # 读取为灰度图

    # 使用模板匹配来找到图片的位置
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # 获取匹配位置
    locations = np.where(result >= threshold)

    # 如果找到匹配位置，则返回该位置
    if len(locations[0]) > 0:
        # 获取第一个匹配位置
        top_left = (locations[1][0], locations[0][0])  # (x, y) 坐标

        # 计算点击位置的中心点
        template_height, template_width = template.shape
        click_x = top_left[0] + template_width // 2
        click_y = top_left[1] + template_height // 2

        return (click_x, click_y)
    else:
        return None