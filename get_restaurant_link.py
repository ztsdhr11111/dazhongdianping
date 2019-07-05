import requests
from lxml import etree


locations_ids = ['1481', '1484', '2595', '1500', '1503', '1482', '1483', '1486', '1499', '2873', '1994', '23028', '1488', '1489', '2588', '1493', '1490', '1494', '1491', '1996', '2587', '2589', '1496', '23030', '1492', '1497', '23034', '23029', '23033', '23988', '23032', '23031', '70131', '23023', '1475', '23024', '1504', '2066', '1503', '1486', '1479', '1477', '2590', '2591', '23022', '1505', '23026', '89473', '1923', '1926', '1924', '2578', '2580', '1470', '23002', '1471', '2078', '1466', '1469', '23010', '1472', '2583', '22997', '2579', '70191', '23020', '1468', '1473', '22998',
                '2871', '23019', '1465', '1467', '23004', '2584', '2870', '23003', '2591', '2581', '7509', '23001', '23013', '23007', '22996', '23000', '23005', '22999', '23006', '12013', '12015', '12012', '83304', '2586', '23014', '23018', '70269', '23037', '89852', '85511', '89473', '25600', '1507', '2879', '2592', '2878', '23036', '1508', '2877', '1994', '23039', '70132', '2881', '7506', '1995', '2880', '7507', '7041', '70610', '23040', '23038', '23037', '89861', '64877', '23041', '2585', '64878', '86569', '30781', '12011', '67342', '67346', '67350', '67384', '5959', '5961',
                '5960', '7043', '70633', '85684', '89861', '5953', '5954', '5955', '7042', '23043', '23044', '86575', '7521', '23045', '5958', '5957', '5956', '23990', '64883', '25907', '64882', '70618', '86548', '65439', '65441', '27617', '27618', '27615', '27614', '27616']
foods_types = ['1845', '219', '101', '114', '1338', '33759', '26482', '251', '34055', '113', '132', '116', '104', '112', '34014', '118', '250', '110', '246', '26481', '34059', '103', '34032', '111', '34236', '6743', '1817', '109', '2714', '106', '34284', '508', '102', '311', '117', '3243', '26483', '115', '1783', '107']

base_url = 'http://www.dianping.com/beijing/ch10/'

class GetRestaurantLink(object):
    def request(self, url, params=None):
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response
        except Exception as e:
            print(e)
    



