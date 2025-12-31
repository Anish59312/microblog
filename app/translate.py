from flask_babel import _
from google.cloud import translate_v2 as translate
from flask import current_app
from googletrans import Translator
import asyncio


def translate_locally(text, source_language='en', dest_language='en'):
    translator = Translator()
    try:
        result = translator.translate(
            text,
            dest=dest_language
        )
        print("############################ RESULT", result)
        return result.text
    except Exception:
        return _('Error: the translation service is down')
 


# note this funciton don't make any use source_lanague variable
def translate_api(text, source_language='en', dest_language='en'):

    if current_app.config['TRANSLATION_KEY_JSON'] is None:
        return _('Error: the translation service is down')

    try:
        print("################################ inside block 1")

        client = translate.Client.from_service_account_json(current_app.config['TRANSLATION_KEY_JSON'])
        result = client.translate(text, target_language=dest_language)

    except:
        try:
            return translate_locally(text, source_language, dest_language)
        except:
            return _('Error: the translation service is down')
    
    return str(result['translatedText'])