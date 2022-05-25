import scrapy


class EspnSpider(scrapy.Spider):
    name = 'espn'
    allowed_domains = ['www.espn.com']
    start_urls = ["https://www.espn.com/soccer/team/squad/_/id/382/league/ENG.1"]
                    # "https://www.espn.com/soccer/team/squad/_/id/364/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/363/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/367/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/360/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/371/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/380/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/375/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/331/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/337/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/376/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/384/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/361/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/362/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/357/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/368/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/379/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/395/league/ENG.1",
                    # "https://www.espn.com/soccer/team/squad/_/id/381/league/ENG.1"]

    def parse(self, response):
        table = response.css('.Table__TD').extract()
        teams = response.css('.fw-bold').extract()
        print(teams)
        for i in range(0, len(table), 16):
            player_data = table[i:i+16]
            name = player_data[0]
            team = teams # figure out how to assign team data
            jersey = player_data[0]
            position = player_data[1]
            age = player_data[2]
            height = player_data[3]
            weight = player_data[4]
            nation = player_data[5]
            # print(player_data[3])
            break
            print("\n\n\n\n")
        # rows = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Table__TR--sm", " " ))]')
        # print(len(table))
        # for i in range(len(table)):
        #     print(table[i])
        #     break
        # for row in rows:
        #     text = row.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Table__TD", " " ) )]')
        #     print(len(text))
        #     break
        # print("\n\n\n Player: ", table[0], "\n\n\n")
