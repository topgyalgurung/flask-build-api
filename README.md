
## RUNNING FLASK
- flask --app server run --debug run

### TEST THE ENDPOINT WITH CURL COMMAND
 curl -X GET -i -w '\n' localhost:5000/no_content 
 curl -X GET -i -w '\n' localhost:5000/data
 curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
 curl -X GET -i -w '\n' "localhost:5000/name_search"
 curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty" 

