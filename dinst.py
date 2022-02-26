import platform
if platform.system() != "Windows":
  print("You don't seem to be running this on a Windows machine!")
  input("Press Enter to Exit... ")
  exit()
import os

try:
  import requests
except ImportError:
  os.system("python -m pip install requests")
              ## Main application ##
print("Welcome to the MS-DOS installer for Windows!")
print("Attempting to get latest GitHub release...")
link = "https://github.com/microsoft/MS-DOS/archive/refs/heads/master.zip"
file_name = dir + "/" + asset
with open(file_name, "wb") as f:
             response = requests.get(link, stream=True)
             total_length = response.headers.get('content-length')
          
             if total_length is None: # no content length header
               f.write(response.content)
else:
  dir = os.path.realpath(__file__)
  dl = 0
  total_length = int(total_length)
  for data in response.iter_content(chunk_size=4096):
        dl += len(data)
        f.write(data)
        done = int(50 * dl / total_length)
        per = int(done * 2)
        sys.stdout.write(f"\rDownloading MS-DOS archive from github... %s[%s]" % ('#' * done, ' ' * (50-done)) + f" | {per}% Done" )    
        sys.stdout.flush()
  print("Try compiling one of the files in one of the 'v2.0' or 'v1.25' folders.")
  import time
  time.sleep(2)
