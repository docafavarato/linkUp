$(document).ready(function() {
    $("#loginButton").click(function(e) {
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

$("#fileInput").change(function() {
    filename = this.files[0].name;
    console.log("Mudou");
    console.log(filename);
});


$(document).ready(function() {
    const currentUrl = window.location.href;
    if (currentUrl.includes("/linkup/all")) {
        document.querySelector(".sourceAll").classList.add("current");
    } else if (currentUrl.includes("/linkup/following")) {
        document.querySelector(".sourceFollowing").classList.add("current");
    }
})