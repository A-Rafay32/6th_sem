<!DOCTYPE html>
<html>

<head>

    <?php

    $conn = mysqli_connect('localhost', 'root', '', 'employees');

    if (!$conn) {
        echo "Connection Error : ", mysqli_connect_error();
    }

    $employeesList = [];

    function getData()
    {
        $sql = "SELECT * FROM EmpTable";
        $results  =  mysqli_query($GLOBALS["conn"], $sql);
        $GLOBALS["employeesList"] = mysqli_fetch_all($results, MYSQLI_ASSOC);
    }

    function addEmployee($name, $designation, $department, $manager)
    {
        $insertQuery = "INSERT INTO EmpTable VALUES('$name', '$designation', '$department', '$manager')";
        $results  =  mysqli_query($GLOBALS["conn"], $insertQuery);
        getData();
    }

    function displayEmployees($employees)
    {
        echo "<h2>Employee Records</h2>";
        echo "<ul class='list-group'>";
        foreach ($employees as $employee) {
            echo "<li class='list-group-item'>Name: " . $employee['Name'] . ", Designation: " . $employee['Designation'] . ", Department: " . $employee['Department'] . ", Manager: " . $employee['Manager'] . "</li>";
        }
        echo "</ul>";
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve form data
        $name = $_POST['name'];
        $designation = $_POST['designation'];
        $department = $_POST['department'];
        $manager = $_POST['manager'];

        // Add new employee
        addEmployee($name, $designation, $department, $manager);
    }

    getData();

    ?>


    <title>Employee Records</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
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
                    <a class="nav-link active" aria-current="page" href="#">Employee</a>
                    <a class="nav-link" href="userPage.php">Tasks</a>
                </div>
            </div>
            <form class="d-flex">
                <a class="btn btn-success" href="login.php">Login</a>
            </form>
        </div>
    </nav>
    <div class="container mt-5">

        <!-- Employee Record Form -->
        <h2>Add Employee Record</h2>
        <form method="post" action="employee.php">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="designation">Designation:</label>
                <select class="form-control" id="designation" name="designation">
                    <option value="Team lead">Team lead</option>
                    <option value="Manager">Manager</option>
                    <option value="Developer">Developer</option>
                </select>
            </div>
            <div class="form-group">
                <label for="department">Department:</label>
                <input type="text" class="form-control" id="department" name="department">
            </div>
            <div class="form-group">
                <label for="manager">Manager:</label>
                <select class="form-control" id="manager" name="manager">
                    <?php
                    // Populate manager dropdown with existing employees
                    foreach ($GLOBALS["employeesList"] as $employee) {
                        if ($employee['designation'] == "Manager")
                            echo "<option value='" . $employee['name'] . "'>" . $employee['name'] . "</option>";
                    }
                    ?>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        <?php
        // Display all employees
        displayEmployees($employeesList);
        ?>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>

</html>