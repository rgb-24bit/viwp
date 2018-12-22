function showRandStar(data) {
  let tbody = document.querySelector("#tableBody");
  let itemTemplate = templateQuerySelector('#itemTemplate');

  for (let repo of data) {
    tbody.innerHTML += itemTemplate(repo);
  }

  hideElement(document.querySelector("#loader"));
  showElement(document.querySelector("#table"));
}

window.onload = function() {
  getJSON('/randstar/api/' + /user\/(\S+)\//.exec(window.location)[1], showRandStar);
};
