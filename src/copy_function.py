import os
import shutil

def copy_cont(src,dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
        
    for filename in os.listdir(src):
        new_dest = os.path.join(dest,filename)
        new_src = os.path.join(src,filename)
        print(f" * {new_src} -> {new_dest}")
        if os.path.isfile(new_src):
            shutil.copy(new_src,new_dest)
        else:
            copy_cont(new_src,new_dest)