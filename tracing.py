import urllib2
from bs4 import BeautifulSoup
import sqlite3

# Zeitraum: 04/15/2011 bis 07/19/2011

# 07/19/2011 - 04/26/2011

# Datum [month/day/year]
# Type [changeset, closedticket, newticket, em(defect, enhancement, ...) ]
# Number [#number fuer ticket, [number] fuer changeset]
# Author

# die datenbank
connection = sqlite3.connect("trac.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS stat (
	datum TEXT,
	type TEXT,
	nummer TEXT,
	author TEXT
	)""")

adress = "https://dev.spline.de/trac/CommonUnfold/timeline?from=2011-04-25&daysback=9&authors="
# adress = "https://dev.spline.de/trac/CommonUnfold/timeline?from=2011-07-19&daysback=97&authors="
website = urllib2.urlopen(adress)
website_html = website.read()
website.close()

soup = BeautifulSoup(website_html)

dates = soup.find_all('h2')

del dates[0:1]

days = soup.find_all('dl')

count = 0
for day in days:
	items = day.find_all('dt')

	for item in items:
		date 		= str(dates[count].string[:-2])
		typ 		= item['class'][0]
		number 	= str(item.find('em').string)
		author 	= str(item.find('span', {"class" : "author"}).string)
		sql 		= ("""INSERT INTO stat VALUES (?, ?, ?, ?)""")
		values 	= (date, typ, number, author)
		print type(date), type(typ), type(number), type(author)

		cursor.execute(sql, values)
		connection.commit()

	count = count + 1

