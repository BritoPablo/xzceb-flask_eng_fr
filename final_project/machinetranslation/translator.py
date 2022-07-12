'''Script to translate'''
from ibm_watson import LanguageTranslatorV3
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


#gettig a intance of lenaguage translator watson
authenticator = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

lt.set_service_url(url)

'''function to translate to frech'''
def english_to_french(english_text):
    #write the code here
    translation = lt.translate(text=english_text,
    model_id='en-fr').get_result()

    return translation['translations'][0]['translation']

'''function to translate'''
def french_to_english(french_text):
    #write the code here
    translation = lt.translate(text=french_text,
    model_id='fr-en').get_result()

    return translation['translations'][0]['translation']
