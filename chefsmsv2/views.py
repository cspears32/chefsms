# views.py

from twilio.rest import TwilioRestClient
from twilio import twiml
from django.http import HttpResponse
from datetime import datetime, timedelta
#from django.views.decorators.csrf import csrf_exempt
from django_twilio.decorators import twilio_view

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "####"
auth_token  = "####"
CID="####"
#API="2010-04-01"
#sms_path='/%s/Accounts/%s/SMS/Messages'%(API,account_sid) 
client = TwilioRestClient(account_sid, auth_token)

@twilio_view
#@csrf_exempt

#Prompt with initial choices. 
	#HttpResponse if using form submission
	#twiml to respond
def message(request):
	#thing= HttpResponse('From', None)#getting closer
	body_meal= request.POST.get('Body','')
	#message = client.messages.create(
		#body="Thanks for testing this. Breakfast lunch or dinner?"
    	#to= "6263942388",
    		#or replace with an html/django form that someone has filled in from index.html
    	#from_="+14144486479",) #Twilio number
	if "Breakfast" in body_meal:
		twiml='<Response><Message>Breakfast is my favorite meal. Good choice. </Message></Response>'
		return twiml
	elif "Lunch" in body_meal:
		twiml='<Response><Message>Let\'s Lunch!</Message></Response>'
		return twiml
	elif "Dinner" in body_meal:
		twiml='<Response><Message>Aww yiss it\'s dinner time.</Message></Response>'
		return twiml
	else:
		twiml='<Response><Message>http://allrecipes.com/search/results/?wt=%s&sort=re</Message></Response>' % (body_meal)
		return twiml 
		#return HttpResponse (<h1>'An index.html page should be here!'</h1>)
	#should this go into urls py instead? With views redirecting to the appropriate page/app/model? Check Macbook for links
	"""
	body_user_name= request.POST.get('Body','')
	twiml = '<Response><Message>Hey %s, this is Chefsms, your personal recipe finder. Hungry? Text back: Breakfast, Lunch, Dinner, or Snack</Message></Response>' % (user_name)
	#add if response is y, then....etc
	#add user_name to database/track with cookies
	return twiml #HttpResponse(twiml, content_type='text/xml')

def breakfast(request):
	link_breakfast=#web crawler for random brekkie recipe
		#choose from different site each time to avoid fatigue

		scrape from http://allrecipes.com/search/results/?wt=breakfast&sort=re


		two options:
		cycle through 5+ sites with "meal" in search, pull random with high scores
		cycle through 5+ sites with "body_meal" in search, ^^^
	"""
