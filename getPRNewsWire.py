import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
import os

data = requests.get(url, proxies=proxies)
soup = BeautifulSoup(data.text, 'html.parser')

# def lambda_handler(event, context):

# 	conn = psycopg2.connect(database="stitch", user=os.environ.get("db_user"), password=os.environ.get("db_password"), host="analytics.fly4.cheap", port="5432")
# 	cur = conn.cursor()
# 	conn.autocommit = True

# 	now = datetime.now() # current date and time
# 	ddmmyy = now.strftime("%Y-%m-%d")

# 	url = "https://www.kayak.com/travel-restrictions"

# 	http_proxy = "http://"+os.environ.get("proxy_user")+":"+os.environ.get("proxy_password")+"@proxy.packetstream.io:31112"
# 	https_proxy = "http://"+os.environ.get("proxy_user")+":"+os.environ.get("proxy_password")+"@proxy.packetstream.io:31112"

# 	proxies = {
# 	"http" : http_proxy,
# 	"https" : https_proxy,
# 	}
# 	data = requests.get(url, proxies=proxies)
# 	soup = BeautifulSoup(data.text, 'html.parser')
# 	soupstr = str(soup)
# 	restrictionText = soupstr[soupstr.find('"restrictionEntries":[')+21:soupstr.find(',"googleApiKey":')].encode('ascii', 'ignore').decode()
# 	restrictionText2 = restrictionText.replace("\\'", "")
# 	restrictionJson = json.loads(restrictionText2)
# 	# print(json.dumps(restrictionJson))

# 	# DELETE EXISTING DATA
# 	delete_sql = "DELETE FROM public.legislation_country2;"
# 	cur.execute(delete_sql)
# 	print("Rows Deleted")

# 	for country in restrictionJson:
# 		# print(country["htmlId"])
# 		article = soup.find("article", "CountryReport", id=country["htmlId"])
# 		if article is None:
# 			continue
# 		summary = article.find("p", "CountryReport__paragraph")
# 		detail = article.find("div", "CountryReport__paragraph")
# 		data = [
# 			country["country"]["ccfips"],
# 			country["country"]["cciso2"],
# 			country["country"]["cciso3"],
# 			country["country"]["rankedAliases"][0],
# 			country["borderStatus"],
# 			str(summary) + str(detail),
# 			ddmmyy
# 			]
# 		cur.execute("INSERT INTO public.legislation_country2 VALUES (%s, %s, %s, %s, %s, %s, %s);", tuple(data))
# 	print("Rows Inserted")

# 	# Update flags on deal destinations
# 	cur.execute("""
# 	UPDATE public.deal_destinations as dd
# 	SET valid = (r.borderstatus = 'NO_RESTRICTIONS')
# 	FROM public.legislation_country2 r
# 	WHERE r.name like concat('%', dd.country, '%')
# 	and dd.type = 'International'
# 	;
# 	""")

# 	# TODO implement
# 	return {
# 		'statusCode': 200,
# 		'body': json.dumps('Hello from Lambda!')
# 	}
