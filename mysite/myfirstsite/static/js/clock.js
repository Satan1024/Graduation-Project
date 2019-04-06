var canvas = document.getElementById("canvas");
		var ctx = canvas.getContext("2d");
		ctx.strokeStyle = '#00ffff';
		ctx.lineWidth = 5;
		ctx.shadowBlur= 4;
		ctx.shadowColor = '#00ffff'

		function degToRad(degree){
			var factor = Math.PI/180;
			return degree*factor;
		}

		function renderTime(){
			var now = new Date();
			var today = now.toDateString();
			var time = now.toLocaleTimeString();
			var hrs = now.getHours();
			var min = now.getMinutes();
			var sec = now.getSeconds();
			var mil = now.getMilliseconds();
			var smoothsec = sec+(mil/1000);
      var smoothmin = min+(smoothsec/60);

			//Background
			gradient = ctx.createRadialGradient(100, 100, 100, 100, 100, 60);
			gradient.addColorStop(0, "#1b1f22");
			gradient.addColorStop(1, "black");
			ctx.fillStyle = gradient;
			//ctx.fillStyle = 'rgba(00 ,00 , 00, 1)';
			ctx.fillRect(0, 0, 200, 200);
			//Hours
			ctx.beginPath();
			ctx.arc(100,100,95, degToRad(270), degToRad((hrs*30)-90));
			ctx.stroke();
			//Minutes
			ctx.beginPath();
			ctx.arc(100,100,80, degToRad(270), degToRad((smoothmin*6)-90));
			ctx.stroke();
			//Seconds
			ctx.beginPath();
			ctx.arc(100,100,60, degToRad(270), degToRad((smoothsec*6)-90));
			ctx.stroke();
			//Date
			ctx.font = "10px Helvetica";
			ctx.fillStyle = 'rgba(00, 255, 255, 1)'
			ctx.fillText(today, 70, 120);
			//Time
			ctx.font = "10px Helvetica Bold";
			ctx.fillStyle = 'rgba(00, 255, 255, 1)';
			ctx.fillText(time+":"+mil, 70, 100);

		}
		setInterval(renderTime, 40);