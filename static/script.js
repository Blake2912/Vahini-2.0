const toggle = document.getElementById('toggle');
const automatebttn = document.getElementById('automate');
const right = document.getElementById('right');
const left = document.getElementById('left');
const forward = document.getElementById('forward');
const reverse = document.getElementById('reverse');
toggle.addEventListener('change', function () {
  if (this.checked) {
    fetch('/on').then(console.log('on'));
  } else {
        fetch('/off').then(console.log('off'));
  }
});
const RANDOM = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);
const PARTICLES = document.querySelectorAll('.particle');
PARTICLES.forEach((P) => {
  P.setAttribute(
    'style',
    `
		--x: ${RANDOM(20, 80)};
		--y: ${RANDOM(20, 80)};
		--duration: ${RANDOM(6, 20)};
		--delay: ${RANDOM(1, 10)};
		--alpha: ${RANDOM(40, 90) / 100};
		--origin-x: ${Math.random() > 0.5 ? RANDOM(300, 800) * -1 : RANDOM(300, 800)}%;
		--origin-y: ${Math.random() > 0.5 ? RANDOM(300, 800) * -1 : RANDOM(300, 800)}%;
		--size: ${RANDOM(40, 90) / 100};
	`
  );
});
automatebttn.addEventListener('click', function () {
  fetch('/automate_vehicle').then(console.log('automate'));
});
right.addEventListener('click', function () {
  fetch('/right').then(console.log('right'));
}
);
left.addEventListener('click', function () {
    fetch('/left').then(console.log('left'));
}   
);
forward.addEventListener('click', function () {
    fetch('/forward').then(console.log('forward'));
}
);
reverse.addEventListener('click', function () {
    fetch('/reverse').then(console.log('reverse'));
}   
);


