define(['jquery', 'bootstrap', 'lib/bootstrap/datepicker', 'ajax'], function($, bootstrap, datepicker, ajax) {

  function _setupDatePicker(){
    $('.datepicker').datepicker({
      format: 'yyyy-mm-dd',
      viewMode: 'months'
    });
  }

  function _setupToggle(){
    $(document).on('click', '[data-toggle]', [], function(){
      var _target = $(this).attr('data-toggle');
      $('#' + _target).toggle().removeClass('hidden');
    });
  }

  function _init(){
    _setupDatePicker();
    _setupToggle();
    ajax.initialize();
  }

  return {
    initialize: _init
  };
});