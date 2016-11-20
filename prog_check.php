<?php
header("Content-Type: text/json");
#print_r(json_encode($_POST['user']));
#print_r(json_encode('{"data":"content"}'));
# $phpInput = file_get_contents("php://input");
# print_r($phpInput);

$phpInput = file_get_contents("php://input");
$jobj = json_decode($phpInput, true);
$username = $jobj['user'];


$fruits = array(
	"fruits" => array("a" => "orange", "b" => "banana", "c" => "apple"),
	"numbers" => array(1, 2, 3, 4, 5, 6),
	"holes" => array("first", 5=> "second", "third"),
	"userBack" => array("allen", $username)
	);
echo json_encode($fruits);
?>
