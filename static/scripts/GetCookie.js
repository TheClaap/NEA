function getCookieLog(){
    let name = "Id" + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(";");
    for(let i =0; i<ca.length; i++){
        let c = ca[i];
        while(c.charAt(0) == ' '){
            c= c.substring(1);
        }
        if (c.indexOf(name)==0){
            return window.location.href = "/Home/"+c.substring(3);
        }
    }
    return "";
}

function getCookieHome(id){
    let name = "Id" + "=";
    let decodedCookie= decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(";");
    let c =ca[0]
    if (0<c.length){
        if (Number(c.substring(3))!=id){
            return window.location.replace("/Home/"+Number(c.substring(3)))
        }
        else{
            return ""
        }
    }else{
        return window.location.replace("/Login");
    }
}