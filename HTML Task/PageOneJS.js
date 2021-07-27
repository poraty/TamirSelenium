const elem = document.createElement("div");
elem.setAttribute("id", "maccabi_logo");
elem.setAttribute("alt", "Image");
elem.setAttribute("class", "practice");
elem.style.backgroundImage = "url('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')";
elem.style.height = "200px";
elem.style.width = "100%";
elem.style.src = "http://automationpractice.com/img/p/1/1-thickbox_default.jpg";


function showGoogleLogo() {
    var myNode = document.getElementById("automationpractice_photo");
    while (myNode.firstChild != null) {
        myNode.removeChild(myNode.lastChild);
    }
    if (confirm("Do you wish the Google's logo to be shown?")) {
        setTimeout(function(){ myNode.appendChild(elem);
        document.getElementById("maccabi_logo").innerText = "maccabi_logo"}
        , 3000);
    }
}


function onloadFuc(){
    window.a = "jnk";
    window.b = "diffrent jnk";
}


function maccabi(){
    const myNode = document.getElementById("automationpractice_photo");
    myNode.appendChild(elem);
    document.getElementById("maccabi_logo").innerText = "Maccabi Logo";
    return window.a;
}



function showPreferredBackgroundImage(item) {
    var myNode = document.getElementById("automationpractice_photo");
    while (myNode.firstChild) {
        myNode.removeChild(myNode.lastChild);
    }

    var elem = document.createElement("div");
    elem.setAttribute("id", item);
    elem.setAttribute("alt", "Image");
    elem.style.height = "200px";
    elem.style.width = "100%";

    if (item == "Maccabi") {
        elem.style.backgroundImage = "url('https://1.bp.blogspot.com/-K0hjAVqrzP0/Xyc6Lua7tFI/AAAAAAABfig/E7ynl9hmb1Qz0XTm7gdlZ13H0mPl1k5xgCLcBGAsYHQ/s512/Maccabi%2BHaifa%2BFC.png')";
    } else if (item == "Google") {
        elem.style.backgroundImage = "url('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')";
    } else if (item == "Automation_Practice") {
        elem.style.backgroundImage = "url('http://automationpractice.com/img/p/1/1-thickbox_default.jpg')";
    }

    myNode.appendChild(elem);
    
    return item;
}