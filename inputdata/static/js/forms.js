
//-------------------------------------------------------- DEPARTMENT --------------------------------------------------------------------------------------------------------->
//-------------------------------------------------------- DEPARTMENT --------------------------------------------------------------------------------------------------------->


var form_configsd ={button:null};

$("#save_department").click(function(){
  form_configsd.button = 'submit1';
});

$("#update_department").click(function(){
  form_configsd.button = 'submit2';
});

$(document).on('submit', '#form_department', function(e) {
  e.preventDefault();


  var submiturld;
  if (form_configsd.button == 'submit1') {submiturld = '/create-dep'}
  else if (form_configsd.button  === 'submit2') {submiturld = '/update-dep'}

  $.ajax({
    type: 'POST',
    url: submiturld,

    data: {
      dep_name: $('#d_name').val(),
      id: $('#idd').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },



    success: function(data) {
      $('#messageDep').html(data)
      updatelistSec()
      $('#d_name, #idd').val("");
      $('#update_department').attr('disabled', 'disabled');
      $('#save_department').removeAttr('disabled');


    },
    error: function(data) {
      $('#messageDep').html(data)
    }
  })
});

$("#department").click(function(){
  updatelistSec();
});

function updatelistSec(){

  $.ajax({
  type: 'GET',
  url: '/json-dep',
  success: function(response){
    $('#table_department').empty()
    const sectorData = response.department_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = "- "+item.name
      option.setAttribute("value", item.id)
      $('#table_department').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}
//-------------------------------------------------------- EDIT DEPARTMENT --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_department', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-dep-edit',
    data: {
      selDepartment: $('#table_department').val(),

    },
    success: function(response) {
      const sec = response.department
      $('#update_department').removeAttr('disabled')
      $('#save_department').attr('disabled', 'disabled');
      $('#d_name').val(sec[0]['name'])
      $('#idd').val(sec[0]['id'])


    }
  })
});

//-------------------------------------------------------- DELETE DEPARTMENT --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#department_list_edit', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-dep',

    data: {
      id: $('#table_department').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messageDep').html(data)
      updatelistSec()

    },
    error: function() {
      $('#messageDep').html("El departamento no pudo eliminarse porque tiene categorías asignadas")
    }
  })
});

//-------------------------------------------------------- SERVICE --------------------------------------------------------------------------------------------------------->
//-------------------------------------------------------- SERVICE --------------------------------------------------------------------------------------------------------->
function updateDepartment(){

  $.ajax({
  type: 'GET',
  url: '/json-dep',
  success: function(response){
    $('#department-service').empty()
    const sectorData = response.department_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#department-service').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona departamento'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#department-service').prepend(option)


  },
  error: function(error){
      console.log(error)
  }
  })
}


$("#service").click(function(){
  updateDepartment();
});

var form_configs ={button:null};

$("#save_service").click(function(){
  form_configs.button = 'submit1';
});

$("#update_service").click(function(){
  form_configs.button = 'submit2';
});

$(document).on('submit', '#form_service', function(e) {
  e.preventDefault();


  var submiturls;
  if (form_configs.button == 'submit1') {submiturls = '/create-ser'}
  else if (form_configs.button  === 'submit2') {submiturls = '/update-ser'}

  $.ajax({
    type: 'POST',
    url: submiturls,

    data: {
      department: $('#department-service').val(),
      sname: $('#s_name').val(),
      id: $('#ids').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },



    success: function(data) {
      $('#messageSer').html(data)
      updatelistSer()
      $('#s_name, #ids').val("");
      $('#update_service').attr('disabled', 'disabled');
      $('#save_service').removeAttr('disabled');


    },
    error: function(data) {
      $('#messageSer').html(data)
    }
  })

});

$("#department-service").change(function(){
  updatelistSer();
});

function updatelistSer(){
  var sel = $("#department-service").val()

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    'selDepartment':sel
  },
  success: function(response){
    $('#table_service').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = "- "+item.name
      option.setAttribute("value", item.id)
      $('#table_service').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}

//-------------------------------------------------------- EDIT SERVICE --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_service', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-ser-edit',
    data: {
      selService: $('#table_service').val(),

    },
    success: function(response) {
      const cat = response.service
      $('#update_service').removeAttr('disabled')
      $('#save_service').attr('disabled', 'disabled');
      $('#s_name').val(cat[0]['name'])
      $('#ids').val(cat[0]['id'])


    }
  })
});



//-------------------------------------------------------- DELETE SERVICE --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#service_list_edit', function(e) {
  e.preventDefault();


  $.ajax({
    type: 'POST',
    url: '/delete-ser',

    data: {
      id: $('#table_service').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messageSer').html(data)
      updatelistSer()


    },
    error: function() {
      $('#messageSer').html("El servicio no pudo eliminarse porque tiene personal y/o guardias asignadas")
    }
  })
});



// ------------------------------------------------------------------- GUARD----------------------------------------------------------------------------------------------
// ------------------------------------------------------------------- GUARD----------------------------------------------------------------------------------------------
function updateDepartmentGuard(){

  $.ajax({
  type: 'GET',
  url: '/json-dep',
  success: function(response){
    $('#department-data-guard').empty()
    const sectorData = response.department_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#department-data-guard').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona departamento'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#department-data-guard').prepend(option)
  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateServiceGuard(){

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    selDepartment:$("#department-data-guard").val()
  },
  success: function(response){
    $('#service-data-guard').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#service-data-guard').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona servicio'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#service-data-guard').prepend(option)
  },
  error: function(error){
      console.log(error)
  }
  })
}

$("#guard").click(function(){
  updateDepartmentGuard();
});

$("#department-data-guard").change(function(){
  updateServiceGuard();
});

var form_configg ={button:null};

$("#save_guard").click(function(){
  form_configg.button = 'submit1';
});

$("#update_guard").click(function(){
  form_configg.button = 'submit2';
});

$(document).on('submit', '#form_guard', function(e) {
e.preventDefault();


var submiturlg;
if (form_configg.button == 'submit1') {submiturlg = '/create-guar'}
else if (form_configg.button  === 'submit2') {submiturlg = '/update-guar'}

$.ajax({
  type: 'POST',
  url: submiturlg,

  data: {
    service: $('#service-data-guard').val(),
    name: $('#name').val(),
    type: $('#type').val(),
    duration: $('#duration').val(),
    id: $('#idg').val(),
    csrfmiddlewaretoken: window.CSRF_TOKEN,
  },



  success: function(data) {
    $('#messageGuar').html(data)
    updatelistGuar()
    $('#name, #type, #duration, #idg').val("");
    $('#update_guard').attr('disabled', 'disabled');
    $('#save_guard').removeAttr('disabled');


  },
  error: function(data) {
    $('#messageGuar').html(data)
  }
})

});

$("#service-data-guard").change(function(){
  updatelistGuar();
});

function updatelistGuar(){
  var sel = $("#service-data-guard").val()
  $.ajax({
  type: 'GET',
  url: '/json-guar',
  data: {
    'selServ':sel
  },
  success: function(response){
    $('#table_guard').empty()
    console.log(response)
    const sectorData = response.guards
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = "- " + item.name + " - " + item.type + " - " + item.duration_hs + "Hs."
      option.setAttribute("value", item.id)
      $('#table_guard').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}
// -------------------------------------------------------- EDIT GUARD --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_guard', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-guar-edit',
    data: {
      selGuard: $('#table_guard').val(),

    },
    success: function(response) {
      console.log(response)
      var guard = response.guard
      $('#update_guard').removeAttr('disabled')
      $('#save_guard').attr('disabled', 'disabled');
      $('#name').val(guard[0]['name'])
      $('#type').val(guard[0]['type'])
      $('#duration').val(guard[0]['duration_hs'])
      $('#idg').val(guard[0]['id'])

    }
  })
});


//-------------------------------------------------------- DELETE GUARD --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#guard_list_edit', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-guar',

    data: {
      id: $('#table_guard').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      updatelistGuar()
      $('#messageGuar').html(data)
    },
    error: function() {
      $('#messageGuar').html("La guardia no pudo eliminarse porque fue asignada a una planificación")
    }
  })
});


// ------------------------------------------------------------------- PERSONAL-------------------------------------------------------------------------------------------------
// ------------------------------------------------------------------- PERSONAL-------------------------------------------------------------------------------------------------
function updatelistPer(){
  var sel = $("#service-data-personal").val()
  $.ajax({
  type: 'GET',
  url: '/json-per',
  data: {
    'selSer':sel
  },
  success: function(response){
    $('#table_personal').empty()
    console.log(response)
    const sectorData = response.personal
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = "- " + item.last_name + ", " + item.name + " - " + item.profession + " - " + item.phone
      option.setAttribute("id", "option_personal")
      option.setAttribute("value", item.id)
      $('#table_personal').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateDepartmentPersonal(){

  $.ajax({
  type: 'GET',
  url: '/json-dep',
  success: function(response){
    $('#department-data-personal').empty()

    const sectorData = response.department_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#department-data-personal').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona departamento'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#department-data-personal').prepend(option)

  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateServicePersonal(){

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    selDepartment:$("#department-data-personal").val()
  },
  success: function(response){
    $('#service-data-personal').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#service-data-personal').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona servicio'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#service-data-personal').prepend(option)
  },
  error: function(error){
      console.log(error)
  }
  })
}

$("#personal").click(function(){
  updateDepartmentPersonal();
});

$("#department-data-personal").change(function(){
  updateServicePersonal();
});


var form_config ={button:null};

$("#save_person").click(function(){
  form_config.button = 'submit1';
});

$("#edit_person").click(function(){
  form_config.button = 'submit2';
});


$(document).on('submit', '#form_personal', function(e) {
  e.preventDefault();


  var submiturl;
  if (form_config.button == 'submit1') {submiturl = '/create-per'}
  else if (form_config.button  === 'submit2') {submiturl = '/update-per'}


  $.ajax({
    type: 'POST',
    url: submiturl,
    data: {
      service: $('#service-data-personal').val(),
      file: $('#legajo_person').val(),
      d: $('#d').val(),
      name: $('#name_person').val(),
      last_name: $('#last_name').val(),
      profession: $('#profession').val(),
      phone: $('#phone').val(),
      is_pro: $('#is_pro').val(),
      id: $('#id').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messagePer').html(data)
      updatelistPer()
      $('#name_person, #last_name, #profession, #phone, #id, #legajo_person, #d').val("");
      $('#update_person').attr('disabled', 'disabled');
      $('#save_person').removeAttr('disabled');



    }
  })
});

$("#service-data-personal").change(function(){
  updatelistPer();
});


// --------------------------------------------DELETE PERSONA-----------------------------

$(document).on('submit', '#personal_list_edit', function(e) {
  e.preventDefault();


  $.ajax({
    type: 'POST',
    url: '/delete-per',
    data: {
      id: $('#table_personal').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messagePer').html(data)
      updatelistPer()
    },
    error: function() {
      $('#messagePer').html("La persona no pudo eliminarse porque tiene guardias asignadas")
    }
  })
});

//---------------------------------------------- EDIT PERSONAL------------------------------

$(document).on('click', '#edit_person', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-per-edit',
    data: {
      selPer: $('#table_personal').val(),

    },
    success: function(response) {
      const per = response.person
      $('#update_person').removeAttr('disabled')
      $('#save_person').attr('disabled', 'disabled')
      $('#name_person').val(per[0]['name'])
      $('#legajo_person').val(per[0]['file'])
      $('#d').val(per[0]['d'])
      $('#last_name').val(per[0]['last_name'])
      $('#profession').val(per[0]['profession'])
      $('#phone').val(per[0]['phone'])
      $('#is_pro').val(per[0]['is_pro'])
      $('#id').val(per[0]['id'])


    }
  })
});

//-------------------------------------------------------- NOT WORKING DAYS --------------------------------------------------------------------------------------------------------->
//-------------------------------------------------------- NOT WORKING DAYS --------------------------------------------------------------------------------------------------------->


var form_configsw ={button:null};

$("#save_notworking").click(function(){
  form_configsw.button = 'submit1';
});

$("#update_notworking").click(function(){
  form_configsw.button = 'submit2';
});

$(document).on('submit', '#form_notworking', function(e) {
  e.preventDefault();


  var submiturlw;
  if (form_configsw.button == 'submit1') {submiturlw = '/create-nowork'}
  else if (form_configsw.button  === 'submit2') {submiturlw = '/update-nowork'}

  $.ajax({
    type: 'POST',
    url: submiturlw,

    data: {
      id: $('#idw').val(),
      date: $('#w_date').val(),
      w_name: $('#w_name').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {

      $('#messageWo').html(data)
      updateListWork()
      $('#w_name, #idw').val("");
      $('#update_notworking').attr('disabled', 'disabled');
      $('#save_notworking').removeAttr('disabled');


    },
    error: function(data) {
      $('#messageWo').html(data)
    }
  })
});

$("#notworking").click(function(){
  updateListWork();
});

function updateListWork(){

  $.ajax({
  type: 'GET',
  url: '/json-work',
  success: function(response){
    $('#table_notworking').empty()
    const sectorData = response.notworking
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.date + " - " + item.name
      option.setAttribute("value", item.id)
      $('#table_notworking').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}
//-------------------------------------------------------- EDIT NOT WORKING DAYS --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_notworking', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-notw-edit',
    data: {
      selNotWorking: $('#table_notworking').val(),
    },
    success: function(response) {
      const sec = response.notworking
      console.log(sec)
      $('#update_notworking').removeAttr('disabled')
      $('#save_notworking').attr('disabled', 'disabled');
      $('#w_date').val(sec[0]['date'])
      $('#w_name').val(sec[0]['name'])
      $('#idw').val(sec[0]['id'])


    }
  })
});

//-------------------------------------------------------- DELETE NOT WORKING DAYS --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#notworking_list_edit', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-nowork',

    data: {
      id: $('#table_notworking').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messageWo').html(data)
      updateListWork()

    },
    error: function() {
      $('#messageWo').html("El departamento no pudo eliminarse porque tiene categorías asignadas")
    }
  })
});

//-------------------------------------------------------- LICENCES --------------------------------------------------------------------------------------------------------->
//-------------------------------------------------------- LICENCES --------------------------------------------------------------------------------------------------------->


var form_configsli ={button:null};

$("#save_licences").click(function(){
  form_configsli.button = 'submit1';
});

$("#update_licences").click(function(){
  form_configsli.button = 'submit2';
});

$(document).on('submit', '#form_licences', function(e) {
  e.preventDefault();


  var submiturlli;
  if (form_configsli.button == 'submit1') {submiturlli = '/create-licences'}
  else if (form_configsli.button  === 'submit2') {submiturlli = '/update-licences'}

  console.log(submiturlli)

  $.ajax({
    type: 'POST',
    url: submiturlli,

    data: {
      id: $('#idli').val(),
      name: $('#li_name').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {

      $('#messageLi').html(data)
      updateListLiscences()
      $('#li_name, #idli').val("");
      $('#update_licences').attr('disabled', 'disabled');
      $('#save_licences').removeAttr('disabled');


    },
    error: function(data) {
      $('#messageLi').html(data)
    }
  })
});

$("#licences").click(function(){
  updateListLiscences();
});

function updateListLiscences(){

  $.ajax({
  type: 'GET',
  url: '/json-licences',
  success: function(response){
    $('#table_licences').empty()
    const sectorData = response.licences
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#table_licences').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}
//-------------------------------------------------------- EDIT LICENCES --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_licences', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-licences-edit',
    data: {
      selLicences: $('#table_licences').val(),
    },
    success: function(response) {
      const sec = response.licences

      $('#update_licences').removeAttr('disabled')
      $('#save_licences').attr('disabled', 'disabled');
      $('#li_name').val(sec[0]['name'])
      $('#idli').val(sec[0]['id'])


    }
  })
});

//-------------------------------------------------------- DELETE LICENCES --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#licences_list_edit', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-licences',

    data: {
      id: $('#table_licences').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messageLi').html(data)
      updateListLiscences()

    },
    error: function() {
      $('#messageLi').html("La licencia no pudo eliminarse porque tiene personal asignado")
    }
  })
});

//-------------------------------------------------------- POINTS --------------------------------------------------------------------------------------------------------->
//-------------------------------------------------------- POINTS --------------------------------------------------------------------------------------------------------->


var form_configspo ={button:null};

$("#save_points").click(function(){
  form_configspo.button = 'submit1';
});

$("#update_points").click(function(){
  form_configspo.button = 'submit2';
});

$(document).on('submit', '#form_points', function(e) {
  e.preventDefault();


  var submiturlpo;
  if (form_configspo.button == 'submit1') {submiturlpo = '/create-points'}
  else if (form_configspo.button  === 'submit2') {submiturlpo = '/update-points'}

  $.ajax({
    type: 'POST',
    url: submiturlpo,

    data: {
      id: $('#idpo').val(),
      type: $('#points_type').val(),
      day: $('#points_day').val(),
      points: $('#points_points').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },

    success: function(data) {

      $('#messagePo').html(data)
      updateListPoints()
      $('#points_points').val("");
      $('#update_points').attr('disabled', 'disabled');
      $('#save_points').removeAttr('disabled');


    },
    error: function(data) {
      $('#messagePo').html(data)
    }
  })
});

$("#points").click(function(){
  updateListPoints();
});

function updateListPoints(){

  $.ajax({
  type: 'GET',
  url: '/json-points',
  success: function(response){
    $('#table_points').empty()
    const sectorData = response.points
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.type + " - " + item.day + " - " + item.points
      option.setAttribute("value", item.id)
      $('#table_points').prepend(option)
    })


  },
  error: function(error){
      console.log(error)
  }
  })
}
//-------------------------------------------------------- EDIT POINTS --------------------------------------------------------------------------------------------------------->

$(document).on('click', '#edit_points', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/json-points-edit',
    data: {
      selPoints: $('#table_points').val(),
    },
    success: function(response) {
      const sec = response.points

      $('#update_points').removeAttr('disabled')
      $('#save_points').attr('disabled', 'disabled');
      $('#points_type').val(sec[0]['type'])
      $('#points_day').val(sec[0]['day'])
      $('#points_points').val(sec[0]['points'])
      $('#idpo').val(sec[0]['id'])


    }
  })
});

//-------------------------------------------------------- DELETE POINTS --------------------------------------------------------------------------------------------------------->

$(document).on('submit', '#points_list_edit', function(e) {
  e.preventDefault();

  $.ajax({
    type: 'POST',
    url: '/delete-points',

    data: {
      id: $('#table_points').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },


    success: function(data) {
      $('#messagePo').html(data)
      updateListPoints()

    },
    error: function() {
      $('#messagePo').html("El puntaje no puede eliminarse porque tiene planificaciones asignadas, utilice modificar para asignarle otro valor")
    }
  })
});
