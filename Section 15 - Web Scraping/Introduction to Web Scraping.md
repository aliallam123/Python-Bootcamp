# Web Scraping – Intro

This chapter's about web scraping using Python. Basic idea is grabbing data from websites using code. The site gives back HTML, and we use Python to pull out the bits we want.

## Tools I'm using

- `requests` – to get the webpage
- `BeautifulSoup` – to parse the HTML

## The main steps

1. Get the page using `requests`
2. Use `BeautifulSoup` to parse the HTML
3. Find the elements you're after (using tags, classes etc)
4. Extract the data

**Main idea is that:**

- **HTML contains the information**
- **CSS contains the styling**
- **We can use HTML and CSS tags to locate specific information on a page**

## Practice site

The first few examples are from [http://quotes.toscrape.com](http://quotes.toscrape.com) – it’s a practice site made for scraping.

## What I'll do in this chapter

I'll go through exercises like grabbing a title, class, image etc and some book examples too. Just practising different things step by step.

