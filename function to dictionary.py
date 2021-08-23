def list_filter(l):
    odd_list = []
    even_list = []
    odd_sum = 0
    even_sum = 0
    for x in l:
        if x % 2 == 0:
            even_list.append(x)
            even_sum += x
        else:
            odd_list.append(x)
            odd_sum += x    

    return{
        "odd": {
            "sum": odd_sum,
            "list": odd_list,
            "len": len(odd_list)
        },
        "even": {
            "sum": even_sum,
            "list": even_list,
            "len": len(even_list)
        }
    }
numbers = [2,100,3,12,313,44,33,22]    
print(list_filter(numbers))


print('-----------------')


palindrome = 'Talat'

def check_palindrome(string):
    hold = ""
    for x in string:
        hold = x + hold

    if string.lower() == hold.lower():
        return True
    return False
print(check_palindrome(palindrome))            