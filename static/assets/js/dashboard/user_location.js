
	function UserLocation() {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(function(localizacion) {
				console.log(localizacion.coords);
				this.latitude = localizacion.coords.latitude;
				this.longitude = localizacion.coords.longitude;

				console.log(this.latitude);
			});
		}
		else {
			alert("Tu navegador no soporta el uso de mapas, por favor actualiza tu navegador.")
		}
	}
