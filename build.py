# def main():
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

for page in pages:
        #page_title = page["title"]
        openfile = page["filename"]
        output_file = page["output"]
        #template = open("templates/base.html").read()
        page_content = open(openfile).read()
        #finished_content_pages = template.replace("{{content}}", page_content)
        #open(output_file, "w+").write(finished_content_pages)


def apply_template(content):
    """ read template file and combine with content  """
    template = open("templates/base.html").read()  # Read in template
    finished_content_pages = template.replace("{{content}}", page_content)  # string replacing
    open(output_file, "w+").write(finished_content_pages)


def write():
    content = open("docs/index.html")
    resulting_html_for_index = apply_template(content)


def main():

    apply_template(content)
    write()


if __name__ == "__main__":
    main()
