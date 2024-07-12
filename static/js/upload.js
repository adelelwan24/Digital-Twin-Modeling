function updateFileName(inputId) {
    var input = document.getElementById(inputId);
    var label = input.nextElementSibling;
    if (input.files.length > 0) {
        var fileName = input.files[0].name;
        label.textContent = fileName;
    }
}


function showCustomAlert() {
    var alertBox = document.getElementById('customAlert');
    alertBox.classList.add('show');

    setTimeout(function() {
        alertBox.classList.remove('show');
    }, 7000);
}    

function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    e.target.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    e.target.classList.remove('dragover');
}

function handleDrop(e, inputId) {
    e.preventDefault();
    e.stopPropagation();
    e.target.classList.remove('dragover');

    var input = document.getElementById(inputId);
    input.files = e.dataTransfer.files;
    updateFileName(inputId);
}
