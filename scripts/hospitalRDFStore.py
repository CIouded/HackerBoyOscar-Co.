import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF


g = Graph()

result = g.parse("http://dbpedia.org/resource/Tim_Berners-Lee")

for subj, pred, obj in g:
    if(subj, pred, obj) not in g:
        raise Exception("Better be a triple thre... BITCH")


s = g.serialize(format="n3")
