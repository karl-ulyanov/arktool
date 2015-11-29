import subprocess
import time
import SourceRcon
import win32api
import win32con
import shutil


def startServer():
    subprocess.call(["C:/ARK/ShooterGame/Binaries/Win64/ShooterGameServer.exe", "TheIsland?MaxPlayers=70?RCONEnabled=true?RCONPort=32330?QueryPort=27016?Port=7777?GameModIds=510590313,515147216,508404828,534838287,506506101,516096294?listen -server -log"])


def warn():
    server = SourceRcon.SourceRcon('127.0.0.1', 32330, 'RCONPASS')
    server.rcon('broadcast Server Auto-Updating in 15 minutes!')
    time.sleep(300)
    server.rcon('broadcast Server Auto-Updating in 10 minutes!')
    time.sleep(300)
    server.rcon('broadcast Server Auto-Updating in 5 minutes! Saving World!')
    server.rcon('saveworld')
    time.sleep(300)
    server.rcon('broadcast Server Auto-Updating in 1 minutes! Saving World')
    server.rcon('saveworld')
    time.sleep(120)
    server.rcon('doexit')
    time.sleep(90)
    doUpdate()


def checkUpdate():
    print "Checking for Ark Updates..."
    for line in open("C:/ARK/steamapps/appmanifest_376030.acf"):
        if "buildid" in line:
            global current
            current = line.split("\"")[-2]
            scpath = "C:/Users/Administrator/Desktop/steamcmd/appcache"
            win32api.SetFileAttributes(scpath, win32con.FILE_ATTRIBUTE_NORMAL)
            shutil.rmtree(scpath, ignore_errors=False, onerror=None)
            newv = subprocess.check_output(
                ["steamcmd.exe", "+login anonymous", "+app_info_update 1", "+app_info_print 376030", "+quit"])
            if 'buildid' in newv:
                global version
                version = newv.split("\"")[-18]
                if int(current) < int(version):
                    print "Update Found! Warning Users on Server and Updating ARK!"
                    warn()


# Code from Stackoverflow.com to check process. Unsure of original author.
def processExists(processname):
    tlcall = 'TASKLIST', '/FI', 'imagename eq %s' % processname
    # shell=True hides the shell window, stdout to PIPE enables
    # communicate() to get the tasklist command result
    tlproc = subprocess.Popen(tlcall, shell=True, stdout=subprocess.PIPE)
    # trimming it to the actual lines with information
    tlout = tlproc.communicate()[0].strip().split('\r\n')
    # if TASKLIST returns single line without processname: it's not running
    if len(tlout) > 1 and processname in tlout[-1]:
        print('process "%s" is running!' % processname)
        return True
    else:
        print(tlout[0])
        print('process "%s" is NOT running!' % processname)
        return False


def doUpdate():
    subprocess.call(["steamcmd.exe", "+login anonymous", "+force_install_dir C:\ARK", "+app_update 376030", "+quit"])
    time.sleep(300)
    upd = processExists('steamcmd.exe')
    if upd == "False":
        startServer()


count = 0
while count < 1:
    checkUpdate()
    time.sleep(300)
    proc = processExists('ShooterGameServer.exe')
    scd = processExists('steamcmd.exe')
    if scd == "True":
        time.sleep(30)
    elif proc == "True":
        time.sleep(300)
    if (proc == "False" and scd == "False"):
        startServer()
        time.sleep(300)
