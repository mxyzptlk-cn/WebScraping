# coding=utf-8
# Author: Mxyzptlk
# Date: 2018-08-16

import pyautogui as ag
import pyperclip as pc
from time import sleep
from openpyxl import load_workbook


def get_list():
    data_sheet = load_workbook('test.xlsx')
    data = data_sheet.active
    data_list = []
    for i in range(2, 500):
        if data['A' + str(i)].value is None:
            break
        else:
            data_item = []
            data_item.append(data['A' + str(i)].value)
            data_item.append(data['B' + str(i)].value)
            data_item.append(data['C' + str(i)].value)
            data_item.append(data['D' + str(i)].value)
            data_list.append(data_item)
    return data_list


# # aa = 473
# # for i in range(29):
# #     ag.click(15, aa, duration=0.25)
# #     aa += 15
# sleep(0.2)

arg = get_list()
ag.click(1803, 10, duration=0.25)

pc.copy(arg[0][0])  # 编码：
# ag.moveTo(123, 445, duration=0.25)
ag.click(123, 445, duration=0.25)
ag.hotkey('ctrl', 'v')
sleep(0.5)
pc.copy(arg[0][1])  # 姓名：
# ag.moveTo(220, 445, duration=0.25)
ag.click(220, 445, duration=0.25)
ag.hotkey('ctrl', 'v')
sleep(0.5)
