setInterval(update_sensor, 1000);

function update_sensor() {
    $.ajax({
        url: "/sensor",
        method: "GET",
	contentType: "application/json",
	success: function(data) {
	    var resp = JSON.parse(data)
	    document.getElementById("temperature").innerHTML = resp.temp + " C";
	    document.getElementById("co2").innerHTML = resp.co2+ " PPM";
		document.getElementById("voc").innerHTML = resp.tvoc + " PPM";
	}
    })
};