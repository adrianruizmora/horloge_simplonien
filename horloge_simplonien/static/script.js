var timeTitle = document.getElementById("time-title")

        const Http = new XMLHttpRequest()
        const url = 'http://127.0.0.1:5000/clock';

        setInterval(function(){
            Http.open("GET", url);
            Http.send()
        }, 1000);

        Http.open("GET", url);
        Http.send();

        Http.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                timeTitle.textContent = Http.responseText
            }
        }
