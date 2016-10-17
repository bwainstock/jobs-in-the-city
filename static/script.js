var count = 0;
function add_fields() {
  var newInput = document.createElement('input');
  newInput.className = 'form-control';
  newInput.name = 'city' + count;
  newInput.type = 'text';
  document.getElementById('city-form').appendChild(newInput);
  count += 1;
}
