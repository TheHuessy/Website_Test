# Website_Test
A repo for me to slowly teach myself JavaScript, HTML, and CSS to build a website for myself. The goal is to create something that will link to Google Calendar API, allowing me to share when I am booked on comedy shows

...And it works!

## NOTES

### Implementation

The goal will be to use [Netlify](https://www.netlify.com/) to host, meaning that you need to have all data in a git repo. It is unclear whether or not it keeps pulling the repository on a regular basis or if one has to manually trigger it to update. Assuming it's the former, you will need to set up an automated job to:
 * Run the Python you already have to pull your data from the google API 
 * Have it generate a json (or csv or whatever is easiest to load in JS) file with all needed data
     * A job that runs each day would help keep things 'up to date'
 * Pull/push that file to github after it's been loaded

You could do all of that on the Pi server you have!

### Things left to do:
 * Work on mobile version of site
     * first try using media queries to account for device size. [Ref](https://www.w3schools.com/css/css_rwd_mediaqueries.asp) [design ref](https://www.webmalama.com/the-best-full-screen-background-image-sizes-for-web-design/)
          * Decide on min/max size thresholds for the following display types
               * Phone (Android)
                    * Landscape
                    * Portrait
               * Phone (iPhone)
                    * Landscape
                    * Portrait
               * Tablet (Android)
                    * Landscape
                    * Portrait
               * Tablet (iPad)
                    * Landscape
                    * Portrait
          * Create 'mobile' versions of backgrounds and store them in appropriate folders under 'Pictures'
          * Decide on appropriate text sizes given a display type
          * Might be other element tinkering needed while testing on devices
     * It might just be worth it to rely on landscape for desktops and portorait for most mobile devices
          * that is, try to create backgrounds for landscape and portrait orientations and see if that works

 * Get ETL of dates data up and running
     * **FIGURE OUT WHY THE PI HAS DIED!!!!!!**
     * Currently running into github authentication problems in cron
          * [This](https://stackoverflow.com/questions/7548661/git-github-cant-push-to-master) link might help, the answer has you setting an origin which might be needed
               * that being said, if you can push in a non-cron environment, this may not solve the problem in a cron environment
                    * HOWEVER, you might want to try to add the origin setting command to the bash file for the fun of it
          * might need to switch to ssh instead of https for this job
               * figure out what sort of private public key pair you need to generate on the Pi to make that happen
          * Be sure to create the ssh credentials for the root user on the pi
               * it looks like that is a common problem as root runs cron in certain situations
     

### On hold for the time being:
 * Blog/Writing Page [?]
     * __Last Priority__
     * Basically set up a page that acts like a simple Medium page or something
          * Wouldn't be bad to at least give yourself the platform to write on
     * Develop some sort of python tool that you can feed copy into and it will populate the page at the right point
          * -OR- Just have a `.txt` file on the github page with a specific delineator that will allow a JS script to easily parse it to a div much like you did with the dates page.
 
 * Get some more, better, photos done
     * Ugh, paying people to click buttons is silly
     * Having good, recent photos is not silly



### Done:
 * ~~Go in and add '#comedy' or something similar to all comedy related events going forward~~
 	* ~~Want to be able to easily identify the event~~
 * ~~Rewrite Python to parse calendar data differently~~
     * ~~Grab dates you DO have events~~
     * ~~Get the following fields:~~
     	* ~~Show Name~~
     	* ~~Show Date~~
     	* ~~Show Start Time~~
     	* ~~Show Cost~~
     	* ~~Show Location~~
     * ~~With show location, see what sort of geocoding/google place API stuff you can do~~
     * ~~Generate test file for JS to point to~~
 * ~~Write Snippet of JS that reads either JSON or CSV data and presents it~~
 	* ~~Worry about format later, I'm sure there will be a CSS method to prettify things~~
 * ~~Home Server ETL Work~~
     * ~~__Securley__ transfer Google API credentials to home server~~
     * ~~Rewrite notebook script to `.py` file and set up cron job on PiNas~~
          * ~~Be sure to have it also perform git pushes when it's done~~
 * ~~Develop Design Scheme~~ It won't matter
     * ~~Monotone pallet is nice, but maybe venture into something a little more pleasing to others~~
     * ~~Get a font group figured out~~
          * ~~Not loving the standard times new roman or whatever it is~~
 * ~~Resize existing photos~~
     * ~~Bigger isn't better it would seem~~
          * ~~Need to find the best size for loading without looking like total garbage~~

 * ~~Create individual pages~~
     * ~~Upcoming Shows~~ [`dates.html`]
          * Using js to pull in google calednar api
     * ~~Home Page [`home.html`]~~
          * Bio
          * Selected Photos
               * Sarah Silverman
               * VCC
               * Studio
               * Highlarious
               * Lawyer Bros
          * Social Media Links [?]
               * Not really going to be impressive
     * ~~Tapes Page [`tapes.html`]~~
          * Pull in videos from Youtube
               * Looks like it should be prety straight forward with an `iframe`
               * Maybe only the most recent/submission ready one(s)
                    * Long one (10-12)
                    * Short one (3-5)
     * ~~Contact Page~~ [`contac.html`]
          * Maybe just a simple but CSS'd html form
               * Going to have to figure out the email/pop/stmp thing here
                    * Can't go google because they are stupid
               * Is it easy to create an email address if you already have a domain?
               * Best to probs 
     * ~~Develop a Parallax version of the site and see if you like that more~~
