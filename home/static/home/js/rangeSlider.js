const slideValue = document.getElementById('slider_span');
const inputSlider = document.getElementById('slider');
slideValue.style.left = (inputSlider.value) + "%"
slideValue.textContent = inputSlider.value;
inputSlider.oninput = (() =>{
    let value = inputSlider.value;
    slideValue.textContent = value;
    slideValue.style.left = (value) + "%"
    slideValue.classList.add("show")
});
inputSlider.onblur = (()=>{
    slideValue.classList.remove("show")
});