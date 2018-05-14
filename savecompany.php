<?php
    include 'dbh.php';
    $uid = $_SESSION['ID'];
    $comnum = $_POST['searchtarget'];
    $sql = "INSERT INTO savecompany (ID, COMNUM) 
    VALUES ('$uid','$comnum')";

    $result = $conn->query($sql);

    header("Location: dashboard.php");
?>