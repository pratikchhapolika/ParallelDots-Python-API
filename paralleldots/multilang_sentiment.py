from paralleldots.config import get_api_key
import requests
import json

def get_multilang_sentiment( text, lang ):
	apikey  = get_api_key()
	if not apikey == None:
		if type( text ) != str or type( lang ) != str:
			return "Input must be a string." 
		elif text in [ "", None ] or lang in [ "", None ]:
			return "Input string cannot be empty."
		url = "http://apis.paralleldots.com/multilang_sentiment"
		r =  requests.post( url, params={ "apikey": apikey, "text": text, "lang": lang } )
		if r.status_code != 200:
			return "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues."
		r = json.loads( r.text )
		r["usage"] = "By accessing ParallelDots API or using information generated by ParallelDots API, you are agreeing to be bound by the ParallelDots API Terms of Use: http://www.paralleldots.com/terms-and-conditions"
		return r
	else:
		return "API key does not exist"