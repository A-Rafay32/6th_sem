function max(num1, num2) {
    if (num1 > num2) {
        return num1;
    } else {
        return num2;
    }
}
console.log("max : ", max(6, 9));


function isVowel(char) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    return vowels.includes(char.toLowerCase());
}
console.log("is vowel : ", isVowel("X"));


function sum(arr) {
    return arr.reduce((total, num) => total + num, 0);
}
console.log("sum : ", sum([1, 2, 3, 4, 5, 6, 7]));


function multiply(arr) {
    return arr.reduce((total, num) => total * num, 1);
}
console.log("mulitply : ", multiply([1, 2, 3, 4, 5, 6, 7]));


function reverse(str) {
    return str.split('').reverse().join('');
}
console.log("reverse : ", reverse("Hello World"));


