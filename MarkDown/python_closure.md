#Python的闭包

闭包概念都是一样的，实现机制一样，看看下面的代码是不是和javascript很像

```python
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
```