function add() {

    const elements = document.getElementsByClassName('form-control');
    for (i = 2; i < elements.length; i++) {
        if (elements[i].style && elements[i].style.display != 'block') {
            elements[i].style.display = 'block';
            elementsForShow = i;
            break;
        }
    }
}

function hide() {
    const elements = document.getElementsByClassName('form-control');
    for (i = elements.length - 1; i > 1; i--) {
        if (elements[i].style && elements[i].style.display == 'block') {
            elements[i].style.display = 'none';
            elements[i].value = "";
            elementsForShow = i;
            break;
        }
    }
}

function validator() {
    const elementsHtml = document.getElementsByClassName('form-control');
    const emptyArr = [];
    for (let i = 0; i < elementsHtml.length; i++) {
        const element = elementsHtml[i];
        if (/\S/.test(element.value)) {
            if (!(emptyArr.includes(element.value))) {
                emptyArr.push(element.value);
            } else {
                emptyArr.push(element.value);
                if (element.value.length > 0) {
                    element.value = element.value + " " + emptyArr.filter(x => x === element.value).length;
                }
            }
        }
    }
}

function checknames(){
    const elementsHtml = document.getElementsByClassName('form-control');
    const tempArr = [];
    for (let i = 0; i < elementsHtml.length; i++) {
        const element = elementsHtml[i];
        if (element.value.length > 0) {
            tempArr.push(element.value);
        }
    }
    for (let i = tempArr.length-1; i > 0; i--) {
        const count = tempArr.filter(x => x === elementsHtml[i].value).length;
        if (count > 1){
            elementsHtml[i].value += " " + count;
            tempArr[i] = elementsHtml[i].value;
        }
    }
}

function submitOnOff() {
    const tempArr = [];
    const elementsHtml = document.getElementsByClassName('form-control');
    const subbutton = document.getElementById('submit-button');

    for (let i = 0; i < elementsHtml.length; i++) {
        const element = elementsHtml[i];
        if (/\S/.test(element.value) && element.style.display == '') {
            tempArr.push(element.value);
            }
        }
    
    if (tempArr.length <= 1) {
        subbutton.disabled = true;
    } else {
        subbutton.disabled = false;
    }
}

function voteShow() {
    const textContent = document.getElementsByClassName("result-box");
    for (let text = 0; text < textContent.length; text++) {
        const element = textContent[text].innerText;
        if (element.includes('Empty Choice')) {
            textContent[text].style.display = 'none';
        }
    }
    document.getElementsByClassName('radio-button m-2')[0].checked = true;
    
}


function vote() {
    const arr = document.getElementsByClassName('form-field-2');
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i].value);
    }
}



function modalfunc() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";
    span.onclick = function () {
        modal.style.display = "none";
    };
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}
