# !/bin/bash

# تحديد اسم ملف الـ .ini
ini_file="cssonfig.ini"

# الحصول على المسار الحالي للملف
file_path=$(pwd)

# إنشاء ملف الـ .ini وكتابة المسار فيه
echo "[Settings]" > $ini_file
echo "path = $file_path" >> $ini_file

# تأكيد إنشاء الملف بنجاح
echo "تم إنشاء الملف $ini_file بنجاح."
