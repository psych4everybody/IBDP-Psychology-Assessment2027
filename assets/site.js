/* IB Psychology revision site: shared behaviour.
   1. Section switching on paper pages (tabs, side menu, previous/next)
   2. Self-test tables (blur to hide, tap to reveal)
   3. Checklists saved in this browser (localStorage, guarded)
   4. Paper 1 Section C question builder
   5. Hub ticks for completed checklists */

(function(){
  'use strict';

  // ---------- safe storage ----------
  var store={
    get:function(k){try{return window.localStorage.getItem(k);}catch(e){return null;}},
    set:function(k,v){try{window.localStorage.setItem(k,v);}catch(e){}}
  };
  var PREFIX='ibpsy27:';

  // ---------- 1. section switching ----------
  var topics=[].slice.call(document.querySelectorAll('.topic'));
  var tabs=[].slice.call(document.querySelectorAll('#tabs a'));
  var toc=document.getElementById('tocList');
  var current=null, obs=null;

  function buildNav(t,i){
    var nav=t.querySelector('.topic-nav');
    if(!nav)return;
    var html='';
    if(i>0){var p=topics[i-1];html+='<a class="prev" href="#'+p.id+'"><small>Previous</small>&larr; '+p.dataset.short+'</a>';}
    if(i<topics.length-1){var n=topics[i+1];html+='<a class="next" href="#'+n.id+'"><small>Next</small>'+n.dataset.short+' &rarr;</a>';}
    nav.innerHTML=html;
  }
  topics.forEach(buildNav);

  function observeSections(t){
    if(!toc||!('IntersectionObserver' in window))return;
    if(obs)obs.disconnect();
    var links=[].slice.call(toc.querySelectorAll('a'));
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
    obs=new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){
          links.forEach(function(a){a.classList.remove('active');});
          var a=map[en.target.id];if(a)a.classList.add('active');
        }
      });
    },{rootMargin:'-90px 0px -65% 0px'});
    t.querySelectorAll('section.card[data-toc]').forEach(function(s){obs.observe(s);});
  }

  function show(t){
    if(!t||current===t)return;
    current=t;
    topics.forEach(function(x){x.classList.toggle('shown',x===t);});
    tabs.forEach(function(a){
      var on=a.dataset.tab===t.id;
      a.classList.toggle('on',on);
      if(on){
        a.setAttribute('aria-current','page');
        var strip=a.parentNode;
        if(strip.scrollWidth>strip.clientWidth){strip.scrollLeft=a.offsetLeft-strip.offsetLeft-(strip.clientWidth-a.offsetWidth)/2;}
      }else a.removeAttribute('aria-current');
    });
    var h=document.getElementById('heroTitle'), s=document.getElementById('heroSub');
    if(h&&t.dataset.title)h.textContent=t.dataset.title;
    if(s&&t.dataset.sub)s.textContent=t.dataset.sub;
    if(document.body.dataset.paper)document.title=t.dataset.title+' | '+document.body.dataset.paper+' | IB Psychology 2027 Revision';
    if(toc){
      toc.innerHTML='';
      t.querySelectorAll('section.card[data-toc]').forEach(function(sec){
        var li=document.createElement('li');
        li.innerHTML='<a href="#'+sec.id+'">'+sec.dataset.toc+'</a>';
        toc.appendChild(li);
      });
    }
    observeSections(t);
  }

  function topicOf(el){return el?(el.classList.contains('topic')?el:el.closest('.topic')):null;}

  function route(){
    if(!topics.length)return;
    var id=decodeURIComponent(location.hash.slice(1));
    var el=id?document.getElementById(id):null;
    var t=topicOf(el)||topics[0];
    show(t);
    if(el&&el!==t)el.scrollIntoView();
  }

  if(topics.length){
    window.addEventListener('hashchange',route);
    window.addEventListener('popstate',route);
    document.addEventListener('click',function(e){
      var a=e.target.closest('a[href^="#"]');
      if(!a)return;
      var id=decodeURIComponent(a.getAttribute('href').slice(1));
      var el=id?document.getElementById(id):null;
      var t=topicOf(el);
      if(!t)return;
      e.preventDefault();
      show(t);
      try{history.pushState(null,'','#'+id);}catch(err){}
      if(el===t){var bar=document.querySelector('.topbar');window.scrollTo(0,bar?bar.offsetTop:0);}
      else el.scrollIntoView();
    });
    route();
  }

  // ---------- 2. self-test tables ----------
  document.querySelectorAll('.toggle-btn[data-target]').forEach(function(btn){
    var target=document.getElementById(btn.dataset.target);
    if(!target)return;
    btn.addEventListener('click',function(){
      var on=!target.classList.contains('testing');
      target.classList.toggle('testing',on);
      btn.setAttribute('aria-pressed',on?'true':'false');
      btn.textContent=on?'Show all answers':'Hide the answers';
      target.querySelectorAll('.revealed').forEach(function(c){c.classList.remove('revealed');});
    });
  });
  document.addEventListener('click',function(e){
    var cell=e.target.closest('.testing .can-hide');
    if(cell)cell.classList.toggle('revealed');
  });

  // ---------- 3. checklists ----------
  document.querySelectorAll('ul.checklist[data-key]').forEach(function(list){
    var key=PREFIX+list.dataset.key;
    var boxes=[].slice.call(list.querySelectorAll('input[type="checkbox"]'));
    var saved={};
    try{saved=JSON.parse(store.get(key)||'{}')||{};}catch(e){saved={};}
    var prog=list.parentNode.querySelector('.progress');
    function update(){
      var n=boxes.filter(function(b){return b.checked;}).length;
      if(prog)prog.textContent=n+' of '+boxes.length+' ticked'+(n===boxes.length?'. Ready.':'');
      store.set(key+':done',n===boxes.length?'1':'0');
    }
    boxes.forEach(function(b,i){
      b.checked=!!saved[i];
      b.addEventListener('change',function(){saved[i]=b.checked;store.set(key,JSON.stringify(saved));update();});
    });
    update();
  });

  // ---------- 5. hub ticks ----------
  document.querySelectorAll('[data-done-key]').forEach(function(el){
    if(store.get(PREFIX+el.dataset.doneKey+':done')==='1'){
      var t=el.querySelector('.tick');if(t)t.textContent='✓ ready';
    }
  });

  // ---------- 6. random Section A question ----------
  var saGo=document.getElementById('saGo');
  if(saGo){
    var saRows=[].slice.call(document.querySelectorAll('#a-bank tr[data-q]'));
    var saOut=document.getElementById('saOut'), saReveal=document.getElementById('saReveal'), saAns=document.getElementById('saAns');
    var esc=function(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML;};
    saGo.addEventListener('click',function(){
      var r=saRows[Math.floor(Math.random()*saRows.length)];
      var qs=r.dataset.q.split('||');
      var q=qs[Math.floor(Math.random()*qs.length)];
      var verb=Math.random()<0.5?'Describe':'Explain';
      q=q.replace('Describe/Explain',verb)+' [4]';
      saOut.innerHTML='<span class="small">'+esc(r.dataset.approach)+'</span>'+esc(q);
      saOut.classList.add('on');
      saAns.innerHTML='<p><b>Recommended study:</b> '+esc(r.dataset.study)+'</p><p><b>Key vocabulary:</b> '+esc(r.dataset.vocab)+'</p><p class="small">Check your glue sentence: does it say why the study demonstrates '+esc(r.dataset.term.toLowerCase())+'?</p>';
      saReveal.hidden=false; saReveal.open=false;
    });
  }

  // ---------- 7. random scenario ----------
  var scnGo=document.getElementById('scnGo');
  if(scnGo){
    var scns=[].slice.call(document.querySelectorAll('#b-bank .scenario'));
    scnGo.addEventListener('click',function(){
      scns.forEach(function(s){s.classList.remove('flash');});
      document.querySelectorAll('#b-bank details.scn-group').forEach(function(d){d.open=false;});
      var s=scns[Math.floor(Math.random()*scns.length)];
      var d=s.closest('details');if(d)d.open=true;
      s.classList.add('flash');
      s.scrollIntoView({block:'start'});
    });
  }

  // ---------- 4. question builder ----------
  var qb=document.getElementById('qbOut');
  if(qb){
    var AREAS={
      'health and well-being':[
        'biological explanations of one mental health disorder',
        'cognitive models of one mental health disorder',
        'cultural differences in mental health',
        'environmental factors in mental health disorders',
        'changes in the prevalence of one health problem',
        'the role of social learning in one health problem',
        'the role of stress in one health problem',
        'one biological treatment for one mental health disorder',
        'one psychological treatment for one mental health disorder',
        'prevention or treatment strategies for one health problem'
      ],
      'human development':[
        'the role of brain maturation in development',
        'critical periods in development',
        'neuroplasticity in development',
        'sociocultural factors in development',
        'stage theories and continuous models of development',
        'theory of mind',
        'attachment and the development of self',
        'the enculturation of social norms',
        'peer influence on the development of self',
        'the role of childhood experiences in the development of self'
      ],
      'human relationships':[
        'acculturation strategies',
        'compliance techniques',
        'conformity in groups',
        'cultural dimensions',
        'social identity theory',
        'social learning in groups',
        'chemical messengers in interpersonal relationships',
        'cognitive explanations of interpersonal relationships',
        'communication in interpersonal relationships',
        'strategies for improving interpersonal relationships'
      ],
      'learning and cognition':[
        'cognitive biases in decision-making',
        'classical and operant conditioning',
        'the dual processing model',
        'schema theory',
        'social learning theory',
        'biological factors in one cognitive process',
        'cognitive models of one cognitive process',
        'cultural factors in one cognitive process',
        'environmental influences on one cognitive process',
        'strategies to improve one cognitive process'
      ]
    };
    var T={
      bias:{
        'discuss':'discuss the role of bias in research on {a}.',
        'evaluate':'evaluate how bias may affect research on {a}.',
        'to what extent':'to what extent does bias limit what research on {a} can tell us about behaviour?'
      },
      causality:{
        'discuss':'discuss what research on {a} can and cannot show about cause and effect.',
        'evaluate':'evaluate the extent to which research on {a} can establish causal relationships.',
        'to what extent':'to what extent can research on {a} establish cause and effect?'
      },
      change:{
        'discuss':'discuss what research on {a} shows about change in behaviour.',
        'evaluate':'evaluate what research on {a} shows about how behaviour changes.',
        'to what extent':'to what extent does research on {a} show that behaviour can change?'
      },
      measurement:{
        'discuss':'discuss the challenges of measurement in research on {a}.',
        'evaluate':'evaluate the strategies psychologists use to measure behaviour in research on {a}.',
        'to what extent':'to what extent can research on {a} measure behaviour accurately?'
      },
      perspective:{
        'discuss':'CLAIM',
        'evaluate':'evaluate {a} with reference to more than one perspective.',
        'to what extent':'to what extent does research on {a} show that more than one perspective is needed to explain behaviour?'
      },
      responsibility:{
        'discuss':'discuss the responsibilities of psychologists when researching or applying {a}.',
        'evaluate':'evaluate the ethical responsibilities involved in research on {a}.',
        'to what extent':'to what extent do psychologists act responsibly when they research or apply {a}?'
      }
    };
    var CONCEPTS=Object.keys(T), COMMANDS=['discuss','evaluate','to what extent'];
    var ctxSel=document.getElementById('qbContext'), conSel=document.getElementById('qbConcept'), cmdSel=document.getElementById('qbCommand');
    var meta=document.getElementById('qbMeta');
    function pick(arr){return arr[Math.floor(Math.random()*arr.length)];}
    function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
    function build(){
      var ctx=ctxSel.value==='any'?pick(Object.keys(AREAS)):ctxSel.value;
      var con=conSel.value==='any'?pick(CONCEPTS):conSel.value;
      var cmd=cmdSel.value==='any'?pick(COMMANDS):cmdSel.value;
      var area=pick(AREAS[ctx]);
      var tpl=T[con][cmd], q;
      if(tpl==='CLAIM'){
        q='One claim in the psychology of '+ctx+' is that a single perspective is not enough to explain behaviour. Discuss this claim with reference to '+area+'. [15]';
      }else{
        q='In the context of '+ctx+', '+tpl.replace('{a}',area)+' [15]';
      }
      qb.textContent=q;
      meta.innerHTML='<span class="chip">Context: '+cap(ctx)+'</span>'+
        '<span class="chip">Area of study: '+cap(area)+'</span>'+
        '<span class="chip cc cc-'+con+'">Concept: '+cap(con)+'</span>'+
        '<span class="chip">Command term: '+cap(cmd)+'</span>';
    }
    document.getElementById('qbGo').addEventListener('click',build);
    build();
  }
})();
