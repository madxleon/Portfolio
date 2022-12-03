#!/bin/sh
export RSYNC_PASSWORD="12345"
DATE=`date '+%Y-%m-%d %H:%M:%S'`	
user=gcti  				#Пользователь под которым выполняется подключение
hosts=(EOSCODGEN05 EOSCODGEN06 EOSCODGEN07 EOSCODGEN08) #Массив хостов где будет выполняться синхронизация
# Список деректорий
tomcat_path='/opt/GCTI/MediaServer/Samba/WEBAnnouncements/ai_message' #Путь до каталога tomcat с роликами
samba='/opt/GCTI/MediaServer/Samba/MCP/' #Путь до шары
path='/opt/GCTI/MediaServer/' #Путь до директори с MCP
folders=(annc announcement inbound_ivr music) #Содержимое MCP
EOSCODGEN05=(GVP_MCP_1 GVP_MCP_3  GVP_MCP_5)
EOSCODGEN06=(GVP_MCP_2 GVP_MCP_4 GVP_MCP_6) #Массив каталогов MCP на хосте
EOSCODGEN07=(GVP_MCP1_CPD GVP_MCP3_CPD GVP_MCP5_CPD) #Массив каталогов MCP на хосте
EOSCODGEN08=(GVP_MCP2_CPD GVP_MCP4_CPD GVP_MCP6_CPD) #Массив каталогов MCP на хосте
del=false  #Включение удаления файлов


if [ "$del" = true ] ; then
    echo Warning!!!  Delete files is enable!
    delete='--delete'
else
    delete=''    
fi

echo Step-1

  for host in "${hosts[0]}"; do
     hoste=$user'@'$host     
      for media_dir in "${EOSCODGEN05[@]}"; do
        for folder in "${folders[@]}"; do
           echo RSync on host: $hoste  media_dir: $media_dir folder: $folder 
           src_folder=$samba$folder
           dst_folder=$media_dir"_"$folder
           dst_path=$path$media_dir"/"$folder
           echo chown/chmod src_folders: $src_folder
           chown gcti:gcti $src_folder -R; chmod 755 $src_folder
           echo chown/chmod dst_folders: $dst_path
           sshpass -p r12xVa_hwe ssh $hoste chown gcti:gcti $dst_path -R| sshpass -p r12xVa_hwe ssh $hoste chmod 755  $dst_path
           echo src folder: $src_folder
           echo dst folder: $dst_folder
           echo "rsync://$hoste:/$dst_folder"
           /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
        done
       src_folder=''  #Выполняется затирка переменных на всякий случай
       dst_folder=''
      done
    done

echo Next: Step-2

  for host in "${hosts[1]}"; do
       hoste=$user'@'$host       
        for media_dir in "${EOSCODGEN06[@]}"; do
          for folder in "${folders[@]}"; do
             echo RSync on host: $hoste  media_dir: $media_dir folder: $folder 
             src_folder=$samba$folder
             dst_folder=$media_dir"_"$folder
             dst_path=$path$media_dir"/"$folder
             echo chown/chmod src_folders: $src_folder
             chown gcti:gcti $src_folder -R; chmod 755 $src_folder
             echo chown/chmod dst_folders: $dst_path
             sshpass -p r12xVa_hwe ssh $hoste chown gcti:gcti $dst_path -R| sshpass -p r12xVa_hwe ssh $hoste chmod 755  $dst_path
             echo src folder: $src_folder
             echo dst folder: $dst_folder
             echo "rsync://$hoste:/$dst_folder"
             /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
          done
         src_folder=''  #Выполняется затирка переменных на всякий случай
         dst_folder=''
        done
      done


echo Next: Step-3
  for host in "${hosts[2]}"; do
       hoste=$user'@'$host       
        for media_dir in "${EOSCODGEN07[@]}"; do
          for folder in "${folders[@]}"; do
             echo RSync on host: $hoste  media_dir: $media_dir folder: $folder 
             src_folder=$samba$folder
             dst_folder=$media_dir"_"$folder
             dst_path=$path$media_dir"/"$folder
             echo chown/chmod src_folders: $src_folder
             chown gcti:gcti $src_folder -R; chmod 755 $src_folder
             echo chown/chmod dst_folders: $dst_path
             sshpass -p r12xVa_hwe ssh $hoste chown gcti:gcti $dst_path -R| sshpass -p r12xVa_hwe ssh $hoste chmod 755  $dst_path
             echo src folder: $src_folder
             echo dst folder: $dst_folder
             echo "rsync://$hoste:/$dst_folder"
             /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
          done
         src_folder=''  #Выполняется затирка переменных на всякий случай
         dst_folder=''
        done
      done

echo Next: Step-4
  for host in "${hosts[3]}"; do
       hoste=$user'@'$host       
        for media_dir in "${EOSCODGEN08[@]}"; do
          for folder in "${folders[@]}"; do
             echo RSync on host: $hoste  media_dir: $media_dir folder: $folder 
             src_folder=$samba$folder
             dst_folder=$media_dir"_"$folder
             dst_path=$path$media_dir"/"$folder
             echo chown/chmod src_folders: $src_folder
             chown gcti:gcti $src_folder -R; chmod 755 $src_folder
             echo chown/chmod dst_folders: $dst_path
             sshpass -p r12xVa_hwe ssh $hoste chown gcti:gcti $dst_path -R| sshpass -p r12xVa_hwe ssh $hoste chmod 755  $dst_path
             echo src folder: $src_folder
             echo dst folder: $dst_folder
             echo "rsync://$hoste:/$dst_folder"
             /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
          done
         src_folder=''  #Выполняется затирка переменных на всякий случай
         dst_folder=''
        done
      done

echo Next: Step-5
  for host in "${hosts[2]}"; do
     hoste=$user'@'$host           
           src_folder=$tomcat_path
           dst_folder='Tomcat_ai_message'
           dst_path='/var/lib/tomcat/webapps/ai_message/'
           echo RSync on host: $hoste  media_dir: $dst_path folder: $dst_folder 
           echo chown/chmod src_folders: $src_folder
           chown gcti:gcti $src_folder -R; chmod 755 $src_folder
           echo chown/chmod dst_folders: $dst_path
           sshpass -p r12xVa_hwe ssh $hoste chown gcti:gcti $dst_path -R| sshpass -p r12xVa_hwe ssh $hoste chmod 755  $dst_path
           echo src folder: $src_folder
           echo dst folder: $dst_folder
           echo "rsync://$hoste:/$dst_folder"
           /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
       
    done

echo Next: Step-6
  for host in "${hosts[3]}"; do
     hoste=$user'@'$host        
           src_folder=$tomcat_path
           dst_folder='Tomcat_ai_message'
           dst_path='/var/lib/tomcat/webapps/ai_message/'
           echo RSync on host: $hoste  media_dir: $dst_path folder: $dst_folder 
           echo src folder: $src_folder
           echo dst folder: $dst_folder
           echo "rsync://$hoste:/$dst_folder"
           /usr/bin/rsync -rltD $src_folder  rsync://$hoste:/$dst_folder $delete
       
    done
