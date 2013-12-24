require.config({
    paths: {
      'jquery': '//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min',
      'bootstrap': '//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min'
    },
    shim:{
      'lib/bootstrap/datepicker': {
        deps: ['jquery']
      },
      'lib/fullcalendar.min': {
        deps: ['jquery']
      }
    }
});

require(['app'], function(app) {
  app.initialize();
});