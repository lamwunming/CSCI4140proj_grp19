<?php
    include 'dbh.php';
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="js\jquery-3.3.1.min.js"></script>
    <link rel="stylesheet" href="css\bootstrap.min.css">
    <link rel="stylesheet" href="css\dashboard.css">
    <script src="js\script.js"></script>
    <title>Dashboard</title>
    <script>

    function showandhide(id) {
      var dashb = document.getElementById('dashboard');
      var mysav = document.getElementById('mysave');
      var analy = document.getElementById('analysis');
      var compa = document.getElementById('compare');
      var repor = document.getElementById('report');

      var dive = document.getElementById(id);
      if(dive.id!='dashboard'){
        document.getElementById('show').style.display = 'none';
      }
      else{
        document.getElementById('show').style.display = 'block';
      }
      if(dive.id!='compare'){
        document.getElementById('secondCode').style.display = 'none';
      }
      else{
        document.getElementById('secondCode').style.display = 'block';
      }

      dashb.style.display = 'none';
      mysav.style.display = 'none';
      analy.style.display = 'none';
      compa.style.display = 'none';
      repor.style.display = 'none';
      dive.style.display = 'block';
    }

    </script>

  </head>
  <body>
    <nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
        <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Bankruptcy prediction</a>
        <div class="alert alert-primary" role="alert">
        <?php
            if (isset($_SESSION['FIRST'])){
              echo "Hello! ", $_SESSION['FIRST'];
            }else {
              echo "Not login yet!";
            }
        ?>
        </div>


        <ul class="navbar-nav px-3">
          <li class="nav-item text-nowrap">
            <a class="nav-link" href="signout.php">Sign out</a>
          </li>
        </ul>
      </nav>

      <div class="container-fluid">
        <div class="row">
          <nav class="col-md-2 d-none d-md-block bg-light sidebar">
            <div class="sidebar-sticky">
              <ul class="nav flex-column">
                <li class="nav-item">
                  <a class="nav-link" id="dashclick" href="#" onclick="showandhide('dashboard')">
                    <span data-feather="home"></span>
                    Dashboard
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" id="saveclick" href="#" onclick="showandhide('mysave')">
                    My saved companies
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" id="analysisclick" href="#" onclick="showandhide('analysis')">
                    Analysis
                  </a>
                </li>
              </ul>


            </div>
          </nav>


          <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <div>
              <form method="POST" class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <input class="form-control" id="codesearch" type="text" placeholder="Search (Stock number)" aria-label="Search" name="searchtarget">
                <select class="form-control" id="show" name="show">
                  <option value="financials" selected="selected">Income Statement</option>
                  <option value="balance-sheet">Balance Sheet</option>
                  <option value="cash-flow">Cash Flow</option>
                </select>
                <input class="form-control" id="secondCode" style="display:none" type="text" placeholder="Search (Second Stock number)" aria-label="Search">
                <button type="button" class="btn btn-primary" id="search">Search</button>
                <button class="btn btn-primary" type="submit" name="save" formaction="savecompany.php">Save to my lists</button>
              </form> 
            </div>
            <!-- div session begin in here -->
            <div id="dashboard">
                  <h3>Dashboard</h3>
                  <img src="waiting.gif" id="waiting" style="display: none">
            </div>
            <div id="mysave" style="display: none;">
                  <h3>My saved companies</h3>
                  <?php
                    $uid = $_SESSION['ID'];
                    $sql = "SELECT COMNUM FROM savecompany WHERE ID = $uid;";
                    $result = $conn->query($sql);
                    while($row = mysqli_fetch_assoc($result)){
                      echo '<div class="alert alert-primary" role="alert">';
                      echo 'Company stock number: ';
                      echo $row['COMNUM'].'<br/>';
                      echo '</div>';
                    }
                  ?>
            </div>
            <div id="analysis" style="display: none;">
                  <h3>Analysis</h3>
                  <img src="waiting.gif" id="waiting2" style="display: none">
            </div>
            <script>
              $(document).ready(function(){
                $("#dashclick").click(function(){
                    document.getElementById("dashboard").setAttribute("style","display: block");
                    document.getElementById("analysis").setAttribute("style","display: none");
                    document.getElementById("mysave").setAttribute("style","display: none");
                });
              });

              $(document).ready(function(){
                $("#saveclick").click(function(){
                    document.getElementById("dashboard").setAttribute("style","display: none");
                    document.getElementById("analysis").setAttribute("style","display: none");
                    document.getElementById("mysave").setAttribute("style","display: block");
                });
              });

              $(document).ready(function(){
                $("#search").click(function(){
                  if ($("#codesearch")[0].value.trim() != "") {
                  document.getElementById("waiting").setAttribute("style","display: block");
                  document.getElementById("dashboard").setAttribute("style","display: block");
                  document.getElementById("analysis").setAttribute("style","display: none");
                  var com = $("#codesearch")[0].value.trim();
                  var num_ = com.toString();
                  objdata = {
                    company: num_,
                    show: $('#show').val(),
                  }
                  if (document.getElementById('fT') != null){
                           document.getElementById('fT').parentNode.removeChild(document.getElementById('fT'));
                           document.getElementById('sT').parentNode.removeChild(document.getElementById('sT'));
                  }
                  $.ajax({
                    type: 'POST',
                    data: objdata,
                    url: 'grab.php',
                    success: function(data) {
                        // alert(data);
                        document.getElementById("waiting").setAttribute("style","display: none");
                        data = eval(data);
                        var firstTable = "<div id='fT'><table><thead><tr>";
                        var _th0 = "<th>Searched Code:<br>" + data[0][0] + "</th>";
                        var _th1 = "<th>Searched Statement:<br>" + data[0][1] + "</th>";
                        var _th2 = "<th>" + data[0][2] + "</th>";
                        var _th3 = "<th>" + data[0][3] + "</th>";
                        firstTable = firstTable + _th0 + _th1 + _th2 + _th3;
                        firstTable = firstTable + "</tr></thead></table></div>";

                        var secondTable = "<div id='sT'><table>";
                        // console.log(data.length);
                        for(i=1; i<data.length; i++){
                          if(i==1){
                            var row = "<thead><tr>";
                            for(j=0; j<data[i].length; j++){
                              row = row + "<th>" + data[i][j] + "</th>";
                            }
                            row = row + "</tr></thead>";
                            secondTable = secondTable + row;
                          }
                          else{
                            secondTable = secondTable + "<tbody>";
                            var row;
                            if(data[i].length>1){
                              row = "<tr>";
                            }
                            else{
                              row = "<tr colspan='4' style='text-align: center;'>";
                            }
                            for(j=0; j<data[i].length; j++){
                              row = row + "<td>" + data[i][j] + "</td>";
                            }
                            row = row + "</tr>";
                            secondTable = secondTable + row;
                          }
                        }
                        secondTable = secondTable + "</tbody>";
                        secondTable = secondTable + "</table></div>";

                        $( "#dashboard" ).append( firstTable );
                        $( "#dashboard" ).append( secondTable );
                      }
                    });
                  }
                  else {}
                });

                $("#analysisclick").click(function(){
                  if ($("#codesearch")[0].value.trim() != "") {
                  document.getElementById("analysis").setAttribute("style","display: block");
                  document.getElementById("waiting2").setAttribute("style","display: block");
                  var num = $("#codesearch")[0].value.trim();
                  var n = num.toString();
                  var objdata_an = {"stockcode": n};
                  if (document.getElementById('anfig') != null){
                           document.getElementById('anfig').parentNode.removeChild(document.getElementById('anfig'));
                  }
                  $.ajax({
                    type: 'POST',
                    data: objdata_an,
                    url: 'draw.php',
                    success: function(data) {
                              var img = document.createElement("img");
                              img.src = data;
                              img.id = "anfig";
                              document.getElementById("analysis").appendChild(img);
                              document.getElementById("waiting2").setAttribute("style","display: none");
                            }
                        });
                      }
                   else {}
                    });
              });
            </script>
          </main>
        </div>
      </div>




  </body>
</html>
