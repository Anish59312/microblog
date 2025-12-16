from flask_babel import _
from google.cloud import translate_v2 as translate
from app import app
client = translate.Client.from_service_account_json(app.config['TRANSLATION_KEY_JSON'])

def translate(text, source_language='en', dest_language='en'):
    if app.config['TRANSLATION_KEY_JSON'] is None:
        return _('Error: the translation service is down')

    try:
        result = client.translate(text, target_language=dest_language)
    except:
        return _('Error: the translation service is down')
    
    return str(result['translatedText'])