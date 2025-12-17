from flask_babel import _
from google.cloud import translate_v2 as translate
from flask import current_app

# note this funciton don't make any use source_lanague variable
def translate_api(text, source_language='en', dest_language='en'):

    print("working", current_app.config['TRANSLATION_KEY_JSON'])

    if current_app.config['TRANSLATION_KEY_JSON'] is None:
        return _('Error: the translation service is down')

    try:
        print("working", current_app.config['TRANSLATION_KEY_JSON'], text, dest_language)

        client = translate.Client.from_service_account_json(current_app.config['TRANSLATION_KEY_JSON'])
        print('client', client)
        result = client.translate(text, target_language=dest_language)
        print('text',text)
    except:
        return _('Error: the translation service is down')
    
    return str(result['translatedText'])