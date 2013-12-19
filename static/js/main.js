require.config({
    paths: {
      'jquery': '//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min',
      'bootstrap': '//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min'
    }
});

require(['app'], function(app) {
  app.initialize();
});