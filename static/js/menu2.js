/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function test() {
	event.stopPropagation();
	document.getElementById("myBrain").classList.toggle("show2");
 }

// Close the dropdown if the user clicks outside of it
// Close the dropdown menu if the user clicks outside of it
	window.onclick = function(event) {
    document.getElementById("myBrain").classList.remove("show2");
}