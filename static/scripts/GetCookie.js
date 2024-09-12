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
            return window.location.href = "/Home";
        }
    }
    return "";
}

function getCookieHome(cname){
    let name = cname + "=";
    let decodedCookie= decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(";");
    for(let i=0; i<ca.length; i++){
        let c = ca[i];
        while(c.charAt(0)==' '){
            c = c.substring(1);
        }
        if (c.indexOf(name)==0){
            return "";
        }
    }
    return window.location.href = "/Login";
}

