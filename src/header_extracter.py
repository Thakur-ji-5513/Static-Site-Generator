

def head_extract(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2: ]
    raise Exception("No h1 found!") 

# def main():
#     txt = "# Tolkien Fan Club \n\n ![JRR Tolkien sitting](/images/tolkien.png)\nHere's the deal, **I like Tolkien**."
#     print(head_extract(txt))

# main()