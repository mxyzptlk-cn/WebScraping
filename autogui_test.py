# coding=utf-8
# Author: Mxyzptlk
# Date: 2018-08-16

# 1	医生
# 2	护士
# 3	医技
# 4	药房
# 5	后勤
# 6	物资
# 7	收费员


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


def fill_form(arg):
    pc.copy(arg[0])  # 编码：
    # ag.moveTo(123, 445, duration=0.25)
    ag.click(123, 445, duration=0.25)
    ag.hotkey('ctrl', 'v')
    sleep(0.5)
    pc.copy(arg[1])  # 姓名：
    # ag.moveTo(220, 445, duration=0.25)
    ag.click(220, 445, duration=0.25)
    ag.hotkey('ctrl', 'v')
    sleep(0.5)
    pc.copy(arg[2])  # 科室：
    # ag.moveTo(124, 549, duration=0.25)
    ag.click(124, 549, duration=0.25)
    ag.hotkey('ctrl', 'v')
    ag.hotkey('\n')
    sleep(0.5)


def prescription_setting():
    coordinates = [[535, 470], [570, 525], [633, 525], [700, 525], [587, 703],
                   [359, 777], [446, 777], [453, 821], [553, 821]]
    for i in coordinates:
        # ag.moveTo(i[0], i[1], duration=0.25)
        ag.click(i[0], i[1], duration=0.25)
        sleep(0.5)


def privilege_setting(arg):
    aa = 473
    ag.doubleClick(189, 228, duration=0.25)
    sleep(0.5)
    # 可以登陆:
    ag.click(544, 379, duration=0.25)
    if arg == 1:
        ag.click(15, aa, duration=0.25)
    elif arg == 2:
        ag.click(15, aa + 15 * (arg - 1), duration=0.25)
    elif arg == 3:
        ag.click(15, aa + 15 * (arg - 1), duration=0.25)
    elif arg == 4:
        ag.click(15, aa + 15 * (arg - 1), duration=0.25)
    ag.click(1026, 599, duration=0.25)
    ag.click(976, 600, duration=0.25)
    ag.click(1812, 997, duration=0.25)
    ag.click(439, 33, duration=0.25)
    ag.click(502, 131, duration=0.25)
    sleep(1)


list_item = get_list()
# 最小化当前窗口
# ag.moveTo(1803, 10, duration=0.25)
ag.click(1803, 10, duration=0.25)

for l in list_item:
    print(type(l[3]))
    if l[3] == 1:
        # 1	医生
        fill_form(l)
        ag.click(391, 703, duration=0.25)  # 病区：
        ag.hotkey('\n')
        sleep(0.5)
        prescription_setting()
        # 保存607, 1002
        ag.click(607, 1002, duration=0.25)
        sleep(0.5)
        # 插入成功976, 600
        ag.click(976, 600, duration=0.25)
        sleep(0.5)
        privilege_setting(1)

    elif l[3] == 2:
        # 2	护士
        fill_form(l)
        ag.click(391, 703, duration=0.25)  # 病区：
        ag.hotkey('\n')
        sleep(0.5)
        # 保存607, 1002
        ag.click(607, 1002, duration=0.25)
        sleep(0.5)
        # 插入成功976, 600
        ag.click(976, 600, duration=0.25)
        sleep(0.5)
        privilege_setting(2)
    elif l[3] == 3:
        # 3	医技
        fill_form(l)
        # 保存607, 1002
        ag.click(607, 1002, duration=0.25)
        sleep(0.5)
        # 插入成功976, 600
        ag.click(976, 600, duration=0.25)
        sleep(0.5)
        privilege_setting(3)
    elif l[3] == 4:
        # 4	药房
        pass
    elif l[3] == 5:
        # 5	后勤
        pass
    elif l[3] == 6:
        # 6	物资
        pass
    elif l[3] == 7:
        # 7	收费员
        pass

print('Done.')
