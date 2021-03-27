import subprocess

#subprocess.run(['ls', '-la'])

p1 = subprocess.run(['ls','-la'])

print(p1.stdout)


