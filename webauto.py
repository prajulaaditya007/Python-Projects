import webbrowser as wb


def webauto():
    chrome_path = ' C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "youtube.com",
        "instagram.com",
        "twitter.com",
        "github.com"
    )
    for url in URLS:
        print("opening : " + url)
        wb.get(chrome_path).open(url)


webauto()
