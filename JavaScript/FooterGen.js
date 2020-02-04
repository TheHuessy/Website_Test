
var today = new Date();

var year = today.getFullYear()

// build copyright statement
var html = '<a>Copyright ' + year + ' James Huessy</a>';


// insert into div
$('#footer').append(html);