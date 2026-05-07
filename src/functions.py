from textnode import TextNode,TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            content = node.text
            broken_cont = content.split(delimiter)
            if len(broken_cont)%2 == 0 :
                raise Exception("delimiter not found!")
            even = True
            for new_broken_nodes in broken_cont:
                if even:
                    temp = TextNode(new_broken_nodes,TextType.TEXT)
                else:
                    temp = TextNode(new_broken_nodes,text_type)
                even = not even
                new_nodes.append(temp)
        else:
            new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    return  re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    


def split_nodes_image(old_nodes): 
    ans = []
    for node in old_nodes:
        count = 0
        images = extract_markdown_images(node.text)
        if len(images) > 0:
            content = node.text
            while count < len(images):
                image_alt = images[count][0]
                image_link = images[count][1]   
                sections = content.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    ans.append( TextNode(sections[0], TextType.TEXT) )
                ans.append( TextNode(image_alt,TextType.IMAGE,image_link))
                count += 1
                content = sections[1]
            if content != "":
                ans.append(TextNode(content, TextType.TEXT))

        else:
            ans.append(node)

    return ans

def split_nodes_link(old_nodes):
    ans = []
    for node in old_nodes:
        count = 0
        links = extract_markdown_links(node.text)
        if len(links) > 0:
            content = node.text
            while count < len(links):
                link_to = links[count][0]
                image_link = links[count][1]
                sections = content.split(f"[{link_to}]({image_link})", 1)
                if sections[0] != "":
                    ans.append(TextNode(sections[0], TextType.TEXT))
                ans.append(TextNode(link_to, TextType.LINK, image_link ))
                count+=1
                content = sections[1]
            if content != "":
                ans.append(TextNode(content, TextType.TEXT))

        else:
            ans.append( node )
    return ans

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    new_ans = split_nodes_delimiter(node, "**", TextType.BOLD)
    new_ans = split_nodes_delimiter(new_ans, "_", TextType.ITALIC)
    new_ans = split_nodes_delimiter(new_ans, "`", TextType.CODE)
    new_ans = split_nodes_image(new_ans)
    new_ans = split_nodes_link(new_ans)
    return new_ans


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    ans = []
    for line in lines:
        line = line.strip()
        if line !="":
            ans.append(line)
    return ans