var constraints = {
  video: { facingMode: "user" },
  audio: false,
};

const cameraView = document.querySelector("#camera-view"),
  cameraSensor = document.querySelector("#camera-sensor"),
  cameraOutput = document.querySelector("#camera-output"),
  cameraTriger = document.querySelector("#camera-triger");

const filterBtn = [...document.querySelectorAll("#filter")];

/*cameraTriger.onclick=function() {
  cameraSensor.width=cameraView.videoWidth; 
  cameraSensor.height=cameraView.videoHeight;
  cameraSensor.getContext("2d").drawImage(cameraView,0 ,0);
  cameraOutput.src=cameraSensor.toDataURL();
  cameraOutput.classList.add('taken');
}*/

function cameraStart() {
  navigator.mediaDevices
  .getUserMedia(constraints)
  .then(function (stream) {
    track = stream.getTracks()[0];
    cameraView.srcObject=stream;
  })
  .catch(function (error) {
    console.error("Ooopss une erreur"+error);
  });

  /*setInterval(() => {
    cameraTriger.click()
  }, 1000);*/
}

  function addCanvas() {
    const width=video.videoWidith;
    const height=video.videoHeight;
    let filterType=this.dataset.filter || 0;
    console.log(this.dataset, 'this' , filterType);
  }

  

  document.getElementById('scanner').addEventListener('click', cameraStart, false)
