import httpx
from pyquery import PyQuery as pq
res = httpx.get('https://www.phb123.com/renwu/fuhao/zhou_AS_9.html')
q = pq(res.text)
items = q('.rank-table a')

imgUrls = []
names = []
for item in items.items():
  print(item)

