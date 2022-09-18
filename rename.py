#C115-Project


import os
import random 


nm = input('Enter file name >> ')
ext = input('Enter extension (eg-- .txt)>> ')

source = nm + ext
dest = "newfile.txt"
name,extension = os.path.splitext(dest)
print(name + '/'+ ext)
rename = name + str(random.randint(0,999)) + extension

if(os.path.exists(rename)):
  print('This path already exists')
else:
  os.rename(source,rename)
  print('Successfully moved files')
  

