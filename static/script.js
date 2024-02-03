  document.addEventListener("DOMContentLoaded", function () {
    let themeSwitcher = document.getElementById("themeSwitcher");
    let bodyElement = document.body;

    // Check if the theme preference is stored in local storage
    if (localStorage.getItem("theme") === "light") {
      bodyElement.dataset.bsTheme = "light";
      themeSwitcher.checked = true;
    };

    // Add an event listener to the theme switcher checkbox
    themeSwitcher.addEventListener("change", function () {
      if (this.checked) {
        bodyElement.dataset.bsTheme = "light";
        localStorage.setItem("theme", "light");
      } else {
        bodyElement.dataset.bsTheme = "dark";
        localStorage.setItem("theme", "dark");
      }
    });

  });