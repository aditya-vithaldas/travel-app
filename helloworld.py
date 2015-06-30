import json
import urllib2
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
		surlbasearr = [ "http://www.tripadvisor.in/TourismChildrenAjax?geo=293860&offset=",
			"http://www.tripadvisor.in/TourismChildrenAjax?geo=297627&offset="]

		c = 0

		for s in range(1):
			surlbase  = surlbasearr[c]
			ctr = 1
			print  c
			#print "state is " + state
			self.response.write( "url is " +surlbase)
			for i in range(1):
				surl = ("%s%i" % (surlbase, i))

				self.response.write( "URL to open : " + surl	)
				
				u = urllib2.urlopen(surl)
				scont = u.read()
				
				state = "dummy"
				from bs4 import BeautifulSoup
				soup = BeautifulSoup(scont)
				
				for sturl in soup.findAll("a"):
					url = sturl['href']
					start = url.find('_')
					end = url.find('-Vacations')
					state = url[start+1:end]
					#print "state = " + state
					
				geourl = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBATu7aHC1ROhUBOohSmWIPPMeklDsWh8I&address="
				#print soup
				for res in soup.findAll(attrs={'class' : 'popularCity'}):
							
					for city in res.select('img'):

						strcity = city['alt']
						strcity = strcity.replace(" ", "%20")

						gurl = geourl + strcity #city['alt']
						self.response.write( gurl)
						gu = urllib2.urlopen(gurl)
						gcont = gu.read()
						j = json.loads(gcont)
						
						if j["status"] <> "ZERO_RESULTS":
							strcity = j["results"][0]["formatted_address"]
							strlat = j["results"][0]["geometry"]["location"]["lat"]
							strlong = j["results"][0]["geometry"]["location"]["lng"]
							self.response.write( strlat)
							self.response.write( strlong)
							start = strcity.find(", ")
							end = strcity.find(", ", start+1)
						
							state = strcity[start+2:end]
							self.response.write( strcity)
							self.response.write( state)
							#print j['results']['geometry']['location']['lat']
	
					ctr = ctr + 1
			c = c + 1

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)