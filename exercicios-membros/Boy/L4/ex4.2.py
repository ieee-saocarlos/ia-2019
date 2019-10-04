import math


def test():
    dic={"a": 0 ,"b": 0 , "c":0}
    for a in range (499):
        for b in range (499):
            if((a)+(b)+math.sqrt((a**2)+(b**2))==1000):
                dic['a']=a
                dic['b']=b
                dic['c'] = round(math.sqrt((a ** 2) + (b ** 2)))
                return dic

pit=test()
print(f'a = {pit["a"]}')
print(f'b = {pit["b"]}')
print(f'c = {pit["c"]}')
print(f'a + b + c = {pit["a"]+pit["b"]+pit["c"]}')
print(f'a * b * c = {pit["a"]*pit["b"]*pit["c"]}')