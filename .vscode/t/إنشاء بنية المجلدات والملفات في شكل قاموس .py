import os
import json


def get_directory_structure(rootdir):
    """
    إنشاء بنية المجلدات والملفات في شكل قاموس
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

        # إضافة الملفات
        if filenames:
            current_level['files'] = filenames

    return directory_structure


def save_to_json(data, output_file):
    """
    حفظ البيانات في ملف JSON
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# تحديد مسار المجلد الجذري
root_directory = r'D:\App.py\progrmming\configrition\bin\_con'  # استبدل هذا المسار بمسار المجلد الجذري لديك
output_file = 'directory_structure_file_is_empty.json'

# الحصول على بنية المجلدات والملفات
directory_structure = get_directory_structure(root_directory)

# حفظ البنية في ملف JSON
save_to_json(directory_structure, output_file)

