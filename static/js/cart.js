let updateBtns = document.getElementsByClassName('update-cart')
let updateWishlBtns = document.getElementsByClassName('update-wishlist')
let delBtns = document.getElementsByClassName('remove-cart')
let delProd = document.getElementsByClassName('product-cartown')

for (let i = 0; i < updateBtns.length; i ++){
    updateBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        productid = this.dataset.product
        action = this.dataset.action

        
        
        if (user == 'AnonymousUser'){
            console.log('User not loged in');
        }
        else{
            updateUserCart(productid, action)
        }
    })

}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function updateUserCart(productid, action){
    console.log(`user is ${user}`);

    let url = '/en/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productid' : productid, 'action': action})
    })
    .then((response) => {
        return response.json()
    }).then((data) => {
        console.log('Data:', data);
        location.reload()
    })
}



for(let i = 0; i < delBtns.length; i ++){
    delBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        let itemid = delBtns[i].dataset.item
        let url = `${location.origin}/en/api/wishlist/${itemid}/`
        console.log(url);
        
        fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
        })
        .then((data) => {
            delProd[i].innerHTML = ''
        })        
    })
}