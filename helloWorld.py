import os
import subprocess

# Call PowerShell and set execution policy to unrestricted
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "set-executionpolicy unrestricted -force"])

# Run PowerShell command from Python script
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "get-command"])

# Run PowerShell script from Python script
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "C:\\users\\pmccaul\\Desktop\\PowerShell_Scripts\\testScript.ps1"])

# Get all computers in AD and assign to a variable $adComputers
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "$adComputers = (get-adcomputer -filter * | sort-object | select Name)"])

#os.system('dir')

print("Hello World!")