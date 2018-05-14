#! /usr/bin/env python
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


print("Content-Type: text/html\n\n")  # html markup follows
print("<html>")
print("<head>")
print("<Title>Index</Title>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
# print('<link rel="icon" type="image/png" href="/css/table/images/icons/favicon.ico"/>'
print('<link rel="stylesheet" type="text/css" href="/css/table/vendor/bootstrap/css/bootstrap.min.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/fonts/font-awesome-4.7.0/css/font-awesome.min.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/vendor/animate/animate.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/vendor/select2/select2.min.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/vendor/perfect-scrollbar/perfect-scrollbar.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/css/main.css">')
print('<link rel="stylesheet" type="text/css" href="/css/table/css/util.css">')
print("</head>")
print("<body>")
if(not error):
    print("<div class='table100 ver6 m-b-110' style='margin:0px;'>")
    print("<table data-vertable='ver6'>")
    print("<thead>")
    print("<tr class='row100 head'>")

    # print("<br>"
    if(form.getvalue("code")):
        print("<th class='column100 column1' data-column='column1'>")
        print("Searched Code:<br>" + form.getvalue("code"))
        print("</th>")
        # print("<div>" + form.getvalue("code") + "</div>"
    else:
        print("<th class='column100 column1' data-column='column1'>")
        print("Default Code:<br>APPL")
        print("</th>")
        # print("<div>APPL</div>"

    # print("<br>"
    if(form.getvalue("show")):
        print("<th class='column100 column1' data-column='column1'>")
        printShow = None
        if(show=="financials"):
            printShow = "Income Statement"
        elif(show=="balance-sheet"):
            printShow = "Balance Sheet"
        else:
            printShow = "Cash Flow"
        print("Searched Statement:<br>" + printShow)
        print("</th>")
        # print("<div>" + form.getvalue("show") + "</div>"
    else:
        print("<th class='column100 column1' data-column='column1'>")
        print("Default Statement:<br>Income Statement")
        print("</th>")
        # print("<div>cash-flow</div>"

    # print("<br>"
    print("<th class='column100 column1' data-column='column1'>")
    print(name)
    print("</th>")
    # print(name
    # print("<br>"
    print("<th class='column100 column1' data-column='column1'>")
    print(currency)
    print("</th>")

    print("</tr>")
    print("</thead>")
    print("</table>")
    print("</div>")

    print("<div class='table100 ver2 m-b-110' style='margin:0px;'>")
    print("<table data-vertable='ver2'>")

    count = 0
    for tr in table.findAll('tr'):
        if(count==0):
            print("<thead>")

        elif(count==1):
            print("<tbody>")
            count = count + 1

        if(count==0):
            print("<tr class='row100 head'>")
        else:
            print("<tr class='row100'>")

        column = 1

        td = tr.findAll('td')
        first = 1
        if(len(td)<4):
            span = td[0].find('span')
            if(count==0):
                print("<th class='column100 column" + str(column) + "' data-column='column" + str(column) + "' colspan=4>")
                print(span.text)
                print("</th>")
            else:
                print("<td class='column100 column" + str(column) + "' data-column='column" + str(column) + "' colspan=4>")
                print(span.text)
                print("</td>")
            # print(td[0].find('span').text,"-------------------------------------------------<br>"
        else:
            for tableData in td:
                span = tableData.find('span')
                if(span):
                    if(count==0):
                        print("<th class='column100 column" + str(column) + "' data-column='column" + str(column) + "'>")
                        print(span.text)
                        print("</th>")
                    else:
                        print("<td class='column100 column" + str(column) + "' data-column='column" + str(column) + "'>")
                        print(span.text)
                        print("</td>")
                    # print(span.text,
                    # if(first==1):
                    #     print(":",
                    #     first = 0
                else:
                    if(count==0):
                        print("<th class='column100 column" + str(column) + "' data-column='column" + str(column) + "'>")
                        print("-")
                        print("</th>")
                    else:
                        print("<td class='column100 column" + str(column) + "' data-column='column" + str(column) + "'>")
                        print("-")
                        print("</td>")
                    # print("-",

                column = column + 1
            # print("<br>"



        print("</tr>")
        if(count==0):
            print("</thead>")
            count = count + 1

    print("</tbody>")
    print("</table>")
    print("</div>")
else:
    print("<div>No Result Found for Code " + company + ". <a href='/dashboard.html'>Click me</a> return DashBoard</div>")

print("</body>")
print("</html>")
