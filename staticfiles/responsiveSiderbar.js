const sidebar = document.getElementById("default-sidebar");
const buttonSidebar = document.getElementById("sidebar-responsive-button");

buttonSidebar.addEventListener("click", () => {
    sidebar.classList.toggle("translate-x-0");
});

console.log("Sidebar butttuibn")