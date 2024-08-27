import os
import subprocess
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except OSError:
        return False

if is_admin():
    folder_path = r"D:\use-case\rpa-cordash\app\automate-task-scheduler\data"

    xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]

    for xml_file in xml_files:
        full_path = os.path.join(folder_path, xml_file)
        task_name = os.path.splitext(xml_file)[0]

        task_path = f"\\PowerAutomate\\RPACordash\\{task_name}"
        
        try:
            subprocess.run(['schtasks', '/Create', '/TN', task_path, '/XML', full_path], check=True)
            print(f"Successfully imported task: {task_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to import task: {task_name}, Error: {e}")
else:
    print("Please run this script as administrator.")
