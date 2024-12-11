from rich import print
import tdqm

global_var = 10

def func():
    ans = 0
    for i in tdqm(range(1000)):
        ans += global_var * i
    return ans

func()