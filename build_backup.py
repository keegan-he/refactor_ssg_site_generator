def main():
    #top_temp = open("templates/top.html").read()
    #content = open("content/index.html").read()
    #bottom_temp = open("templates/bottom.html").read()
    #index_html = top_temp + content + bottom_temp
    #open("docs/index.html", "w+").write(index_html)

    #content = open("content/about.html").read()
    #about = top_temp + content + bottom_temp
    #open("docs/about.html", "w+").write(about)

    #content = open("content/contact.html").read()
    #contact = top_temp + content + bottom_temp
    #open("docs/contact.html", "w+").write(contact)

    #content = open("content/projects.html").read()
    #projects = top_temp + content + bottom_temp
    #open("docs/projects.html", "w+").write(projects)

    #content = open("content/music.html").read()
    #music = top_temp + content + bottom_temp
    #open("docs/music.html", "w+").write(music)

    #content = open("content/photography.html").read()
    #photography = top_temp + content + bottom_temp
    #open("docs/photography.html", "w+").write(photography)
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
        page_title = page["title"]
        openfile = page["filename"]
        output_file = page["output"]
        top_temp = open("templates/top.html").read()
        bottom_temp = open("templates/bottom.html").read()
        content = open(openfile).read()
        master_template = top_temp + content + bottom_temp
        open(output_file, "w+").write(master_template)

print("I ran")

if __name__ =="__main__":
    main()