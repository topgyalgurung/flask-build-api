
## RUNNING FLASK
- flask --app server run --debug run

### TEST THE ENDPOINT WITH CURL COMMAND
 - curl -X GET -i -w '\n' localhost:5000/no_content
 - curl -X GET -i -w '\n' localhost:5000/data
 - curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
 - curl -X GET -i -w '\n' "localhost:5000/name_search"
 - curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty" 

- curl -X GET -i -w '\n' "localhost:5000/count"
- curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
- curl -X GET -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
