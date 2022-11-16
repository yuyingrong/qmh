
var data = [//somehow loop traces]

loop(get_json)

var traces = {};// a list of trace items

function loop(point) {
	var i;
	for(i = 0; i < point.length; i++) {
		var trace += {//???? an item in the list "trace"
			x: point.x,
			y: point.y,
			name: point.name,
			mode: 'markers',
			type: 'scatter',
			text: point.y,
			marker: {size: 5}
		}
	};
}







myFunction(myArray);

function myFunction(arr) {
  var out = "";
  var i;
  for(i = 0; i < arr.length; i++) {
    out += '<a href="' + arr[i].url + '">' + 
    arr[i].display + '</a><br>';
  }
  document.getElementById("id01").innerHTML = out;
}


