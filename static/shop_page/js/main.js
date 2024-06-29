


const button1text = '1';
const button2text = '2';
const button3text = '3';
let one = document.getElementById('one')

const button1 = document.querySelector('#button1')
button1.addEventListener(
    type = 'click',
    
    listener= function (event) {
        
        
        one.style.display = 'flex'
        

        if(document.cookie != '' ){
            var existingProducts = document.cookie.replace(/(?:(?:^|.*;\s*)products\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            document.cookie = `products = ${existingProducts} ${button1text}; path = /`
        }
        else{
            document.cookie = `products = ${button1text}; path = /`
        }
        var number = document.getElementById('one');
        var varnumber = parseInt(number.innerText);
        number.innerText = varnumber + 1;
    }
)

const button2 = document.querySelector('#button2')

button2.addEventListener(
    type = 'click',
    listener= function (event) {
        
        
        one.style.display = 'flex'
        
            
        
        if(document.cookie != '' ){
            var existingProducts = document.cookie.replace(/(?:(?:^|.*;\s*)products\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            document.cookie = `products = ${existingProducts} ${button2text}; path = /`
        }

        else{
            document.cookie = `products = ${button2text}; path = /`
        }

        var number = document.getElementById('one');
        var varnumber = parseInt(number.innerText);
        number.innerText = varnumber + 1;
        
    }
)

const button3 = document.querySelector('#button3')

button3.addEventListener(
    type = 'click',
    
    listener= function (event) {

        one.style.display = 'flex'
        
        
        if(document.cookie != '' ){
            var existingProducts = document.cookie.replace(/(?:(?:^|.*;\s*)products\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            document.cookie = `products = ${existingProducts} ${button3text}; path = /`
        }

        if(document.cookie == ''){
            document.cookie = `products = ${button3text}; path = /`
        }
        
        var number = document.getElementById('one');
        var varnumber = parseInt(number.innerText);
        number.innerText = varnumber + 1;
    }
)





