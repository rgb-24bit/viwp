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
