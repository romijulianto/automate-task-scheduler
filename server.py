import json
import os

xml_template = '''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2024-08-26T21:27:41.7160271</Date>
    <Author>IEDCC10\\iedcc_10</Author>
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
      <UserId>S-1-5-21-611098785-3368896855-1873054752-1003</UserId>
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
      <Command>"C:\\Program Files\\WindowsApps\\Microsoft.PowerAutomateDesktop_11.2407.242.0_x64__8wekyb3d8bbwe\\PAD.Console.Host.exe"</Command>
      <Arguments>{link}</Arguments>
    </Exec>
  </Actions>
</Task>
'''

def create_xml_from_json(data):
    if not os.path.exists('data'):
        os.makedirs('data')

    for item in data:
        nama_file = item.get('nama_file')
        link = item.get('link').replace('&', '&amp;')
        start_time = item.get('start_time')

        xml_content = xml_template.format(nama_file=nama_file, link=link, start_time=start_time)

        file_name = f"data/{nama_file}.xml"
        with open(file_name, 'w', encoding='utf-16') as file:
            file.write(xml_content)
        print(f"File {file_name} telah dibuat.")

with open('data/list_flow.json', 'r') as json_file:
    json_data = json.load(json_file)
    
create_xml_from_json(json_data)
