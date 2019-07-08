from fontTools.ttLib import TTFont
import requests

url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/f4a0711f919614e98d3eb4744a4a9a7f.css'
res = requests.get(url)

# with open('dzdp.woff', 'wb') as f:
#     f.write(res.content)
font = TTFont('./dzdp.ttf')
print(font)