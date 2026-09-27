ACTIONS = ("wink", "double blink", "close your eyes", "jump", "reverse")

def commands(binary_str):    
    result = [
        ACTIONS[i]
        for i, b in enumerate(binary_str[::-1][:-1])
        if b == "1"
    ]    
    return result if binary_str[0] == "0" else result[::-1]