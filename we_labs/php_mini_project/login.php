
<?php 

    $conn = mysqli_connect('localhost','root','','employees');

    if(!$conn){
        echo "Connection Error : ", mysqli_connect_error();
    }

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>

    <div class="container">
        <div class="row">
          <div class="card col-4" style="margin:auto;margin-top: 250px;" >
            <div class="card-body">
                <form action="employee.php" method="">
                    <h5 class="card-title">Login Form</h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">Please Enter your credentials to login</h6>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="inputGroup-sizing-default">Email</span>
                        <input type="text" class="form-control" name="email" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="inputGroup-sizing-default">Password</span>
                        <input type="text" class="form-control" name="password" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
                    </div>  
                    <button type="submit" class="btn btn-success">Login</button>
                </form>
             </div>
          </div>
        </div>
    </div>

    
</body>
</html>
Login.php
Displaying Login.php.