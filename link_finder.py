from html.parser import HTMLParser
from urllib import parse



file = open('testfile.txt', 'r') 
string = file.readline()
list1 = string.split(';')

string1 = list1[0]
string2 = list1[1]

file.close()

specific_string = str(string2)

specifics = specific_string.split(',')

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        ispresent = True
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    for field in specifics:
                        if field not in url:
                            ispresent = False
                            break
                    if ispresent == True:
                        self.links.add(url)
                            

    def page_links(self):
        return self.links

    def error(self, message):
        pass
