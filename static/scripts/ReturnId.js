function GetId(){
    let cookie = decodeURIComponent(document.cookie)
    let id = cookie.split(";")
    id = id[0]
    return id.substring(3)
}

function retHours(){
    let id = GetId()
    $.ajax({
        type: "POST",
        url: "/id",
        data: {"Id":id},
        success: function (response) {
            if(response=="False"){
                console.log(response);
            } else{
                console.log(response);
                document.getElementById("Hourtxt").innerHTML.replace(response)
            }
        }, error(){
            console.log()
        }
    });

}