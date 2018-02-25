/**
 * Created by KlaraMariaDersche on 23.02.18.
 */


var express = require('express')
var app = express()


// This setting tells express that we use handlebars as our view engine.
app.set("view engine", "hbs")


app.get('/', function(request, response){
    response.render('index.hbs')
})

app.get('/test', function(request, response){
    response.end("It's working!")
})

app.listen(3000, () => console.log('My website is listening on port 3000!'))


//Code for query other endpoints - simple query to get height of eiffel tower
var fetch = require('isomorphic-fetch')
var SparqlHttp = require('sparql-http-client')
SparqlHttp.fetch = fetch

var endpoint = new SparqlHttp({endpointUrl: 'http://dbpedia.org/sparql'})
//actual query
var query = 'SELECT ?height ' +
    'WHERE { <http://dbpedia.org/resource/Eiffel_Tower> <http://dbpedia.org/property/height> ?height }'

/*example query
var query = 'select distinct ?Concept where {[] a ?Concept} LIMIT 5'
 */

// run query with promises
endpoint.selectQuery(query).then(function (res) {
    return res.json()
}).then(function (result) {
    console.log(result.results.bindings)
}).catch(function (err) {
    console.error(err)
})
