$(document).ready(function () {
    getAllList();
});

let list = null
let regex = /[^0-9]/g

function getAllList() {
    $('.card-list').empty()
    $.ajax({
        type: "GET",
        url: "/allList",
        data: {},
        success: function (response) {
            list = response['all_list']
            for (let i = 0; i < list.length; i++) {
                let title = list[i]['title']
                let image = list[i]['image']
                let price = list[i]['price']
                let like = list[i]['like']

                list[i]['price'] = price.replace(regex, "")

                let temp_html = `<div class="card">
                                            <img class="card-img-top" src="${image}" alt="Card image cap">
                                            <div class="tour-card-body">
                                                <h5 class="tour-title">${title}</h5>
                                                <p class="tour-price">${price}원</p>
                                            </div>
                                            <footer class="card-footer">
                                                <span class="icon" onclick="likeTour('${title}')">
                                                     <i class="fa fa-heart-o"></i>
                                                </span>
                                                <p class="tour-like">${like}</p>
                                            </footer>
                                         </div>`
                $('.card-list').append(temp_html)
            }
        }
    })
}

function sortList(key) {
    $('.card-list').empty()
    let keyValue = key
    let sortedList = null
    if (keyValue == 1) {
        sortedList = list.sort(function (a, b) {
            return a.price - b.price; // [2, 4, 11, 33] (오름차순)
        })
    } else if (keyValue == 2) {
        sortedList = list.sort(function (a, b) {
            return b.price - a.price // (내림차순)
        })
    } else if (keyValue == 3) {
        sortedList = list.sort(function (a, b) {
            return b.like - a.like // (내림차순)
        })
    } else {
        alert('오류')
    }

    for (let i = 0; i < sortedList.length; i++) {
        let title = sortedList[i]['title']
        let image = sortedList[i]['image']
        let price = sortedList[i]['price'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
        let like = sortedList[i]['like']

        let temp_html = `<div class="card">
                                    <img class="card-img-top" src="${image}" alt="Card image cap">
                                    <div class="tour-card-body">
                                        <h5 class="tour-title">${title}</h5>
                                        <p class="tour-price">${price}원</p>
                                    </div>
                                    <footer class="card-footer">
                                        <span class="icon" onclick="likeTour('${title}')">
                                            <i class="fa fa-heart-o"></i>
                                        </span>
                                        <p class="tour-like">${like}</p>
                                    </footer>
                                 </div>`
        $('.card-list').append(temp_html)
    }
}

function test(){
            // location.href = 'http://twdomain.shop/'
            alert('알람작동')
        }
