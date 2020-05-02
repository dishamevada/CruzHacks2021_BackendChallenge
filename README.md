# CruzHacks2021_BackendChallenge

# How to Run:
Dependencies: Flask (pip install Flask) https://flask.palletsprojects.com/en/1.1.x/installation/
Run the command python main.py on one terminal, open a separate one to run curl commands

My URL is http://localhost:8085/getHackerInfo instead of http://[projectID].cloudfunctions.net/getHackerInfo with my endpoint being /getHackerInfo

Make sure to manually change the path on line 7 to match yours (I know in practice this is very very unsafe, but I had trouble working around it)

The authorization is not set up, so there is no need to pass in a token 

An example of a command that would work: 
curl -X GET -H "Content-Type:applicaton/json" http://localhost:8085/getHackerInfo -d '{"firstName": "John", "lastName": "Doe"}'

# My Design: 
I chose to identify my documents through this format "firstName lastName", so every command should have the fields firstName and lastName in the data. Cons of this design is that it is not uniquely identifiable, which would be not ideal in practical situations. If I were redesiging this, I would choose to identify my documents through an unique id number and have a different endpoint for each type of request (/putHackerData, /postHackerData)

For valid GET requests, I chose to return the content of the document instead of a status code and a message

# My Shortcomings: 
PUT does not fully work because it is unable to identify which document to update. I was trying to implement something like the following: curl -X GET -H "Content-Type:applicaton/json" http://localhost:8085/getHackerInfo -d "Jane Doe" '{"firstName": "John", "lastName": "Doe"}'
Where the first string after -d would be the document to update and the JSON string would be the values to update it with. Looking back, I think a better way of implementing this is to pass in the name of the document I wanted to update as a query paramter, like this http://localhost:8085/putHackerInfo?user=JaneDoe

The database does not enforce the restrictions of each field as outlined in the schema provided. 

Was unable to test with unit tests, but here are some of the scenarios I would have checked for

-GET with an existing document 
-GET with an non-existing document
-POST with data that follows the schema
-POST with data that does not follow the schema
-POST with data that already exists in the database
-PUT with an exisiting document
-PUT with an non-exisiting document
-creating duplicate documents and trying to retrieve them 
 
 In general, I would have also implemented classes in order for the data be to more well structured and easier to work with
  
# Lessons Learned: 
Don't wait until the last minute:)
