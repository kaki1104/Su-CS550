#I have neither given nor received unauthorized aid. Jiaqi Su
#Sources: https://doc.scrapy.org/en/latest/intro/overview.html#intro-overview
#https://doc.scrapy.org/en/latest/intro/tutorial.html
#http://quotes.toscrape.com/
#https://www.tutorialspoint.com/scrapy/index.htmimport scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    #we are naming this spider "author"

    start_urls = ['http://quotes.toscrape.com/']
    #the spider will start scraping at the above web url

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)
            # follow links to author pages

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)
            # follow pagination links

    def parse_author(self, response): #definition of specific elements to extract for each author
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
