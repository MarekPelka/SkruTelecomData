<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple Polygon</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      // This example creates a simple polygon representing the Bermuda Triangle.

      function initMap() {


    	 var rightBottomX  = <c:out value="${rightBottomX}"/>;
    	 var rightBottomY  = <c:out value="${rightBottomY}"/>;
    	 var rightTopX  = <c:out value="${rightTopX}"/>;
    	 var rightTopY  = <c:out value="${rightTopY}"/>;
    	 var leftBottomX  = <c:out value="${leftBottomX}"/>;
    	 var leftBottomY  = <c:out value="${leftBottomY}"/>;
    	 var leftTopX  = <c:out value="${leftTopX}"/>;
    	 var leftTopY  = <c:out value="${leftTopY}"/>;
    	 
        var squareCoords = [
          {lat: rightBottomX, lng: rightBottomY},
          {lat: rightTopX, lng: rightTopY},
          {lat: leftTopX, lng: leftTopY},
          {lat: leftBottomX, lng: leftBottomY}
        ];
		
	  var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 5,
          center: square[0],
          mapTypeId: 'terrain'
        });

        // Define the LatLng coordinates for the polygon's path.


        // Construct the polygon.
        var square = new google.maps.Polygon({
          paths: squareCoords,
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.15
        });
        square.setMap(map);
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAXqSKCo1EO0qbi9RKwBHWlS2dHScscYKo&callback=initMap">
    </script>
  </body>
</html>