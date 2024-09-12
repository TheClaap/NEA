function makeCookieLogged(){
const d = new Date();
d.setTime(d.getTime() + (5*24*60*60*1000));
let expires = "expires="+ d.toUTCString();
document.cookie = "logged=True;SameSite=None; Secure;" + expires;
makeCookieId();
}

function makeCookieId(){
    $.ajax({
        method: "GET",
        url: '/id',
        success: (function(id){
            const d = new Date();
            d.setTime(d.getTime() + (5*24*60*60*1000));
            let expires = "expires="+d.toUTCString();
            document.cookie = "Id=" + id + ";SameSite=None; Secure;" + expires;
            window.location.replace("/Home");
        })
    });
}