<?php
session_start();
exec('unset DYLD_LIBRARY_PATH ;');
putenv('DYLD_LIBRARY_PATH');
putenv('DYLD_LIBRARY_PATH=/usr/bin');
$code = $_POST['stockcode'];
$code_ = (string) $code;
$cmd = "/usr/local/bin/python3 ./algo/CSCI4140.py " . $code_;
$result = exec($cmd);
echo $result;
?>