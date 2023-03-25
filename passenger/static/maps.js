var input1 = document.getElementById("from");
var autocomplete1 = new google.maps.places.Autocomplete(input1, {
  componentRestrictions: {
    'country': ['US'.toLowerCase()]
  }
});

var input2 = document.getElementById("to");
var autocomplete2 = new google.maps.places.Autocomplete(input2, {
  componentRestrictions: {
    'country': ['US'.toLowerCase()]
  }
});

var show_search = document.querySelectorAll("#ways");
var autocomplete = new google.maps.places.Autocomplete(show_search, {
  componentRestrictions: {
    'country': ['US'.toLowerCase()]
  }
});

// trying to fix the waypoints 
// way points end here

//javascript.js
//set map options
var myLatLng = {
  lat: 31.485142148563558,
  lng: -99.25451773100981
}; //  38.346,   -0.4907
var mapOptions = {
  center: myLatLng,
  zoom: 8,
  mapTypeId: google.maps.MapTypeId.ROADMAP,
};

//create map
var map = new google.maps.Map(document.getElementById("maps_di"), mapOptions);

//create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

//create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

//bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);

//define calcRoute function
function calcRoute() {

  // waypoints 
  const waypts = [];
  const checkboxArray = document.querySelectorAll("#ways");

  for (var i = 0; i < checkboxArray.length; i++) {
    // if (checkboxArray.value) { }
      waypts.push({
        location: checkboxArray.value,
        stopover: true,
      });
   
  }

  toastr.info(waypts);

  // waypoints 
  //  var wypts = []
  //  var checkarray = document.getElementById('way_p')
  //  for (var i = 0; i < checkarray.length; i++ ){
  //      if (checkarray.value ) {
  //          wypts.push ({
  //              location:checkarray[i].value,
  //              stopover:true
  //          });
  //      }
  //  }
  //create request
  var request = {
    origin: document.getElementById("from").value,
    destination: document.getElementById("to").value,
    waypoints: waypts, //waypts
    optimizeWaypoints: true,
    travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
    unitSystem: google.maps.UnitSystem.IMPERIAL,
    //waypoints: wypts,
    //intermediates:document.getElementById("way_p").value,
    //optimizeWaypoints: true,
  };

  //pass the request to the route method
  directionsService.route(request, function (result, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      //Get distance and time
      const output = document.querySelector("#output");
      output.innerHTML = "<div class='alert-info'>From: " + document.getElementById("from").value + ".<br />To: " + document.getElementById("to").value + ".<br /> Driving distance <i class='fas fa-road'></i> : " + result.routes[0].legs[0].distance.text + ".<br />Duration <i class='fas fa-hourglass-start'></i> : " + result.routes[0].legs[0].duration.text + ".</div>";

      //display route
      directionsDisplay.setDirections(result);

      var res = result.routes[0].legs[0].distance.text.replace(/,/gi, '')
      var input_distance = document.getElementById('distance')
      var dist = parseFloat(res)
      input_distance.value = dist

      console.log(parseFloat(res))
    } else {
      //delete route from map
      directionsDisplay.setDirections({
        routes: []
      });
      //center map in London
      map.setCenter(myLatLng);

      //show error message
      output.innerHTML =
        "<div class='alert-danger'><i class='fas fa-exclamation-triangle'></i> Could not retrieve driving distance.</div>";
    }
  });

}



//text(directionsResult.