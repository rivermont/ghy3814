var map = L.map('map', {center: [36.21593, -81.68268], zoom: 17});

L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var rsw = L.marker([36.214039, -81.681719]).addTo(map);

var coffee = L.polygon([[36.218060, -81.684023],[36.218112, -81.683971],[36.218077, -81.683912],[36.218034, -81.683960]]).addTo(map);

var route = L.polyline([[36.214314, -81.681692],[36.215239, -81.682050],[36.215721, -81.682489], [36.216385, -81.683184], [36.216900, -81.682599],[36.217805, -81.684187], [36.218047, -81.683998]]).addTo(map);

coffee.bindPopup("Espresso News").openPopup();
rsw.bindPopup("Rankin Science West");
