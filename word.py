#"[10, 5, 1, 7, 40, 50]", "1", "7"
s = []
s = input()
print(type(s))
s1 = s[0:1]
print(s1)
listToStr = ' '.join(map(str, s1))
print(listToStr)
list1 = [listToStr]
print(type(list1))
