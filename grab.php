<?php
session_start();
exec('unset DYLD_LIBRARY_PATH ;');
putenv('DYLD_LIBRARY_PATH');
putenv('DYLD_LIBRARY_PATH=/usr/bin');
$company = $_POST['company'] . ".HK";
$show = $_POST['show'];
$cmd = "/usr/local/bin/python3 ./cgi-bin/scraper/financialStatement_yahoo_json.py " . $company . " " . $show;
$result = exec($cmd);
echo $result;
?>