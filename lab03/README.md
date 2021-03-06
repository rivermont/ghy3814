## Lab 03&#8212;Optimal Birding Routes

This map shows a driving route between Durham, North Carolina and Boone, North Carolina, and highlights optimal birding locations (hotspots) along the route.
The optimal hotspots are both close to the main route and have high species totals.

The map is built with the [Leaflet](https://leafletjs.com) library, using the National Geographic World Map tile layer provided by Esri (which is notably out of date).
The route data was derived from a Google Maps route.
The hotspot information is taken from [eBird](https://ebird.org), a citizen science project that records bird sightings.

The map code is written in Javascript, while the rest of the page is in HTML.
The data for the route and hotspots is loaded from local JS files.
For each hotspot, the a tooltip is attached to the map with the name of the hotspot, and a a popup is attached with a description containing the number of species and a link to eBird.

<!--
In this third lab, I learned how to use Leaflet to create an online interactive slippy map. I learned how to use different hosted raster tile layers to get a suitable look and feel to the map. I learned how to convert different data formats (gpx) to GeoJSON for use as layers in Leaflet. I used geojson.io to edit the raw JSON to add attributes to the data that can then be displayed on the map. For my data I used the results from a previous project that analyzed birding hotspots along a route. In the future I may use Leaflet to create interactive site maps for a professor in the Biology department. I already use Leaflet indirectly when editing my project using Mediawiki, as the maps extension uses Leaflet to display data. I also see Leaflet services whenever I edit OpenStreetMap, as both the website and main editor use Leaflet to serve tiles.
-->
