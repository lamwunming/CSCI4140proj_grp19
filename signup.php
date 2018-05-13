<?php
session_start();
include 'dbh.php';

$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$uid = $_POST['uid'];
$password = $_POST['password'];

$sql = "INSERT INTO user (FIRST, LAST, UID, PASSWORD) 
VALUES ('$firstname','$lastname','$uid','$password')";

$result = $conn->query($sql);

header("Location: registersuccess.html");
?>