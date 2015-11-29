# arktool
Python Script to Auto-Update ARK Survival Evolved
Using Python 2.7

Currently only runs on Windows. Your best bet for Linux would be ark-server-tools  
https://github.com/FezVrasta/ark-server-tools  

Dependencies:

pywin32: http://sourceforge.net/projects/pywin32/files/  
Make sure you install the correct version.  
Required to clear steamcmd's appcache folder which is read only. If someone knows a better way, that would be awesome.  
Currently, steamcmd (at least on Windows) ignores app_info_update 1 if there's a recent appcache, and the result is  
steamcmd does not always give you the latest buildid for gamefiles. The fix I found was deleting appcache and then  
checking for app info updates.  

RCON Implementation by frostschutz.   
https://github.com/frostschutz/SourceLib/blob/master/SourceRcon.py  
He has examples in his python script.  

Installation and Usage:

Install Python 2.7  
Install the correct version of pywin32  
Download steamcmd and run it. let it update itself.  
Download SourceRcon.py, and store it in steamcmd's folder  
Download ark.py, and store it in steamcmd's folder  

For now, you'll have to change the hard-coded steamcmd and ARK directories.      
Eventually I will code the script to search for both installs and save their paths.  

On line 10, Change the ARK Install path to where you have the gameserver installed.   
On line 14, Change the RCON IP, Port, Password to match your configuration.   
On line 32, Change the ARK Install path to where you have the gameserver installed.   
On line 36, Change the Steamcmd Install path to where you have steamcmd installed.   
On line 68, Change the Steamcmd arguments so that ARK is updating to YOUR gameserver install location.   

These will eventually be detected by the script. But for now they are hard-coded to mirror my setup.
