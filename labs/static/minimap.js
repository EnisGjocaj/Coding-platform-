// minimap.js

console.log("EnisGKJkljk")

document.addEventListener('DOMContentLoaded', function () {
    let minimapContainer;
    createMinimap();
});

function createMinimap() {
     minimapContainer = document.getElementById('minimap-container');
    const h1Elements = document.querySelectorAll('h1');

    h1Elements.forEach((h1, index) => {

        section_id = `section-${index + 1}`;

        h1.setAttribute("id", section_id);

        const anchor = document.createElement('a');
        anchor.href = section_id;
        anchor.textContent = h1.textContent;

        anchor.setAttribute("class", "text-lg transition-all duration-300 ease-in-out hover:text-slate-200 max-[1025px]:text-sm");

        const minimapItem = document.createElement('div');
        minimapItem.classList.add('minimap-item');

        minimapItem.appendChild(anchor);

        minimapContainer.appendChild(minimapItem);

        anchor.addEventListener('click', function (event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(0);
            const targetElement = document.getElementById(targetId);

            console.log(targetId)
            console.log(targetElement)

            if(targetElement){
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }

        });
    });
}
