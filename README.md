Project Group 5, Section 2
UNIs: [df2761,ty2418]
The link to the server running our application is:
https://tools1-255501.appspot.com/


#Summary:
Maplot is an app created to edit and view detailed information of each squirrel that was part of the central park squirrel census carried out in 2018, as well as to register new squirrel sightings. Its functionality also includes a map view with the location of 100 registered sightings of these animals and a view of certain stats of interest from the data gathering.

#Description:
In order to perform the squirrel tracker app, we import the squirrel census data of 2018 into our database. The application has 6 page views, which are:

1) / sightings: Shows the complete list of squirrels in the database, along with links to add, edit and view detailed information of a squirrel

2) / sightings / map: which displays 100 squirrel locations in the central park, using the Latitude and Longitude attributes of these sightings

3) / sightings / add: form view that allows you to add a new squirrel in the database db.mysql3
 
4) / sightings / <Unique_Squirrel_ID>: Displays the form of a squirrel already created to edit its information

5) / sightings / <Unique_Squirrel_ID> / details: shows the detailed information of each squirrel, along with a link to edit in case you want to change the information

6) / sightings / stats: Shows stats of certain squirrel attributes, which are the following: total amount of sightings, amount of juvenile squirrels, amount of running squirrels, amount of squirrels with moans, amount of indifferent squirrels.

