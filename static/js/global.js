const topNav = document.querySelector(".top-navigation-section");
        
if(window.location.href == "http://127.0.0.1:8000/register") {
    topNav.classList.add("displayAsNone");
}
else if (window.location.href == "http://127.0.0.1:8000/login") {
    topNav.classList.add("displayAsNone");
} 
