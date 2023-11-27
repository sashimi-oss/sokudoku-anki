const text = document.getElementById('text');
const display = document.getElementById('display');
const a = new RegExp(/\n|。|、|,/);


let count = 0;
function takeValue() {
  const textValue = text.value;
  const arr1 = textValue.split(a);
  let start = setInterval(() => {
    if (count < arr1.length) {
      display.innerHTML = arr1[count];
      count++;
    } else {
      clearInterval(start);
      count = 0;
    }
  }, 1000);
}

let nannkaime = -1;
const clickValue = () => {
  const textValue = text.value;
  const arr1 = textValue.split(/\n|、|。|,/);
  if (nannkaime + 1 === arr1.length) {
    display.innerHTML = "";
    nannkaime = -1;
  } else {
    nannkaime++;
    display.innerHTML = arr1[nannkaime];
  }
}

const clickValueSub = () => {
  const textValue = text.value;
  const arr1 = textValue.split(/\n|、|。|,/);
  if (nannkaime !== 0) nannkaime--;
  display.innerHTML = arr1[nannkaime];
}

let nannkaime2 = 0;
const clickValueEn = () => {
  const textValue = text.value;
  const arr1 = textValue.split(/\./);
  if (nannkaime2 === arr1.length) {
    display.innerHTML = "";
    nannkaime2 = 0;
  } else {
    display.innerHTML = "<p>" + arr1[nannkaime2] + "</p>";
    nannkaime2++;
  }
}

const body = document.getElementsByTagName('body')[0];
let colorCount = 0;
const back_color = () => {
  if (colorCount % 2 === 0) {
    body.style.backgroundColor = 'skyblue';
    colorCount++;
  } else {
    body.style.backgroundColor = 'beige';
    colorCount++;
  }
}