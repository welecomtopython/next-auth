import os
import json


def create_structure_from_json(json_file, rootdir):
    """
    قراءة بنية المجلدات والملفات من ملف JSON وإنشاؤها في نظام الملفات
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        structure = json.load(f)

    def create_items(base_path, items):
        for name, content in items.items():
            if name == 'files':
                for filename in content:
                    file_path = os.path.join(base_path, filename)
                    open(file_path, 'w').close()
            else:
                folder_path = os.path.join(base_path, name)
                os.makedirs(folder_path, exist_ok=True)
                create_items(folder_path, content)

    create_items(rootdir, structure)


# تحديد مسار ملف JSON
json_file = 'directory_structure_file_is_empty.json'

# تحديد مسار المجلد الجذري حيث سيتم إنشاء البنية
root_directory = r'D:\App.py\progrmming\configrition\bin\_con\test'  # استبدل هذا المسار بمسار المجلد الجذري لديك

# إنشاء بنية المجلدات والملفات من ملف JSON
create_structure_from_json(json_file, root_directory)

print(f"تم إنشاء بنية المجلدات والملفات في {root_directory}")
