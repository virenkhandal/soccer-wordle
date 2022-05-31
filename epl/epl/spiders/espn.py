import scrapy


class EspnSpider(scrapy.Spider):
    name = 'espn'
    allowed_domains = ['www.espn.com']
    # start_urls = ["https://www.espn.com/soccer/team/squad/_/id/382/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/364/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/363/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/367/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/360/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/371/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/380/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/375/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/331/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/337/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/376/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/384/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/361/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/362/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/357/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/368/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/379/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/395/league/ENG.1",
    #                 "https://www.espn.com/soccer/team/squad/_/id/381/league/ENG.1"]

    # Manchester City, Liverpool, Manchester United, Tottenham Hotspurs, Arsenal, Chelsea
    # Real Madrid, FC Barcelona, Athletico Madrid
    # Paris Saint-Germain
    # Juventus, Napoli, Inter Milan, AC Milan
    # Bayern Munich, Borussia Dortmund
    # Ajax
    start_urls = ["https://www.espn.com/soccer/team/squad/_/id/382/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/364/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/360/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/363/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/367/league/ENG.1",
                    "https://www.espn.com/soccer/team/squad/_/id/86/league/ESP.1",
                    "https://www.espn.com/soccer/team/squad/_/id/83/league/ESP.1",
                    "https://www.espn.com/soccer/team/squad/_/id/1068/league/ESP.1",
                    "https://www.espn.com/soccer/team/squad/_/id/160/league/FRA.1",
                    "https://www.espn.com/soccer/team/squad/_/id/111/league/ITA.1",
                    "https://www.espn.com/soccer/team/squad/_/id/110/league/ITA.1",
                    "https://www.espn.com/soccer/team/squad/_/id/103/league/ITA.1",
                    "https://www.espn.com/soccer/team/squad/_/id/114/league/ITA.1",
                    "https://www.espn.com/soccer/team/squad/_/id/132/league/GER.1",
                    "https://www.espn.com/soccer/team/squad/_/id/132/league/GER.1",
                    "https://www.espn.com/soccer/team/squad/_/id/124/league/GER.1"]

    def parse(self, response):
        squad = []
        team = response.css('.fw-bold::text').get()
        data = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "inline", " " ))]/text()').extract()
        jerseys = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "n10", " " ))]/text()').extract()
        names = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "inline", " " ))]/a/text()').extract()
        index = 0
        for i in range(0, len(names)):
            name = names[i]
            jersey = jerseys[i]
            position = data[index][0]
            if position == 'G':
                yield {'Name': name,
                   'Team': team,
                   'Jersey' : jersey,
                   'Stats': data[index:index+14]}
                # stats = data[index:index+14]
                index += 14
            else:
                yield {'Name': name,
                   'Team': team,
                   'Jersey' : jersey,
                   'Stats': data[index:index+15]}
                index += 15
