var menuitem = 0;

// open hidden layer
function menu_open(id)
{	
	// close old layer
	if(menuitem) menuitem.style.visibility = 'hidden';

	// get new layer and show it
	menuitem = document.getElementById(id);
	menuitem.style.visibility = 'visible';

}
// close showed layer
function menu_close()
{
	if(menuitem) menuitem.style.visibility = 'hidden';
}

// close layer when click-out
document.onclick = menu_close; 