/* globals Chart:false, feather:false */

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

// ------------------------ FILL TABLE GUARDS-----------------------------------

function updateListGuardDay(){
  const dated = $('#date_d').val()
  const guard_idd = $('#guard_id_d').val()
  const table = $('#table_edit')

  table.empty()

  $.ajax({
  type: 'GET',
  url: '/get-guards',
  data: {
    date:dated,
    guard_id: guard_idd
  },
  success: function(response){
    const personal = response
    console.log(response)
    personal.map(item=>{
      const option = document.createElement('option')
      if(item.shift == "24"){
      option.textContent = item.is_active + " | " + item.name + ", " + item.last_name
      option.setAttribute("value", item.id)
      table.prepend(option)
    }else{
      if(item.shift == "12"){
      option.textContent = item.is_active + " | " + item.name + ", " + item.last_name
      option.setAttribute("value", item.id)
      table.prepend(option)
    }else{
      if(item.is_extra == "no"){
      option.textContent = item.shift+ " | " + item.name + ", " + item.last_name
      option.setAttribute("value", item.id)
      table.prepend(option)
    }else{
      option.textContent = "Hs. extra | " + item.shift+ " | " + item.name + ", " + item.last_name
      option.setAttribute("value", item.id)
      table.prepend(option)
    }
    }}
    })
    $('#title_edit').html("")
    $('#title_edit').html(personal[0].guard + " - " + personal[0].date_name)
  },
  error: function(error){
    console.log(error)
  }
  })
}

// ---------------DISABLE INPUTS----------------------------
function disableInputs(){
  $('#personal_edit').attr('disabled', 'disabled')
  $('#is_active').attr('disabled', 'disabled')
  $('#shift_edit').attr('disabled', 'disabled')
  $('#hours').attr('disabled', 'disabled')
  $('#all_personal_edit').attr('disabled', 'disabled')
  $('#extra_hours').attr('disabled', 'disabled')
  $('#save_guard_entry').attr('disabled', 'disabled')
  $('#update_guard_entry').attr('disabled', 'disabled')
  $('#hours').val('')
  $('#all_personal_edit').prop('checked', false)
  $('#extra_hours').prop('checked', false)
  $('#is_active').prop('checked', false)
}
// ------------- OPEN EDIT TAB -------------------------------------

$(".btnguard").click(function(){
  $(".edit_entry").fadeIn(200)
  $(".edit_entry").css('display', "flex")
  const date = $(this).children('.date').val()
  const month_year = $(this).children('.month_year').val()
  const is_working_day = $(this).children('.is_working_day').val()
  const guard_id = $(this).children('.guard_id').val()
  const service_id = $(this).children('.service').val()
  const department_id = $(this).children('.department').val()
  const shift = $(this).children('.shift').val()
  const selectMenu = $('#personal_edit')
  const table = $('#table_edit')
  $('#date_d').attr('value', date)
  $('#month_year_d').attr('value', month_year)
  $('#is_working_day_d').attr('value', is_working_day)
  $('#guard_id_d').attr('value', guard_id)
  $('#service_d').attr('value', service_id)
  $('#department_d').attr('value', department_id)
  $('#shift_d').attr('value', shift)

  selectMenu.empty()
  table.empty()

  $.ajax({
  type: 'GET',
  url: '/service',
  data: {
    selService:service_id
  },
  success: function(response){

    const personal = response.service_personal
    personal.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.last_name + ", " + item.name
      option.setAttribute("value", item.id)
      selectMenu.prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Seleccione personal'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    selectMenu.prepend(option)


  },
error: function(error){
    console.log(error)
}
})

updateListGuardDay()
});

$(".close").click(function(){
  $(".edit_entry").fadeOut(200)
  disableInputs()
});

// ------------------------UPDTADE PERSONAL LIST -----------------------------------

$('#all_personal_edit').click(function() {
  const service_id = $('#service_d').val()
  const department_id = $('#department_d').val()
  const selectMenu = $('#personal_edit')
  if($(this).is(':checked')) {
    selectMenu.empty()
    $.ajax({
    type: 'GET',
    url: '/department',
    data: {
      selDepartment:department_id
    },
    success: function(response){

      const personal = response.department_personal
      personal.map(item=>{
        const option = document.createElement('option')
        option.textContent = item.last_name + ", " + item.name
        option.setAttribute("value", item.id)
        selectMenu.prepend(option)
      })
      const option = document.createElement('option')
      option.textContent = 'Seleccione personal'
      option.setAttribute("selected", "selected")
      option.setAttribute("hidden", "hidden")
      selectMenu.prepend(option)


    },
  error: function(error){
      console.log(error)
  }
  })

  } else {
    selectMenu.empty()
    $.ajax({
    type: 'GET',
    url: '/service',
    data: {
      selService:service_id
    },
    success: function(response){

      const personal = response.service_personal
      personal.map(item=>{
        const option = document.createElement('option')
        option.textContent = item.last_name + ", " + item.name
        option.setAttribute("value", item.id)
        selectMenu.prepend(option)
      })
      const option = document.createElement('option')
      option.textContent = 'Seleccione personal'
      option.setAttribute("selected", "selected")
      option.setAttribute("hidden", "hidden")
      selectMenu.prepend(option)


    },
  error: function(error){
      console.log(error)
  }
  })
 }
});

// ---------------------ENABLE INPUTS---------------------


$('#save_guard_d').click(function(){
  if($('#shift_d').val() == '24'){
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').removeAttr('disabled')
    $('#shift_edit').attr('disabled', 'disabled')
    $('#hours').attr('disabled', 'disabled')
    $('#all_personal_edit').attr('disabled', 'disabled')
    $('#extra_hours').attr('disabled', 'disabled')
    $('#save_guard_entry').removeAttr('disabled')
  }else{
    if($('#shift_d').val() == '12'){
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').removeAttr('disabled')
    $('#shift_edit').attr('disabled', 'disabled')
    $('#hours').attr('disabled', 'disabled')
    $('#all_personal_edit').attr('disabled', 'disabled')
    $('#extra_hours').attr('disabled', 'disabled')
    $('#save_guard_entry').removeAttr('disabled')
  }else{
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').attr('disabled', 'disabled')
    $('#shift_edit').removeAttr('disabled')
    $('#hours').removeAttr('disabled')
    $('#all_personal_edit').removeAttr('disabled')
    $('#extra_hours').removeAttr('disabled')
    $('#save_guard_entry').removeAttr('disabled')
  }}
})

// ---------------------- SAVE / EDIT ENTRY ---------------------

var form_configguard ={button:null};

$("#save_guard_entry").click(function(){
  form_configguard.button = 'submit1';
});

$("#update_guard_entry").click(function(){
  form_configguard.button = 'submit2';
});

$(document).on('submit', '#form_entry_mods', function(e) {
  e.preventDefault();


  var submiturls_d;
  if (form_configguard.button == 'submit1') {submiturls_d = '/create-guard-entry'}
  else if (form_configguard.button  === 'submit2') {submiturls_d = '/update-guard-entry'}

  var isActive = ""
  var extra = ""

  if($('#is_active').is(':checked')){
    isActive = "activa"
  }else{
    isActive = "pasiva"
  }

  if($('#extra_hours').is(':checked')){
    extra = "yes"
  }else{
    extra = "no"
  }

  $.ajax({
    type: 'POST',
    url: submiturls_d,


    data: {
      id: $('#guard_day_id').val(),
      guard_id: $('#guard_id_d').val(),
      date: $('#date_d').val(),
      month_year: $('#month_year_d').val(),
      is_working_day: $('#is_working_day_d').val(),
      personal_id: $('#personal_edit').val(),
      shift: $('#shift_d').val(),
      shift_day: $('#shift_edit').val(),
      hours: $('#hours').val(),
      is_extra: extra,
      is_active: isActive,
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {
      $('#messageSer').html(data)
      updateListGuardDay()
      disableInputs()

    },
    error: function(data) {
      $('#messageSer').html(data)
    }
  })

});

// ----------------- EDIT ----------------------------------------------


$('#edit_guard_d').click(function(){

  if($('#shift_d').val() == '24'){
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').removeAttr('disabled')
    $('#shift_edit').attr('disabled', 'disabled')
    $('#hours').attr('disabled', 'disabled')
    $('#all_personal_edit').attr('disabled', 'disabled')
    $('#extra_hours').attr('disabled', 'disabled')
    $('#update_guard_entry').removeAttr('disabled')
  }else{
    if($('#shift_d').val() == '12'){
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').removeAttr('disabled')
    $('#shift_edit').attr('disabled', 'disabled')
    $('#hours').attr('disabled', 'disabled')
    $('#all_personal_edit').attr('disabled', 'disabled')
    $('#extra_hours').attr('disabled', 'disabled')
    $('#update_guard_entry').removeAttr('disabled')
  }else{
    $('#personal_edit').removeAttr('disabled')
    $('#is_active').attr('disabled', 'disabled')
    $('#shift_edit').removeAttr('disabled')
    $('#hours').removeAttr('disabled')
    $('#all_personal_edit').removeAttr('disabled')
    $('#extra_hours').removeAttr('disabled')
    $('#update_guard_entry').removeAttr('disabled')
  }}

  $.ajax({
    type: 'GET',
    url: '/get-guard',
    data: {
      selGuard: $('#table_edit').val(),
    },
    success: function(response){
      console.log(response)
      const sec = response
      $('#update_guard_d').removeAttr('disabled')
      $('#save_guard_entry').attr('disabled', 'disabled');
      $('#personal_edit').val(sec['personal_id'])
      $('#shift_edit').val(sec['shift'])
      $('#hours').val(sec['duration'])
      $('#guard_day_id').val(sec['id'])
      if (sec['shift'] === "24"){
            if (sec['is_active'] === "activa"){
        $('#is_active').prop('checked', true)
      }}
      if (sec['shift'] === "12"){
            if (sec['is_active'] === "activa"){
        $('#is_active').prop('checked', true)
      }}
      if (sec['is_extra'] !== "no"){
        $('#extra_hours').prop('checked', true)
        $('#hours').val(sec['is_extra'])

      }
    }
  })
});

// ----------------- EDIT ----------------------------------------------


$('#delete_guard_d').click(function(){

  $.ajax({
    type: 'GET',
    url: '/del-guard',
    data: {
      selGuard: $('#table_edit').val(),
    },
    success: function(response){
    updateListGuardDay()
    }
  })
});
