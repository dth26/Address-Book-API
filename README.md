# Address-Book-API

To start the rest api service run ```flask run --port=80```


	Method: POST
	URL : /people/contact
	Payload: {'name': 'Daniel Hui','number': '267-234-8911'}
	Response : {'name': string,'number': string}



	Method: PUT
	URL : /people/contact/<name>
	Payload: {'number': '267-234-8911'}
	Response : {'name': string,'number': string}



	Method: GET
	URL : /people/contact/<name>
	Payload:  None
	Response : [{'name': string,'number': string}]



	Method: DELETE
  URL : /people/contact/<name>
	Payload: None
	Response : {'result': string}





	Method: GET
  URL : /people/contact
 	Request Params :  pageSize={}&page={}&query={}
	Payload:  None
	Response : [{'name': string,'number': string}]



