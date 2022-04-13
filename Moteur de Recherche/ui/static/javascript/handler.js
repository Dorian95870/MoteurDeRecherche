let hamburger = document.getElementById("hamburger");
let optionsMenu = document.getElementById("optionsMenu");
let searchBar = document.getElementById("searchBar");
let searchBarSuggestion = document.getElementById("searchBarSuggestion");
let colorMode = document.getElementById("colorMode");

hamburger.addEventListener("click", () => {
    optionsMenu.classList.contains("hidden")
        ? optionsMenu.classList.remove("hidden")
        : optionsMenu.classList.add("hidden");
});

colorMode.addEventListener("click", () => {
    document.querySelector("html").classList.contains("dark")
        ? document.querySelector("html").classList.remove("dark")
        : document.querySelector("html").classList.add("dark");
});

searchBar.addEventListener("keyup", () => {
    if (searchBar.value != "") {
        searchBarSuggestion.classList.remove("hidden");
    } else {
        searchBarSuggestion.classList.add("hidden");
    }
});

