<?php
session_start();
include 'dbh.php';

$uid = $_POST['uid'];
$password = $_POST['password'];

$sql = "SELECT * FROM user WHERE UID='$uid' AND PASSWORD='$password'";

$result = $conn->query($sql);

if (!$row = $result->fetch_assoc()) {
    echo "Your user id or password is wrong!";
} else {
    $_SESSION['ID'] = $row['ID'];
    $_SESSION['FIRST'] = $row['FIRST'];
    $_SESSION['LAST'] = $row['LAST'];
    $_SESSION['UID'] = $row['UID'];
    $_SESSION['PASSWORD'] = $row['PASSWORD'];
    header("Location: dashboard.php");
}

?>
