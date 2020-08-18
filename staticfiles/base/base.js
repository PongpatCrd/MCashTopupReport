// make select search able
function make_select_search_able(element_id){
  $(element_id).select2({theme: "bootstrap4"});
}

// make input type text to datepicker
function make_input_to_datepicker(element_id){
  $(element_id).datepicker({
    dateFormat: 'dd/mm/yy',
    maxDate: '0'
  });
  $(element_id).attr( 'readOnly' , 'true' );
}

// loading_screen controller
function loading_screen(bool_turn_on){
  if(bool_turn_on){
    $("#Loading_screen").attr('hidden', false);
  }
  else{
    $("#Loading_screen").attr('hidden', true);
  }
}

// set datepicker value
function set_datepicker_value(element_id, val){
  // val must in format dd/mm/yy
  $(element_id).datepicker('setDate', val);
}

function create_default_datepicker_value(minus_date){
  let current_date = new Date();
  let date_use = new Date(new Date().setDate(current_date.getDate()-minus_date));

  let day = date_use.getDate();
  let month = date_use.getMonth()+1;
  let year = date_use.getFullYear();

  if(day < 10){
    day = '0' + day;
  }
  else{
    day = day.toString();
  }

  if(month < 10){
    month = '0' + month;
  }
  else{
    month = month.toString();
  }

  year = year.toString();

  ans = day + '/' + month + '/'+ year;
  return ans
}