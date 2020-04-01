# https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html#completion-suggester
# dev script on Kibana dev to test autocompletion  

DELETE title
PUT title
{
    "mappings": {
        "properties" : {
            "suggest" : {
                "type" : "completion"
            },
            "title" : {               #still works without title field
                "type": "keyword" 
            }
        }
    }
}

# all job tites can NOT be stored in one _doc

PUT music/_doc/1?refresh
{
    "suggest" : {
        "input": [ "Data Engineer"]
    }
}

PUT music/_doc/2?refresh
{
    "suggest" : {
        "input": [ "Data scientist"]
    }
}

POST music/_search?pretty
{
    "suggest": {
        "song-suggest" : {
            "prefix" : "dat", 
            "completion" : { 
                "field" : "suggest" 
            }
        }
    }
}




