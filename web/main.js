

window.onload=function(){
    if(!navigator.onLine){
        Swal.fire(
          'No Internet?',
          'Checking the network cables, modem and router or Reconnecting to Wi-Fi',
          'question'
        )
     }
    var input = document.getElementById("myInput");
    input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("myBtn").click();
//        makeSendButton();
        }
    });
}

const chatBox = document.getElementById("chatBox");

function makeSendButton(){
    var myInput = document.getElementById("myInput");
	if (myInput && myInput.value && (myInput.value.length === 1)) {
  		document.getElementsByClassName('zmdi-mic')[0].className = "zmdi zmdi-mail-send";
	}
    else if(myInput.value.length === 0) {
    	document.getElementsByClassName('zmdi-mail-send')[0].className = "zmdi zmdi-mic";
    }
}

eel.expose(printUserText);
function printUserText(){
     if(!navigator.onLine){
        Swal.fire(
          'No Internet?',
          'Checking the network cables, modem and router or Reconnecting to Wi-Fi',
          'question'
        )
     }
    var userText = document.getElementsByClassName('input-msg')[0].value;
    if (userText){
        document.getElementsByClassName('input-msg')[0].value = "";
        console.log(userText);
        eel.check(userText);
        printUserDom(userText);
        makeSendButton();
    }
    else{
        eel.speechConversation()
    }
}

eel.expose(printUserDom);
function printUserDom(statment){
    shouldScroll = chatBox.scrollTop + chatBox.clientHeight === chatBox.scrollHeight;
    var DemoDom = document.createElement("p");
    DemoDom.innerText = statment;
    DemoDom.id = "usertext"
    chatBox.appendChild(DemoDom);
    if (!shouldScroll) {
       scrollToBottom();
    }
    return
}



eel.expose(printAgentDom);
function printAgentDom(statment){
    shouldScroll = chatBox.scrollTop + chatBox.clientHeight === chatBox.scrollHeight;

    var DemoDom = document.createElement("p");
    DemoDom.innerText = statment;
    DemoDom.id = "agenttext";
    chatBox.appendChild(DemoDom);
    if (!shouldScroll) {
       scrollToBottom();
    }
    return
}

function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

scrollToBottom();

eel.expose(selectPDF);
function selectPDF(moduleSelection){
    console.log("select pdf called")
    var DemoDom = document.createElement("input");
    DemoDom.setAttribute('type','file');
    DemoDom.setAttribute('name','myfile');
    DemoDom.id = "agenttext";
    DemoDom.setAttribute('class','selectButton');
    DemoDom.setAttribute('multiple','');
    DemoDom.setAttribute('onchange','showname("'+moduleSelection+'")')
    chatBox.appendChild(DemoDom);

}
eel.expose(showname);
function showname(moduleSelection){
    console.log("i am here");
    var file = document.getElementsByClassName('selectButton');
    var fileList = [];
    console.log(file[0].files.length)
    if (file[0].files.length > 0) {
        for (var i = 0; i < file[0].files.length; i++) {
            console.log("File name: ", file[0].files[i].name);
            fileList.push(file[0].files[i].name);
        }
        file[0].className = 'selectButtonDone';
        eel.getFileName(fileList, moduleSelection);
    }

//    console.log("i am here")
//    var name = document.getElementsByClassName('selectButton');
//    //console.log(name[0].files[0].name)
//    var fileList = [];
////    console.log(event.target.value)
////    console.log(event.target.files)
////    console.log(name[0].files.length)
////    console.log(name[0].files[0].name)
//    //eel.getFileName(name[0].files[0].name,moduleSelection);
//    if(name[0].files.length === 1){
//        console.log("File name: ", name[0].files[0].name)
//        var temp = name[0].files[0].name;
////        event.target.value = ''
//        eel.getFileName(temp,moduleSelection);
//    }
//    else{
//        for (var i = 0; i < name[0].files.length; i++) {
//            console.log("File name for loop: ", name[0].files[i].name)
//           fileList.push(name[0].files[i].name);
//        }
////        event.target.value = ''
//        eel.getFileName(fileList,moduleSelection);
//    }
//    return
}

eel.expose(getInput);
function getInput(){
    var DemoDom = document.createElement("input");
    DemoDom.setAttribute('type','text');
    DemoDom.id = "agenttext";
    DemoDom.setAttribute('class','inputBox');
    DemoDom.setAttribute('onchange','getInputText(this.value)')
    chatBox.appendChild(DemoDom);
    return
}

eel.expose(getInputText);
function getInputText(val){
    console.log("getting input text", val)
    console.log("getting input text", typeof val)
    eel.inputValue(val);
}

eel.expose(getPathInput);
function getPathInput(){
    var DemoDom = document.createElement("input");
    DemoDom.setAttribute('type','text');
    DemoDom.id = "agenttext";
    DemoDom.setAttribute('class','inputBox');
    DemoDom.setAttribute('onchange','getPathText(this.value)')
    chatBox.appendChild(DemoDom);
    return
}
eel.expose(getPathText);
function getPathText(val){
    console.log("Path text : ", val);
    eel.inputPathValue(val)
}

eel.expose(getSingleQueryInput);
function getSingleQueryInput(flag){
    var DemoDom = document.createElement("input");
    DemoDom.setAttribute('type','text');
    DemoDom.id = "agenttext";
    DemoDom.setAttribute('class','inputBox');
    DemoDom.setAttribute('onchange','getSingleQueryInputText(this.value, "'+flag+'")')
    chatBox.appendChild(DemoDom);
    return
}

eel.expose(getInputText);
function getSingleQueryInputText(val, flag){
    console.log("getting input text", val)
    console.log("flag--", flag)
    eel.SingleQueryinputValue(val, flag);
}
