
document.addEventListener("DOMContentLoaded", function () {
    
    // const options = document.querySelectorAll(".options");
    const options = document.querySelectorAll(".options");

    options.forEach(function (option) {

      option.addEventListener("click", function () {

        const minNavbar = document.querySelector(".minNavbar");
        

        minNavbar.classList.toggle("hidden");
      });
    });

    const options_for_data = document.querySelectorAll(".options_data");
    console.log("OPtions")
    options_for_data.forEach(function (option) {

      option.addEventListener("click", function () {

        const minNavbar = document.querySelector(".minNav");
        
        minNavbar.classList.toggle("hidden");
      });
    });

  });