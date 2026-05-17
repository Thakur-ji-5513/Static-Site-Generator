from copy_function import copy_cont
from page_generator import generate_page,generate_pages_recursive
import os
import shutil
import sys


dir_path_static = "./static"
dir_path_docs = "./docs"

def main():
    if len(sys.argv) > 1:
        basePath = sys.argv[1]
    else:
        basePath = "/"

    print(f"deleting public dir")

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    print("Copying static files to public directory...")

    copy_cont(dir_path_static,dir_path_docs)
    
    generate_pages_recursive("./content", "template.html", dir_path_docs, basePath)
    
main()
