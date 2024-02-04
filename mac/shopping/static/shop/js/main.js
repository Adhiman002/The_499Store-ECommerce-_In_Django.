const MainImg = document.getElementById("MainImg");
const smallImg = document.getElementsByClassName("small-img");
smallImg[0].onclick = function() {
    MainImg.src = smallImg[0].src;
}
smallImg[1].onclick = function() {
    MainImg.src = smallImg[1].src;
}
smallImg[2].onclick = function() {
    MainImg.src = smallImg[2].src;
}
smallImg[3].onclick = function() {
    MainImg.src = smallImg[3].src;
}
// $(window).scroll(function() {
//     let scrl = $(window).scrollTop();
//     if (scrl < 70) {
//         $('.navbar').removeClass('navbg');
//     } else {
//         $('.navbar').addClass('fix');

//     }
// });




