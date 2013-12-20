define(['jquery'], function($) {

  function _setupDelete(){
    $(document).on('click', '[data-delete-type]', [], function(){
      if(!confirm('Are you sure to delete this')){
        return false;
      }

      var _type = $(this).attr('data-delete-type');
      var _id = $(this).attr('data-delete-id');

      $.ajax({
        dataType: 'json',
        url: '/' + _type + '?id=' + _id,
        type: 'DELETE',
        complete: function(data){
          location.reload();
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