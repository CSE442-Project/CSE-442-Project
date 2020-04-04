import { getCookie } from "./Cookies";


function asyncPost(xhr, url, onload, payload){
  xhr.open("POST", url, true);
  var csrfToken = getCookie("csrftoken");
  xhr.setRequestHeader("X-CSRFToken", csrfToken);
  xhr.onload = onload;
  xhr.send(payload);
}

function asyncGet(xhr, url, onload){
  xhr.open("GET", url, true);
  var csrfToken = getCookie("csrftoken");
  xhr.setRequestHeader("X-CSRFToken", csrfToken);
  xhr.onload = onload;
  xhr.send();
}

function checkForErrors(xhr){
  if(xhr.status === 200 || xhr.status === 201){
    return true;
  }else{
    alert("Server returned status code: " + xhr.status);
  }
}

function processServerDateTime(dt){
  //assuming format: 2019-12-10T17:50:41.092901Z
  var whenChunks = dt.split("T");
  var date = whenChunks[0];
  var dateChunks = date.split("-");
  var time = whenChunks[1];
  var timeChunks = time.split(":");
  return {
    year: dateChunks[0],
    month: dateChunks[1],
    date: dateChunks[2],
    hour: timeChunks[0],
    minute: timeChunks[1]
  };
}


function serverAddressToString(addr){
  var address = addr.street_1;
  if(addr.street_2 != ""){
    address += ", " + addr.street_2;
  }
  if(addr.street_3 != ""){
    address += ", " + addr.street_3;
  }
  address += ", " + addr.city + " " + addr.zip;
  return address;
}

export {
  asyncPost,
  asyncGet,
  checkForErrors,
  processServerDateTime,
  serverAddressToString
};
