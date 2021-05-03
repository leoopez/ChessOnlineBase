'use strict'

document.querySelector(".nav_link").addEventListener('click',   function() {
    document.querySelector(".nav_link").href=document.querySelector(".url_value").value;
    return false;
});