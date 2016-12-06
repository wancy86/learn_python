# Python字符进度条

from tqdm import trange
from time import sleep

for r in trange(10, 1, -1):
    try:
        sleep(0.1)
    except:
        print()
        print("异常错误~~~")
        sleep(0.6)
