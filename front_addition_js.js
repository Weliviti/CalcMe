let numA, numB, answer;
let startTime;
let currentRound = 1;
const totalRounds = 10;
let totalCorrect = 0;
let totalTime = 0;

function newRound() {
  numA = Math.floor(Math.random() * 50);
  numB = Math.floor(Math.random() * 50);
  answer = numA + numB;
  document.getElementById("numA").textContent = numA;
  document.getElementById("numB").textContent = numB;
  document.getElementById("guess").value = "";
  document.getElementById("result").textContent = "";
  document.getElementById("time").textContent = "0.00";
  startTime = Date.now();
}

function submitGuess() {
  const guess = Number(document.getElementById("guess").value);
  if (!guess && guess !== 0) return;

  const endTime = Date.now();
  const timeTaken = ((endTime - startTime) / 1000).toFixed(2);
  document.getElementById("time").textContent = timeTaken;

  const result = document.getElementById("result");
  totalTime += parseFloat(timeTaken);

  if (guess === answer) {
    result.textContent = "Correct! The answer is " + answer;
    result.className = "correct";
    totalCorrect++;
  } else {
    result.textContent = "Wrong! Correct answer was " + answer;
    result.className = "wrong";
  }
}

function nextRound() {
  if (currentRound < totalRounds) {
    currentRound++;
    document.getElementById("currentRound").textContent = currentRound;
    newRound();
  } else {
    alert(`Game over!\nTotal Correct: ${totalCorrect} / ${totalRounds}\nTotal Time: ${totalTime.toFixed(2)} sec`);
    currentRound = 1;
    totalCorrect = 0;
    totalTime = 0;
    document.getElementById("currentRound").textContent = currentRound;
    newRound();
  }
}

newRound();