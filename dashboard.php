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
                  <a class="nav-link" href="#" onclick="showandhide('dashboard')">
                    <span data-feather="home"></span>
                    Dashboard
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#" onclick="showandhide('mysave')">
                    My saved companies
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#" onclick="showandhide('analysis')">
                    Analysis
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#" onclick="showandhide('compare')">
                    Compare
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#" onclick="showandhide('report')">
                    Report
                  </a>
                </li>
              </ul>


            </div>
          </nav>


          <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
              <input class="form-control" id="code" type="text" placeholder="Search (Stock number)" aria-label="Search">
              <select class="form-control" id="show" name="show">
                <option value="financials" selected="selected">Income Statement</option>
                <option value="balance-sheet">Balance Sheet</option>
                <option value="cash-flow">Cash Flow</option>
              </select>
              <input class="form-control" id="secondCode" style="display:none" type="text" placeholder="Search (Second Stock number)" aria-label="Search">
              <button type="button" class="btn btn-primary" id="search">Search</button>
              <button type="button" class="btn btn-primary">Save to my lists</button>
            </div>
            <script src="/js/finStat.js"></script>
            <!-- div session begin in here -->
            <div id="dashboard">
                  <h3>Dashboard</h3>
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
            </div>
            <div id="compare" style="display: none;">
                  <h3>Compare</h3>
            </div>
            <div id="report" style="display: none;">
                  <h3>Report</h3>
            </div>
          </main>
        </div>
      </div>




  </body>
</html>
