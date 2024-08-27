import json
import os
import re 
from dotenv import load_dotenv


load_dotenv()

author = os.getenv('AUTHOR')
user_id = os.getenv('USER_ID')
path_rpa_console = os.getenv('PATH_RPA_CONSOLE')
ms_console_parent = os.getenv('MS_CONSOLE_PARENT')

xml_template = '''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2024-08-26T21:27:41.7160271</Date>
    <Author>{author}</Author>
    <URI>\\PowerAutomate\\RPACordash\\{nama_file}</URI>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>{start_time}</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>{user_id}</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>"{path_rpa_console}"</Command>
      <Arguments>{ms_console_parent}&amp;workflowid={workflowid}&amp;source=Other</Arguments>
    </Exec>
  </Actions>
</Task>
'''

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def create_xml_from_json(data):
    if not os.path.exists('data'):
        os.makedirs('data')

    for item in data:
        nama_file = item.get('nama_file')
        workflowid = item.get('workflowid')
        start_time = item.get('start_time')

        clean_nama_file = sanitize_filename(nama_file)

        xml_content = xml_template.format(
            author=author,
            user_id=user_id,
            path_rpa_console=path_rpa_console,
            ms_console_parent=ms_console_parent,
            nama_file=clean_nama_file,
            workflowid=workflowid,
            start_time=start_time
        )

        file_name = f"data/{clean_nama_file}.xml"
        with open(file_name, 'w', encoding='utf-16') as file:
            file.write(xml_content)
        print(f"File {file_name} telah dibuat.")

with open('data/list_flow_cordash.json', 'r') as json_file:
    json_data = json.load(json_file)
    
create_xml_from_json(json_data)
