document.getElementById("transcript").onclick = function () { transcriptScan() };

function transcriptScan() {

    document.getElementById("transcript").addEventListener("change",function(){
        var file = this.files[0];

        if (file) {
            var reader = new FileReader();

            reader.onerror = function (evt) {
                console.error("An error ocurred reading the file",evt);
            };

            reader.readAsText(file, "UTF-8");
        }
    },false);
}