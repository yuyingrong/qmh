var collapsibles = document.getElementsByClassName("collapsible");

for (var collapsible of collapsibles) {
  collapsible.addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });

  var content = collapsible.nextElementSibling;
  if (content) {
    var ul = content.firstElementChild;
    for (var li of ul.children) {
      var a = li.firstElementChild;
      if (a.href == document.location.href) {
        collapsible.click();
	a.removeAttribute("href");
	li.style = "background-color: #333; color: white;" + li.style;
	a.style = "color: white;" + a.style;
      }
    }
  }
}
