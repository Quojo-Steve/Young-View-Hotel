const del = document.querySelectorAll('.delete');
const act = document.querySelectorAll('.activate');
const display = document.querySelector('.form');
const display1 = document.querySelector('.form1');
const remove = document.querySelector('.no');
const remove1 = document.querySelector('.no1');
const red = document.querySelectorAll('.r')
const standard = document.querySelectorAll('.s')
const green = document.querySelectorAll('.g')
const ordinary = document.querySelectorAll('.o')
const executive = document.querySelectorAll('.e')

act.forEach((btn) => {
    btn.addEventListener('click', () => {
        display1.classList.remove('remove')
    })
});
del.forEach((btn) => {
    btn.addEventListener('click', () => {
        display.classList.remove('remove')
    })
});
remove.addEventListener('click', () => {
    display.classList.add('remove')
})
remove1.addEventListener('click', () => {
    display1.classList.add('remove')
})

window.addEventListener("resize", function(){
    alert("This page isnt responsive")
});
  
function getSelectedValue() {
    var select = document.getElementById('select').value;
    if (select === 'red') {
        green.forEach((btn) => {
            btn.style.display = 'none'
        });
        red.forEach((btn) => {
            btn.style.display = 'flex'
        });
        console.log('red')
    } else if (select === 'green') {
        green.forEach((btn) => {
            btn.style.display = 'flex'
        });
        red.forEach((btn) => {
            btn.style.display = 'none'
        });
    } else if (select === 'ordinary') {
        ordinary.forEach((btn) => {
            btn.style.display = 'flex'
        });
        executive.forEach((btn) => {
            btn.style.display = 'none'
        });
        standard.forEach((btn) => {
            btn.style.display = 'none'
        });
    } else if (select === 'executive') {
        ordinary.forEach((btn) => {
            btn.style.display = 'none'
        });
        standard.forEach((btn) => {
            btn.style.display = 'none'
        });
        executive.forEach((btn) => {
            btn.style.display = 'flex'
        });
    } else if (select === 'standard') {
        ordinary.forEach((btn) => {
            btn.style.display = 'none'
        });
        standard.forEach((btn) => {
            btn.style.display = 'flex'
        });
        executive.forEach((btn) => {
            btn.style.display = 'none'
        });
    } else {
        location.reload()
    }
}