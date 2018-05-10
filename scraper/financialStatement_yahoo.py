import requests
from bs4 import BeautifulSoup

# company = "0005.HK"
company = "GOOG"

# Show: "finacials" | "balance-sheet" | "cash-flow"
show = "cash-flow"

url = "https://finance.yahoo.com/quote/" + company + "/" + show + "?p=" + company

source = requests.get(url)

text = source.text

soup = BeautifulSoup(text, "lxml")

# with open("Output.txt", "w") as text_file:
#     text_file.write(str(soup)

section = soup.find(attrs={"data-test" : "qsp-financial"})

# print section

table = soup.find("table")

# print table

count = 0
for tr in table.findAll('tr'):
    td = tr.findAll('td')
    first = 1
    if(len(td)<4):
        print td[0].find('span').text,"-------------------------------------------------\n"
    else:
        for tableData in td:
            span = tableData.find('span')
            if(span):
                print span.text,
                if(first==1):
                    print ":",
                    first = 0
            else:
                print "-",
        print "\n"

    # if(count==0):
    #     print (len(td))
    #     print td
    # count = count + 1
    # if(len(td)<4):
    #     print td[0].find('span').text
