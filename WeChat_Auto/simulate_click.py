import pyautogui
import random
import time
import math



def click_at_position(position, duration=1, jitter=10, curve_factor=0.2, speed_up_factor=0.5, click_type='left'):
    """
    根据传入的坐标，模拟点击屏幕上的某个位置，使其更加符合人类操作。

    参数:
    position (tuple): 坐标 (x, y)，表示点击位置。
    duration (float): 模拟鼠标移动的总时间（秒）。较长时间让移动更平滑。
    jitter (int): 模拟鼠标移动过程中，位置的随机抖动范围（像素）。用于模拟人类的不规则操作。
    curve_factor (float): 鼠标移动过程中曲线的变化程度。0 代表直线，1 代表非常弯曲。
    speed_up_factor (float): 模拟加速和减速的程度。1 代表匀速，值越小加速和减速越明显。
    click_type (str): 模拟的点击类型，可以是 'left', 'double', 或 'right'。

    返回:
    None
    """
    if position:
        # 获取屏幕分辨率，以调整鼠标移动速度和抖动范围
        screen_width, screen_height = pyautogui.size()
        screen_ratio = screen_width / 1920  # 以 1920 宽屏为基准

        # 动态调整 jitter 和 duration 以适应不同分辨率
        adjusted_jitter = int(jitter * screen_ratio)
        adjusted_duration = duration * screen_ratio

        # 目标位置附近增加随机抖动，模拟人类的“抖动”
        jitter_x = random.randint(-adjusted_jitter, adjusted_jitter)
        jitter_y = random.randint(-adjusted_jitter, adjusted_jitter)

        # 初始位置（当前鼠标位置）
        start_x, start_y = pyautogui.position()

        # 目标位置加抖动
        target_x = position[0] + jitter_x
        target_y = position[1] + jitter_y

        # 总移动的时间和步数
        total_steps = int(adjusted_duration * 60)  # 以每秒60次的频率计算步数
        move_x = target_x - start_x
        move_y = target_y - start_y

        # 路径优化：如果目标距离远，使用更弯曲的路径
        distance = math.hypot(move_x, move_y)
        if distance > 200:  # 例如，当目标距离大于 200 像素时，使用更大范围的曲线
            curve_factor = 0.5  # 提升曲线幅度

        # 使用加速和减速来模拟人类鼠标操作的自然性
        for i in range(total_steps + 1):
            # 模拟加速和减速
            progress = i / total_steps
            # 使用非线性函数（如正弦）模拟加速减速效果
            easing = (math.sin(progress * math.pi / 2) ** speed_up_factor) if progress < 0.5 else (
                        math.cos((1 - progress) * math.pi / 2) ** speed_up_factor)

            # 非线性路径模拟（弯曲路径）
            curve_factor_adjusted = curve_factor * easing
            x_step = start_x + move_x * easing + random.uniform(-curve_factor_adjusted, curve_factor_adjusted)
            y_step = start_y + move_y * easing + random.uniform(-curve_factor_adjusted, curve_factor_adjusted)

            # 移动鼠标到计算出来的新位置
            pyautogui.moveTo(x_step, y_step, duration=0.01)

            # 轻微随机等待时间模拟人类移动的不稳定性
            time.sleep(random.uniform(0.01, 0.03))

        # 等待一小段时间模拟自然点击
        time.sleep(random.uniform(0.1, 0.3))

        # 执行不同类型的点击
        if click_type == 'left':
            pyautogui.click()  # 单击
        elif click_type == 'double':
            pyautogui.doubleClick()  # 双击
        elif click_type == 'right':
            pyautogui.rightClick()  # 右键点击

        #print(f"{click_type.capitalize()} click at position: {target_x}, {target_y}")
    else:
        print("无效的点击位置")


