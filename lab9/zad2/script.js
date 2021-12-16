const iterations = 50;
const multiplier = 1000000000;

function calculatePrimes(iterations, multiplier) {
  var primes = [];
  for (var i = 0; i < iterations; i++) {
    var candidate = i * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
  }
  return primes;
}

let SetIntervalTime = []
let SetTimeoutTime = []

let N = 21;

let intervalID;
let timeoutID;

function start() {
    let M = parseInt(document.forms[0].delay.value);
    setIntervalId = setInterval(doTimeConsumingCallculationsWithSetInterval, M);
    setTimeoutId = setTimeout(doTimeConsumingCallculationsWithSetTimeout, M);
    requestAnimationFrame(drawChart);
}   

document.forms[0].start.onclick = start


document.forms[0].stop.onclick = function () {
    console.log('stop');
    clearInterval(setInterId);
    clearTimeout(timeoutID);
    
}

function doTimeConsumingCallculationsWithSetInterval(){
    SetIntervalTime.push(performance.now());
    if (SetIntervalTime.length > N) {SetIntervalTime.shift();}
    calculatePrimes(1000, 100000000);
}

function doTimeConsumingCallculationsWithSetTimeout(){
    SetTimeoutTime.push(performance.now());
    if (SetTimeoutTime.length > N) {SetTimeoutTime.shift();}
    calculatePrimes(1000, 100000000);
    let M = parseInt(document.forms[0].delay.value);
    timeoutID = setTimeout(doTimeConsumingCallculationsWithSetTimeout, M);
}

function drawChart(){
    let intervalValues = [];
    let timeoutValues = [];
    for (let i = 1 ; i < SetIntervalTime.length; i++){
        intervalValues.push({x: i, y: SetIntervalTime[i] - SetIntervalTime[i - 1]});
    }
    for (let i = 1 ; i < SetTimeoutTime.length; i++){
        timeoutValues.push({x: i, y: SetTimeoutTime[i] - SetTimeoutTime[i - 1]});
    }
    var chart = new CanvasJS.Chart("chartContainer",{
        title:{
        text: "Output time"
        },
        data: [
        {
            type: "line",
            dataPoints: intervalValues
        },
        {
            type: "line",
            dataPoints: timeoutValues
        }
    ]
    });
    chart.render();
    requestAnimationFrame(drawChart);
}