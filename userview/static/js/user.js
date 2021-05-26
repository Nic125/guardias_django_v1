$('.user_month_plan').click(function(){
  $(".user_month_plan").slideUp(0)
  $(".day_guards").slideUp(200)
  $(".total").slideDown(200)
  $(".month").slideDown(200)
  $(".user_month_plan2").slideDown(200)
});

$('.user_month_plan2').click(function(){
  $(".user_month_plan2").slideUp(0)
  $(".day_guards").slideDown(200)
  $(".total").slideUp(200)
  $(".month").slideUp(200)
  $(".user_month_plan").slideDown(200)
});
