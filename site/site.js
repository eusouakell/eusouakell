(function(){
var bg=document.querySelector('.bg'),nv=document.getElementById('nv');
if(bg){bg.addEventListener('click',function(){var o=nv.classList.toggle('op');bg.setAttribute('aria-expanded',o)})}
// reveal on scroll
var els=[].slice.call(document.querySelectorAll('[data-rv]'));
els.forEach(function(e){var i=[].indexOf.call(e.parentNode.children,e);e.classList.add('rv');e.style.setProperty('--d',(Math.min(i,5)*.08)+'s')});
if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')})}
else{var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.1,rootMargin:'0px 0px -5% 0px'});els.forEach(function(e){io.observe(e)});setTimeout(function(){els.forEach(function(e){e.classList.add('in')})},7000)}
})();

// pause/play controls for marquees
var mqs=[].slice.call(document.querySelectorAll('.mq'));
mqs.forEach(function(m){
  var w=document.createElement('div');w.className='mqw';
  m.parentNode.insertBefore(w,m);w.appendChild(m);
  var b=document.createElement('button');
  b.type='button';b.className='mqpp';b.setAttribute('aria-pressed','false');b.setAttribute('aria-label','Pausar carrossel');
  b.innerHTML='<svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="6" y="5" width="4" height="14" rx="1" fill="currentColor"/><rect x="14" y="5" width="4" height="14" rx="1" fill="currentColor"/></svg><svg class="i-play" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>';
  b.addEventListener('click',function(){
    var p=w.classList.toggle('paused');
    b.setAttribute('aria-pressed',p?'true':'false');
    b.setAttribute('aria-label',p?'Retomar carrossel':'Pausar carrossel');
  });
  w.appendChild(b);
});
