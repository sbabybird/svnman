$(document).ready(function() {
		drawcanvas($('#canv')[0]);
		});

function drawcanvas (canvas) {
	var ctx = canvas.getContext("2d");
	var w = canvas.attributes.width.value;
	var h = canvas.attributes.height.value;
	ctx.fillStyle = "rgb(0,0,0)";
	ctx.fillRect(0, 0, w, h);
	var imgdata = ctx.getImageData(0, 0, w, h);
	var pixels = imgdata.data;
	var i = 0;
	for (var y = 0; y < h; y++)
		for (var x = 0; x < w; x++) {
			var b = parseInt(x/16)%2 == 0 ? 255:0;
			if (parseInt(y/16)%2 == 0) b = b==0 ? 255:0;
			pixels[i++] = b;
			pixels[i++] = b;
			pixels[i++] = b;
			pixels[i++] = 255; //透明度
		}
	ctx.putImageData(imgdata, 0, 0);
}

