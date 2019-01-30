#I have neither given nor received unauthorized aid. Jiaqi Su
#Sources: https://doc.scrapy.org/en/latest/intro/overview.html#intro-overview
#https://doc.scrapy.org/en/latest/intro/tutorial.html
#http://quotes.toscrape.com/
#https://www.tutorialspoint.com/scrapy/index.htm

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    #You call the spider by this name in the Terminal when running.

    allowed_domains = ["quotes.toscrape.com"] 
    #the domain(s) that a spider could crawl

    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
    #the url that a spider could start with.

    # if you want to limit the extracted quotes to the ones with a specific tag, you could replace the allowed_domains and start_urls with the following definition:
    """def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)"""
    #The above definition will direct you specifically to the page that shows you all the quotes with a specific tag.

def parse(self, response): #defines what types of information to scrape
	for quote in response.css('div.quote'): #for each "quote" contained in the html tag "div.quote"...
		yield {
		'text': quote.css('span.text::text').extract_first(), 
        #returns the text of the quote itself
		'author': quote.css('small.author::text').extract_first(), 
        #returns the author's name
		'tags': quote.css('div.tags a.tag::text').extract(), 
        #returns the tags attached to the quote
		}

	next_page = response.css('li.next a::attr(href)').extract_first() 
    #defines next_page as the link embedded under the "next" button in the end of the page
        if next_page is not None: 
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            #as long as there is a next page, the spider will automatically hit on that link and recursively scrape data.