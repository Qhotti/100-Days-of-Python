import time
import requests
from bs4 import BeautifulSoup
import lxml

# with open('website.html','r', encoding='utf-8') as file:
    # contents = file.read()
    
# soup= BeautifulSoup(contents,'html.parser')
# print(soup.title)
# print(soup.title.string) # get string from title
#print(soup.prettify()) #makes html look nice
# print(soup.h3)

# anchor_tag = soup.find_all(name='a')

# for tag in anchor_tag:
    # print(tag.getText()) #get all words in anchor tag
    # print(tag.get('href')) #get all links in anchor tag

# heading = soup.find(name='h1',id='name') #find specific id
# print(heading)

# section_heading = soup.find(name='h3',class_='heading') #find specific class
# print(section_heading.getText())


# company_url = soup.select_one(selector='p a')  #get even more specific item ex.(selector = #name)(selector = .heading)
# print(company_url)

# company_url = soup.select(selector='p a')  #select all in a tag
# print(company_url)
# response = requests.get('https://news.ycombinator.com/news')
# webpage = response.text

# soup = BeautifulSoup(webpage, 'html.parser')

# article = soup.find_all(name = 'a',class_=None)
# article_texts = []
# article_links = []
# for a in article:
#     text = a.getText()
#     article_texts.append(text)
#     link = a.get('href')
#     article_links.append(link)

# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

# largest_number = max(article_upvote)
# largest_index = article_upvote.index(largest_number)

# most_upvoted_article_title = article_texts[largest_index]
# most_upvoted_article_link = article_links[largest_index]


# print(article_texts)
# print(article_links)
# print(article_upvote)


response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
webpage = response.text
soup = BeautifulSoup(webpage, 'lxml')
movies = soup.find_all(name='h3', class_='title')

movie_titles =[m.getText() for m in movies]


with open('movies.txt','w', encoding='utf-8') as file:
    for title in movie_titles[::-1]:
        file.write(f'{title}\n')



