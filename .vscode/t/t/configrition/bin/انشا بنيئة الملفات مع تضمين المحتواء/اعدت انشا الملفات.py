import os
import json

def create_structure_from_json(json_file, rootdir):
    """
    قراءة بنية المجلدات والملفات من ملف JSON وإنشاؤها في نظام الملفات، وكتابة المحتوى المحدد في الملفات.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        structure = json.load(f)

    def create_items(base_path, items):
        for name, content in items.items():
            if name == 'files':
                # معالجة الملفات
                for file_info in content:
                    if isinstance(file_info, dict):
                        for filename, file_content in file_info.items():
                            file_path = os.path.join(base_path, filename)
                            os.makedirs(os.path.dirname(file_path), exist_ok=True)
                            with open(file_path, 'w', encoding='utf-8') as file:
                                file.write(file_content)  # كتابة النص المحدد في JSON داخل الملف
            else:
                # معالجة المجلدات
                folder_path = os.path.join(base_path, name)
                os.makedirs(folder_path, exist_ok=True)
                create_items(folder_path, content)

    create_items(rootdir, structure)

# تحديد مسار ملف JSON
json_file = 'directory_structure.json'
# تحديد مسار المجلد الجذري حيث سيتم إنشاء البنية
root_directory = r'D:\App.py\progrmming\configrition\bin\_con\test'  # استبدل هذا المسار بمسار المجلد الجذري لديك

# إنشاء المجلدات والملفات من ملف JSON وكتابة المحتوى
create_structure_from_json(json_file, root_directory)

print(f"تم إنشاء بنية المجلدات والملفات في {root_directory} وكتابة المحتوى المحدد.")
