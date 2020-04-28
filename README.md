# Rest-API-with-Flask-Development-and-Testing

#Development

The task_1.py will walk you through how to create a rest api using falsk.
In this demo, we have made use of a config file with a sample data of cisco 
router configurations.

The data is parsed using the ciscoconfparse module and is served over a rest api.
The service is prey straight forward and will have the following routes 
  GET /interface/all/ will return all interface blocks.
  GET /interface/<name> will return info for a parcular block who’s name matches the text passed in <name>.


#Testing

The task_2.py will help you understand how we made use of http.clinet library
to connect to the above webservice by making requests to the routes 
   - /interface/all/ 
   - /interface/<name>
  
The obtained response is then displayed in the form of an ascii table.
