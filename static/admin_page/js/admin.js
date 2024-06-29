let listOfButtonsImages = document.querySelectorAll('.edit-img')

for (let count = 0; count < listOfButtonsImages.length; count++){
    let button = listOfButtonsImages[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            document.getElementById('p-text').textContent = 'IMAGE'
            input_image.type = "file"
            input_image.name = "image"
            input_image.accept = "image/*"
            document.querySelector('.submit-change').value = `image-${button.id}`

            console.log(input_image.type, input_image.name, input_image.placeholder)
            console.log(document.querySelector('.submit-change').value)
        }
    )  
}
let listOfButtonsNames = document.querySelectorAll('.edit-name')

for (let count = 0; count < listOfButtonsNames.length; count++){
    let button = listOfButtonsNames[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            document.getElementById('p-text').textContent = 'TEXT'
            input_image.type = "text"
            input_image.name = "name"
            input_image.placeholder = "Задайте нове ім'я"   
            
            document.querySelector('.submit-change').value = `name-${button.id}`
        
            console.log(input_image.type, input_image.name, input_image.placeholder, document.getElementById('p-text').textContent = 'TEXT')
            console.log(document.querySelector('.submit-change').value)
        
        }



    )
}

let listOfButtonsPrices = document.querySelectorAll('.edit-price')

for (let count = 0; count < listOfButtonsPrices.length; count++){
    let button = listOfButtonsPrices[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            document.getElementById('p-text').textContent = 'TEXT'
            input_image.type = "text"
            input_image.name = "price"
            input_image.placeholder = "Введіть новий текст"   
            
            document.querySelector('.submit-change').value = `name-${button.id}`
        
            console.log(input_image.type, input_image.name, input_image.placeholder, document.getElementById('p-text').textContent = 'TEXT')
        
        
        }



    )
}


let listOfButtonsDiscounts = document.querySelectorAll('.edit-discount')

for (let count = 0; count < listOfButtonsDiscounts.length; count++){
    let button = listOfButtonsDiscounts[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            document.getElementById('p-text').textContent = 'TEXT'
            input_image.type = "text"
            input_image.name = "name"
            input_image.placeholder = "Введіть новий текст"   
            
            document.querySelector('.submit-change').value = `name-${button.id}`
        
            console.log(input_image.type, input_image.name, input_image.placeholder, document.getElementById('p-text').textContent = 'TEXT')
        
        
        }



    )
}

let listOfButtonsNew = document.querySelectorAll('.add-product')

for (let count = 0; count < listOfButtonsNames.length; count++){
    let button = listOfButtonsNames[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window-new').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            input_image.type = "text"
            input_image.name = "name"
            input_image.placeholder = "Задайте нове ім'я"
            //  document.querySelector('.submit-change').value = `name-${button.id}`
        }
    )
}

const addProduct = document.getElementById('addproduct') 

addProduct.addEventListener('click', function(){
    document.querySelector('.modal-window-new').style.display = 'block' 
})