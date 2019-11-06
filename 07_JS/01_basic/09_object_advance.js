// ES5
var books = ['Learning JS', 'Eloquent JS'];

var comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

var magazine = {}

var bookshop = {
    books: books,
    comics: comics,
    magazine: magazine,
}

// ES6+ 
const books = ['Learning JS', 'Eloquent JS'];

const comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

const magazine = {}

const bookshop = {
    books, comics, magazine,
}

// Method(객체 안의 함수)
// 절대 arrow function () => {} 쓰지말자
const me = {
    name:'neo',
    // 메서드 정의
    greet: function() {
            return `hello, i am ${name} `
    }
};