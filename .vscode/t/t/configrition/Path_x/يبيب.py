from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os

def encrypt_file(file_path, password):
    # إنشاء ملح (salt) عشوائي
    salt = os.urandom(16)

    # استخدام Scrypt لاشتقاق مفتاح التشفير من كلمة المرور
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # إنشاء IV عشوائي
    iv = os.urandom(16)

    # إنشاء كائن التشفير
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # قراءة محتويات الملف
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # تشفير البيانات
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # كتابة الملح و IV والنص المشفر إلى ملف جديد
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + ciphertext)

    print(f"File '{file_path}' has been encrypted to '{file_path}.enc'")

# مثال على الاستخدام
encrypt_file('plaintext.txt', 'yourpassword')
