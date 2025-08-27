function performSearch() {
  const searchTerm = document.getElementById("searchInput").value.toLowerCase();
  const resultsContainer = document.getElementById("results");

  if (searchTerm.trim() === "") {
    // trim - избавляется от лишних пробелов слева и справа
    resultsContainer.innerHTML =
      '<div class="no-results">Введите запрос для поиска</div>';
    return;
  }
  $.ajax({
    method: "GET",
    url: `/search?q=${searchTerm}`,
    success: function (response) {
      if (response["count"] == 0) {
        resultsContainer.innerHTML =
          '<div class="no-results">Ничего не найдено</div>';
      } else {
        resultsContainer.innerHTML = null;
        response["result"].forEach((product) => {
          let card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
        <h4>${product["title"]}</h4>
        <p>${product["price"]}</p>
        `;

          resultsContainer.appendChild(card);
        });
      }
    },
  });
}

document
  .getElementById("searchInput")
  .addEventListener("keypress", function (e) {
    // реализация по нажатию клавиши - enter
    if (e.key === "Enter") {
      performSearch();
    }
  });
