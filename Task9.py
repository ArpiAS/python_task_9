def func_num(text):
    text_str = str(text)
        
    if type(text) is int and text_str[0] != "0":
        print('0'+ text_str)
    elif text_str[0] == "0":
        print(text_str)
    else:
        print("Not a Number")

func_num(10)
func_num("0102")
func_num("014502")
func_num("aaaaa")

    

