import time
from concurrent.futures import ThreadPoolExecutor
import random

lst = [random.randint(1, 100) for i in range(1000)]

def sum_list(lst):
    return sum(lst)

def multi_thread_sum(lst):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(sum_list, lst[i:i+100]) for i in range(0, len(lst), 100)]
    result = sum([f.result() for f in futures])
    end_time = time.time()
    print("start time: ",start_time)
    print("end time: ",end_time)
    print("Multi thread time: ", end_time - start_time)
    print ("Result sum lst: ", result)
    

def single_thread_sum(lst):
    start_time = time.time()
    result = sum_list(lst)
    end_time = time.time()
    print("start time: ",start_time)
    print("end time: ",end_time)
    print("Single thread time: ", end_time - start_time)
    print ("Result sum lst: ", result)


print(single_thread_sum(lst))
print(multi_thread_sum(lst))