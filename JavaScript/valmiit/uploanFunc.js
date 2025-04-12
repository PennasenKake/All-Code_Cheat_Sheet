

function displayImage() {
    const input = document.getElementById("upload-input");
    const file = input.file[0];
}
if (file) {
    const reader = new FileReader();
    reader.onload = function(event) { 
        const imageDataUrl = event.target.result;
        updateImageSrc(imageDataUrl);
    };
    reader.onerror = function(error) {
        console.error("Error reading the file: " + error.message);
    };
    reader.readAsDataURL(file);
}