import requests
from bs4 import BeautifulSoup

# company = "0005.HK"
company = "00024"

# Show: "pl" (Income Statement (Profit & Loss)) |
#       "bs" (Financial Position (Balance Sheet)) |
#       "cashflow" (Cash Flow Statement)
show = "cashflow"

url = "http://www.etnet.com.hk/www/eng/stocks/realtime/quote_ci_" + show + ".php?code=" + company

source = requests.get(url)

text = source.text

soup = BeautifulSoup(text, "lxml")

# with open("Output.txt", "w") as text_file:
#     text_file.write(str(soup)

# table = soup.find(attrs={"class" : "figureTable"})
# text = table[1].previousSibling.text
# print text

if(show=="pl"):
    div = soup.find(attrs={"class" : "DivFigureContent"})
    tables = div.findAll(attrs={"class" : "figureTable"})
    for i in range(len(tables)):
        if(i>0):
            head = tables[i].parent.find('div', {'class':['TextBold']})
            print head.text,"-------------------------------------------------\n"
        for tr in tables[i].findAll('tr', {'class':['oddRow', 'evenRow', 'TableHeader']}):
            td = tr.findAll('td')
            first = 1
            for tableData in td:
                if(tableData.text):
                    print tableData.text.strip(),
                    if(first==1):
                        print ":",
                        first = 0
                else:
                    print "-",
                    if(first==1):
                        first = 0
            print "\n"
elif(show=="bs"):
    div = soup.find(attrs={"class" : "DivFigureContent"})
    tables = div.findAll(attrs={"class" : "figureTable"})
    for i in range(len(tables)):
        if(i>0):
            print tables[i].previousSibling.text,"-------------------------------------------------\n"
        for tr in tables[i].findAll('tr'):
            td = tr.findAll('td')
            first = 1
            for tableData in td:
                if(tableData.text):
                    print tableData.text.strip(),
                    if(first==1):
                        print ":",
                        first = 0
                else:
                    print "-",
                    if(first==1):
                        first = 0
            print "\n"
elif(show=="cashflow"):
    div = soup.find(attrs={"class" : "DivFigureContent"})
    table = div.find(attrs={"class" : "figureTable"})
    for tr in table.findAll('tr'):
        td = tr.findAll('td')
        first = 1
        for tableData in td:
            if(tableData.text):
                print tableData.text.strip(),
                if(first==1):
                    print ":",
                    first = 0
            else:
                print "-",
                if(first==1):
                    first = 0
        print "\n"
