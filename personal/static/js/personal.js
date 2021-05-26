function updateDepartmentP(){

  $.ajax({
  type: 'GET',
  url: '/json-dep',
  success: function(response){
    $('#department_p99').empty()
    const sectorData = response.department_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#department_p99').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Todos'
    option.setAttribute("selected", "selected")

    $('#department_p99').prepend(option)


  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateLicenses(){
  $.ajax({
  type: 'GET',
  url: '/get-licences',
  data:{
    id:$('#table_perso').val()
  },

  success: function(response){

    $('#table_lic').empty()
    $('#list_lic-3').empty()
    const sectorData = response.licences
    const sector = response.lic
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#list_lic-3').prepend(option)
    })
    sector.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.license_id_id + " - " + item.from_date + " / " + item.till_date
      option.setAttribute("value", item.id)
      $('#table_lic').prepend(option)
    })
  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateServiceGuardP(){

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    selDepartment:$("#department_p99").val()
  },
  success: function(response){
    $('#service_p99').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#service_p99').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Todos'
    option.setAttribute("selected", "selected")

    $('#service_p99').prepend(option)
  },
  error: function(error){
      console.log(error)
  }
  })
}

function updatePersonalList(){
  $.ajax({
  type: 'GET',
  url: '/list-personal',
  data: {
    law: $('#law').val(),
    department: $('#department_p99').val(),
    service: $('#service_p99').val()
  },
  success: function(response){
    $('#table_perso').empty()
    const sectorData = response.list_personal
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.last_name + ", " + item.name
      option.setAttribute("value", item.id)
      $('#table_perso').prepend(option)
    })

  },
  error: function(error){
      console.log(error)
  }
  })
}

$(document).ready(function(){
  updateDepartmentP();
  updatePersonalList()
});

$("#department_p99").change(function(){
  updateServiceGuardP();
});

$("#update_p").click(function(){
  updatePersonalList()
});

$("#table_perso").change(function(){
  $.ajax({
    type: 'get',
    url: '/personal-data',
    data: {
      id: $('#table_perso').val(),
    },
    success: function(response) {
      const data = response.personal_data
      const service = response.service
      const department = response.department
      $("#lic").slideUp(10)
      $("#info").slideUp(10)
      $('#p_file').empty()
      $('#p_dep').empty()
      $('#p_profession').empty()
      $('#p_tel').empty()
      $('#per_name').empty()
      $('#per_name').html(data[0].last_name + ", " + data[0].name)
      $('#p_file').html("Legajo: " + data[0].file + " / " + data[0].d)
      $('#p_dep').html("Departamento: " + department[0].name + " - " + service[0].name)
      $('#p_profession').html("Función: " + data[0].profession)
      $('#p_tel').html("Teléfono: " + data[0].phone)
      $("#info").slideDown(200)

    },
    error: function() {
      $('#messagePer').html("")
    }
    })
});

$("#licences_p").click(function(){
  $("#lic").slideDown(200)
  $('#messageLic').empty()
  updateLicenses()
})

$(document).on('submit', '#save_lic', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/save-licenses',
    data: {
      from: $('#from').val(),
      till: $('#till').val(),
      personal_id: $('#table_perso').val(),
      licences_id: $('#list_lic-3').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {
      $('#messageLic').html(data)
      updateLicenses()

    }
  })
});

$(document).on('submit', '#form_licences', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-license-date',
    data: {
      id: $('#table_lic').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {
      updateLicenses()
      $('#messageLic').html(data)

    }
  })
});
