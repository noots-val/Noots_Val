/**
 * 素のJavascriptによるモーダルメニュー展開処理
 *
 * @returns
 */
document.getElementById("modal_on").addEventListener("click", function() {

	const navMenu = document.getElementsByClassName("nav_menu")[0];

	navMenu.style.height = document.body.clientHeight + "px";
	navMenu.classList.add('open');
});

/**
 * 素のJavascriptによるモーダルメニュー消去処理
 * モーダル領域外をタップすることで、メニューを消去する
 *
 * @returns
 */
document.getElementById("nav_menu").addEventListener("click", function() {

	const navMenu = document.getElementsByClassName("nav_menu")[0];
	navMenu.classList.remove('open');
});

/**
 * モーダル領域内をタップされたときの、バブリング停止処理
 *
 * @param event
 * @returns
 */
document.getElementById("main_menu").addEventListener('click', function(event) {

	event.stopPropagation()
});