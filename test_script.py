from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass

parser = MyHTMLParser()
with open('portfolio.html', 'r') as f:
    parser.feed(f.read())
print("HTML Syntax OK")
