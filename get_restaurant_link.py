import requests
import time
from lxml import etree


locations_ids = ['1481', '1484', '2595', '1500', '1503', '1482', '1483', '1486', '1499', '2873', '1994', '23028', '1488', '1489', '2588', '1493', '1490', '1494', '1491', '1996', '2587', '2589', '1496', '23030', '1492', '1497', '23034', '23029', '23033', '23988', '23032', '23031', '70131', '23023', '1475', '23024', '1504', '2066', '1503', '1486', '1479', '1477', '2590', '2591', '23022', '1505', '23026', '89473', '1923', '1926', '1924', '2578', '2580', '1470', '23002', '1471', '2078', '1466', '1469', '23010', '1472', '2583', '22997', '2579', '70191', '23020', '1468', '1473', '22998',
                '2871', '23019', '1465', '1467', '23004', '2584', '2870', '23003', '2591', '2581', '7509', '23001', '23013', '23007', '22996', '23000', '23005', '22999', '23006', '12013', '12015', '12012', '83304', '2586', '23014', '23018', '70269', '23037', '89852', '85511', '89473', '25600', '1507', '2879', '2592', '2878', '23036', '1508', '2877', '1994', '23039', '70132', '2881', '7506', '1995', '2880', '7507', '7041', '70610', '23040', '23038', '23037', '89861', '64877', '23041', '2585', '64878', '86569', '30781', '12011', '67342', '67346', '67350', '67384', '5959', '5961',
                '5960', '7043', '70633', '85684', '89861', '5953', '5954', '5955', '7042', '23043', '23044', '86575', '7521', '23045', '5958', '5957', '5956', '23990', '64883', '25907', '64882', '70618', '86548', '65439', '65441', '27617', '27618', '27615', '27614', '27616']
foods_types = ['1845', '219', '101', '114', '1338', '33759', '26482', '251', '34055', '113', '132', '116', '104', '112', '34014', '118', '250', '110', '246', '26481', '34059', '103', '34032', '111', '34236', '6743', '1817', '109', '2714', '106', '34284', '508', '102', '311', '117', '3243', '26483', '115', '1783', '107']


class GetRestaurantLink(object):
    base_url = 'http://www.dianping.com/beijing/ch10/g{}r{}'

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
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response
        except Exception as e:
            print(e)
    
    def parse(self, response):
        html = etree.HTML(response.text)
        shop_names = html.xpath('//div[@id="shop-all-list"]/ul/li/div[@class="txt"]//h4/text()')
        for shop_name in shop_names:
            print(shop_name)
        
    
    def structure_urls(self):
        for g in foods_types:
            for r in locations_ids:
                url = self.base_url.format(g, r)
                yield url

    def run(self):
        num = 1
        urls = self.structure_urls()
        for url in urls:
            response = self.request(url)
            if response is not None:
                if '没有找到符合条件的商户' in response.text:
                    print('该地区没有商户')
                    continue
                self.parse(response)
            time.sleep(10)
            num += 1
            if num == 10:
                break


if __name__ == "__main__":
    restaurant_links = GetRestaurantLink()
    restaurant_links.run()