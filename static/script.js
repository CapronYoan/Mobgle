document.addEventListener("DOMContentLoaded", () => {

    document.querySelector(".form-control").value = "";

    document.querySelector(".btn").disabled = true;

    document.querySelector(".form-control").onkeyup = () => {
    if (document.querySelector(".form-control").value.length > 0)
        document.querySelector(".btn").disabled = false;
    else
        document.querySelector(".btn").disabled = true;
    };

    document.querySelector("#chance").onclick = function () {
    document.querySelector(".img").innerHTML = "<img src='static/smile.svg'/>";
    };
})
