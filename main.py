import subprocess
import threading
import shlex
from pyrosm import get_data



def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(f"Command {command}: \n stdout: {stdout.decode()}")
    else:
        print(f"Command {command}: \n stderr: {stderr.decode()}")



def uruchom(nazwa_miasta):
    
    # downloading osm.pbf data
    fp = get_data(nazwa_miasta, directory="my_data", update=True)

    # deleting graph-cache folder for future running with other place
    subprocess.run(['rmdir', '/s', 'graph-cache'], shell=True)


    #running graphhopper and fastapi simultaneously
    command_line1 = f'java -D"dw.graphhopper.datareader.file=my_data/{nazwa_miasta}.osm.pbf" -jar graphhopper-web-9.1.jar server config.yml'
    command_line2 = f'uvicorn fastapp:app --reload'
    args1 = shlex.split(command_line1)
    args2 = shlex.split(command_line2)
    thread1 = threading.Thread(target=run_command, args=(command_line1,))
    thread2 = threading.Thread(target=run_command, args=(command_line2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


# executing 
uruchom("Warsaw")
