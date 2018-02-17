function load() {
	var mydata = JSON.parse(data);
	var table = document.getElementById("mytable");
	for(i = 0; i < 60; i++) {
		var ins = table.insertRow(i + 1);
		var cell1 = ins.insertCell(0);
		var cell2 = ins.insertCell(1);
		var cell3 = ins.insertCell(2);
		var cell4 = ins.insertCell(3);
		var cell5 = ins.insertCell(4);
		
		cell1.innerHTML = mydata[i].tempC;
		cell2.innerHTML = mydata[i].light;
		cell3.innerHTML = mydata[i].envelope;
		cell4.innerHTML = mydata[i].tempF;
		cell5.innerHTML = mydata[i].humidity;
	}
}