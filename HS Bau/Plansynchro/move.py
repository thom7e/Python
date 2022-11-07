import os
import shutil
import datetime
import schedule
import time





def copyfiles(root_src_dir,root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
            print(f"Neuer Ordner {dst_dir} erstellt")
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)

            if os.path.exists(dst_file):
                # in case of the src and dst are the same file

                if os.path.getmtime(src_file) >= os.path.getmtime(dst_file):
                   shutil.copy(src_file,dst_dir)
                   #print(time.ctime(os.path.getmtime(src_file)),time.ctime(os.path.getmtime(dst_file)))
                   print(f"copied {src_file}, weil {round(os.path.getmtime(src_file)/100000000)} ist jünger als {round(os.path.getctime(dst_file)/100000000)}")

                else:
                    continue






            else:
                shutil.copy(src_file,dst_dir)
                print(f"neue Datei {src_file} erstellt")

        #if not os.path.exists(dirs):
         #   print(f"ist da: {dirs}")
            #if not dirs_ in os.listdir(src_dir):

                #os.rmdir(dst_dir)
                #print(f"altes Verzeichnis {dst_dir} gelöscht")

def delete_old(root_src_dir,root_dst_dir):

    try:
        for dst_dir, dirs, files in os.walk(root_dst_dir):
            src_dir = dst_dir.replace(root_dst_dir, root_src_dir, 1)
            #print(f"Planunterlagen {dst_dir}")
            #print(f"Company: {src_dir}")

            if os.path.exists(src_dir):
                pass
            else:
                shutil.rmtree(dst_dir)
                shutil.rmtree(root_dst_dir)
                print(f"{dst_dir} has been removed")


# Deleting Files
            for file_ in files:
                dst_file = os.path.join(dst_dir, file_)
                src_file = os.path.join(src_dir, file_)
                #print(f"Planunterlagen: {dst_file}")
                #print(f"Company {src_file}")
                if os.path.exists(src_file):
                    #print(src_file)
                    pass
                else:

                    os.remove(dst_file)
                    print(f"{dst_file} File is old and got deleted")
    except FileNotFoundError:
        print("File not Found error skipped")
        pass










#Windows
#source = "C:/Users/thoma/Documents/Testdatei/BV 20"
#destination = f"C:/Users/thoma/Documents/Testdatei/Planunterlagen/"

def planunterlage(source,destination):
    #for jahr in range(21,23):
    #    sparten = ["01_Hochbau","02_Tiefbau","03_Schlüsselfertig","04_Energieberatung"]
    #    for sparte in sparten:
    #        sourcepath = f"{source}{sparte}/20{jahr}"
    if os.path.exists(source):
        planordner = os.listdir(source)
        for ordner in planordner:
            if os.path.isdir(f"{source}/{ordner}") == True:
                if not os.path.exists(f"{destination}/{ordner}"):
                    os.mkdir(f"{destination}/{ordner}")
                    copyfiles(f"{source}/{ordner}/3_Planunterlagen",f"{destination}{ordner}")
                    delete_old(f"{destination}{ordner}",f"{source}/{ordner}/3_Planunterlagen")
                else:
                    print(f"kopiere von {ordner}/3_Planunterlagen nach {destination}/{ordner}")
                    copyfiles(f"{source}/{ordner}/3_Planunterlagen",f"{destination}{ordner}")
                    delete_old(f"{source}/{ordner}/3_Planunterlagen",f"{destination}{ordner}")

                    #datumsource = os.path.getmtime(f"{sourcepath}/{ordner}")
                    #ds = datetime.datetime.fromtimestamp(datumsource)
                    #print(ds.strftime("'%Y\\%m\\%d'"))
                    #datumdest = os.path.getmtime(f"{destination}/{ordner}")
                    #dd = datetime.datetime.fromtimestamp(datumdest)
                    #print(dd.strftime("'%Y\\%m\\%d'"))
                    #if ds <= dd:
                    #    print("copied, ist älter")
                    #    copyfiles(f"{source}{jahr}/{ordner}/3_Planunterlagen",f"{destination}{ordner}")
                    #else:
                    #    print("same date")
                #print(f"copied {ordner}")
        print("copy ready")
        with open('planunterlagen.log','a') as logfile:
            logfile.write(f'copied on {datetime.datetime.now()} \n')

        print(datetime.datetime.now())
source = f"E:\\Bauteil A"
destination = f"F:\\FEsti"
planunterlage(source,destination)
#schedule.every(5).minutes.do(lambda: planunterlage(source,destination))
#planunterlage(source,destination)

#while True:
#    schedule.run_pending()
#    time.sleep(1)