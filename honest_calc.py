msg_0 = "Enter an equation"  # write your code here
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
operands_ = ['+', '-', '*', '/']
memory = 0
result = 0
def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ""
    while True:
        if is_one_digit(v1) and is_one_digit(v2):
            msg = msg + msg_6
        if (v1 == 1 or v2 == 1) and v3 == '*':
            msg = msg + msg_7
        if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
        print(msg)
        break


while True:
    calc = input(msg_0)
    new_calc = calc.split()
    x = new_calc[0]
    oper = new_calc[1]
    y = new_calc[2]
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper in operands_:
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        try:
            if oper == '/':
                result = x / y
        except ZeroDivisionError:
            print(msg_3)
            continue
        print(result)
    else:
        print(msg_2)
    print(msg_4)
    answ_1 = input()
    if answ_1 == 'y':
        if is_one_digit(result):
            msg_index = 10
            print(msg_[msg_index])
            answ_3 = input()
            if answ_3 == 'y':
                if msg_index < 12:
                    msg_index += 1
                    print(msg_[msg_index])
                    answ_3 = input()
                    if answ_3 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            print(msg_[msg_index])
                            answ_3 = input()
                            if msg_index == 12:
                                memory = result
                                print(msg_5)
                                answ_2 = input()
                                if answ_2 == 'y':
                                    continue
                                elif answ_2 == 'n':
                                    break
                    elif answ_3 == 'n':
                        print(msg_5)
                        answ_2 = input()
                        if answ_2 == 'y':
                            continue
                        elif answ_2 == 'n':
                            break
            elif answ_3 == 'n':
                print(msg_5)
                answ_2 = input()
                if answ_2 == 'y':
                    continue
                elif answ_2 == 'n':
                    break
                else:
                    memory = result
        else:
            memory = result
            print(msg_5)
            answ_2 = input()
            if answ_2 == 'y':
                continue
            elif answ_2 == 'n':
                break
    elif answ_1 == 'n':
        print(msg_5)
        answ_2 = input()
        if answ_2 == 'y':
            continue
        elif answ_2 == 'n':
            break





