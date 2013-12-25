define(['jquery', 'lib/bootstrap/bootbox.min', 'lib/fullcalendar.min'], function ($) {

  function editExpense(cal, jsEvent, title){
    var _expenseID = cal.id;
    var _carID = cal.car;
    var _url = '/car/' + _carID + '/expense/' + _expenseID;

    $.get(_url, function(html){
      bootbox.dialog({
        message: html,
        title: "Edit Expense"
      });

      // make sure dom is visible before init map, or 2nd time map will ne abnormal
      setTimeout(function(){_setupMap();}, 200);
      _setupEditForm();
    });
  }

  function _setupMap(){
    var map = new BMap.Map("baidu-map");

    var marker = undefined;
    var lng = $("#expenseLngEdit").val(), lat = $("#expenseLatEdit").val();
    if (lng && lat){
      var _initPoint = new BMap.Point(lng,lat);

      marker = new BMap.Marker(_initPoint);
      map.addOverlay(marker);

      setTimeout(function(){map.centerAndZoom(_initPoint,17);}, 200);
    } else {
      map.centerAndZoom("厦门",15);
    }

    map.enableScrollWheelZoom(true);

    map.addEventListener("click",function(e){
      $("#expenseLngEdit").val(e.point.lng);
      $("#expenseLatEdit").val(e.point.lat);

      map.removeOverlay(marker);
      marker = new BMap.Marker(e.point);
      map.addOverlay(marker);
    });

    var local = new BMap.LocalSearch(map, {
      renderOptions:{map: map}
    });
    $('span.map-search').click(function(){
      local.search($('#expenseAddressEdit').val());
    });
  }

  function _setupEditForm(){
    $('#expenseEditForm').submit(function(e){
      e.preventDefault();
      var _data = $(this).serialize();
      var _url = $(this).attr('action') + '?ajax=1';

      $.ajax({
        dataType: 'json',
        url: _url,
        data: _data,
        type: 'POST',
        complete: function(data){
          bootbox.hideAll();
        }
      });
    });
  }

  function _setupCalendar() {
    $(document).ready(function () {
      $('.calendar').each(function () {
        $(this).fullCalendar({
          header: {
            left: 'prevYear,prev',
            center: 'title',
            right: 'today next,nextYear'
          },
          firstDay: 1,
          weekMode: 'liquid',
          events: $(this).data('full-calendar-events'),
          eventClick: editExpense
        });
      });
    });
  }

  function _setupDayClickEvt() {
    $(document).on('click', 'td.fc-day', [], function () {
      $('td.fc-day').removeClass('fc-state-highlight');
      $(this).addClass('fc-state-highlight');
      $('#expense_date').val($(this).attr('data-date'));
    });
  }

  function _init() {
    _setupCalendar();
    _setupDayClickEvt();
  }

  return {
    initialize: _init
  }
});