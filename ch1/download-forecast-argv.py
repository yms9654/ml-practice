import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId': '109'
}

params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)