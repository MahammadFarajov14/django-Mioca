let delBtns = document.getElementsByClassName('remove-wishlist')
let delProd = document.getElementsByClassName('del-prod')

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