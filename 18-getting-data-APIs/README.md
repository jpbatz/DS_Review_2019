# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Getting Data and APIs
Unit 4 : DS Applications | Lesson 1 : Getting Data and APIs

---

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Part 1: APIs | [Here](./APIs/intro-to-web-services-apis.ipynb) |
| | Part 2: Webscraping (Optional supplement, time permitting) | [Here](./WebScraping/webscraping-in-class.ipynb) |
| Practice | Case Study Twitter API and NLP | [Here](./practice/case-study-twitter-api-nlp.ipynb) |
|          | Practice Using APIs            | [Here](./practice/practice-using-apis-lab.ipynb)    |
|          | Webscraping with Selenium      | [Here](./practice/webscraping-selenium.ipynb)       |
| Source Materials | Original files used to create the API portion of the lesson | [Here](./APIs/assets/slides/) |
| Solution  | Solution code for blanked out lesson samples - Webscraping Portion | [Here](./WebScraping/solution-code/webscraping-in-class-solutions.ipynb) |

---

## Learning Objectives

#### Part 1: Intro to Web Services & APIs
_After this lesson, you will be able to:_
- Identify relevant HTTP Verbs & their uses.
- Describe Application Programming Interfaces (APIs) and know how to make calls and consume API data.
- Access public APIs and get information back.
- Read and write data in JSON format.
- Use the `requests` library.

#### Part 2: Webscraping in Class (Optional)
_After this lesson, you will be able to:_
- Revisit how to locate elements on a webpage
- Aquire unstructure data from the internet using Beautiful soup.
- Discuss limitations associated with simple requests and urllib libraries
- Introduce Selenium as a solution, and implement a scraper using selenium (Instructor Demo only)

---

## Lesson Outline

#### Part 1
> TOTAL (170 min)

- Introduction to APIs
- What is an API? (10 min)
- Famous APIs (5 min)
    - Facebook
    - Yelp
    - Echonest
- Web APIs (5 min)
- Making API calls (5 min)
- HTTP (10 min)
- Web applications (5 min)
- Demo: HTTP (10 min)
- Independent practice: HTTP (10 min)
- HTTP Request (10 min)
    - HTTP Request methods
    - HTTP Request structure
- HTTP Response (5 min)
    - Response types overview
- JSON (10 min)
- Independent practice: validating JSON (10 min)
- Guided practice: pulling data from APIs (35 min)
    - Example 1: Star Wars (15 min)
    - Submit queries to the API (10 min)
    - Example 2: Google Geocode (10 min)
- OAuth (15 min)
- Independent practice: python APIs (30 min)
- Closing questions


#### Part 2
> TOTAL (170 min)

- Introduction (10 min)
- Building a web scraper (5 min)
- Retrieving data from the HTML page (65 min)
    - Retrieving the restaurant names (20 min)
    - Challenge: Retrieving the restaurant locations (15 min)
    - Retrieving the restaurant prices (10 min)
    - Retrieving the restaurant number of bookings (20 min)
- Introducting Selenium (90 min)
    - Running JavaScript before scraping (15 min)
    - Using regex to only get digits (20 min)
    - Challenge: Use Pandas to create a DataFrame of bookings (40 min)
    - Auto-typing using Selenium (15 min)
- Summary

---

## Student Requirements

Before this lesson(s), students should already be able to:
- Interpret and use Python dictionaries
- Build Pandas DataFrames from dictionaries
- Perform simple data manipulation on Pandas objects\
- Build `for` and `while` loops in Python
- Use `pip install` for package management

---

### Environment Requirements

- Have Beautiful Soup installed.
> ```pip install bs4```


**If including Selenium demo:**
- Have Selenium installed, using one of the following:
> Anaconda: ```conda install -c conda-forge selenium```
> pip: ```pip install selenium```

- Have [FireFox browser](https://www.mozilla.org/en-US/firefox/new/?utm_source=google&utm_medium=cpc&utm_campaign=Firefox-Brand-US-GGL-Exact&utm_term=firefox&utm_content=A144_A203_A006336&gclid=Cj0KEQjwnPLKBRC-j7nt1b7OlZwBEiQAv8lMLJUyReT6cPzSYdmEA6uD3YDoieuuuusddgAU7XH6smEaAoje8P8HAQ&gclsrc=aw.ds) installed.

- Have GeckoDriver installed:
> ```brew install geckodriver```

---

## Additional Resources

For more information on this topic, check out the following resources:

- Find elements: [Selenium docs](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements)
- Using Selenium to enter website information: [demo](http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/)
- Python regex tester: [here](http://pythex.org/)
- Setup Firefox profile: [here](http://stackoverflow.com/questions/9907492/how-to-get-firefox-working-with-selenium-webdriver-on-mac-osx)
