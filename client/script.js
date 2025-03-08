document.addEventListener('DOMContentLoaded', function () {

    let menu = document.querySelector('.header .menu');
    let menuButton = document.querySelector('#menu-btn');

    if (menuButton) {
        menuButton.onclick = () => {
            menu.classList.toggle('active');
        }
    } else {
        console.warn('#menu-btn not found');
    }

    window.onscroll = () => {
        menu.classList.remove('active');
    }

    document.querySelectorAll('input[type="number"]').forEach(inputNumber => {
        inputNumber.oninput = () => {
            if (inputNumber.value.length > inputNumber.maxLength) {
                inputNumber.value = inputNumber.value.slice(0, inputNumber.maxLength);
            }
        };
    });

    document.querySelectorAll('.view-property .details .thumb .small-images img').forEach(images => {
        images.onclick = () => {
            let src = images.getAttribute('src');
            let bigImage = document.querySelector('.view-property .details .thumb .big-image img');
            if (bigImage) {
                bigImage.src = src;
            } else {
                console.warn('.big-image img not found');
            }
        }
    });
    

    document.querySelectorAll('.faq .box-container .box h3').forEach(headings => {
        headings.onclick = () => {
            headings.parentElement.classList.toggle('active');
        }
    });
});
