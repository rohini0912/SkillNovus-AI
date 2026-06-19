a// Function to send question to backend
async function askAI() {

    // Get user's question
    let question = document.getElementById("question").value;

    // Check if input is empty
    if(question==""){
        return;
    }

    // Show loading message
    document.getElementById("response").innerText =
    "Generating response...";

    // Send request to FastAPI backend
   try{

    let response =
    await fetch(
    `http://127.0.0.1:8000/chat?question=${encodeURIComponent(question)}`
    );

    let data =
    await response.json();

    document.getElementById("response").innerText =
    data.response;

}
catch(error){

    document.getElementById("response").innerText =
    "Unable to connect to AI server.";

}

}
