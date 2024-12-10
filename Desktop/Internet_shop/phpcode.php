<?php 
  if(isset($_POST['submit'])){ 
  if(isset($_GET['go'])){ 
  if(preg_match("/^[  a-zA-Z]+/", $_POST['name'])){ 
  $name=$_POST['name']; 
  // Connect to my database
  $db=mysql_connect  ("infinityfreeapp", "runon",  "********") or die ('I can not connect to database, because: ' . mysql_error()); 
  // Choose database
  $mydb=mysql_select_db("yourDatabase"); 
  // Choose to table
  $sql="SELECT  ID, FirstName, LastName FROM Contacts WHERE FirstName LIKE '%" . $name .  "%' OR LastName LIKE '%" . $name ."%'"; 
  // Function of MySQL Query
  $result=mysql_query($sql); 
  // Create loope in this program
  while($row=mysql_fetch_array($result)){ 
          $FirstName  =$row['FirstName']; 
          $LastName=$row['LastName']; 
          $ID=$row['ID']; 
  // Result of this code as array
  echo "<ul>n"; 
  echo "<li>" . "<a  href="search.php?id=$ID">"   .$FirstName . " " . $LastName .  "</a></li>n"; 
  echo "</ul>"; 
  } 
  } 
  else{ 
  echo  "<p>Enter your search query</p>"; 
  } 
  } 
  } 
?>