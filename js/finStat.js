var search = document.getElementById("search");

search.addEventListener("click", function(){
    var code = document.getElementById("code").value;
    if(!code){
      code = "AAPL";
    }
    var show = document.getElementById("show").value;
    var url = "cgi-bin/scraper/financialStatement_yahoo.py?code=" + code + "&show=" + show;
    window.open(url);
});
