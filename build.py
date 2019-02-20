
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact",
    },
    {
        "filename": "content/music.html",
        "output": "docs/music.html",
        "title": "Music",
    },
    {
        "filename": "content/photography.html",
        "output": "docs/photography.html",
        "title": "Photography",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
]
def read_content():
    for page in pages:
            openfile = page["filename"]
            page_content = open(openfile).read()
            return page_content
            #page_title = page["title"]
            #output_file = page["output"]
            #template = open("templates/base.html").read()
            #finished_content_pages = template.replace("{{content}}", page_content)
            #open(output_file, "w+").write(finished_content_pages)

def apply_template():
    """ read template file and combine with content  """
    template = open("templates/base.html").read()  # Read in template
    finished_content_pages = template.replace("{{content}}", read_content())  # string replacing
    return finished_content_pages

def write():
    for page in pages:
        output_file = page["output"]
        open(output_file, "w+").write(apply_template())


def main():
    #read_content()
    #apply_template()
    write()


if __name__ == "__main__":
    main()
