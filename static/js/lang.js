define(['locale/cn'], function(_dict) {

  function tran(input){
    var _q = input.toLowerCase();
    if (_q in _dict){
      return _dict[_q];
    }

    return input;
  }

  return tran;
});