from bs4 import BeautifulSoup


with open("page_content.html", 'r', encoding='utf-8') as file:
    content = file.read()


soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())