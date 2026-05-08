from copy_function import copy_cont
from page_generator import generate_page,generate_pages_recursive
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print(f"deleting public dir")

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")

    copy_cont(dir_path_static,dir_path_public)
    
    generate_pages_recursive("./content", "template.html", "./public")
    
main()
