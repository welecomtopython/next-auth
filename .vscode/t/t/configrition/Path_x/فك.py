from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

def decrypt_file(file_path, password):
    # قراءة البيانات من الملف المشفر
    with open(file_path, 'rb') as f:
        data = f.read()

    # استخراج الملح و IV والنص المشفر
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]

    # استخدام Scrypt لاشتقاق مفتاح التشفير من كلمة المرور
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # إنشاء كائن فك التشفير
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # فك تشفير البيانات
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # كتابة النص العادي إلى ملف جديد
    with open(file_path.replace('.enc', '_decrypted.txt'), 'wb') as f:
        f.write(plaintext)

    print(f"File '{file_path}' has been decrypted to '{file_path.replace('.enc', '_decrypted.txt')}'")

# مثال على الاستخدام
decrypt_file('plaintext.txt.enc', 'yourpassword')

with open('plaintext.txt.enc','a') as s:
    print(s.write('sedsssssssssssssssssssssssssssssssss'))