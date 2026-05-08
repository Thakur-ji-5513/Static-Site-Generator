import os
from Block import markdown_to_html_node
from header_extracter import head_extract
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating from ->** {from_path} ** using -> ** {template_path} ** to {dest_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_contents = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    htmlNode = markdown_to_html_node(markdown_contents)
    htmlNode = htmlNode.to_html()

    title = head_extract(markdown_contents)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", htmlNode)
    
    dir_path = os.path.dirname(dest_path)

    os.makedirs(dir_path, exist_ok=True)

    with open(dest_path,"w") as f:
        f.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    data = os.listdir(dir_path_content)
    for dt in data:
        if os.path.isfile(os.path.join(dir_path_content,dt)):
            P = Path( os.path.join(dest_dir_path,dt) )
            P = P.with_suffix(".html")
            generate_page(os.path.join(dir_path_content,dt) , template_path, P)
        else:
            generate_pages_recursive(os.path.join(dir_path_content,dt), template_path, os.path.join(dest_dir_path,dt))
    return