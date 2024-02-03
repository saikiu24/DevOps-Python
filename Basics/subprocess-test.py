# To send commands, stdin, stdout
import subprocess

# Sending 'ls' command in Linux
subprocess.run('ls', shell=True)
p1 = subprocess.run(['ls', '-la'])
print(p1)

# Capturing stdout in Bytes (Does NOT show spaced contents)
p2 = subprocess.run(['ls', '-la'], capture_output=True)
print(p2.stdout)

# Capturing stdout in TEXT
p3 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(p3.stdout)

# OR
# Capturing stdout in TEXT
p4 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(p4.stdout)

# Redirecting stdout to a file
with open('output.txt', 'w') as f:
# Redirecting to our file 'f'
    p5 = subprocess.run(['ls', '-la'], stdout=f, text=True)

# Listing a non-existed directory in Linux
#p6 = subprocess.run(['ls', '-la', '/notExist'], capture_output=True, text=True, check=True)
#print(p6.returncode)
# This will not work => Python does not necessarily return error code
#print(p6.stderr)

#if p2.returncode != 0 
#...

# Redirecting stderr to /dev/null
#p7 = subprocess.run(['ls', '-la', '/notExist'], stderr=subprocess.DEVNULL)
#print(p7.stderr)

# cat file.txt | grep content
#p8 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True, stderr=subprocess.DEVNULL)
#print(p8.stdout)

# Passing p4.stdout => p5
#p9 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p4.stdout)

# OR use shell
# p10_touch = subprocess.run('touch test.txt', capture_output=True, text=True, shell=True)
# p10_touch.wait()
# p10 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)
# print(p10.stdout)

# Sending 'dir' command in Windows
#subprocess.run('dir')
