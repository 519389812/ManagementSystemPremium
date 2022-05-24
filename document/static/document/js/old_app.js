var wrapper = document.getElementById("signature-pad");
var clearButton = wrapper.querySelector("[data-action=clear]");
var changeColorButton = wrapper.querySelector("[data-action=change-color]");
var undoButton = wrapper.querySelector("[data-action=undo]");
var savePNGButton = wrapper.querySelector("[data-action=save-png]");
var saveJPGButton = wrapper.querySelector("[data-action=save-jpg]");
var saveSVGButton = wrapper.querySelector("[data-action=save-svg]");
var canvas = wrapper.querySelector("canvas");
var signaturePad = new SignaturePad(canvas, {
  // It's Necessary to use an opaque color when saving image as JPEG;
  // this option can be omitted if only saving as PNG or SVG
  backgroundColor: 'rgb(255, 255, 255)'
});

// Adjust canvas coordinate space taking into account pixel ratio,
// to make it look crisp on mobile devices.
// This also causes canvas to be cleared.
function resizeCanvas() {
  // When zoomed out to less than 100%, for some very strange reason,
  // some browsers report devicePixelRatio as less than 1
  // and only part of the canvas is cleared then.
  var ratio =  Math.max(window.devicePixelRatio || 1, 1);

  // This part causes the canvas to be cleared
  canvas.width = canvas.offsetWidth * ratio;
  canvas.height = canvas.offsetHeight * ratio;
  canvas.getContext("2d").scale(ratio, ratio);

  // This library does not listen for canvas changes, so after the canvas is automatically
  // cleared by the browser, SignaturePad#isEmpty might still return false, even though the
  // canvas looks empty, because the internal data of this library wasn't cleared. To make sure
  // that the state of this library is consistent with visual state of the canvas, you
  // have to clear it manually.
  signaturePad.clear();
}

// On mobile devices it might make more sense to listen to orientation change,
// rather than window resize events.
window.onresize = resizeCanvas;
resizeCanvas();

function download(dataURL, filename) {
  if (navigator.userAgent.indexOf("Safari") > -1 && navigator.userAgent.indexOf("Chrome") === -1) {
    window.open(dataURL);
  } else {
    var blob = dataURLToBlob(dataURL);
    var url = window.URL.createObjectURL(blob);

    var a = document.createElement("a");
    a.style = "display: none";
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    window.URL.revokeObjectURL(url);
  }
}

// One could simply use Canvas#toBlob method instead, but it's just to show
// that it can be done using result of SignaturePad#toDataURL.
function dataURLToBlob(dataURL) {
  // Code taken from https://github.com/ebidel/filer.js
  var parts = dataURL.split(';base64,');
  var contentType = parts[0].split(":")[1];
  var raw = window.atob(parts[1]);
  var rawLength = raw.length;
  var uInt8Array = new Uint8Array(rawLength);

  for (var i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }

  return new Blob([uInt8Array], { type: contentType });
}

clearButton.addEventListener("click", function (event) {
  signaturePad.clear();
});

undoButton.addEventListener("click", function (event) {
  var data = signaturePad.toData();

  if (data) {
    data.pop(); // remove the last dot or line
    signaturePad.fromData(data);
  }
});

changeColorButton.addEventListener("click", function (event) {
  var r = Math.round(Math.random() * 255);
  var g = Math.round(Math.random() * 255);
  var b = Math.round(Math.random() * 255);
  var color = "rgb(" + r + "," + g + "," + b +")";

  signaturePad.penColor = color;
});

function getCookie(name){
  var strcookie = document.cookie;
  var arrcookie = strcookie.split("; ");
  for ( var i = 0; i < arrcookie.length; i++) {
    var arr = arrcookie[i].split("=");
    if (arr[0] == name){
      return arr[1];
    }
  }
  return "";
  }

function randomNum(n) {
  let sString = "";
  let strings = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  for (i = 0; i < n; i++) {
    ind = Math.floor(Math.random() * strings.length);
    sString += strings.charAt(ind);
  }
  return sString;
}

function aesEncrypt(data, key) {
  var k = CryptoJS.enc.Utf8.parse(key);
  var d = CryptoJS.enc.Utf8.parse(data);
  var encrypted = CryptoJS.AES.encrypt(d, k, {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7});
  return encrypted.toString();
}

savePNGButton.addEventListener("click", function (event) {
  if (signaturePad.isEmpty()) {
    alert("请先签名！");
  } else {
    var key = randomNum(16);
    var dataURL = aesEncrypt(encodeURIComponent(signaturePad.toDataURL()), key);
//    var dataURL = encodeURIComponent(signaturePad.toDataURL());
    var xhr=new XMLHttpRequest();
    var cxck = getCookie("csrftoken");
    if (contentId!="") {
      var jsonData = JSON.stringify({
        "data": dataURL,
        "docx_id": docxId,
        "content_id": contentId,
        "key": key,
      });
      xhr.open('post','/document/fill_signature/', true);
    } else {
      var jsonData = JSON.stringify({
        "data": dataURL,
        "docx_id": docxId,
        "signature_key": signatureKey,
        "key": key,
      });
      xhr.open('post','/document/supervisor_signature/', true);
    }
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader("X-CSRFToken", cxck);
    xhr.onreadystatechange = function () {  //绑定响应状态事件监听函数
      if (xhr.readyState == 4) {  //监听readyState状态
        if (xhr.status == 200 || xhr.status == 0) {  //监听HTTP状态码
          alert("提交成功，页面将自动跳转！");  //接收数据
        } else {
          alert("提交失败！");
        }
        window.location.href = "/document/view_docx/" + docxId;
      }
    }
    xhr.send(jsonData);
    alert("签名成功，请等待页面反馈！");
  }
});

//saveJPGButton.addEventListener("click", function (event) {
//  if (signaturePad.isEmpty()) {
//    alert("Please provide a signature first.");
//  } else {
//    var dataURL = signaturePad.toDataURL("image/jpeg");
//    download(dataURL, "signature.jpg");
//  }
//});
//
//saveSVGButton.addEventListener("click", function (event) {
//  if (signaturePad.isEmpty()) {
//    alert("Please provide a signature first.");
//  } else {
//    var dataURL = signaturePad.toDataURL('image/svg+xml');
//    download(dataURL, "signature.svg");
//  }
//});
