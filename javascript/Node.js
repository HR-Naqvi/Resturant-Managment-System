// #sare menu ko dectionary me likhen
const menu = {
    'chiken karahi': 1000,
    'mutton karahi': 2050,
    'beef karahi': 1900,
    'mutton korma': 1850,
    'pizza': 1100,
    'burger': 300,
    'shawarma': 150,
    'sandwich': 250,
    'pepsi': 170,
    'purified water': 100,
    'coffee': 300,
    'organic juice': 250,
    'soda water': 150,
    'ice cream': 200,
    'brownies': 300,
    'cake': 900
}
// ......................................

let total = 0;
const all_orders = []
let order_detail = document.getElementById("order_details")
let total_order = document.getElementById("order_total")



// ....................................................

firstOrder = () => {
    costumer_order = document.getElementById("user_input").value.toLowerCase();
    if (costumer_order in menu) {
        alert("Sure Sir")
        total += menu[costumer_order]
        all_orders.push(`${costumer_order.charAt(0).toUpperCase() + costumer_order.slice(1)} &nbsp;&nbsp;&nbsp;  ${menu[costumer_order]}`)
        Order_details_print()
        display_hidden_order_class()
        display_hidden_payment_class()
    }
    else {
        alert("Sorry sir, this item is not found")
    }
}

// ..............................................................\

Order_details_print = () => {

    order_detail.innerHTML = `<h4>Your Order Details ...</h4><p class="detail_Print">Items&nbsp;&nbsp;&nbsp;Prices<br> ${all_orders.join(" + <br>")}</p>`

    total_order.innerHTML = `Total : ${total}`

}

// ..............................................................

let payment_div = document.getElementById("payment_div")
let payment_methods = document.getElementById("payment_methods")


payment_methods.addEventListener("change", function () {
    let selected_payment_method = this.value
    if (selected_payment_method === "Jazzcash") {
        payment_div.innerHTML = `<p>Jazzcash num: 03265212300</p>`
    }
    else if (selected_payment_method === "Easypaisa") {
        payment_div.innerHTML = `<p>Easypaisa num: 03107577184</p>`
    }
    else if (selected_payment_method === "Bank transfer") {
        payment_div.innerHTML = `<p>Bank Name:  HBL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
       &nbsp;&nbsp; Account num: PK94HBL0000001123456702</p>`
    }
    else if (selected_payment_method === "Cash on delivery") {
        payment_div.innerHTML = `<p>Sure Sir , Your Order will be Ready in half an hour</p>`
    }
    else {
        payment_div.innerHTML = `<p>Enter Correct Choice</p>`
    }
})

// .....................................................................

display_hidden_order_class = () => {
    let display_order = document.getElementById("display_order")
    display_order.classList.remove("hidden")
}
// ....................................................
display_hidden_payment_class = () => {
    let payment_method = document.getElementById("payment_method")
    payment_method.classList.remove("hidden1")
}
// ...................................
