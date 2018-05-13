<?php
session_start();
$conn = mysqli_connect("localhost", "root", "", "4140");

if (!$conn) {
    die("Connection error : ".mysqli_connect_error());
}
?>