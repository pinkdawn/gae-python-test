define(['jquery'], function($) {

  function _setupDelete(){
    $(document).on('click', '[data-delete-type]', [], function(){
      var _type = $(this).attr('data-delete-type');
      var _id = $(this).attr('data-delete-id');

      $.ajax({
        dataType: 'json',
        url: '/' + _type + '?id=' + _id,
        type: 'DELETE',
        complete: function(data){
          location.href = location.href;
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