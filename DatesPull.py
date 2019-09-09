from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import datetime
import re
from calendar import monthcalendar as mc

##############################
######GETTING ALL EVENTS######
##############################

cols = ["Show_Name",
"Show_Date",
"Show_Day",
"Show_Month",
"Show_Year",
"Show_Start_Time",
"Show_Venue_Name",
"Show_Street_Address",
"Show_City",
"Show_State",
"Show_Zip",
"Show_Country",
"Ticket_Link"]


termine = pd.DataFrame({"Show_Name":[],
                        "Show_Date": [],
                        "Show_Day": [],
                        "Show_Month": [],
                        "Show_Year": [],
                        "Show_Start_Time": [],
                        "Show_Venue_Name": [],
                        "Show_Street_Address": [],
                        "Show_City": [],
                        "Show_State": [],
                        "Show_Zip": [],
                        "Show_Country": [],
                        "Ticket_Link": []}
                      )

 ## SCOPES AND CREDENTIAL LOCATION CODING
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = '/home/james/Documents/PythonNotebooks/Calendar API/calendar.json'
##SERVICE_ACCOUNT_FILE = '/home/pi/Documents/calendar.json'

## BUILDING CREDENTIAL OBJECT
print("BUILDING CREDENTIAL OBJECT")
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

## CREATING API SERVICE INSTANCE
print("CREATING API SERVICE INSTANCE")
service = build('calendar', 'v3', credentials=credentials)

## CALLING ALL EVENTS FOR THE CALENDAR FOR JAMESHUESSY@GMAIL.COM
print("CALLING ALL EVENTS FOR THE CALENDAR FOR JAMESHUESSY@GMAIL.COM")
t_now = datetime.datetime.utcnow()

d = service.events().list(calendarId='jameshuessy@gmail.com', 
                            timeMin=t_now.isoformat()+'Z'
                             )
### Calling 'execute()' is how you make the api call
dd = d.execute()

## Parsing into dataframe
print("Parsing into dataframe")
try:
    events = pd.DataFrame(dd['items'])
except Exception as err:
    print("Couldn't get items into the dataframe\nError: {}".format(err))
else:
    print("Done!")


for i in range(len(events)):
    tst = events.description[i]
    if isinstance(tst, float):
        continue
    elif '#comedy' in tst:
        # Get manually entered ticket link from description if it's there
        tkt_link_chk = tst.split("\n")
        tkt_link = [x for x in tkt_link_chk if 'http' in x]
        if tkt_link:
            tkt_link = tkt_link.pop()
        else:
            tkt_link = None        
        
        ## Getting the event ID
        e_id = events.id[i]
        ## Getting more detailed event data
        e_data = service.events().get(calendarId='jameshuessy@gmail.com', eventId=e_id).execute()
        
        ## Show Name
        e_name = e_data['summary']
        
        ## Show Location
        try:
            e_loc = e_data['location'].split(", ")
        except:
            e_loc = "TBA"
            print(e_name)        
        if 'TBA' not in e_loc:
            if "730 Tavern" in e_loc:
                ## This is a terrible solution, but I'm lazy for the time being
                ## if more venues have commas in their names, then I will have to 
                ## actually try to build something that can handle it with regex
                loc_venue_name = "{} {}".format(e_loc[0], e_loc[1])
                loc_street_address = e_loc[2]
                loc_city = e_loc[3]                
                loc_state = e_loc[4].split(" ")[0]
                loc_zip = e_loc[4].split(" ")[1]
                loc_country = e_loc[5]
            else:
            ## Create all vars            
                ## It looks like it follows the same pattern:
                ## [0] = Establishment Name
                ## [1] = Street Address
                ## [2] = City/Town
                ## [3] = State+Zip
                ## [4] = Country
                loc_venue_name = e_loc[0]
                loc_street_address = e_loc[1]
                loc_city = e_loc[2]
                loc_state = e_loc[3].split(" ")[0]
                loc_zip = e_loc[3].split(" ")[1]                
                loc_country = e_loc[4]
        else:
            ## Leave the vars null
            loc_venue_name = "TBA"
            loc_street_address = None
            loc_city = None
            loc_state = None
            loc_zip = None
            loc_country = None
        
        ## Show DatTime
        e_dat_date = e_data['start']['dateTime']
        e_dat_date = re.sub(pattern=":00-.*", repl="", string= e_dat_date)
        e_dat_date = datetime.datetime.strptime(e_dat_date, '%Y-%m-%dT%H:%M')
        e_dat_date_year = int(e_dat_date.year)
        e_dat_date_month = e_dat_date.strftime("%B")
        e_dat_date_day = int(e_dat_date.day)
        
        ## Show Date
        e_date = e_dat_date.strftime("%x")
        
        ## Show Start Time
        e_start = e_dat_date.strftime("%I:%M %p")
        
        loader = pd.DataFrame({"Show_Name":[e_name],
                               "Show_Date": [e_date],
                               "Show_Day": [int(e_dat_date_day)],
                               "Show_Month": [e_dat_date_month],
                               "Show_Year": [e_dat_date_year],
                               "Show_Start_Time": [e_start],
                               "Show_Venue_Name": [loc_venue_name],
                               "Show_Street_Address": [loc_street_address],
                               "Show_City": [loc_city],
                               "Show_State": [loc_state],
                               "Show_Zip": [loc_zip],
                               "Show_Country": [loc_country],
                               "Ticket_Link": [tkt_link]})
        termine = termine.append(loader)

termine['Show_Day'] = pd.to_numeric(termine['Show_Day'], downcast='integer')
termine['Show_Year'] = pd.to_numeric(termine['Show_Year'], downcast='integer')
termine = termine.sort_values(by=['Show_Date', 'Show_Start_Time'], axis=0)

termine.to_csv("/home/james/Documents/JavaScript/Data/dates.csv", 
# termine.to_csv("/home/pi/Documents/Website_Test/Data/dates.csv", 
    index=False,
    columns=cols
    )

print("Done")
