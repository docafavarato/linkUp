$(document).ready(function () {
    $("#loginButton").click(function (e) {
        $(".alert").fadeIn("slow");
    });

    const inputField = document.getElementById("tag-name-input");
    const hashtagContainer = document.getElementById("hashtags");
    const addButton = document.getElementById("add-tag-button");
    addButton.addEventListener("click", function () {

        if (countNonEmptyDivs() >= 5) { return; }

        const hashtag = inputField.value.trim();
        if (hashtag !== "") {
            const hiddenInput = document.createElement("input");
            hiddenInput.type = "hidden";
            hiddenInput.name = "tags";
            hiddenInput.value = hashtag;
            hiddenInput.style.display = "none";
            document.getElementById("postForm").appendChild(hiddenInput);
            const hashtagElement = document.createElement("div");
            hashtagElement.innerHTML = `
                <div class="hashtag" id="hashtag-${hashtag}">
                    <button type="button" class="remove-hashtag-button btn btn-outline-primary" onclick="removeTag('hashtag-${hashtag}')">
                        <span class="hashtag-text">${hashtag}</span>
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>
            `
            hashtagContainer.appendChild(hashtagElement);
            inputField.value = "";
        }
    });

    const publishButton = document.getElementById('publishButton');

    publishButton.addEventListener("click", function () {
        setTimeout(function () {
            document.getElementById('postForm').reset();
        }, 1000);
    });
});

function countNonEmptyDivs() {
    var nonEmptyDivsCount = 0;
    var hashtags = document.querySelectorAll('.hashtag');
    hashtags.forEach(function (div) {
        if (div.innerHTML.trim() !== '') {
            nonEmptyDivsCount++;
        }
    });
    return nonEmptyDivsCount;
}

function removeTag(id) {
    var hiddenInput = document.querySelector('input[name="tags"][value="' + id.split('hashtag-')[1] + '"]');
    hiddenInput.parentNode.removeChild(hiddenInput);

    var tag = document.getElementById(id);
    tag.remove();
}

function isTagAlreadyAdded(tag) {
    const hiddenInput = document.querySelector('input[name="tags"]');
    const tags = hiddenInput.value.split(",");
    return tags.includes(tag);
}

$(function () {
    var modals = document.querySelectorAll(".modal");
    modals.forEach(modal => {
        $(modal).draggable({
            handle: ".modal-header",
        });
    })
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
        let inputValue = event.target.value.replace(/\D/g, '');
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

function loadToolTips() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
}

$(document).ready(function () {
    loadToolTips();
});


document.addEventListener('htmx:afterSwap', function (event) {
    loadToolTips();
});

$("#fileInput").change(function () {
    filename = this.files[0].name;
});


document.addEventListener('DOMContentLoaded', function () {
    var followButtons = document.querySelectorAll('.follow-button');
    followButtons.forEach(function (button) {
        button.addEventListener('mouseover', function () {
            if (this.textContent.trim() === 'Following') {
                this.textContent = 'Unfollow';
            }
        });
        button.addEventListener('mouseout', function () {
            if (this.textContent.trim() === 'Unfollow') {
                this.textContent = 'Following';
            }
        });
    });
});

$(document).ready(function () {
    const currentUrl = window.location.href;
    if (currentUrl.includes("/source%3Dall")) {
        document.querySelector(".sourceAll").classList.add("current");
    } else if (currentUrl.includes("/source%3Dfollowing")) {
        document.querySelector(".sourceFollowing").classList.add("current");
    } else if (currentUrl.includes("/source%3Dprofile-posts")) {
        document.querySelector(".sourcePosts").classList.add("current");
    } else if (currentUrl.includes("/source%3Dprofile-liked")) {
        document.querySelector(".sourceLiked").classList.add("current");
    } else if (currentUrl.includes("/source%3Dtrending")) {
        document.querySelector(".sourceTrending").classList.add("current");
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
            fakeInput.setAttribute("placeholder", "Select or drop an image");
        }
    });
})

$(document).ready(function () {
    var realInputs = document.querySelectorAll(".editPostImageFile");
    realInputs.forEach(realInput => {
        realInput.addEventListener("change", function (ev) {
            console.log("changed " + realInput.id)
            var fakeInput = document.getElementById("editPostImageFileButton-" + realInput.id.split("-")[1]);
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
        })
    })
})

function clearPostImageInput() {
    var realInput = document.getElementById("postImageFile");
    var fakeInput = document.getElementById("postImageFileButton");

    realInput.value = null;
    fakeInput.innerHTML = null;
    fakeInput.innerHTML = `
            <i class="fa-solid fa-cloud-arrow-up"></i>
            Select or drop an image
    `;
}

function handlePostImageInput() {
    var realInput = document.getElementById("postImageFile");
    realInput.click();
}

function handleEditPostImageInput(id) {
    var realInput = document.getElementById("editPostImageFile-" + id);
    realInput.click()
}

function clearEditPostImageInput(id) {
    var realInput = document.getElementById("editPostImageFile-" + id)
    var fakeInput = document.getElementById("editPostImageFileButton-" + id);

    realInput.value = null;
    fakeInput.innerHTML = null;
    fakeInput.innerHTML = `
            <i class="fa-solid fa-cloud-arrow-up"></i>
            Select an image
    `;
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

window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 1500 || document.documentElement.scrollTop > 1500) {
        document.getElementById("scrollBtn").classList.add("show");
    } else {
        document.getElementById("scrollBtn").classList.remove("show");
    }
}

function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}