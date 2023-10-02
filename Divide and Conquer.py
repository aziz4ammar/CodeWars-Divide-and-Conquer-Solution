def div_con(x):
    int_sum = 0
    char_sum = 0
    
    for item in x:
        if isinstance(item, int):
            int_sum += item
        elif isinstance(item, str) and item.isdigit():
            char_sum += int(item)
    
    return int_sum - char_sum