
 var time = 3600;
  setInterval(function() {
    if(time > 0) {
    document.getElementById("timecounter").innerHTML = "You will be redirected in "
    + time + " seconds. If you do not complete the payment your order will be deleted";
    time--;
    console.log(time)
    } else {
      location.href="/" //this will redirect to your index
    }

  },1000)