

function changeCSS(newlink) {

    let sheet = document.getElementById('theme');

    sheet.href=newlink;
}

function changeCSS2()
{
    let sheet = document.getElementById('theme');
    const cssLink = document.querySelector('link[href="{% static "/css/Theme-2.css" %}"]');
    sheet.href=cssLink;
}

function ChangeCSS3()
{    let sheet = document.getElementById('theme');
    const cssLink = document.querySelector('link[href="{% static "/css/Theme-3.css" %}"]');
    sheet.href=cssLink;
}

function changeCSS4()
{    
    let sheet = document.getElementById('theme');
    const cssLink = document.querySelector('link[href="{% static "/css/Theme-4.css" %}"]');
    sheet.href=cssLink;
}

function changeCSS5()
{   
    let sheet = document.getElementById('theme');
    const cssLink = document.querySelector('link[href="{% static "/css/Theme-5.css" %}"]');
    sheet.href=cssLink;
}
