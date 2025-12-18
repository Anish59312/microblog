from flask import current_app

# in elasticsearch a index is fundamental unit of storage
# it is collection of documents that share similar structure and purpose
# added as (index, id, body)
# stored as {index : (id1, body1), (id2, body2)}
def add_to_index(index, model):
    if current_app.config['ELASTICSEARCH_URL'] is None:
        return
    
    payload = {}

    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    
    current_app.elasticsearch.index(index=index, id=model.id, body=payload)

def remove_from_index(index, model):
    if current_app.config['ELASTICSEARCH_URL'] is None:
        return 
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    if current_app.config['ELASTICSEARCH_URL'] is None:
        return [], 0

    search = current_app.elasticsearch.search(
                index=index, 
                body= {'query': {'multi_match': {'query': query, 'fields': ['*']}},
                       'from': (page-1)*per_page,
                        'size': per_page }
                )
    
    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    return ids, search['hits']['total']['value']
