**Natural Event Tracker**

*Destination and description of the project:*

The destination of the project was to create an application to track fires, storms, volcanic eruptions and other natural events based on information from the NASA API. The application generates map with markers that shows where in a particular place there is an current natural event in the world. "Current"  means only this events that have not ended until the program starts. There is an additional option to filter events based on their categories. Filter menu contains only a set of non-repeating event categories on the map.

*Program division into classes:*

The main part of the application (natural\_event\_tracker.py file) consists of:

1) methods to retrieve event information from the NASA Eonet site, 
1) an Event class that when downloading information using the previous method gives the opportunity to create event data objects and delivery to the user only the most necessary information about the event, such as a category, short description and geographical location on the map, 
1) Map class, which can create a map object, add tags and filtering to it, saving to a separate html file and display this map in the user's browser.

*User Manual:*

Basic steps to make the application work:

1) You must have version 3+ of Python downloaded. 
1) You need to install additional python libraries by typing in the terminal commands: 
   1. pip install requests
   1. pip install folium
1) To run the program, open the src folder in the terminal and then enter the command:
   1. python visualization.py

This will create a filemap.html in the main folder of application and display the

map in the browser. Markers are reflecting the exact location of the event. After clicking the marker, a short description is shown above it. You can freelymove with the mouse and zoom in and out with the option "+" and "-" in the upper left corner. Under the zoom option is locate a filtering option. When you click that, it will display the categories of events on the map. After selecting a category, only those tags that display the same category will be shown.

*Personal opinion part:*

I am satisfied with the scope of work done. All the tasks that I set myself are fulfilled. The hardest for me turned out efficient use of the methods offered by the folium library. I spent most of my time looking for a possibility to add filter option to map.

![](Aspose.Words.e768bd2e-9217-44b6-95d8-d3e6a4639ba2.001.png)





