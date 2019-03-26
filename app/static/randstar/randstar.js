window.onload = function() {
  let url = '/randstar/api/' + /user\/(\S+)\//.exec(window.location)[1];

  fetch(url).then(function(response) {
    if (response.ok) {
      return response.json();
    } else {
      document.querySelector('#container').innerHTML = '<p>Load error!</p>';
    }
    return undefined;
  }).then(function(json) {
    let tbody = document.querySelector("#tableBody");
    let itmpl = templateQuerySelector('#itemTemplate');

    for (let repo of json) {
      tbody.innerHTML += itmpl(repo);
    }

    hideElement(document.querySelector("#loader"));
    showElement(document.querySelector("#table"));
  });
};
