from webdav3.client import Client
import datetime
import os
options = {
 'webdav_hostname': "https://cloud.hsbau-muehlacker.de:8443/remote.php/dav/files/tku/",
 'webdav_login':    "tku",
 'webdav_password': "1lKaHuber#"
}
client = Client(options)

path = "Company/1_Bauvorhaben/01_Hochbau/2022/21H042_Schützingen_EFH Kurfiß"

path_info = client.info(path)
path_date = [path_info[x] for x in path_info if x == "modified"][0]
today = datetime.datetime.now()
path_date =path_date.split("GMT")[0]
path_date_conv =datetime.datetime.strptime(path_date, "%a, %d %b %Y %H:%M:%S ")
print(today-path_date_conv)
path_to_copy = "C:\\Users\\thoma\\OneDrive\\Privat\\Immobilien\\Ziegeläcker\\09 Gewerke\\01 Rohbau Erdbau AA"
print(os.stat(path_to_copy))
print(type(os.stat(path_to_copy)))
#if today < path_date_conv:
# client.download_sync(remote_path=path, local_path="C:\\Users\\thoma\\OneDrive\\Privat\\Immobilien\\Ziegeläcker\\09 Gewerke\\01 Rohbau Erdbau AA")