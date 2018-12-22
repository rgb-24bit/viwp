/**
 * Convert html string to html object.
 *
 * Note:
 *     The parameter htmlString should guarantee only one top level node.
 */
function asHTML(htmlString) {
  let el = document.createElement('div');
  el.innerHTML = htmlString;
  return el.firstChild;
}

/**
 * Get the returned data in the Json format of the specified link and
 * perform the corresponding action.
 */
function getJSON(url, callback) {
  let request = new XMLHttpRequest();

  request.open('GET', url, true);

  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      callback(JSON.parse(request.responseText));
    } else {
      // We reached our target server, but it returned an error
    }
  };

  request.onerror = function() {
    // There was a connection error of some sort
  };

  request.send();
}

/**
 * Hide specified elements.
 */
function hideElement(element) {
  element.style.display = 'none';
}

/**
 * Display the specified element.
 */
function showElement(element) {
  element.style.display = '';
}
