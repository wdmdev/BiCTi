# BiCTi
Project on scraping news information from Danish public media on the war in Ukraine.

The name BiCTi was chosen for the project because it means news in Ukrainian (according to Google Translate).

## Reason for the project
I have created this project because I'm interested in finding out how the war in Ukraine is portraited in the Danish media. To make the project possible I particularly focus on **public** Danish media sources.

## Scraping
The `scraping` folder contains a `scrapy` project where the available scrapers can be found in the `spiders` folder.
<br>
The project can be used with [Scrapy](https://scrapy.org/) to crawl pages by using the command: 
```
scrapy crawl <name of spider>
```
and the results will be saved in the `data` folder in the `scraping` project folder.
<br><br>
An example could be:
```
scrapy crawl dr
```
Which will generate a `.json` file with the scraped data in the `data` folder in `scraping`.