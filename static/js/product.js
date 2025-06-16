const orderingSort = document.getElementById('ordering_sort')
const pagination_sort = document.getElementById('pagination_sort')
const slider_range = document.getElementById('slider-range')
const slider_range_min = document.getElementById('slider-range-min')

let container = document.querySelector('.price-filter-products')

orderingSort.addEventListener('change', async function () {
    const selectedValue = this.value
    const ordering = await sortedProducts(selectedValue)
    const responseSort = await fetch(`http://127.0.0.1:8000/en/api/products/?ordering=${ordering}`);

    const dataSort = await responseSort.json()
    
    
    returnproducts(dataSort)
    
})

async function sortedProducts(value) {
    let ordering = ''

    switch (value) {
        case '1':
            ordering = 'title'
            break
        case '2':
            ordering = '-title'
            break
        case '3':
            ordering = 'price'
            break
        case '4':
            ordering = '-price'
            break
        
    console.log(ordering);
    return ordering
}}

function returnproducts(data){
    let htmlSort = ''

    data.forEach(p => {
        htmlSort += `
                    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-6 mb-30px d-flex" data-aos="fade-up" data-aos-delay="200">
                        <div class="product">
                            <a href="/products/${p.slug}/">   <!-- don't use Django tags at runtime -->
                                <div class="thumb">
                                    <img src="${p.cover_image}" alt="Product"/>
                                    <span class="badges"><span class="new">${p.type}</span></span>
                                    <div class="actions">
                                        <a href="/wishlist/" class="action wishlist update-wishlist" data-product="${p.id}" data-action="add" title="Wishlist">
                                            <i class="pe-7s-like"></i>
                                        </a>
                                        <a href="#" class="action quickview" data-link-action="quickview" title="Quick view"
                                        data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            <i class="pe-7s-look"></i>
                                        </a>
                                        <a href="/compare/" class="action compare" title="Compare"><i class="pe-7s-refresh-2"></i></a>
                                    </div>
                                </div>
                                <div class="content">
                                    <span class="ratings">
                                        <span class="rating-wrap"><span class="star" style="width:100%"></span></span>
                                    </span>
                                    <h5 class="title">${p.title}</h5>
                                    <span class="price"><span class="new">$${p.price}</span></span>
                                </div>
                                <button class="add-to-cart update-cart" data-product="${p.id}" data-action="add">Add To Cart</button>
                            </a>
                        </div>
                    </div>`
    });

    container.innerHTML = htmlSort
}


pagination_sort.addEventListener('change', async function () {
    const selectedValue = this.value
    sortedProducts(selectedValue)
    const responseSort = await fetch(`http://127.0.0.1:8000/en/api/products/`);

    const datafirst = await responseSort.json()

    let dataSort = []

    if (datafirst > count && dataSort < count){
        for (data of dataSort){
            dataSort.push(data)
        }
    }
    
    
    returnproducts(dataSort)
    
})

async function sortedProducts(value) {
    let count = ''

    switch (value) {
        case '1':
            count = '12'
            break
        case '2':
            count = '10'
            break
        case '3':
            count = '25'
            break
        case '4':
            count = '20'
            break
        
}}

function returnproducts(data){
    let htmlSort = ''

    data.forEach(p => {
        htmlSort += `
                    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-6 mb-30px d-flex" data-aos="fade-up" data-aos-delay="200">
                        <div class="product">
                            <a href="/products/${p.slug}/">   <!-- don't use Django tags at runtime -->
                                <div class="thumb">
                                    <img src="${p.cover_image}" alt="Product"/>
                                    <span class="badges"><span class="new">${p.type}</span></span>
                                    <div class="actions">
                                        <a href="/wishlist/" class="action wishlist update-wishlist" data-product="${p.id}" data-action="add" title="Wishlist">
                                            <i class="pe-7s-like"></i>
                                        </a>
                                        <a href="#" class="action quickview" data-link-action="quickview" title="Quick view"
                                        data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            <i class="pe-7s-look"></i>
                                        </a>
                                        <a href="/compare/" class="action compare" title="Compare"><i class="pe-7s-refresh-2"></i></a>
                                    </div>
                                </div>
                                <div class="content">
                                    <span class="ratings">
                                        <span class="rating-wrap"><span class="star" style="width:100%"></span></span>
                                    </span>
                                    <h5 class="title">${p.title}</h5>
                                    <span class="price"><span class="new">$${p.price}</span></span>
                                </div>
                                <button class="add-to-cart update-cart" data-product="${p.id}" data-action="add">Add To Cart</button>
                            </a>
                        </div>
                    </div>`
    });

    container.innerHTML = htmlSort
}

const max_price = document.getElementById('max_price')
const min_price = document.getElementById('min_price')


max_price.addEventListener('click', async (event) => {
    event.preventDefault();

    try {
        const response      = await fetch('http://127.0.0.1:8000/en/api/products/');
        const products      = await response.json();   // array of objects
        let   html_to_write = '';                      // collect first

        for (const p of products) {
            console.log(p);
            

            if (p.price >= Number(String(slider_range.value) + '.00')) {
                console.log(p.price, slider_range.value);
                
                html_to_write += `
                    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-6 mb-30px d-flex" data-aos="fade-up" data-aos-delay="200">
                        <div class="product">
                            <a href="/products/${p.slug}/">   <!-- don't use Django tags at runtime -->
                                <div class="thumb">
                                    <img src="${p.cover_image}" alt="Product"/>
                                    <span class="badges"><span class="new">${p.type}</span></span>
                                    <div class="actions">
                                        <a href="/wishlist/" class="action wishlist update-wishlist" data-product="${p.id}" data-action="add" title="Wishlist">
                                            <i class="pe-7s-like"></i>
                                        </a>
                                        <a href="#" class="action quickview" data-link-action="quickview" title="Quick view"
                                        data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            <i class="pe-7s-look"></i>
                                        </a>
                                        <a href="/compare/" class="action compare" title="Compare"><i class="pe-7s-refresh-2"></i></a>
                                    </div>
                                </div>
                                <div class="content">
                                    <span class="ratings">
                                        <span class="rating-wrap"><span class="star" style="width:100%"></span></span>
                                    </span>
                                    <h5 class="title">${p.title}</h5>
                                    <span class="price"><span class="new">$${p.price}</span></span>
                                </div>
                                <button class="add-to-cart update-cart" data-product="${p.id}" data-action="add">Add To Cart</button>
                            </a>
                        </div>
                    </div>`;
            }
        }

        container.innerHTML = html_to_write || '<p>No products in this price range.</p>';
    } catch (err) {
        console.error(err);
        container.innerHTML = '<p class="text-danger">Sorry, something went wrong.</p>';
    }
});


min_price.addEventListener('click', async (event) => {
    event.preventDefault();

    try {
        const response      = await fetch('http://127.0.0.1:8000/en/api/products/');
        const products      = await response.json();   // array of objects
        let   html_to_write = '';                      // collect first

        for (const p of products) {
            console.log(p);
            

            if (p.price <= Number(String(slider_range_min.value) + '.00')) {
                console.log(p.price, slider_range_min.value);
                
                html_to_write += `
                    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-6 mb-30px d-flex" data-aos="fade-up" data-aos-delay="200">
                        <div class="product">
                            <a href="/products/${p.slug}/">   <!-- don't use Django tags at runtime -->
                                <div class="thumb">
                                    <img src="${p.cover_image}" alt="Product"/>
                                    <span class="badges"><span class="new">${p.type}</span></span>
                                    <div class="actions">
                                        <a href="/wishlist/" class="action wishlist update-wishlist" data-product="${p.id}" data-action="add" title="Wishlist">
                                            <i class="pe-7s-like"></i>
                                        </a>
                                        <a href="#" class="action quickview" data-link-action="quickview" title="Quick view"
                                        data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            <i class="pe-7s-look"></i>
                                        </a>
                                        <a href="/compare/" class="action compare" title="Compare"><i class="pe-7s-refresh-2"></i></a>
                                    </div>
                                </div>
                                <div class="content">
                                    <span class="ratings">
                                        <span class="rating-wrap"><span class="star" style="width:100%"></span></span>
                                    </span>
                                    <h5 class="title">${p.title}</h5>
                                    <span class="price"><span class="new">$${p.price}</span></span>
                                </div>
                                <button class="add-to-cart update-cart" data-product="${p.id}" data-action="add">Add To Cart</button>
                            </a>
                        </div>
                    </div>`;
            }
        }

        container.innerHTML = html_to_write || '<p>No products in this price range.</p>';
    } catch (err) {
        console.error(err);
        container.innerHTML = '<p class="text-danger">Sorry, something went wrong.</p>';
    }
});