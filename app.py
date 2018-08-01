from flask import Flask, jsonify, request, json
import data as elasticsearch
import ConfigParser



config = ConfigParser.ConfigParser()
config.read('config.ini')

FLASK_HOST = config.get('FLASK','host')
FLASK_PORT = config.get('FLASK','port')






app = Flask(__name__)



#	Method: POST
#	URL : /people/contact
#	Payload: {'name': 'Daniel Hui','number': '267-234-8911'}
#	Response : {'name': string,'number': string}
#	
@app.route("/people/contact", methods=["POST"])
def create_contact():
	req_json = request.json
	name = req_json['name']
	contact = req_json['contact']


	res_obj = elasticsearch.create_contact(name,contact)
	_id = res_obj['_id']
	doc = elasticsearch.get(_id)
	
	return jsonify(doc)


#	Method: PUT
#	URL : /people/contact/<name>
#	Payload: {'number': '267-234-8911'}
#	Response : {'name': string,'number': string}
#
@app.route("/people/contact/<name>", methods=["PUT"])
def update_contact(name):
	req_json = request.json
	contact = req_json['contact']
	res_obj = elasticsearch.update_contact(name,contact)

	_id = res_obj['_id']
	doc = elasticsearch.get(_id)
	
	return jsonify(doc)



#	Method: GET
#	URL : /people/contact/<name>
#	Payload:  None
#	Response : [{'name': string,'number': string}]
#
@app.route("/people/contact/<name>", methods=["GET"])
def get_contact(name):
	contact_objs = elasticsearch.search(name=name, args=None)

	return jsonify(contact_objs)



#	Method: DELETE
# 	URL : /people/contact/<name>
#	Payload: None
#	Response : {'result': string}
#
@app.route("/people/contact/<name>", methods=["DELETE"])
def delete_contact(name):
	success = elasticsearch.delete_contact(name)
	response = {'result': success}
	
	return jsonify(response)




#	Method: GET
# 	URL : /people/contact
#	Request Params :  pageSize={}&page={}&query={}
#	Payload:  None
#	Response : [{'name': string,'number': string}]
#
@app.route("/people/contact", methods=["GET"])
def get_contact_options():
	params = {}

	
	params['size'] = request.args.get('pageSize')
	params['from'] = request.args.get('page')
	params['query'] = request.args.get('query')


	res_obj = elasticsearch.search(name=None, args=params)

	return jsonify(res_obj)








if __name__ == '__main__':
	app.run(debug=True, host=FLASK_HOST, port=FLASK_PORT)