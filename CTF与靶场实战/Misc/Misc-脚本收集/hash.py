import hashlib

def find_password(target_md5):
    for password in range(1000000):  # 从 000000 到 999999 的 6 位数字密码范围
        password_str = str(password).zfill(6)  # 用 0 填充到 6 位
        md5_hash = hashlib.md5(password_str.encode()).hexdigest()

        if md5_hash == target_md5:
            return password_str

    return None  # 未找到匹配的密码

# 给定的 MD5 值
target_md5 = "bd5b2d0550c9329961ab1be67c0890ca"

# 查找密码
result = find_password(target_md5)

if result:
    print(f"找到密码：{result}")
else:
    print("未找到匹配的密码")


"""
import hashlib
import itertools
import string

def find_password(target_md5):
    # 定义密码字符集
    characters = string.digits + string.ascii_letters + string.punctuation

    # 生成长度为 6 的密码组合
    password_combinations = itertools.product(characters, repeat=6)

    for password_tuple in password_combinations:
        password_str = ''.join(password_tuple)
        md5_hash = hashlib.md5(password_str.encode()).hexdigest()

        if md5_hash == target_md5:
            return password_str

    return None  # 未找到匹配的密码

# 给定的 MD5 值
target_md5 = "e6a64ac8020097475992a566db299828"

# 查找密码
result = find_password(target_md5)

if result:
    print(f"找到密码：{result}")
else:
    print("未找到匹配的密码")

"""