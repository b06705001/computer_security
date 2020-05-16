
import hashlib

prefix_length = 5
base = 'kaibro'
nonce = 0 # 為了方便計算，我們使用數字作為nonce字串
want=input()
while True:
    hash_input = base + str(nonce) # 兩個字串接在一起
    hash_func = hashlib.md5()
    hash_func.update(hash_input.encode('utf-8')) # 以SHA256計算hash值
    result = hash_func.hexdigest() # 將結果轉成16進位的字串
    
    if result[:prefix_length] == want :# 檢查結果是否符合條件
        print('Nonce:', nonce) # 最後的nonce值就是我們要的答案
        print('Result:', result)
        break
    else:
        nonce += 1 # 如果hash值不符合條件，將nonce+1再算一次