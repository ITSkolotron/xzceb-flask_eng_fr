import json
""" imports """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-08-16',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """ translates english to french"""
    french_dict = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    french_text1 = french_dict['translations']
    french_text2 = french_text1[0]
    french_text = french_text2['translation']
    return french_text


def french_to_english(frenchtext):
    """translates french to english"""
    english_dict = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    english_text1 = english_dict['translations']
    english_text2 = english_text1[0]
    english_text = english_text2['translation']
    return english_text
