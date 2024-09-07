<html>

<body>
<h2>View</h2>
<pre><?php
    $file = $_GET['file']?$_GET['file']:'';
    echo $file;
    if(preg_match('/flag|:/i', $file)){
        exit('Permission denied');
    }
    echo file_get_contents($file);
?>
</pre>
</body>
<html>
