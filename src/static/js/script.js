function uploadImage(idInput, idImage) {
  var input = document.getElementById(idInput);
  if (input.files.length == 0) {
    return;
  }

  let file = input.files[0];
  let url = URL.createObjectURL(file);
  document.getElementById(idImage).src = url;
}

//uploadImage('image', 'imageView');

function assignedValue(idInput, idList) {
  var id1 = document.getElementById(idInput);
  var id2 = document.getElementById(idList).textContent;
  id1.value = id2.trim().toString();
}

var btns=document.querySelectorAll(".nav-item")

function menu(i,path) {
  console.log(i+" "+window.location.pathname==path)
  if(window.location.pathname==path){
    btns[i].className="nav-item w-100 active"
  }


}

menu(0,"/");
menu(1,"/agence/")
menu(2,"/postes/");
menu(3,"/conges/")
menu(4,"/presences/")

