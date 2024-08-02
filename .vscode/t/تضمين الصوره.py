import os
import json
import base64

def get_directory_structure(rootdir):
    """
    إنشاء بنية المجلدات والملفات في شكل قاموس، مع تضمين محتوى كل ملف.
    """
    directory_structure = {}

    for dirpath, dirnames, filenames in os.walk(rootdir):
        # التقسيم بناءً على الجذر
        folder_path = dirpath.replace(rootdir, "").strip(os.sep)
        folder_levels = folder_path.split(os.sep) if folder_path else []

        # الحصول على المرجع في البنية
        current_level = directory_structure
        for level in folder_levels:
            current_level = current_level.setdefault(level, {})

        # إضافة المجلدات
        for dirname in dirnames:
            current_level[dirname] = {}

        # إضافة الملفات مع محتواها
        if filenames:
            files_info = []
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_content = ""
                try:
                    # محاولة قراءة الملف باستخدام ترميز UTF-8
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                    files_info.append({filename: {"type": "text", "content": file_content}})
                except (UnicodeDecodeError, IsADirectoryError):
                    # إذا كان الملف ثنائي (مثل الصور) أو مجلد
                    try:
                        with open(file_path, 'rb') as file:
                            binary_content = file.read()
                            file_content = base64.b64encode(binary_content).decode('utf-8')
                        files_info.append({filename: {"type": "binary", "content": file_content}})
                    except Exception as e:
                        file_content = f"Error reading file: {e}"
                        files_info.append({filename: {"type": "error", "content": file_content}})

            current_level['files'] = files_info

    return directory_structure

def save_to_json(data, output_file):
    """
    حفظ البيانات في ملف JSON
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# تحديد مسار المجلد الجذري
root_directory = r'D:\App.py\progrmming\configrition\bin\_con'  # استبدل هذا المسار بمسار المجلد الجذري لديك
output_file = 'directory_structure_with_iamge.json'

# الحصول على بنية المجلدات والملفات
directory_structure = get_directory_structure(root_directory)

# حفظ البنية في ملف JSON
save_to_json(directory_structure, output_file)

print(f"تم حفظ بنية المجلدات والملفات في {output_file}")
