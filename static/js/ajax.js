define(['jquery'], function($) {

  function _setupDelete(){
    $(document).on('click', '[data-delete-url]', [], function(){
      if(!confirm('Are you sure to delete this')){
        return false;
      }

      var _url = $(this).attr('data-delete-url');
      var _target = $(this).attr('data-remove-selector');
      var _refresh = $(this).attr('data-remove-refresh');

      $.ajax({
        dataType: 'json',
        url: _url,
        type: 'DELETE',
        complete: function(data){
          if (_refresh){
            location.reload();
          } else {
            $(_target).remove();
          }
        }
      });
    });
  }

  function _init(){
    _setupDelete();
  }

  return {
    initialize: _init
  };
});