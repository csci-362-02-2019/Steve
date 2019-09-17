<?php
echo "Contents:";
$path = ".";
$dh = opendir($path);
$i=1;
$output= "";
$html = 'contents.html';
while (($file = readdir($dh)) !== false) {
    if($file != "." && $file != ".." && $file != "index.php" && $file != ".htaccess" && $file != "error_log" && $file != "cgi-bin") {
        echo "$file " ;
        $output = $output ." " ."$file";
        $i++;
        file_put_contents($html, $output);
    }
}
include("contents.html");
closedir($dh);
?> 
