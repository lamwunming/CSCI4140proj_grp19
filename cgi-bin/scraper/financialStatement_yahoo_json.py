#! /usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup
# import cgi
# import cgitb
# cgitb.enable()
#
# form = cgi.FieldStorage()

# company = "0005.HK"
# company = "GOOG"
# company = form.getvalue("code")
company = sys.argv[1]
# Show: "financials" | "balance-sheet" | "cash-flow"
# show = "financials"
# show = form.getvalue("show")
company = sys.argv[2]

url = "https://finance.yahoo.com/quote/" + company + "/" + show + "?p=" + company

source = requests.get(url)

text = source.text

soup = BeautifulSoup(text, "lxml")

error = soup.find(attrs={"id" : "lookup-page"})

table = None

if(not error):
    header = soup.find(attrs={"data-test" : "quote-header"})
    name = header.find_all(recursive=False)[1].find_all(recursive=False)[0].find("h1").text
    currency = header.find_all(recursive=False)[1].find_all(recursive=False)[0].find("span").text.split(".")[1]


    section = soup.find(attrs={"data-test" : "qsp-financial"})

    # print(section

    table = section.find("table")

    # print(table

dict = []
printShow = None
if(show=="financials"):
    printShow = "Income Statement"
elif(show=="balance-sheet"):
    printShow = "Balance Sheet"
else:
    printShow = "Cash Flow"
dict.append([company, printShow, name, currency])


count = 0
for tr in table.findAll('tr'):
    td = tr.findAll('td')
    first = 1
    if(len(td)<4):
        span = td[0].find('span')
        # print(td[0].find('span').text,"............")
        dict.append([td[0].find('span').text])
    else:
        arr = []
        for tableData in td:
            span = tableData.find('span')
            if(span):
                # print(span.text, end='  ')
                arr.append(span.text)
                # if(first==1):
                #     print(":", end='  ')
                #     first = 0
            else:
                # print("-", end='  ')
                arr.append("-")
        dict.append(arr)
            # column = column + 1
#     print("")
#
# for i in dict:
#     print(i)

print(dict)
