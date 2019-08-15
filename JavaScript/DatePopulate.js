//this was modified from this: https://www.jqueryscript.net/table/jQuery-Plugin-To-Generate-A-Table-From-A-CSV-File-CSV-Parser.html
$.get('https://raw.githubusercontent.com/TheHuessy/Website_Test/master/dates.csv', function(data) {
// start the table
var html = '';

// split into lines
var rows = data.split("\n");

// parse lines
rows.forEach(function getvalues(ourrow) { 				



// split line into columns
if (ourrow == rows[0]){
	return;
	}
if (ourrow == rows[0]){
	return;
	}
else {

	// Show_Name = [0]
	// Show_Date = [1]
	// Show_Day = [2]
    // Show_Month = [3]
    // Show_Year = [4]
	// Show_Start_Time = [5]
	// Show_Venue_Name = [6]
	// Show_Street_Address = [7]
	// Show_City = [8]
	// Show_State = [9]
	// Show_Zip = [10]



	//Create split row variable
	var columns = ourrow.split(",");
		
		//catch undefined last row which seems to be an issue with this parser
		//it returns a final row after the last row, so we just skip it if it sees it
	if (columns[1] == null){
	return;
}

	html += '<div class="Show_Box">';
		//Get show date, show name, and time

		var date_full = columns[3] + ' ' + columns[2]

		//Evaluate if the date has already been added
		//If it hasn't, create the ShowDate line, otherwise just create the show info block and keep going
		if(html.indexOf(date_full) <= 0){
			html += '<h2 class="show_date">' + columns[3] + ' ' + columns[2] + '</h2><hr width="75%"> ';

			
		}				
	
	//Get show name and time if available, else just print the show name
	if (columns[2] != "??"){
		html += '<h3 class="show_name_time">' + columns[0] + ' | ' + columns[5] + '</h3>';
	} else{
		html += '<h3 class="show_name_time">' + columns[0] + '</h3>';
	}

	//Get and combine show venue name, if not present/=TBA, then just pass "TBA"
	if (columns[6] == "TBA"){

		html += '<h5 class="show_add">' + columns[6] + '</h5>';

	} else {

		html += '<h5 class="show_add">' + columns[6] + '<br>' + columns[7] + '<br>' + columns[8] + ', ' + columns[9] + '</h5>';
	
	}
}
// close div
html += "</div>";
})

// close div
html += "</div><br>";

// insert into div
$('#Shows').append(html);
});