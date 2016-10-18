var count = 0;
function addCity() {
  var newFormGroup = document.createElement('div');
  newFormGroup.className = 'form-group';
  newFormGroup.id = 'form-city'+count
  newFormGroup.innerHTML = '<div class="col-sm-10"><input type="text" id="city'+count+'" name="city'+count+'" class="form-control">';
  newFormGroup.innerHTML += '<button type="button" class="btn btn-default col-sm-2" onclick="removeCity(this)">Remove city</button>'
  //var newInput = document.createElement('input');
  //newInput.className = 'form-control';
  //newInput.name = 'city' + count;
  //newInput.type = 'text';
  document.getElementById('city-form').appendChild(newFormGroup);
  count += 1;
}

function removeCity(field) {
  var fieldId = field.parentNode.id;
  var fieldToRemove = document.getElementById(fieldId);
  document.getElementById('city-form').removeChild(fieldToRemove);
}

function removeAllCities() {
  document.getElementById('city-form').innerHTML = '';
}
