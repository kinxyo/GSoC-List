# About
Find organizations that have been participating in gsoc for recent years.

# How to use
  1. ## Clone the repository
    git clone https://github.com/kinxyo/GSoC-List.git
  2. ## Install the requirements
    pip install -r requirements.txt
  3. ## Run the files
     Running `python scraper.py` in terminal will scrape relevant data and pack it into .json file for each year.<br>
    <br>
     Running `python records.py` in terminal will find common organizations amongst that data then create a list for it.<br>
    <br>
  5. ## Done
     In the root directory, you'll find ***output.xlsx*** which contains the final list. You can then adjust the column-width and format square brackets from the list to make it look cleaner.<br>
     Here an example:-<br><br>
     ![image](https://github.com/kinxyo/GSoC-List/assets/90744941/74eaf6db-d773-45bc-b6a8-c658f817723a)


# Ending Note
Before making this, I tried various other solutions for scraping. Weirdly enough, they all seemed to pretend as if the content found on the GSoC's *browse organizations* page is static, so none of them actually worked. It's impossible to scrape dynamic content by only using BeautifulSoup4, hence **Selenium** was used in this project. The scraping takes a lot of time (~ 25 mins) as my priority was get the job done. I might redo this project in Rust someday; that is when I'd focus on runtime, however any change for more optimized code is welcomed.
