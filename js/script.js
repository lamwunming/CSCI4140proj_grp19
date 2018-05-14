function showandhide(id) {
  var dashb = document.getElementById('dashboard');
  var mysav = document.getElementById('mysave');
  var analy = document.getElementById('analysis');
  var compa = document.getElementById('compare');
  var repor = document.getElementById('report');

  var dive = document.getElementById(id);
  if(dive.id!='dashboard'){
    document.getElementById('show').style.display = 'none';
  }
  else{
    document.getElementById('show').style.display = 'block';
  }
  if(dive.id!='compare'){
    document.getElementById('secondCode').style.display = 'none';
  }
  else{
    document.getElementById('secondCode').style.display = 'block';
  }

  dashb.style.display = 'none';
  mysav.style.display = 'none';
  analy.style.display = 'none';
  compa.style.display = 'none';
  repor.style.display = 'none';
  dive.style.display = 'block';
}
