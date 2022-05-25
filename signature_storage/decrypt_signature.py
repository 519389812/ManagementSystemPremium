import os
import rsa
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5, PKCS1_OAEP
from urllib import parse


def set_crypto_pri_key(pem_dir='', mode='PKCS1_OAEP/PKCS1_v1_5', version='v1'):
    if pem_dir == '':
        pem_dir = os.getcwd()
    pem_path = os.path.join(pem_dir, 'pri_%s.pem' % version)
    if not os.path.exists(pem_path):
        raise "private pem file not found."
    crypto_pri_key = RSA.import_key(open(pem_path).read())
    if mode == 'PKCS1_OAEP':
        cipher_pri_PKCS1_OAEP = PKCS1_OAEP.new(crypto_pri_key)
        return cipher_pri_PKCS1_OAEP
    elif mode == 'PKCS1_v1_5':
        cipher_pri_PKCS1_v1_5 = PKCS1_v1_5.new(crypto_pri_key)
        return cipher_pri_PKCS1_v1_5


def crypto_rsa_decrypt(cipher, text='b64encode string', mode='PKCS1_OAEP/PKCS1_v1_5'):
    if type(text) is not bytes:
        try:
            text = base64.b64decode(text)
        except:
            return "decrypt error. not a b64encode text."
    if mode == 'PKCS1_OAEP':
        return cipher.decrypt(text).decode()
    elif mode == 'PKCS1_v1_5':
        return cipher.decrypt(text, "decrypt error").decode()
    else:
        return "mode error."


def crypto_rsa_decrypt_long(cipher, text='b64encode text', mode='PKCS1_OAEP/PKCS1_v1_5', rsa_length=128):
    if type(text) is not bytes:
        try:
            text = base64.b64decode(text)
        except:
            return "decrypt error. not a b64encode text."
    text_length = len(text)
    result = []
    for i in range(0, text_length, rsa_length):
        result.append(crypto_rsa_decrypt(cipher, text[i:i + rsa_length], mode))
    return ''.join(result)


def rsa_decrypt(enc_text, pem_path='./pri.pem'):
    if not os.path.exists(pem_path):
        return "decrypt error, private pem file not found."
    with open(pem_path, 'rb') as f:
        pri_key = f.read()
    pri_key = rsa.PrivateKey.load_pkcs1(pri_key)
    return rsa.decrypt(enc_text, pri_key)


def aes_decrypt(text, key):
    if type(key) == str:
        key = key.encode()
    aes = AES.new(key, mode=AES.MODE_ECB)
    decrypted_text = aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).decode("utf8")
    decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位
    return decrypted_text


if __name__ == '__main__':
    signature_storage = os.listdir(os.path.join(os.getcwd(), 'signature'))
    current_version = ''
    print('Start.')
    for signature in signature_storage:
        file_name, ext = os.path.splitext(signature)
        if ext == '.txt':
            # try:
            print(file_name)
            id_, key, version = file_name.split('-')
            print(key)
            if current_version != version or 'cipher' not in locals():
                cipher = set_crypto_pri_key(mode='PKCS1_v1_5', version=version)
            key = crypto_rsa_decrypt(cipher, key, "PKCS1_v1_5")
            with open(signature, 'r') as f:
                text = parse.unquote(aes_decrypt(f.read(), key))
                encoded_image = text.split(",")[1]
                decoded_image = base64.b64decode(encoded_image)
            with open('%s.png' % id_, 'wb') as f:
                f.write(decoded_image)
            os.remove(signature)
            # except:
            #     continue
