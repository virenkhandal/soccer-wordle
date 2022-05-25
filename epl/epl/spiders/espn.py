import scrapy


class EspnSpider(scrapy.Spider):
    name = 'espn'
    allowed_domains = ['www.espn.com']
    start_urls = ["https://www.espn.com/soccer/team/squad/_/id/382/league/ENG.1", 
                    "https://www.espn.com/soccer/team/squad/_/id/364/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/363/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/367/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/360/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/371/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/380/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/375/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/331/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/337/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/376/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/384/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/361/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/362/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/357/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/368/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/379/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/395/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/381/league/ENG.1"]

    def parse(self, response):
        items = response.css('.inline').extract()
        print(items)


        for i in range(len(items)):
            yield {
                'Item': items[i]
            }

