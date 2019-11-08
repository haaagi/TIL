// 19_callbackFunction.js

function a(x, y) {
    return x + y;
}

function b(n) {
    return n++;
}

function c(f1, f2) {
    return f1(10,10) + f2(99);
}

console.log(
    c(a,b)
)
// 이거 119 나온다. return 하고나서 99 가 100됌 