<?php
// Declare an associative array with supermarket items and their prices
$items = [
    "cereal" => 5.00,
    "coffee beans" => 2.50,
    "bananas" => 3.50,
    "onion" => 1.00,
    "lettuce" => 2.40,
    "tomato" => 1.00
];

// Function to calculate the total price of all items
function calculateTotalPrice($items) {
    $total = 0;
    foreach ($items as $price) {
        $total += $price;
    }
    return $total;
}

// Print the array
echo "Array ( ";
foreach ($items as $item => $price) {
    echo "[$item] => $price ";
}
echo ")\n";

// Print each item and its price
foreach ($items as $item => $price) {
    echo ucfirst($item) . " costs $" . number_format($price, 2) . "\n";
}

// Calculate and print the total price of items
$totalPrice = calculateTotalPrice($items);
echo "The total price of your items is $" . number_format($totalPrice, 2);
?>
