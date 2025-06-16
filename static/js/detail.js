let addBtns = document.getElementById('add-wishlist')
let url = `${location.origin}/en/api/wishlist/`
let productId = addBtns.dataset.product

window.addEventListener('load', async function (e){
    let response = await this.fetch(url)
    let responsedata = await response.json()

    for(let i = 0; i < responsedata.length; i ++){
        if(responsedata[i].product == productId){
            addBtns.innerHTML += 'green'
            break
        }
    }
})

addBtns.addEventListener('click', function(e){
    e.preventDefault()
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        location.reload()
    })

})