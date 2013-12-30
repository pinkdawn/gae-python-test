define(['jquery', 'ajax', 'bootstrap'], function($, ajax) {

  function _setupToggle(){
    $(document).on('click', '[data-toggle]', [], function(){
      var _target = $(this).attr('data-toggle');
      $('#' + _target).toggle().removeClass('hidden');
    });
  }

  function _init(){
    _setupToggle();
    ajax.initialize();
  }

  return {
    initialize: _init
  };
});