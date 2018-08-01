from elasticsearch import Elasticsearch
import ConfigParser
import re
from flask import jsonify


config = ConfigParser.ConfigParser()
config.read('config.ini')

ELASTIC_HOST = config.get('ELASTICSEARCH','host')
ELASTIC_PORT = config.get('ELASTICSEARCH','port')



es_settings =  {
	"settings" : {
		"number_of_shards": 1,
		"number_of_replicas": 0
	},
	"mappings" : {
	    "contact" : {
	     	"properties": {
	     		"contact": {
	     			"type": "text"
	     		},
	     		"name": {
	     			"type": "text"
	     		}
	         }
		}
    }
}


try:
	es = Elasticsearch(host=ELASTIC_HOST, port=ELASTIC_PORT)
	print "Connected", es.info()

except Exception as ex:
	print "Error:", ex




def create_contact_index():

	if not es.indices.exist(index):
		res = es.indices.create(index = 'people', body=es_settings)
		print res
	else:
		print 'Index already created!'



def create_contact(name, contact):
	
	# clean contact and remove non-digits
	clean_contact = ''.join(re.findall(r'\d+', str(contact)))
	contact_obj = {
		'contact': clean_contact, 
		'name': name
	}

	print 'creating contact : '
	print contact_obj


	res = es.index(index='people', doc_type='contact', body=contact_obj)
	es.indices.refresh('people')

	return res


def update_contact(name, contact):
	
	# clean contact and remove non-digits
	clean_contact = ''.join(re.findall(r'\d+', str(contact)))
	#contact_obj = {
	#	'contact': clean_contact, 
	#	'name': name
	#


	body = { "doc": { "name": name, 'contact' : clean_contact } }

	contact_obj = search(name=name)[0]
	id = contact_obj['id']

	res = es.update(index='people', doc_type='contact', body=body, id=id)

	es.indices.refresh('people')

	return res


def search(name=None, args=None):

	body = {}

	if args is not None:
		body['query'] = {
			"query_string" : {
				"query" : args['query']
			}
		}
		body['size'] = args['size']
		body['from'] = args['from']

	else:
		body = {
			"query": {                        # the query
				'match': {
	 				'name': name
	    		}
			}
		}




	contact_res_obj = es.search(index='people', body=body)
	


	contact_objs = []
	for contact in contact_res_obj['hits']['hits']: 
		curr = contact['_source']
		curr['id'] = contact['_id']
		contact_objs.append(contact['_source'])



	return contact_objs



def delete_contact(name):
	ret_val = True
	contact_obj = search(name=name)[0]



	res = es.delete(index='people', doc_type='contact', id=contact_obj['id'])

	es.indices.refresh('people')

	if res['_shards']['successful'] != 1:
		ret_val = False

	return ret_val



def get(id):
	res = es.get(doc_type="contact",index="people", id=id, ignore=[404])
	
	return res['_source']








