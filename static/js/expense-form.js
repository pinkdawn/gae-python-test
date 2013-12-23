define(['jquery'], function($) {

  function _init(){
    $(document).on('click', '[data-expense-type]', [], function(event){
      var _form = $(this).parents('form');
      var _type = $(this).attr('data-expense-type');
      $('#expense_type').val(_type);

      _form.submit();
    });
  }

  return {
    initialize: _init
  };
});