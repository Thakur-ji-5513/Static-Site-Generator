import os
from Block import markdown_to_html_node
from header_extracter import head_extract


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