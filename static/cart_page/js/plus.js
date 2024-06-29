const buttons = document.querySelectorAll('.plus')
for (let i = 0; i < buttons.length; i++){
    let button = buttons[i]
    button.addEventListener(
        type = 'click',
        listener = function(event){
            if (document.cookie == ""){
                document.cookie = `products = ${button.id}`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
            }
            else{
                let currentProduct = document.cookie.split('=')[1]
                document.cookie = `products= ${currentProduct} ${button.id}; path = /`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
            }
        }
    )
}