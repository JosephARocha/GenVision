<?php
$target_dir = "uploads/";

 if ( !file_exists($target_dir) ) {
     $oldmask = umask(0);  // helpful when used in linux server  
     mkdir ($target_dir, 0744);
 }

$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
chmod($target_file, 0777);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        $uploadOk = 1;
    } else {
        $uploadOk = 0;
    }
}

if (file_exists($target_file)) {
    $uploadOk = 0;
} 

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
// if everything is ok, try to upload file
} else {
    move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
}

$output = "Failed";
$output = shell_exec ('python GenVision.py ' . $target_file .  ' 2>&1');
if (strpos($output, "FEMALE") !== false){ 
    $gender = "Female";
}else{
   $gender = "Male";
}
//echo $output;
?>

<html lang="en">
<head>
    <title>GenVision</title>
    <link rel="stylesheet" href="Http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
        <div class="navbar-header">
        <a class="navbar-brand" href="#">GenVision</a>
        </div>
        <ul class="nav navbar-nav">
        <li><a href="https://github.com/Folasade111/Independent-Study">Github</a></li>
        </ul>
        </div>
    </nav>
</head>
<body style="background-color: #1e1b29;">
    <div class="container" style="background-color: #ffffb5">
<h4>GenVision is an
application which demonstrates
the power of convolutional neural networks.
</br></br>Simply upload an image and the classifier will predict whether
it is a male or female.</h4>
    </div>
    </br>
    <div class="container" style="background-color: #ffffb5">
        <form action="GenVision.php" method="post" enctype="multipart/form-data">
            <div class="form-group">
            <label for="file"><h3>Select an Image to Upload:</h3></label>
            <input type="file" name="fileToUpload" id="fileToUpload">
            </br>
            <input class="btn btn-primary"  type="submit" value="Upload Image" name="submit">
            </div>
        </form>
    </div>
    </br>
    <div class="container" style="background-color: #ffffb5">
    <h2><?php echo "The Prediction is: " . $gender; ?></h2>
    </br>
    <img src="<?php echo $target_file?>" class="img-responsive">
    </br>
    </div>
</body>
