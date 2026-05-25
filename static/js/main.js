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
