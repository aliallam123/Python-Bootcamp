Web Scraping – Intro
This chapter's about web scraping using Python. Basic idea is grabbing data from websites using code. The site gives back HTML, and we use Python to pull out the bits we want.

In this section I’m using:

requests – to get the webpage

BeautifulSoup – to parse the HTML

The main steps are:

Get the page using requests

Use BeautifulSoup to parse the HTML

Find the elements you're after (using tags, classes etc)

Extract the data

The first few examples are from http://quotes.toscrape.com – it’s a practice site made for scraping.

Example: Getting quotes and authors
