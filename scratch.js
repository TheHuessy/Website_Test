// Javascript test

document.bgColor="#288BE4"
document.fgColor="#f2f2f2"
document.write("This came from a seperate file that was called in HTML!\nTesting to see how it handles things like slash n to create a new line.\nHere's another one!")
document.write("Another .write element. You CAN specify at least the background and foreground color of things (is font considered foreground?) in javascript itself.")

var x=window.confirm("Would you like to enter?")

if (x)
	window.alert("You hit yes or okay!")
else
	window.alert("You hit cancel. I have no idea how to boot you. Just know you're booted!")

//confirm("Here's a confirm box added without the 'window.' at the beginning. As with alert, this has no conditional logic to it and I assume it will load after the alert because it is on the next line.")

//window.alert("A window.alert line which loads at the start of each page load. I assume that I can build in logic to make this appear after X condition. But for now here it is right when you enter.")


