var search = document.getElementById("search");

search.addEventListener("click", function(){
    var option = document.getElementById("show");
    var secondCode = document.getElementById("secondCode");

    // dashboard
    if(option.style.display!='none'){
      var code = document.getElementById("code").value;
      if(!code){
        code = "AAPL";
      }
      var show = document.getElementById("show").value;
      var url = "cgi-bin/scraper/financialStatement_yahoo.py?code=" + code + "&show=" + show;
      window.open(url);
    }

    // compare
    else if(secondCode.style.display!='none'){
      console.log("COMPARE");
      var code = document.getElementById("code").value;
      if(!code){
        code = "AAPL";
      }
      var secondCode = document.getElementById("secondCode").value;
      if(!secondCode){
        secondCode = "GOOG";
      }
      sessionStorage.setItem("code", code);
      sessionStorage.setItem("secondCode", secondCode);
      var url = "cgi-bin/algo/prob_compare.py";
      window.open(url);
    }

    // analysis
    else if(secondCode.style.display=='none' && option.style.display=='none'){
      console.log("ANALYSIS");
      var code = document.getElementById("code").value;
      if(!code){
        code = "AAPL";
      }
      // var secondCode = document.getElementById("secondCode").value;
      // if(!secondCode){
      //   secondCode = "GOOG";
      // }
      sessionStorage.setItem("code", code);
      // sessionStorage.setItem("secondCode", secondCode);
      var url = "cgi-bin/algo/prob_predict.py";
      window.open(url);
    }

});
