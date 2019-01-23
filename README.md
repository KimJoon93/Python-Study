# Python-Study
## Start 2018.01.01 

+ Crawling
  1. What is Crawling?\
  It means leaning down. It seems to be derived from the activity of crawling and gathering information on the Web. Crawling tools include Beautifulsoup, Jsoup, and Selenium.
  2. Crawling illegal or not?\
  There are lot's of info about Web scrapping is illegal or not. But what I think is it will not be a problem unless I take economical benefits.
  3. Selenium
  
  4. Beautiulsoup
    - First Use pipe to install Beautifulsoup
    - Secondly import package to get html or get source from web using request module.
    
    package import\
    <code>from bs4 import BeautifulSoup</code>
    
    Open html\
    <code>with open("example.html") as jn:
    soup = BeautifulSoup(jn, 'html.parser')</code>
