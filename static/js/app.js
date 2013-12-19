define(['jquery', 'bootstrap', 'lib/bootstrap/datepicker', 'ajax'], function($, bootstrap, datepicker, ajax) {

  function _setupDatePicker(){
    $('.datepicker').datepicker({
      format: 'yyyy-mm-dd',
      viewMode: 'months'
    });
  }

  function _init(){
    _setupDatePicker();
    ajax.initialize();
  }

  return {
    initialize: _init
  };
});