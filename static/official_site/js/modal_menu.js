/**
 * 素のJavascriptによるモーダルメニュー展開処理
 *
 * @returns
 */
document.getElementById("js-header__modal-on").addEventListener("click", function() {

	const navMenu = document.getElementsByClassName("js-nav")[0];

	navMenu.style.height = document.body.clientHeight + "px";
	navMenu.classList.add('nav--is_open');
});

/**
 * 素のJavascriptによるモーダルメニュー消去処理
 * モーダル領域外をタップすることで、メニューを消去する
 *
 * @returns
 */
document.getElementById("js-nav").addEventListener("click", function() {

	const navMenu = document.getElementsByClassName("js-nav")[0];
	navMenu.classList.remove('nav--is_open');
});

/**
 * モーダル領域内をタップされたときの、バブリング停止処理
 *
 * @param event
 * @returns
 */
document.getElementById("js-nav__menu").addEventListener('click', function(event) {

	event.stopPropagation()
});