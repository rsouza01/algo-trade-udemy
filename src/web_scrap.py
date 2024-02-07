import requests
import bs4 as bs


url="https://finance.yahoo.com/quote/ASML/financials?p=ASML"

headers = {"User-Agent" : "Chrome/96.0.4664.110"}
page = requests.get(url, headers=headers)
page_content = page.content
print(page)
print(page.content)