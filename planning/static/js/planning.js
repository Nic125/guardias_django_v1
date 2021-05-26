// // ----------------------------- ENABLE EDIT -------------------------------------------------------
// $('.editable').each(function(){
//   const selectMenu = $(this).closest('.hsguard').children('.personal').children('.list_personal')
//   if($(this).is(':checked')) {
//     selectMenu.removeAttr('disabled');
//   } else {
//     selectMenu.hide();
//     selectMenu.attr('disabled', 'disabled');
//   }
//   });;
//
// $('.editable').click(function() {
//   const selectMenu = $(this).closest('.hsguard').children('.personal').children('.list_personal')
//   const select = $(this)
//   if($(this).is(':checked')) {
//     selectMenu.removeAttr('disabled');
//     selectMenu.empty()
//     selectMenu.slideDown();
//     $.ajax({
//     type: 'GET',
//     url: '/service',
//     data: {
//       selService:select.val()
//     },
//     success: function(response){
//
//       const personal = response.service_personal
//       personal.map(item=>{
//         const option = document.createElement('option')
//         option.textContent = item.last_name + ", " + item.name
//         option.setAttribute("value", item.id)
//         selectMenu.prepend(option)
//       })
//       const option = document.createElement('option')
//       option.textContent = 'Seleccione personal'
//       option.setAttribute("selected", "selected")
//       option.setAttribute("hidden", "hidden")
//       selectMenu.prepend(option)
//
//
//     },
//   error: function(error){
//       console.log(error)
//   }
//   })
//   } else {
//     selectMenu.attr('disabled', 'disabled');
//     selectMenu.slideUp();
//   }
// });
//---------------------GO FROM ACTUAL TO PREVIOUS MONTH -------------

$('#actual').click(function(){
  $(".last_month").slideUp(200)
  $(".current_month").slideDown(200)
});

$('#previous').click(function(){
  $(".last_month").slideDown(200)
  $(".current_month").slideUp(200)
});

// // ------------------- SAVE EDIT DAY -------------------------------
// $(document).on('submit', '.change_day', function(e) {
//   e.preventDefault();
//   const selectMenu = $(this).closest('.hsguard').children('.personal').children('.list_personal')
//   var is_active = ""
//   const id = $(this).closest('.hsguard').children('.idguardsheet').children('.id_gua')
//   const editable = $(this).closest('.hsguard').children('.personal').children('input:checkbox')
//   const sele = $(this).closest('.hsguard').children('.personal').children('.list_personal')
//   const name = $(this).closest('.hsguard').children('.idguar')
//
//
//   if($(this).closest('.hsguard').children('.active').children('.is_active').is(':checked')) {
//     is_active = "activa"
//   } else {
//     is_active = "pasiva"
//   }
//
//   $.ajax({
//     type: 'POST',
//     url: '/update-guard',
//
//     data: {
//       id: id.val(),
//       personal_id: selectMenu.val(),
//       is_active: is_active,
//       csrfmiddlewaretoken: window.CSRF_TOKEN,
//     },
//
//
//     success: function(data) {
//       name.html("")
//       name.html(data)
//       editable.prop('checked', false);
//       sele.slideUp();
//       alert("La guardia a sido modificada con exito");
//
//
//
//     },
//     error: function() {
//
//     }
//   })
// });

// -----------CHANGE COLOR WORKING DAYS-----------------------------
// $('.select_day').children('input[type=checkbox]:checked').each(function(){
// $(this).closest('td').css('background-color','#f6f7d4');
// });
//
// $('.form-check').children('input[type=checkbox]:checked').each(function(){
// $(this).closest('td').css('background-color','#f6f7d4');
// });
//
$('.select_day_single:checked').each(function(){
$(this).closest('td').children('.td').children('.shift2').fadeIn();
});

$('.select_day:checked').each(function(){
  $(this).closest('td').children('.td').children('.shift').css('background-color', '#206a5d');
  $(this).closest('td').children('.td').children('.shift').css('color', 'white');
  $(this).closest('td').children('.td').children('.shift').css('text-shadow', '0px 0px 3px white');
  $(this).closest('td').children('.td').children('.extra_day_div').children('.extra_day').removeAttr('disabled');
});
//
$('.form-check').children('.select_day_single').click(function() {
  if($(this).is(':checked')) {
    $(this).closest('td').children('.td').children('.shift2').fadeIn();

  } else {
    // $(this).parents('td').css('background-color', '');
  $(this).closest('td').children('.td').children('.shift2').fadeOut();
 }
});

$('.form-check').children('.select_day').click(function() {
  if($(this).is(':checked')) {
    // $(this).parents('td').css('background-color', '#99f3bd');
    $(this).closest('td').children('.td').children('.shift').css('background-color', '#206a5d');
    $(this).closest('td').children('.td').children('.shift').css('color', 'white');
    $(this).closest('td').children('.td').children('.shift').css('text-shadow', '0px 0px 3px white');
    $(this).closest('td').children('.td').children('.extra_day_div').children('.extra_day').removeAttr('disabled');
  } else {
    // $(this).parents('td').css('background-color', '');
    $(this).closest('td').children('.td').children('.shift').css('background-color', '');
    $(this).closest('td').children('.td').children('.shift').css('color', '#D6D0D0');
    $(this).closest('td').children('.td').children('.extra_day_div').children('.extra_day').attr('disabled', 'disabled');
 }
});

// $('.select_day').click(function() {
//   if($(this).is(':checked')) {
//     $(this).closest('.row').css('background-color', '#f6f7d4');
//   } else {
//     $(this).closest('.row').css('background-color', '');
//  }
// });

// -----------CHANGE PERSONAL BY SER/DEP-----------------------------

$('.allpersonal').click(function() {
  const selectMenu = $(this).closest('.hsguard').children('.column').children('.select').children('.list_personal')
  if($(this).is(':checked')) {
    selectMenu.empty()
    $.ajax({
    type: 'GET',
    url: '/department',
    data: {
      selDepartment:$("#department_selected").val()
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
      selService:$("#service_selected").val()
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


// -----------FILL OPTION SELECTORS-----------------------------

function updateServicePlan(){

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    selDepartment:$("#department_menu").val()
  },
  success: function(response){
    $('#service_menu').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#service_menu').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona servicio'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#service_menu').prepend(option)
    $('#dep_upd').val($("#department_menu").val())
    $('#dep_ser').val($("#department_menu").val())

  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateServicePlanSearch(){

  $.ajax({
  type: 'GET',
  url: '/json-ser',
  data: {
    selDepartment:$("#department_menu").val()
  },
  success: function(response){
    $('#service_menu_buscar').empty()
    const sectorData = response.service_list
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#service_menu_buscar').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona servicio'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#service_menu_buscar').prepend(option)

  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateGuardPlan(){

  $.ajax({
  type: 'GET',
  url: '/json-guar',
  data: {
    selServ:$("#service_menu").val()
  },
  success: function(response){
    $('#guard_menu').empty()
    const sectorData = response.guards
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#guard_menu').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona guardia'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#guard_menu').prepend(option)

  },
  error: function(error){
      console.log(error)
  }
  })
}

function updateGuardPlanSearch(){

  $.ajax({
  type: 'GET',
  url: '/json-guar',
  data: {
    selServ:$("#service_menu_buscar").val()
  },
  success: function(response){
    $('#guard_menu_buscar').empty()
    const sectorData = response.guards
    sectorData.map(item=>{
      const option = document.createElement('option')
      option.textContent = item.name
      option.setAttribute("value", item.id)
      $('#guard_menu_buscar').prepend(option)
    })
    const option = document.createElement('option')
    option.textContent = 'Selecciona guardia'
    option.setAttribute("selected", "selected")
    option.setAttribute("hidden", "hidden")
    $('#guard_menu_buscar').prepend(option)

  },
  error: function(error){
      console.log(error)
  }
  })
}


$("#department_menu").change(function(){
  updateServicePlan();
  updateServicePlanSearch();
});

$("#service_menu").change(function(){
  updateGuardPlan();
});

$("#service_menu").change(function(){
  updateGuardPlan();
});

$("#service_menu_buscar").change(function(){
  updateGuardPlanSearch();
});
