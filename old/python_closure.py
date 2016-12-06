# python_closure.py
# 闭包实现


def generate_counter():
    cnt = [0]

    def count_one():
        cnt[0] = cnt[0] + 1
        print(cnt[0])
        return cnt[0]

    return count_one

count = generate_counter()
count()  # 1
count()  # 2
count()  # 3
