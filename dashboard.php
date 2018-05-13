<?php
    session_start();
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
                  <a class="nav-link active" href="#">
                    <span data-feather="home"></span>
                    Dashboard <span class="sr-only">(current)</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <span data-feather="file"></span>
                    My saved companies
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <span data-feather="shopping-cart"></span>
                    Analysis
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <span data-feather="users"></span>
                    Compare
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <span data-feather="bar-chart-2"></span>
                    Reports
                  </a>
                </li>
              </ul>
  
              
            </div>
          </nav>
  
          <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
              <input class="form-control" type="text" placeholder="Search (Stock number)" aria-label="Search">
              <button type="button" class="btn btn-primary">Search</button>
              <button type="button" class="btn btn-primary">Save to my lists</button>
            </div>
  
            <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas>
  
          </main>
        </div>
      </div>

    
  </body>
</html>