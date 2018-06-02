from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


RSA_PATH = '.'
RSA_PUBLIC = 'rsa_public.pem'
RSA_PRIVATE = 'rsa_private.pem'

# 生成密钥对
def rsa_generate(type_):
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    # master的秘钥对的生成
    private_pem = rsa.exportKey()

    with open(type_ + 'private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open(type_ + 'public.pem', 'wb') as f:
        f.write(public_pem)





# 使用公钥加密
def rsa_encrypt(message):
    # 加载公钥
    with open(RSA_PATH + '/' + RSA_PUBLIC, 'rb') as f:
        public_pem = f.read().decode('utf-8')
        rsakey = RSA.importKey(public_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_byte = base64.b64encode(cipher.encrypt(message))
        return cipher_byte

# 使用私钥解密
def rsa_decrypt(message):
    with open(RSA_PATH + '/' + RSA_PRIVATE, 'rb') as f:
        private_pem = f.read().decode('utf-8')
        rsakey = RSA.importKey(private_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_byte = cipher.decrypt(base64.b64decode(message),sentinel=None)
        return cipher_byte

# 加密长度不超过117个
# 超过使用分段加密拼合
if __name__ == '__main__':    
    rsa_generate('rsa_')

    print(rsa_decrypt(rsa_encrypt(bytes('123456',encoding='utf-8'))))
# 使用私钥解密

