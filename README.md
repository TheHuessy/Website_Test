# Website_Test
A repo for me to slowly teach myself JavaScript, HTML, and CSS to build a website for myself. The goal is to create something that will link to Google Calendar API, allowing me to share when I am booked on comedy shows

## NOTES

### Implementation

The goal will be to use [Netlify](https://www.netlify.com/) to host, meaning that you need to have all data in a git repo. It is unclear whether or not it keeps pulling the repository on a regular basis or if one has to manually trigger it to update. Assuming it's the former, you will need to set up an automated job to:
 * Run the Python you already have to pull your data from the google API 
 * Have it generate a json (or csv or whatever is easiest to load in JS) file with all needed data
     * A job that runs each day would help keep things 'up to date'
 * Pull/push that file to github after it's been loaded

You could do all of that on the Pi server you have!

### Things left to do:

 * Go in and add '#comedy' or something similar to all comedy related events going forward
 	* Want to be able to easily identify the event
 * Rewrite Python to parse calendar data differently
     * Grab dates you DO have events
     * Get the following fields:
     	* Show Name
     	* Show Date
     	* Show Start Time
     	* Show Cost
     	* Show Location
     * With show location, see what sort of geocoding/google place API stuff you can do
 * Write Snippet of JS that reads either JSON or CSV data and presents it
 	* Worry about format later, I'm sure there will be a CSS method to prettify things