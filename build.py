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
<<<<<<< HEAD

=======
>>>>>>> c611972dd69d368b9236d4642cfe4ebaafa3e0a0
    for page in pages:
        page_title = page["title"]
        openfile = page["filename"]
        output_file = page["output"]
        template = open("templates/base.html").read()
        page_content = open(openfile).read()
        finished_content_pages = template.replace("{{content}}", page_content)
        open(output_file, "w+").write(finished_content_pages)

<<<<<<< HEAD

print("I ran")

=======
# test script ran
print("I ran")

# Create new function to add page to dict.
# def add_page():


>>>>>>> c611972dd69d368b9236d4642cfe4ebaafa3e0a0
if __name__ == "__main__":
    main()
