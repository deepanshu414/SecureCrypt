import pyAesCrypt
import os
import datetime
import pandas as pd
from openpyxl import Workbook
from pathlib import Path
try:
    count_e_d=0
    count_exist=0
    c_e_d=0
    check_e_d=0
    c=0
    def count_files_in_folder(folder_path):
        global file_count,folder_count
        file_count = 0
        folder_count = 0
        for root, dirs, files in os.walk(folder_path):
            folder_count += len(dirs)
            file_count += len(files)

        return folder_count, file_count
    def info(new_row):
        try:
            home=Path.home()
            file_path="SecureCrypt_report.xlsx"
            k=os.path.join((home),file_path)
            if(os.path.exists(k)):
                pass
            else:
                workbook=Workbook()
                worksheet=workbook.active
                worksheet.title="Sheet1"
                workbook.save(filename=k)
            data=pd.read_excel(k)
            df = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
            df.to_excel(k, index=False)
        except FileNotFoundError as e:
            print(e)
    def store(a,k,date):
        global count_e_d,c_e_d
        try:
            z=os.listdir(a)
            if(file_count==count_e_d or file_count==c_e_d  or file_count==count_e_d+count_exist or file_count==c_e_d+count_exist):
                complete="Completed"
                if(check_e_d==1 or count_e_d>0):
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"encode","date":date,"complete":complete,"c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
                    count_e_d=0
                elif(check_e_d==2 or c_e_d>0):
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"decode","date":date,"complete":complete,"c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
                    c_e_d=0
                else:
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"-","date":date,"complete":"-","c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
            else:
                if(check_e_d==1 or count_e_d>0):
                    global c
                    c=file_count-count_e_d 
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"encrypt","date":date,"complete":str(c) + " left","c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
                    count_e_d=0
                elif(check_e_d==2 or c_e_d>0):
                    c=file_count-c_e_d
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"decrypt","date":date,"complete":str(c) + " left","c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
                    c_e_d=0
                else:
                    record={"password":str(k),"f_name":a,"c_encrypt":str(count_e_d),"E or D":"-","date":date,"complete":"-","c_decrypt":str(c_e_d),"exist":str(count_exist),"Total folder":folder_count,"Total file":file_count}
            info(record)
        except Exception as e:
            print(e)
    def onetimeshow(a,k,date):
        try:
            record={"password":str(k),"f_name":a,"c_encrypt":"-","E or D":"-","date":date,"complete":"-","c_decrypt":"-","exist":"-","Total folder":folder_count,"Total file":file_count}
            info(record)
        except Exception as e:
            print(e)
    def encrypt(current_password,path__name,file_password):
        path_name=r'{}'.format(path__name)
        folder_count, file_count = count_files_in_folder(path_name)
        date=datetime.datetime.now()
        onetimeshow(path_name,file_password,date)
        current=date.minute
        global check_e_d
        check_e_d +=1
        def encrypt_file(file_path, password):
            bufferSize = 64 * 1024  
            encrypted_file_path = file_path + '.aes'
            try:
                with open(file_path, 'rb') as fIn:
                    with open(encrypted_file_path, 'wb') as fOut:
                        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                os.remove(file_path)  
                print(f"File '{file_path}' encrypted successfully.")
                global count_e_d
                count_e_d+=1
            except Exception as e:
                print(f"An error occurred while encrypting '{file_path}': {e}")
        def encrypt_folder(folder_path):
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith('.aes'): 
                        try:
                            global count_exist
                            count_exist+=1
                            print("already encrypted")
                            continue
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            file_path = os.path.join(root, file)
                            password_for_file = str(file_password)
                            encrypt_file(file_path, password_for_file)
                        except Exception as e:
                            print(e)
        if(int(current_password)==int(current)):
            if(os.path.exists(path_name) and os.listdir(path_name)!=0):
                encrypt_folder(path_name)
                store(path_name,file_password,date)
            elif(os.path.exists(path_name) and os.listdir(path_name)==0):
                print("This folder is empty")
            else:
                print("folder not found")
        else:
            print("Wrong password")
    def decrypt(current_password,path__name,file_password):
        path_name=r'{}'.format(path__name)
        folder_count, file_count = count_files_in_folder(path_name)
        date=datetime.datetime.now()
        onetimeshow(path_name,file_password,date)
        current=date.minute
        global check_e_d
        check_e_d +=2
        def decrypt_file(encrypted_file_path, password):
            bufferSize = 64 * 1024  
            try:
                file_path = encrypted_file_path[:-4] 
                with open(encrypted_file_path, 'rb') as fIn:
                    with open(file_path, 'wb') as fOut:
                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize)
                os.remove(encrypted_file_path) 
                print(f"File '{file_path}' decrypted successfully.")
                global c_e_d
                c_e_d+=1
            except Exception as e:
                print(f"An error occurred while decrypting '{encrypted_file_path}': {e}")
                if file_path.endswith('.aes'): 
                    pass
                else:
                    os.remove(encrypted_file_path[:-4]) 
        def decrypt_folder(folder_path):
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith('.aes'):  
                        try:
                            file_path = os.path.join(root, file)
                            password=str(file_password)
                            decrypt_file(file_path, password)
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            print("already decrypted")
                            global count_exist
                            count_exist+=1
                            continue
                        except Exception as e:
                            print(e)
        if(int(current_password)==int(current)):
            if(os.path.exists(path_name) and os.listdir(path_name)!=0):
                decrypt_folder(path_name)
                store(path_name,file_password,date)
            elif(os.path.exists(path_name) and os.listdir(path_name)==0):
                print("This folder is empty")
            else:
                print("folder not found")
        else:
            print("Wrong password")
except Exception as e:
    print(e)