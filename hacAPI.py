# python 一些集成 hac 加密算法

import hashlib
import hmac
import base64

class hacAPI():
    # 计算MD5
    @staticmethod
    def md5sum(indata):
        if 'str' in str(type(indata)):
            message = bytes(indata, 'utf-8')
        else:
            message = indata
        m = hashlib.md5() 
        m.update(message) 
        return m.hexdigest()

    # 计算 sha1 hash值
    @staticmethod
    def hashsha1(token,indata):
        if isinstance(token,str):
            token = bytes(token, 'utf-8')
        if isinstance(indata,str):
            indata = bytes(indata, 'utf-8')
        hash = hmac.new(token, indata, hashlib.sha1)
        return hash.hexdigest()

    # 计算 sha1 hash值
    @staticmethod
    def hashsha256(token,indata):
        if isinstance(token,str):
            token = bytes(token, 'utf-8')
        if isinstance(indata,str):
            indata = bytes(indata, 'utf-8')
        hash = hmac.new(token, indata, hashlib.sha256)
        return hash.hexdigest()


    # 计算 sha1 hash值
    @staticmethod
    def hashsha256_base64(token,indata):
        if isinstance(token,str):
            token = bytes(token, 'utf-8')
        if isinstance(indata,str):
            indata = bytes(indata, 'utf-8')
        hash = hmac.new(token, indata, hashlib.sha256)
        digest = hash.digest()
        return base64.b64encode(digest).decode()
if __name__ == '__main__':
    
    # 测试用例
    # 4537b1c76c8a62e330d83badba53c983
    print(hacAPI().md5sum('YcSmile_python'))

    # 69f6222fc55f37571117c5317212f6107611c425
    print(hacAPI().hashsha1('token','YcSmile_python'))
    # 2c06e9a6baa55a410e015161bca1c313b6662a80183c1113fc34dbbc60b5d55b
    print(hacAPI().hashsha256('token','YcSmile_python'))
    # LAbpprqlWkEOAVFhvKHDE7ZmKoAYPBET/DTbvGC11Vs=
    print(hacAPI().hashsha256_base64('token','YcSmile_python'))

