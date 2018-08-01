curl --header "Content-Type: application/json" --request POST --data '{"name":"daniel","contact":":234-223-8911"}' http://localhost:80/people/contact
curl --header "Content-Type: application/json" --request PUT --data '{"contact":":234-223-8911"}' http://localhost:80/people/contact/daniel
curl --header "Content-Type: application/json"  http://localhost:80/people/contact/daniel
curl --header "Content-Type: application/json" --request DELETE  http://localhost:80/people/contact/daniel



curl --header "Content-Type: application/json"  "http://localhost:80/people/contact?pageSize=2&page=1&query=name%3Adaniel"
curl --header "Content-Type: application/json"  "http://localhost:80/people/contact?pageSize=2&page=1&query=contact%3A267"