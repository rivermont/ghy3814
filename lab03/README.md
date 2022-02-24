## Lab 03&emdash;Optimal Birding Routes

This map shows a driving route between Durham, North Carolina and Boone, North Carolina, and highlights optimal birding locations (hotspots) along the route.
The optimal hotspots are both close to the main route and have high species totals.

The map is built with the [Leaflet](https://leafletjs.com) library, using the National Geographic World Map tile layer provided by Esri (which is notably out of date).
The route data was derived from a Google Maps route.
The hotspot information is taken from [eBird](https://ebird.org), a citizen science project that records bird sightings.

The map code is written in Javascript, while the rest of the page is in HTML.
The data for the route and hotspots is loaded from local JS files.
For each hotspot, the a tooltip is attached to the map with the name of the hotspot, and a a popup is attached with a description containing the number of species and a link to eBird.

