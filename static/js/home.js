window.addEventListener('load', async function (event) {
    let response = await this.fetch('http://127.0.0.1:8000/en/api/products/')
    let responseData = await response.json()
    let tab_wooden = this.document.getElementById('tab-woodenm')
    let tab_sculpture = this.document.getElementById('tab-sculpturesm')
    let tab_fabric = this.document.getElementById('tab-fabricm')
    let tab_pottery = this.document.getElementById('tab-potterym')
    let tab_jewelry = this.document.getElementById('tab-jewelrym')
    let tab_painting = this.document.getElementById('tab-paintingsm')

    for (data of responseData){

        html = `<div class="col-lg-4 col-xl-3 col-md-6 col-sm-6 col-xs-6 mb-30px"> 
                    <div class="product">
                        <div class="thumb">
                            <a href="single-product.html" class="image">
                                <img src="${data.cover_image}" alt="Product" />
                                <img class="hover-image" src="${data.cover_image}"
                                    alt="Product" />
                            </a>
                            <span class="badges">
                                <span class="new">${data.type}</span>
                            </span>
                            <div class="actions">
                                <a href="wishlist.html" class="action wishlist" title="Wishlist"><i
                                        class="pe-7s-like"></i></a>
                                <a href="#" class="action quickview" data-link-action="quickview" title="Quick view" data-bs-toggle="modal" data-bs-target="#exampleModal"><i class="pe-7s-look"></i></a>
                                <a href="compare.html" class="action compare" title="Compare"><i
                                        class="pe-7s-refresh-2"></i></a>
                            </div>
                        </div>
                        <div class="content">
                            <span class="ratings">
                                <span class="rating-wrap">
                                    <span class="star" style="width: 100%"></span>
                            </span>
                            <span class="rating-num">( 5 Review )</span>
                            </span>
                            <h5 class="title"><a href="single-product.html">${data.title}
                                </a>
                            </h5>
                            <span class="price">
                                <span class="new">$${data.price}</span>
                            </span>
                        </div>
                        <button title="Add To Cart" class=" add-to-cart">Add
                            To Cart</button>
                    </div>
                </div>`

        if (data.category.title == 'Wooden'){

            tab_wooden.innerHTML += html
        }
        if (data.category.title == 'Pottery'){
            tab_pottery.innerHTML += html
        }
        if (data.category.title == 'Jewelry'){
            console.log(data.title);
            tab_jewelry.innerHTML += html
        }

        if (data.category.title == 'Sculpture'){
            console.log(data.title);
            console.log(data);
            tab_sculpture.innerHTML += html
        }
        if (data.category.title == 'Fabric'){
            console.log(data.title);
            tab_fabric.innerHTML += html
        }
        if (data.category.title == 'Painting'){
            console.log(data.title);
            tab_painting.innerHTML += html
        }
    }

 
})