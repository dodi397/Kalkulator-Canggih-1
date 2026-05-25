document.addEventListener('DOMContentLoaded', () => {
  const root = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const historyBtn = document.getElementById('historyBtn');
  const historyPanel = document.getElementById('historyPanel');

  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    root.setAttribute('data-theme', savedTheme);
  }

  function setTheme(theme) {
    root.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      setTheme(current === 'dark' ? 'light' : 'dark');
      playClick();
    });
  }

  if (historyBtn && historyPanel) {
    historyBtn.addEventListener('click', () => {
      historyPanel.classList.toggle('d-none');
      historyPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
      playClick();
    });
  }

  // Logic form: NOT only needs A
  const logicOp = document.getElementById('logicOp');
  const logicBwrap = document.getElementById('logicBwrap');
  const logicB = document.getElementById('logicB');
  const logicA = document.getElementById('logicA');

  function updateLogicFields() {
    if (!logicOp || !logicBwrap) return;
    const isNot = logicOp.value === 'not';
    logicBwrap.classList.toggle('d-none', isNot);
    if (logicB) logicB.required = !isNot;
    if (logicA) logicA.required = true;
  }

  if (logicOp) {
    logicOp.addEventListener('change', updateLogicFields);
    updateLogicFields();
  }

  // Transform form field switching
  const transformMode = document.getElementById('transformMode');
  const valueWrap = document.getElementById('valueWrap');
  const countWrap = document.getElementById('countWrap');
  const valueLabel = document.getElementById('valueLabel');
  const baseFields = document.getElementById('baseFields');
  const tempFields = document.getElementById('tempFields');
  const currencyFields = document.getElementById('currencyFields');
  const transformValue = document.getElementById('transformValue');
  const transformCount = document.getElementById('transformCount');

  function updateTransformFields() {
    if (!transformMode) return;
    const mode = transformMode.value;

    baseFields.classList.toggle('d-none', mode !== 'base');
    tempFields.classList.toggle('d-none', mode !== 'temperature');
    currencyFields.classList.toggle('d-none', mode !== 'currency');

    const showCount = mode === 'factorial' || mode === 'fibonacci';
    if (valueWrap) valueWrap.classList.toggle('d-none', showCount);
    if (countWrap) countWrap.classList.toggle('d-none', !showCount);

    if (valueLabel) {
      if (mode === 'base') valueLabel.textContent = 'Nilai';
      if (mode === 'temperature') valueLabel.textContent = 'Nilai Suhu';
      if (mode === 'currency') valueLabel.textContent = 'Jumlah';
    }

    if (transformValue) {
      transformValue.required = !showCount;
    }
    if (transformCount) {
      transformCount.required = showCount;
    }
  }

  if (transformMode) {
    transformMode.addEventListener('change', updateTransformFields);
    updateTransformFields();
  }

  // Arithmetic sqrt uses single input
  const arithOp = document.getElementById('arithOp');
  const arithSecondWrap = document.getElementById('arithSecondWrap');
  if (arithOp && arithSecondWrap) {
    const updateArithmeticFields = () => {
      const isUnary = arithOp.value === 'sqrt';
      arithSecondWrap.classList.toggle('d-none', isUnary);
      const bInput = arithSecondWrap.querySelector('input');
      if (bInput) bInput.required = !isUnary;
    };
    arithOp.addEventListener('change', updateArithmeticFields);
    updateArithmeticFields();
  }

  // Click sounds for all clickable elements
  document.querySelectorAll('a, button, select, input, .sound-click').forEach((el) => {
    el.addEventListener('click', () => playClick(), { passive: true });
  });
  document.querySelectorAll('button[type="submit"]').forEach((el) => {
    el.addEventListener('submit', () => playClick(), { passive: true });
  });
});

function playClick() {
  try {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) return;
    const ctx = new AudioContextClass();
    const oscillator = ctx.createOscillator();
    const gain = ctx.createGain();
    oscillator.type = 'triangle';
    oscillator.frequency.value = 700;
    gain.gain.value = 0.06;
    oscillator.connect(gain);
    gain.connect(ctx.destination);
    oscillator.start();
    setTimeout(() => {
      oscillator.stop();
      ctx.close();
    }, 110);
  } catch (e) {}
}

/* MAIN.JS */

const canvas=document.getElementById("matrix-bg");

if(canvas){

const ctx=canvas.getContext("2d");

let w=canvas.width=window.innerWidth;
let h=canvas.height=window.innerHeight;

window.addEventListener("resize",()=>{

w=canvas.width=window.innerWidth;
h=canvas.height=window.innerHeight;

columns=Math.floor(w/fontSize);

});

const chars="010101010101";
const fontSize=15;

let columns=Math.floor(w/fontSize);

const rain=[];

for(let i=0;i<columns;i++){

rain[i]+=0.2;

}

const nodes=[];

for(let i=0;i<70;i++){

nodes.push({

x:Math.random()*w,
y:Math.random()*h,

vx:(Math.random()-.5)*0.7,
vy:(Math.random()-.5)*0.7,

size:Math.random()*2+1

});

}

let hue=220;
let gridOffset=0;

function drawBackground(){

const bg=ctx.createLinearGradient(0,0,0,h);

bg.addColorStop(0,"#040816");
bg.addColorStop(.5,"#050816");
bg.addColorStop(1,"#02030a");

ctx.fillStyle=bg;

ctx.fillRect(0,0,w,h);

}

function drawGrid(){

gridOffset+=0.15;

const gridSize=40;

ctx.lineWidth=1;

for(let x=-gridSize;x<w+gridSize;x+=gridSize){

ctx.beginPath();

ctx.strokeStyle=`hsla(${hue},100%,60%,0.08)`;

ctx.moveTo(x+gridOffset,0);

ctx.lineTo(x-gridOffset,h);

ctx.stroke();

}

for(let y=-gridSize;y<h+gridSize;y+=gridSize){

ctx.beginPath();

ctx.strokeStyle=`hsla(${hue},100%,60%,0.05)`;

ctx.moveTo(0,y+gridOffset);

ctx.lineTo(w,y-gridOffset);

ctx.stroke();

}

}

function drawFlowLines(){

for(let i=0;i<5;i++){

const y=(i*120+gridOffset*8)%h;

const gradient=ctx.createLinearGradient(0,y,w,y);

gradient.addColorStop(0,"transparent");

gradient.addColorStop(.5,`hsla(${hue},100%,65%,0.25)`);

gradient.addColorStop(1,"transparent");

ctx.beginPath();

ctx.strokeStyle=gradient;

ctx.lineWidth=2;

ctx.moveTo(0,y);

ctx.lineTo(w,y);

ctx.stroke();

}

}

function drawRain(){

ctx.font=fontSize+"px monospace";

for(let i=0;i<rain.length;i++){

const text=chars.charAt(Math.floor(Math.random()*chars.length));

const x=i*fontSize;

const y=rain[i]*fontSize;

ctx.fillStyle=`hsla(${hue},100%,70%,0.95)`;

ctx.shadowBlur=6;

ctx.shadowColor=`hsl(${hue},100%,60%)`;

ctx.fillText(text,x,y);

if(y>h&&Math.random()>.975){

rain[i]=0;

}

rain[i]++;

}

}

function drawNodes(){

nodes.forEach(n=>{

n.x+=n.vx;
n.y+=n.vy;

if(n.x<0||n.x>w){

n.vx*=-1;

}

if(n.y<0||n.y>h){

n.vy*=-1;

}

ctx.beginPath();

ctx.arc(n.x,n.y,n.size,0,Math.PI*2);

ctx.fillStyle=`hsla(${hue},100%,70%,1)`;

ctx.shadowBlur=8;

ctx.shadowColor=`hsl(${hue},100%,60%)`;

ctx.fill();

});

}

function drawConnections(){

for(let i=0;i<nodes.length;i++){

for(let j=i;j<nodes.length;j++){

const dx=nodes[i].x-nodes[j].x;

const dy=nodes[i].y-nodes[j].y;

const dist=Math.sqrt(dx*dx+dy*dy);

if(dist<70){

ctx.beginPath();

ctx.strokeStyle=`hsla(${hue},100%,65%,${0.16-dist/900})`;

ctx.lineWidth=.7;

ctx.moveTo(nodes[i].x,nodes[i].y);

ctx.lineTo(nodes[j].x,nodes[j].y);

ctx.stroke();

}

}

}

}

function drawGlow(){

const glow=ctx.createRadialGradient(w/2,h/2,80,w/2,h/2,500);

glow.addColorStop(0,`hsla(${hue},100%,60%,0.12)`);

glow.addColorStop(.5,`hsla(${hue},100%,60%,0.04)`);

glow.addColorStop(1,"transparent");

ctx.fillStyle=glow;

ctx.fillRect(0,0,w,h);

}

function animate(){

hue+=0.25;

if(hue>280){

hue=220;

}

drawBackground();

drawGrid();

drawConnections();

drawFlowLines();

drawNodes();

drawRain();

drawGlow();

requestAnimationFrame(animate);

}

animate();

}