const courtsElements = document.querySelectorAll(".card");

courtsElements.forEach((element) => {
    element.addEventListener("mouseover", () => {
        element.style.backgroundColor = '#99ccff';
        element.style.border = '2px solid black';
        element.style.boxShadow = '2px 2px 4px #000000';
    });
    element.addEventListener("mouseout", () => {
        element.style.backgroundColor = 'white';
        element.style.border = '';
        element.style.boxShadow = '';
    });
})