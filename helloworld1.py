import json
import urllib2
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
		gurl = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBATu7aHC1ROhUBOohSmWIPPMeklDsWh8I&address=Mumbai"
		#print soup
		#print gurl
		gu = urllib2.urlopen(gurl)
		gcont = gu.read()
		j = json.loads(gcont)
		self.response.headers['Content-Type'] = 'text/plain'
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
		
		self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)