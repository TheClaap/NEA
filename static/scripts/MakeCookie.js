function makeCookieId(){
    var id = $('#identification').data("value")
    const d = new Date();
    d.setTime(d.getTime() + (5*24*60*60*1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = "Id=" + id + ";SameSite=None; Secure;" + expires;
    window.location.replace("/Home/"+id);
}