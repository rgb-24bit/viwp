function showRandStar(data) {
  let tbody = document.querySelector("#tableBody");
  let itemTemplate = templateQuerySelector('#itemTemplate');

  for (let url of data) {
    getJSON(url, function(data) {
      tbody.append(asHTML(itemTemplate(data)));
    });
  }
}

window.onload = function() {
  getJSON('/randstar/api/' + /user\/(\S+)\//.exec(window.location)[1], showRandStar);
};
