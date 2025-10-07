from WeChat_Auto.find_image import *
from WeChat_Auto.simulate_click import *
from gaodeditu.return_number import get_next_phone_number
import time


def input_phone_number(phone_number):
    """
    使用 pyautogui 输入号码到当前活动的输入框中。

    参数:
    phone_number (str): 要输入的号码。
    """
    # 等待一些时间，确保当前窗口已准备好接收输入
    time.sleep(2)

    # 输入号码
    pyautogui.typewrite(phone_number)

    print(f"已输入号码：{phone_number}")
if __name__ == '__main__':
    photo_path = [
        r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_1.png'
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_2.png'
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_4.png'
        ,r''
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_5.png'
        , r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_6.png'
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_6_1.png'
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_6_2.png'
        ,r'C:\Users\Administrator\Desktop\WebScraper_Pro\weixin\wx_photo\img_7.png'


                  ]
    for num in range(1,15):

        for a in range(len(photo_path)):
            if a != 3:
                time.sleep(2)
                print(f"NEXT：{photo_path[a]}")
                location = find_image_location(photo_path[a])

                # 如果找到位置，则执行点击
                if location:
                    click_at_position(location)
                else:
                    continue





            if a == 3:

                output_file = r'C:\Users\Administrator\Desktop\WebScraper_Pro\gaodeditu\珠海.csv'
                number = get_next_phone_number(output_file)

                phone_number = str(number)  # 你想输入的号码
                input_phone_number(phone_number)
        print("sleep/20s")
        time.sleep(15)
        if num % 10 == 0:
            print("sleep/40s")
            time.sleep(15)




