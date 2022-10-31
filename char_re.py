import re



if __name__ == '__main__':
    string = "PositionX:100    PositionY:98    Zero_x:110    Zero_y:110"
    print(string)
    print(re.findall("\d+", string))