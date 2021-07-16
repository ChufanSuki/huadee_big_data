# 第一步是引包
import hashlib
# 创建一个md5算法的对象
hs = hashlib.sha1()
print(hs)
data = "123"
# update中的 参数必须是二进制字节流 
hs.update(data.encode())
## hexdigest 返回32位十六进制的字符串(固定长度)
## 用一个hsvar来接收经过哈希算法返回的值
# 加盐
hs.update("13sda23".encode())
hsvar = hs.hexdigest()
print(hsvar)