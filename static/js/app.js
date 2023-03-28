window.onload = () => {
    let loader = document.querySelector("#preloader");
    loader.style.opacity = 0;
    loader.style.visibility = "hidden";
};



let like = document.querySelector('.heart');
let title_text = document.querySelector('#title_text');
let tip = title_text.dataset.type
like.addEventListener('click', (e) => {
    let prog_slug = e.target.dataset.favorit
    let like_classes = e.target.classList
    if (like_classes.contains('fa-regular') ) {
        like.classList.remove('fa-regular')
        like.classList.add('fa-solid');
        ajaxLike(prog_slug, true, title_text.textContent, tip)
    } else {
        like.classList.remove('fa-solid')
        like.classList.add('fa-regular')
        ajaxLike(prog_slug, false, title_text.textContent, tip)
    }
});

function removeFavoriteObj(e){
    ajaxLike(e.target.dataset.favorite, false, 'test')
    window.location.reload()
}

function ajaxLike(slug, is_liked, title, tip){
    $.ajax({
        url: '/check_like/',
        type: "GET",
        data: { slug: slug, like: is_liked, title: title, tip: tip },
        success: function(data){
            console.log(data);
        }
    });
}