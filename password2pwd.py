from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def encrypt(password):
    # 将密码字符串编码为字节数组
    plaintext = password.encode('utf-8')
    # 密钥
    key = b'k;)*(+nmjdsf$#@d'
    # 初始化AES加密器
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # 使用PKCS7填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # 进行AES加密
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # 将ciphertext转换为Base64编码的字符串
    ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')

    return ciphertext_base64
