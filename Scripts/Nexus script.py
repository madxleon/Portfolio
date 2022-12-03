import requests
import win32api
import win32file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
import zipfile
import shutil
import datetime
import time
from win32api import GetFileVersionInfo, LOWORD,HIWORD


def get_file_stat():
    file_version = 'Z:\TestSoft 2.0\Vtb.FrontOffice.RR.Client.exe'
    info = win32api.GetFileVersionInfo(file_version,'\\')
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version1 = HIWORD(ms)
    version2 = LOWORD(ms)
    version3 = HIWORD(ls)
    version4 = LOWORD(ls)
    version = str(version1) + '.' + str(version2) + '.' + str(version3) + '.' + str(version4)
    text = '  Версия установленного билда: ' + version
    get_time(str(text))


def get_time(text):
  time_now = datetime.datetime.now()
  print(time_now.strftime("%d.%m.%Y %H:%M:%S") + text)


def request_distrib():

  if os.path.isfile(r'LastBuild.zip'):
    os.remove(r'LastBuild.zip')
    text = ' Файл LastBuild.zip удален'
    get_time(text)

  else:
    text = ' Файл LastBuild.zip не найден'
    get_time(text)


  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  url = "https://nexus.xxxx.xxx.xxx/service/rest/v1/search/assets/download?sort=version&repository=rctl-maven-test&maven.groupId=distrib&maven.artifactId=rctl&maven.extension=zip"
  payload={}
  headers = {
    'Authorization': 'Basic Y2RsX2Rvc19SQ1RMQxalZ2ldbi55dGIucny6bU10ZjXtWTh6RU5ZOU1IXUY0dFg='
  }
  response = requests.request("GET", url, headers=headers, data=payload, verify=False)
  open('LastBuild.zip', 'wb').write(response.content)
  stat_file = str(time.ctime(os.path.getatime('LastBuild.zip')))
  text = ' Билд скачан: ' + stat_file
  get_time(text)


def clearing_folders():
  Applications = ['Application','Auth','FileToGrtBlotter','TestSoft 2.0','RtAdmin','TestSoft 2.0','TestSoftGrt', 'WatchDog', 'TestSoft', 'TestSoft 2.0', 'TestSoft', 'FileImport', 'TestSoft']

  for path_cleare in Applications:
    path = 'Z:\\' + path_cleare
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
    if os.path.exists(path):
      shutil.rmtree(path)
      text = ' Каталог: ' + path + ' удален'
      get_time(text)

    else:
      text = ' Каталог ' + path + ' не найден'
      get_time(text)


def unzip_build():
  Applications = ['Application', 'Auth', 'FileToGrtBlotter', 'TestSoft 2.0', 'RtAdmin', 'TestSoft 2.0', 'TestSoftGrt', 'WatchDog', 'TestSoft', 'TestSoft 2.0', 'TestSoft', 'FileImport', 'TestSoft']
  with zipfile.ZipFile('LastBuild.zip', 'r') as zip_ref:
    zip_ref.extractall('Z:\\')
  text = ' билд разархивирован'
  get_time(text)

  for move_folder in Applications:
    path_from = 'Z:\\distrib\\' + move_folder
    path_to = 'Z:\\'
    shutil.move(path_from,path_to)
    text = ' перенос директории из ' + path_from +' в директорию ' + path_to
    get_time(text)
  shutil.rmtree('Z:\\distrib\\')
  text = ' каталог distr удален'
  get_time(text)


def replace_conf():
 path_file = [r'Z:\Application\appsettings.St.json',r'Z:\Auth\appsettings.St.json',r'Z:\FileToGrtBlotter\appsettings.St.json',
              r'Z:\TestSoft 2.0\appsettings.json',r'Z:\TestSoft 2.0\appsettings.St.json',r'Z:\RtAdmin\St.json',
              r'Z:\TestSoftGrt\appsettings.St.json', r'Z:\WatchDog\appsettings.St.json', r'Z:\TestSoft\appsettings.St.json',
              r'Z:\TestSoft\appsettings.St.json', r'Z:\FileImport\appsettings.St.json', r'Z:\TestSoft\appsettings.St.json',
              r'Z:\TestSoft 2.0\BoImport\appsettings.St.json', r'Z:\TestSoft 2.0\Import\appsettings.St.json',
              r'Z:\TestSoft 2.0\Transport\appsettings.St.json']

 old_options= ['http://localhost:5000','http://localhost:5011','Server=XX.XXX.XX.XXX;Database=GRT_auto;User Id=GRT;Password=GRT12;',r'C:\\GrtFiles1',r'C:\\GrtFiles\\ProcFiles',
               r'C:\\\\GrtFiles\\ProcFiles\\BadProcFiles',r'C:\\GrtFiles\\ProcFiles\\Trash',r'C:\\RpFiles',r'C:\\mikeden\\Innotech\\GrtTestSoft\\New',
               r'C:\\mikeden\\Innotech\\GrtTestSoft\\Export', 'http://XX.XXX.XX.XXX:6002']

 new_options = ['http://XX.XXX.XX.XXX:6000','http://XX.XXX.XX.XXX:6011','Server=XX.XXX.XX.XXX;Database=GRT;User Id=GRT; Password=GRT12;',r'D:\\temp\\GrtFiles',
                r'D:\\temp\\GrtFiles\\ProcFiles',r'D:\\temp\\GrtFiles\\ProcFiles\\BadProcFiles',r'D:\\temp\\GrtFiles\\ProcFiles\\Trash',r'D:\\temp\\GrtFiles\\RpFiles',
                r'D:\\temp\\TestSoftNew',r'D:\\temp\\TestSoftExport','http://XX.XXX.XX.XXX:6002']

 for replace_file in path_file:
   for new_option,old_option in zip(new_options,old_options):

       with open(replace_file, 'r') as f:
         old_data = f.read()
       new_data = old_data.replace(old_option, new_option)
       with open(replace_file, 'w') as f:
         f.write(new_data)
         text = ' конфигурационный файл ' + replace_file + ' изменен,\n опция: ' + old_option + ' >>>> '   + new_option
         get_time(text)


def request_key():
    key = input("Выполнить обновление AtSoft? Y and N\n")
    if key=='Y':
        install_AtSoft()
    else:
        text = '  Хорошего дня!'
        get_time(text)


def unzip_build_AtSoft():
    Applications = ['Application', 'Auth', 'FileToGrtBlotter', 'TestSoft 2.0', 'RtAdmin', 'TestSoft 2.0', 'TestSoftGrt', 'WatchDog', 'TestSoft', 'TestSoft 2.0', 'TestSoft', 'FileImport', 'TestSoft']
    with zipfile.ZipFile('LastBuild.zip', 'r') as zip_ref:
        zip_ref.extractall('X:\\')
    text = ' билд разархивирован'
    get_time(text)

    for move_folder in Applications:
        path_from = 'X:\\distrib\\' + move_folder
        path_to = 'X:\\'
        shutil.move(path_from, path_to)
        text = ' перенос директории из ' + path_from + ' в директорию ' + path_to
        get_time(text)
    shutil.rmtree('X:\\distrib\\')
    text = ' каталог distr удален'
    get_time(text)


def clearing_folders_AtSoft():
  Applications = ['Application','Auth','FileToGrtBlotter','TestSoft 2.0','RtAdmin','TestSoft 2.0','TestSoftGrt', 'WatchDog', 'TestSoft',
                  'TestSoft 2.0', 'TestSoft', 'FileImport', 'TestSoft']

  for path_cleare in Applications:
    path = 'X:\\' + path_cleare
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
    if os.path.exists(path):
      shutil.rmtree(path)
      text = ' Каталог: ' + path + ' удален'
      get_time(text)

    else:
      text = ' Каталог ' + path + ' не найден'
      get_time(text)


def replace_conf_AtSoft():
 path_file = [r'X:\Application\appsettings.St.json',
              r'X:\Auth\appsettings.St.json',
              r'X:\FileToGrtBlotter\appsettings.St.json',
              r'X:\TestSoft 2.0\appsettings.json',
              r'X:\TestSoft 2.0\appsettings.St.json',
              r'X:\RtAdmin\appsettings.St.json',
              r'X:\TestSoftGrt\appsettings.St.json',
              r'X:\WatchDog\appsettings.St.json',
              r'X:\TestSoft\appsettings.St.json',
              r'X:\TestSoft\appsettings.St.json',
              r'X:\FileImport\appsettings.St.json',
              r'X:\TestSoft\appsettings.St.json',
              r'X:\TestSoft 2.0\BoImport\appsettings.St.json',
              r'X:\TestSoft 2.0\Import\appsettings.St.json',
              r'X:\TestSoft 2.0\Transport\appsettings.St.json'
              ]

 old_options= ['http://XX.XXX.XX.XXX:5000','http://XX.XXX.XX.XXX:5011','Server=(local);Database=GRT;Trusted_Connection=True;',r'C:\\GrtFiles1',r'C:\\GrtFiles\\ProcFiles',
               r'C:\\\\GrtFiles\\ProcFiles\\BadProcFiles',r'C:\\GrtFiles\\ProcFiles\\Trash',r'C:\\RpFiles',r'C:\\mikeden\\Innotech\\GrtTestSoft\\New',
               r'C:\\mikeden\\Innotech\\GrtTestSoft\\Export']

 new_options = ['http://XX.XXX.XX.XXX:6000','http://XX.XXX.XX.XXX:6011','Server=XX.XXX.XX.XXX;Database=GRT;User Id=GRT; Password=GRT12;',r'D:\\temp\\GrtFiles',
                r'D:\\temp\\GrtFiles\\ProcFiles',r'D:\\temp\\GrtFiles\\ProcFiles\\BadProcFiles',r'D:\\temp\\GrtFiles\\ProcFiles\\Trash',r'D:\\temp\\GrtFiles\\RpFiles',
                r'D:\\temp\\TestSoftNew',r'D:\\temp\\TestSoftExport']

 for replace_file in path_file:
   for new_option,old_option in zip(new_options,old_options):

       with open(replace_file, 'r') as f:
         old_data = f.read()
       new_data = old_data.replace(old_option, new_option)
       with open(replace_file, 'w') as f:
         f.write(new_data)
         text = ' конфигурационный файл ' + replace_file + ' изменен,\n опция: ' + old_option + ' >>>> '   + new_option
         get_time(text)


def install_AtSoft():
    clearing_folders_AtSoft()
    unzip_build_AtSoft()
    replace_conf_AtSoft()

def install_soft():
    clearing_folders()
    request_distrib()
    unzip_build()
#    replace_conf()

text = '  Старт'
get_time(text)

install_soft()
request_key()
get_file_stat()

text = '  Завершено'
get_time(text)




