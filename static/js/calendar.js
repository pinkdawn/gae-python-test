define(['jquery', 'lang', 'lib/opentip-jquery.min', 'lib/bootstrap/bootbox.min', 'lib/fullcalendar.min'], function ($, _) {

  function editExpense(cal, jsEvent, title){
    var _expenseID = cal.id;
    var _carID = cal.car;
    var _url = '/car/' + _carID + '/expense/' + _expenseID;

    $.get(_url, function(html){
      bootbox.dialog({
        message: html,
        title: "修改支出"
      });

      // make sure dom is visible before init map, or 2nd time map will ne abnormal
      setTimeout(function(){_setupMap();}, 200);
      _setupEditForm(cal);
    });
  }

  // hover in, init tip and show it
  function hoverExpense(event, jsEvent, view){
    var _tip = $(this).data('tip');
    if (_tip){
      _tip.setContent(event.address); // in case address edited
      _tip.show();
      return;
    }

    var _tip = new Opentip(
      $(this),
      event.address,
      {target:true, tipJoint: 'bottom center', style:'dark'}
    );
    _tip.show();

    $(this).data('tip', _tip);
  }

  // hover out, hide tip
  function hoverOutExpense(event, jsEvent, view){
    var _tip = $(this).data('tip');
    if (_tip){
      _tip.hide();
    }
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

  function _setupEditForm(expense){
    $('#expenseEditForm').submit(function(e){
      e.preventDefault();

      // update expense display and hover tips
      var _formArray = $(this).serializeArray();
      expense.title = '';
      for (var i=0;i<_formArray.length;i++){
        var key = _formArray[i].name;
        var val = _formArray[i].value;

        switch(key){
          case 'amount':
            expense.title = expense.title + ' ' + val;
            break;
          case 'address':
            expense.address = val;
            break;
          case 'type':
            expense.title = _(val) + expense.title;
          default :
            break;
        }
      }
      $('.calendar').fullCalendar('updateEvent', expense);

      // update expense in server
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
          eventClick: editExpense,
          eventMouseover: hoverExpense,
          eventMouseout: hoverOutExpense,
          dayNamesShort: ['日','一','二','三','四','五','六'],
          titleFormat:{month:'yyyy-MM'}
        });
      });
    });
  }

  function _setupEvent() {
    $(document).on('click', 'td.fc-day', [], function () {
      $('td.fc-day').removeClass('fc-state-highlight');
      $(this).addClass('fc-state-highlight');
      $('#expense_date').val($(this).attr('data-date'));
    });
    $(document).keyup(function(e) {
      if (e.keyCode == 27) {
        bootbox.hideAll();
      }
    });
  }

  function _init() {
    _setupCalendar();
    _setupEvent();
  }

  return {
    initialize: _init
  }
});