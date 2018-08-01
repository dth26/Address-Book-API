import unittest
import requests
from flask import jsonify, json
import time

class Test(unittest.TestCase):




	# check that "PUT" request to /people/contact/<name> updates the entry not creates a new one
	def test_update(self):

		headers = {"Content-Type": 'application/json', 'Accept': 'application/json'}

		name = "person" + str(int(time.time()))

		# create contact
		payload = {"name": name, "contact":"234-223-8911"}
		r = requests.post("http://localhost:80/people/contact", data=json.dumps(payload), headers=headers)

		# update contact
		payload = {"contact":":134-223-3911"}
		r = requests.put("http://localhost:80/people/contact/" + name, data=json.dumps(payload), headers=headers)

		# get contact 
		contact_obj = requests.get("http://localhost:80/people/contact/" + name, headers=headers)
		contact_obj = json.loads(contact_obj.text)
		#contact_obj = json.loads(contact_obj)


		self.assertTrue(len(contact_obj) == 1)






	# make sure "DELETE" request actially deletes /people/contact/<name>
	def test_delete(self):

		headers = {"Content-Type": 'application/json', 'Accept': 'application/json'}

		name = "person" + str(int(time.time())) 
		payload = {'name': name,'contact':  '9811231231'}
		contact_obj = requests.post("http://localhost:80/people/contact", data=json.dumps(payload), headers=headers)

		# delete contact 
		contact_obj = requests.delete("http://localhost:80/people/contact/" + name, headers=headers)

		# get contact 
		contact_obj = requests.get("http://localhost:80/people/contact/" + name, headers=headers)
		contact_obj = json.loads(contact_obj.text)


		self.assertTrue(len(contact_obj) == 0)








	# test that post returns the new document object that was created
	def test_post_response(self):
		headers = {"Content-Type": 'application/json', 'Accept': 'application/json'}

		name = "person" + str(time.time())
		payload = {'name': name,'contact':  '9811231231'}
		contact_obj = requests.post("http://localhost:80/people/contact", data=json.dumps(payload), headers=headers)


		# create tuples for comparing to dict
		name = ('name', name)
		contact = ('contact', '9811231231')
	
		self.assertTrue( name in json.loads(contact_obj.text).items() and contact in json.loads(contact_obj.text).items() )







if __name__ == '__main__':
	unittest.main()

