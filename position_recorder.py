import serial
import re
import xlwt
import time


if __name__ == '__main__':
    s1 = serial.Serial('com13', 115200)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('position', cell_overwrite_ok=True)
    worksheet.write(0, 0, "X")
    worksheet.write(0, 1, "Y")
    worksheet.write(0, 2, "zero_x")
    worksheet.write(0, 3, "zero_y")
    cnt = 1
    while True:

        char = str(s1.readline())
        print(len(char))
        if(len(char)>63):
            continue
        # char = char[2:-5]
        nums = re.findall("\d+",char)
        worksheet.write(cnt, 0, str(nums[0]))
        worksheet.write(cnt, 1, str(nums[1]))
        worksheet.write(cnt, 2, str(nums[2]))
        worksheet.write(cnt, 3, str(nums[3]))
        cnt += 1
        print(nums)
        if(cnt == 1000):
            break
    workbook.save("position.xls")