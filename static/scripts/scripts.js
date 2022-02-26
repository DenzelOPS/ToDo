function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function MarkAsDone(e){
    var element = document.getElementById(e);
    var token = getCookie('csrftoken');
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.pathname, false);
    xhr.setRequestHeader('X-CSRFToken', token);       
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.send(JSON.stringify({"id":e}));
    document.location.reload();
};
function SaveText(e){
    var token = getCookie('csrftoken');
    var text_id = 'text_'+e.toString()
    var element = document.getElementById(text_id);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.pathname, false);
    xhr.setRequestHeader('X-CSRFToken', token);       
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.send(JSON.stringify({"text_id":e,"text":element.innerHTML}));
    document.location.reload();
};

function SaveOrder(e){
    document.cookie = "order="+e.toString();
    window.location.href = window.location.href
};
localStorage.setItem('logout-event', 'logout');
function Logout(){
localStorage.setItem('logout-event', 'logout' + Math.random());
};
window.addEventListener('storage', function(event){
    if (event.key == 'logout-event') { 
        setTimeout(function(){window.location.reload();},10);
    }
});