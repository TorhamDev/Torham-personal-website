let audios = document.querySelectorAll("audio");

function setAudio(audio) {
  audio.load();
  let index = audio.dataset.index;
  let buttons = document.querySelector(`.button-group-${index}`);
  let play = buttons.querySelector(".play");
  let pause = buttons.querySelector(".pause");
  let fast = buttons.querySelector(".forward");
  let slow = buttons.querySelector(".backward");
  let playrate = buttons.querySelector(".playrate");
  let backw = buttons.querySelector(".backw");
  let forw = buttons.querySelector(".forw");
  playrate.innerHTML = `${Math.floor(audio.currentTime / 600)}${Math.floor(
    (audio.currentTime / 60) % 10
  )}:${Math.floor((audio.currentTime / 10) % 6)}${Math.floor(
    audio.currentTime % 10
  )}`;
  play.addEventListener("click", (e) => {
    play.style.display = "none";
    pause.style.display = "flex";
    audio.play();
  });
  pause.addEventListener("click", (e) => {
    pause.style.display = "none";
    play.style.display = "flex";
    audio.pause();
  });
  fast.addEventListener("click", (e) => {
    audio.playbackRate += 0.25;
  });
  slow.addEventListener("click", (e) => {
    audio.playbackRate -= 0.25;
  });
  backw.addEventListener("click", (e) => {
    audio.currentTime -= 5;
  });
  forw.addEventListener("click", (e) => {
    audio.currentTime += 5;
  });
  setInterval(() => {
    playrate.innerHTML = `${Math.floor(audio.currentTime / 600)}${Math.floor(
      (audio.currentTime / 60) % 10
    )}:${Math.floor((audio.currentTime / 10) % 6)}${Math.floor(
      audio.currentTime % 10
    )}`;
  }, 1000);
}

audios.forEach(setAudio);
