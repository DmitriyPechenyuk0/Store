// // let minus = document.querySelectorAll('.minus')

// for (let count = 0; count < minus.length; count++) {
//     let button = minus[count]

//     button.addEventListener(
//         type = 'click',
//         listener = function(event){
//             let cookie = document.cookie.split('=')[1]
//             let list_of_products = cookie.split(' ')
//             if (button.nextElementSibling.textContent > 1) {
//                 for (let productCount = 0; productCount < list_of_products.length; productCount++) {
//                     let product = list_of_products[productCount]
//                     if (product == button.id) {
//                         list_of_products.splice(
//                             start = productCount,
//                             deleteCount = 1
//                         )
//                     }
//                     break
//                 }
//                 let newCookie = ""
//                 for (let productCount = 0; productCount < list_of_products.length; productCount++) {
//                     newCookie += list_of_products[productCount]
//                     newCookie += " "
//                 }
//                 document.cookie = `products = ${newCookie}; path = /`
//                 button.nextElementSibling.textContent = +button.nextElementSibling.textContent - 1
//             }

//         }
//     )
// }

// let cookie = document.cookie.split('=')[1]
// let list_of_products = cookie.split(' ')

// let elementToCountOne = '1';
// let elementToCountTwo = '2';
// let elementToCountThree = '3';

// let count1 = 0;
// let count2 = 0;
// let count3 = 0;

// for (let element of list_of_products) {
//     if (element === elementToCountOne) {
//         count1++;
//     }
// }

// for (let element of list_of_products) {
//     if (element === elementToCountTwo) {
//         count2++;
//     }
// }

// // for (let element of list_of_products) {
//     if (element === elementToCountThree) {
//         count3++;
//     }
// }


// let minusOne = document.getElementById('minus1')

// let minusTwo = document.getElementById('minus2')

// let minusThree = document.getElementById('minus3')

// minusOne.addEventListener(
//     type='click',
//     listener = function(event){
//         let cookie = document.cookie.split('=')[1]
//         let list_of_products = cookie.split(' ')

//         if listOfOne

//     }
// )


let minus = document.querySelectorAll('.minus')

for (let count = 0; count < minus.length; count++) {
    let button = minus[count]

    

    button.addEventListener(
        type = 'click',
        listener = function(event){
            let list_of_products = document.cookie.split('=')[1].split(' ')

            if (button.nextElementSibling.textContent > 1) {
                for (let productCount = 0; productCount < list_of_products.length; productCount++) {
                    let product = list_of_products[productCount]

                    console.log(product, button.id)
                    if (product == button.id) {
                        list_of_products.splice(
                            start = productCount,
                            deleteCount = 1
                        )
                    }
                    break
                }
                let newCookie = ""
                for (let productCount = 0; productCount < list_of_products.length; productCount++) {
                    newCookie += list_of_products[productCount]
                    newCookie += " "
                }
                document.cookie = `products = ${newCookie}; path = /`
                button.nextElementSibling.textContent = +button.nextElementSibling.textContent - 1
            }

        }
    )
}