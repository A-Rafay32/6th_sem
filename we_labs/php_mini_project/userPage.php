<!DOCTYPE html>
<html lang="en">

<head>

    <?php
    $conn = mysqli_connect('localhost', 'root', '', 'employees');

    if (!$conn) {
        echo "Connection Error : ", mysqli_connect_error();
    }


    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $TaskTitle = $_POST['TaskTitle'];
        $AssignedTo = $_POST['AssignedTo'];
        $DueDate = $_POST['DueDate'];

        $insertQuery = "INSERT INTO TaskTable (TaskTitle, AssignedTo, DueDate) VALUES ('$TaskTitle', '$AssignedTo', '$DueDate')";
        $results  =  mysqli_query($conn, $insertQuery);
        if (!$results) {
            echo "Error in inserting record";
        }
    }

    ?>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link" href="employee.php">Employee</a>
                    <a class="nav-link active" aria-current="page" href="#">Tasks</a>
                </div>
            </div>
            <form class="d-flex">
                <a class="btn btn-success" href="login.php">Login</a>
            </form>
        </div>
    </nav>


    <div class="container mt-5">
        <h1 class="mb-4">Add Task</h1>

        <form method="POST" action="">
            <div class="form-group">
                <label for="text_field">Task Title</label>
                <input type="text" class="form-control" id="TaskTitle" name="TaskTitle" required>
            </div>
            <div class="form-group">
                <label for="dropdown_menu">Assigned To</label>
                <select class="form-control" id="AssignTo" name="AssignedTo" required>
                    <option value="">Select an option</option>
                    <?php

                    $sql = "SELECT * FROM EmpTable";
                    $results  =  mysqli_query($GLOBALS["conn"], $sql);
                    $employeesList = mysqli_fetch_all($results, MYSQLI_ASSOC);

                    foreach ($employeesList as $employee) {
                        if ($employee['Designation'] !== "Manager")
                            echo "<option value='" . $employee['Name'] . "'>" . $employee['Name'] . "</option>";
                    }

                    ?>
                </select>
            </div>
            <div class="form-group">
                <label for="date_picker">Due Date</label>
                <inwput type="date" class="form-control" id="DueDate" name="DueDate" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Task</button>
        </form>

        <h2 class="mt-5">Task Details</h2>
        <div class="mt-3">

            <?php
            $selectQuery = "SELECT * FROM TaskTable";
            $results  =  mysqli_query($conn, $selectQuery);
            $taskList = mysqli_fetch_all($results, MYSQLI_ASSOC);

            foreach ($taskList as $row) {
                echo "<div class ='border p-3 mb-3'>";
                echo "<p><strong>Task Title:</strong> " . $row['TaskTitle'] . "</p>";
                echo "<p><strong>Assigned To:</strongw> " . $row['AssignedTo'] . "</p>";
                echo "<p><strong>Due Date:</strong> " . $row['DueDate'] . "</p>";
                echo "</div>";
            }
            ?>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>

</html>
userPage.php
Displaying userPage.php.