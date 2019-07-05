import requests
from lxml import etree

url = 'http://www.dianping.com/beijing/ch10/g219r14'

class GetLocation(object):
    def request(self, url, params=None):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'showNav=#nav-tab|0|1; navCtgScroll=100; navCtgScroll=100; showNav=#nav-tab|0|1; _lxsdk_cuid=16a681c201c35-00b59f9192288d-39395704-15f900-16a681c201dc8; _lxsdk=16a681c201c35-00b59f9192288d-39395704-15f900-16a681c201dc8; _hc.v=84d3c394-cda7-c4ac-fbf6-11a725e1f1d2.1556524835; s_ViewType=10; cy=2; cye=beijing; switchcityflashtoast=1; default_ab=shop%3AA%3A5%7Cindex%3AA%3A1%7CshopList%3AC%3A4; cityid=2; PHOENIX_ID=0a512d03-16bbcc90dd3-4242e0e; _tr.u=TfWLrZCx9KxQHme3; _tr.s=C4CNZRxTM4SIvmeB; source=m_browser_test_33; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2; pvhistory=6L+U5ZuePjo8L2Vycm9yL2Vycm9yX3BhZ2U+OjwxNTYyMjQwNzM3MDg5XV9b; m_flash2=1; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_s=16bc12298ce-756-ff8-74f%7C%7C134',
            'Host': 'www.dianping.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        try:
            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print(e)

    def parse_1(self, response):
        html = etree.HTML(response.text)
        location_v1s = html.xpath('//div[@id="region-nav"]/a/@href')
        return location_v1s
    
    def parse_2(self, response):
        html = etree.HTML(response.text)
        location_ids = html.xpath('//div[@id="region-nav-sub"]/a/@data-cat-id')
        food_types = html.xpath('//div[@id="classfy"]/a/@data-cat-id')
        return location_ids, food_types
    
    def run(self, url):
        locations_ids = []
        foods_types = []
        response = self.request(url)
        if response is not None:
            location_v1s = self.parse_1(response)
            for location in location_v1s:
                response = self.request(location)
                locations, food_types = self.parse_2(response)
                locations_ids.extend(locations)
                foods_types.extend(food_types)
        print(locations_ids)
        foods_types = list(set(foods_types))
        print(foods_types)
        
if __name__ == '__main__':
    location = GetLocation()
    location.run(url)