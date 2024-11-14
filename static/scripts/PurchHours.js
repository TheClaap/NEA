function addHrs(hours){
    cookie = decodeURIComponent(document.cookie)
    $.ajax({
        type: "POST",
        url: "/BuyHours/"+(cookie.substring(3)),
        data: {"hrs":hours,"id":cookie.substring(3)},
        success: function (response) {
            window.location.assign("/Confirm/"+cookie.substring(3))
        }, error(response){
            console.log(response)
        }
    });
}