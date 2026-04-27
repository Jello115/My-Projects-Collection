let counter = 0;
function Order() {
    counter += 1;
    const order = document.querySelector('.js-order');
    // const value = document.querySelector('.js-value').value;
    const response = document.querySelector('.js-response');
    if (order.innerHTML === 'Order Now!') {
        order.innerHTML = 'Ordered!';
        order.classList.add('is-ordered')
        // response.innerHTML = value;
        
    } else {
        order.innerHTML = 'Order Now!';
        order.classList.remove('is-ordered');
        // response.innerHTML = '';
    }
    if (counter % 2 === 0) {
        order.classList.add('deactivate')
    } else {
        order.classList.remove('deactivate');
    }
}
function Menu(){
    var bar = document.getElementById('js-section');
    bar.classList.toggle('show_bar')

    let icon = document.getElementById("menuIcon");
    
    if (icon.src.includes("menu.png")) {
        icon.src = "close.png";
    } else {
        icon.src = "menu.png";
    }
}
    