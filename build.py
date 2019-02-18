def main():
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
    return

def readpages(content):
    for page in pages:
        page_title = page["title"]
        openfile = page["filename"]
        output_file = page["output"]
        template = open("templates/base.html").read()
        page_content = open(openfile).read()
        return content

def writepages():
    finished_content_pages = template.replace("{{content}}", page_content)
    open(output_file, "w+").write(finished_content_pages)


print("I ran")

if __name__ == "__main__":
    main()
