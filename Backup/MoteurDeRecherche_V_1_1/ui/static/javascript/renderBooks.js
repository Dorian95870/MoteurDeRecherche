let suggestedBooks = document.getElementById("suggestedBooks");
let recentBooks = document.getElementById("recentBooks");

function renderBook(title, image, url) {
    let result = document.createElement("a");
    result.classList.add(
        "flex",
        "flex-col",
        "h-4/5",
        "w-48",
        "gap-2",
        "items-center"
    );
    result.href = url;
    let div2 = document.createElement("div");
    div2.classList.add("w-48", "h-full", "rounded-2xl", "overflow-hidden");
    let img = document.createElement("img");
    img.classList.add("h-full", "w-full", "hover:scale-110", "transition-all");
    img.src = image;
    let span = document.createElement("span");
    span.classList.add("truncate", "w-4/5");
    span.innerHTML = title;
    div2.appendChild(img);
    result.appendChild(div2);
    result.appendChild(span);

    return result;
}

for (let index = 0; index < 10; index++) {
    suggestedBooks.append(
        renderBook(
            "Livre " + (index + 1) + " : abcdefghijklmnopqrstuvwxyz",
            "static/public/img/bookCover.jpg",
            "#"
        )
    );
}

for (let index = 0; index < 10; index++) {
    recentBooks.append(
        renderBook(
            "Livre " + (index + 1) + " : abcdefghijklmnopqrstuvwxyz",
            "static/public/img/bookCover.jpg",
            "#"
        )
    );
}
