$(document).ready(function () {
    $("#loginButton").click(function (e) {
        $(".alert").fadeIn("slow");
    });
});

$(function () {
    $(".postModal").draggable({
        handle: ".modal-header",
    });
});

function toggleText(element) {
    if (element.innerText.includes("View")) {
        element.innerText = element.innerText.replace("View", "Hide");
    } else {
        element.innerText = element.innerText.replace("Hide", "View");
    }
}

function addDateMask(input) {
    input.addEventListener('input', function (event) {
        // Remove caracteres não numéricos
        let inputValue = event.target.value.replace(/\D/g, '');

        // Formata a data (dd/MM/yyyy)
        if (inputValue.length > 2) {
            inputValue = inputValue.substring(0, 2) + '/' + inputValue.substring(2);
        }
        if (inputValue.length > 5) {
            inputValue = inputValue.substring(0, 5) + '/' + inputValue.substring(5, 9);
        }

        event.target.value = inputValue;
    });
}

window.onload = function () {
    const dateInput = document.getElementById('birthDateInput');
    addDateMask(dateInput);
};

$(document).ready(function () {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
});

$("#fileInput").change(function () {
    filename = this.files[0].name;
    console.log("Mudou");
    console.log(filename);
});


$(document).ready(function () {
    const currentUrl = window.location.href;
    if (currentUrl.includes("/linkup/all")) {
        document.querySelector(".sourceAll").classList.add("current");
    } else if (currentUrl.includes("/linkup/following")) {
        document.querySelector(".sourceFollowing").classList.add("current");
    }

    var realInput = document.getElementById("postImageFile");
    realInput.addEventListener("change", function (ev) {
        var fakeInput = document.getElementById("postImageFileButton");
        if (realInput.files.length > 0) {
            fakeInput.innerHTML = `
                <div>
                    ${realInput.files[0].name}
                    <button style="border: none; background-color: none;" type="button" onclick="clearPostImageInput();"><i class="fa-solid fa-x"></i></button>
                </div>
            `;
        } else {
            fakeInput.setAttribute("placeholder", "Select an image");
        }
    });
})

function clearPostImageInput() {
    var realInput = document.getElementById("postImageFile");
    var fakeInput = document.getElementById("postImageFileButton");

    realInput.value = null;
    fakeInput.innerHTML = null;
    fakeInput.innerHTML = `
            <i class="fa-solid fa-cloud-arrow-up"></i>
            Select an image
    `;
}

function handlePostImageInput() {
    var realInput = document.getElementById("postImageFile");
    realInput.click();
}

$(document).ready(function () {
    var dropArea = document.getElementById("postImageFileButton");
    var fileInput = document.getElementById("postImageFile");

    ['dragover', 'dragenter', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false)
    });

    ['dragover', 'dragenter'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false)
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false)
    });

    dropArea.addEventListener('drop', handleDrop, false);

    function preventDefaults(event) {
        event.preventDefault();
        event.stopPropagation();
    }

    function highlight() {
        dropArea.style.background = "#f2f2f2";
    }

    function unhighlight() {
        dropArea.style.background = "#fff";
    }

    function handleDrop(event) {
        var dt = event.dataTransfer;
        var files = dt.files;

        fileInput.files = files;
        handleFiles(files);
    }

    fileInput.addEventListener('change', function (event) {
        var files = event.target.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        var fakeInput = document.getElementById("postImageFileButton");
        if (fileInput.files.length > 0) {
            fakeInput.innerHTML = `
                <div>
                    ${fileInput.files[0].name}
                    <button style="border: none; background-color: none;" type="button" onclick="clearPostImageInput();"><i class="fa-solid fa-x"></i></button>
                </div>
            `;
        } else {
            fakeInput.setAttribute("placeholder", "Select an image");
        }
    }
})