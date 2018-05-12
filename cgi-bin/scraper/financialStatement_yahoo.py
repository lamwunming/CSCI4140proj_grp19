import requests
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

# company = "0005.HK"
# company = "GOOG"
company = form.getvalue("code")
# Show: "financials" | "balance-sheet" | "cash-flow"
# show = "cash-flow"
show = form.getvalue("show")

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


print("Content-Type: text/html\n\n")  # html markup follows
print "<html>"
print "<head>"
print "<Title>Index</Title>"
print "</head>"
print "<body>"

count = 0
for tr in table.findAll('tr'):
    td = tr.findAll('td')
    first = 1
    if(len(td)<4):
        print td[0].find('span').text,"-------------------------------------------------<br>"
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
        print "<br>"

print "<br>"
if(form.getvalue("code")):
    print "<div>" + form.getvalue("code") + "</div>"
else:
    print "<div>APPL</div>"

print "<br>"
if(form.getvalue("show")):
    print "<div>" + form.getvalue("show") + "</div>"
else:
    print "<div>cash-flow</div>"

print "</body>"
print "</html>"

    # if(count==0):
    #     print (len(td))
    #     print td
    # count = count + 1
    # if(len(td)<4):
    #     print td[0].find('span').text
