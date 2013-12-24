define(['jquery', 'bootstrap', 'lib/bootstrap/datepicker', 'ajax'], function($, bootstrap, datepicker, ajax) {

  function _setupCalendar(){
    $(document).ready(function() {
      $('.calendar').each(function(){
        $(this).fullCalendar({
          header:{
            left: 'prevYear,prev',
            center: 'title',
            right:  'today next,nextYear'
           },
           firstDay :1,
           weekMode : 'liquid',
           events: $(this).data('full-calendar-events')
        });
      });
    });
  }

  function _setupDayClickEvt(){
    $(document).on('click', 'td.fc-day', [], function(){
      $('td.fc-day').removeClass('fc-state-highlight');
      $(this).addClass('fc-state-highlight');
      $('#expense_date').val($(this).attr('data-date'));
    });
  }

  function _init(){
    _setupCalendar();
    _setupDayClickEvt();
  }

  return {
    initialize: _init
  }
});