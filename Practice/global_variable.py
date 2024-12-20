from rich import print
from tqdm import tqdm
from timeit import default_timer as timer

start = timer()
global_var = 10


def func():
    ans = 0
    local_var = global_var  #use local_var inside a function for optimization. As Python iterates line by line.
    for i in tqdm(range(1000)):
        ans += local_var * i
        #print(ans)
    return ans


func()
end = timer()
print(end - start)