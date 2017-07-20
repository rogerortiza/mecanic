class Map {
	constructor()	{
		this.defaultLocation = false;
		this.markerImage = "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
		this.myLatLng = {	lat: 21.8853,	lng: -102.2916};
	};

	userLocation()	{
		let classObj = this;
		return new Promise(function (resolve, reject,	obj = classObj) {
			if (navigator.geolocation && obj.defaultLocation == false) {
				navigator.geolocation.getCurrentPosition(function(	response)	{
					resolve({lat: response.coords.latitude, lng: response.coords.longitude});
				});
			}	else {
					resolve(obj.myLatLng);
			}
		});
	};

	initMap(	objID = "map",	defaultLocation = false)	{
		this.defaultLocation = defaultLocation;
		this.userLocation()
			.then((response)	=>	{
				this.myLatLng = response;
				/*	google.maps.event.addDomListener(window, 'load', function() {});	*/
				const mapOptions = {
					zoom : 13,
					center : this.myLatLng
				};
				const mapa_elemnt =  document.getElementById(	objID);
				const mapa = new google.maps.Map(mapa_elemnt, mapOptions);
				const marker = new google.maps.Marker({
					map : mapa,
					position : this.myLatLng,
					title: 'Hello World!',
					icon : this.markerImage,
	          		animation: google.maps.Animation.DROP
				});
			})
			.catch((error)		=>	{
				console.log(	error)
			});
	};
};
