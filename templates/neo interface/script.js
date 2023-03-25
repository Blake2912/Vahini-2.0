const lights = document.querySelectorAll('.js-headlights'),
  lightsWrap = document.querySelectorAll('.js-headlights-wrap'),
  car = document.querySelector('.js-car-svg'),
  btn = document.getElementById('start/stop'),
  btnText = document.querySelector('.js-btn-text'),
  body = document.getElementsByTagName('body')[0],
  brightness = 210,
  brightnessOff = 0;
// document.querySelector('.car__inner').style.animation =
//   'move 0.8s infinite linear';
let headlightsInterval = null;

// btn.onclick = () => {
//   let dataStatus = btn.getAttribute('data-status'),
//     textOn = btn.getAttribute('data-text-on'),
//     textOff = btn.getAttribute('data-text-off');

//   if ('off' == dataStatus) {
//     btn.setAttribute('data-status', 'on');
//     btnText.textContent = textOff;
//     for (let i = 0; i < lights.length; i++) {
//       lights[i].style.setProperty('--size', brightness + 'px');
//     }
//     car.style.setProperty('--opacity', 1);

//     // headlightsInterval = setInterval(_headlightsMove, 20);
//   } else {
    
//     btn.setAttribute('data-status', 'off');
//     btnText.textContent = textOn;
//     for (let i = 0; i < lights.length; i++) {
//       lights[i].style.setProperty('--size', brightnessOff + 'px');
//     }
//     car.style.setProperty('--opacity', 0.8);
//     clearInterval(headlightsInterval);
//     for (let i = 0; i < lightsWrap.length; i++) {
//       lightsWrap[i].style.setProperty('--x', 0 + 'px');
//       lightsWrap[i].style.setProperty('--y', 0 + 'px');
//     }
//   }
// };

btn.onclick = () => {
  let dataStatus = btn.getAttribute('data-status'),
    textOn = btn.getAttribute('data-text-on'),
    textOff = btn.getAttribute('data-text-off');

  if ('off' == dataStatus) {
    btn.setAttribute('data-status', 'on');
    btnText.textContent = textOff;
    for (let i = 0; i < lights.length; i++) {
      lights[i].style.setProperty('--size', brightness + 'px');
    }
    car.style.setProperty('--opacity', 1);

    // Add animation to car__inner
    document.querySelector('.car__inner').style.animation =
      'move 0.8s infinite linear';

    // headlightsInterval = setInterval(_headlightsMove, 20);
  } else {
    document.querySelector('.car__inner').style.animation =
      '';
    btn.setAttribute('data-status', 'off');
    btnText.textContent = textOn;
    for (let i = 0; i < lights.length; i++) {
      lights[i].style.setProperty('--size', brightnessOff + 'px');
    }
    car.style.setProperty('--opacity', 0.8);
    clearInterval(headlightsInterval);
    for (let i = 0; i < lightsWrap.length; i++) {
      lightsWrap[i].style.setProperty('--x', 0 + 'px');
      lightsWrap[i].style.setProperty('--y', 0 + 'px');
    }
  }
};


function _headlightsMove() {
  let dataStatus = btn.getAttribute('data-status');
  if ('on' == dataStatus) {
    let x = Math.random() * 10 - 5;
    let y = Math.random() * 10 - 5;

    for (let i = 0; i < lightsWrap.length; i++) {
      lightsWrap[i].style.setProperty('--x', x + 'px');
      lightsWrap[i].style.setProperty('--y', y + 'px');
    }
  }
}
// JavaScript used to set randomness for particles.
// Could be done via SSR

const RANDOM = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);
const PARTICLES = document.querySelectorAll('.particle');
PARTICLES.forEach(P => {
  P.setAttribute('style', `
		--x: ${RANDOM(20, 80)};
		--y: ${RANDOM(20, 80)};
		--duration: ${RANDOM(6, 20)};
		--delay: ${RANDOM(1, 10)};
		--alpha: ${RANDOM(40, 90) / 100};
		--origin-x: ${Math.random() > 0.5 ? RANDOM(300, 800) * -1 : RANDOM(300, 800)}%;
		--origin-y: ${Math.random() > 0.5 ? RANDOM(300, 800) * -1 : RANDOM(300, 800)}%;
		--size: ${RANDOM(40, 90) / 100};
	`);
});


// JUST FOR BACKGROUND CHANGE
const toggle = document.querySelector('#toggle');

const updateBackground = (event) => { 
document.body.classList.toggle('on');
}

toggle.addEventListener("click", () => document.body.classList.toggle('on') , false);