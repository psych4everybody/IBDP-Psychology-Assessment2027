/* Paper 2 question pool, question-specific checklists and generators.
   Used by paper2.html (random question) and test.html (test conditions).
   Section B studies are fictional and written for practice. */
(function(){
  'use strict';

  var PRACTICALS = {
    experiment: {
      name: 'experiment', a: 'an experiment', topic: 'memory recall after a short wait',
      q1Type: 'I named the type of experiment we used (true experiment, two conditions, independent samples) and said what that meant in practice.',
      q1Detail: 'I gave one real detail: the IV (30-second wait or immediate recall) and the DV (words correctly recalled out of 20).',
      q1Record: 'I said how the data were recorded and processed (written recall, counted and compared between groups).',
      q1Ethics: 'I described the ethics we actually followed (consent, right to withdraw, debrief, anonymised scores).'
    },
    observation: {
      name: 'observation', a: 'an observation', topic: 'how people use devices in everyday settings',
      q1Type: 'I named the type of observation we used (naturalistic, covert, non-participant) and explained each word.',
      q1Detail: 'I gave one real detail: what counted as "one use" and that we recorded in 15-minute blocks.',
      q1Record: 'I said how behaviour was recorded (tally of uses, total duration, approximate age band).',
      q1Ethics: 'I described the ethics we followed (no consent possible because covert, so everyday settings only, no names, no images, age bands only).'
    },
    interview: {
      name: 'interview', a: 'an interview', topic: 'how a Grade 12 student copes with the stress of university applications',
      q1Type: 'I named the type of interview we used (semi-structured) and said what that meant in practice (core questions plus follow-ups).',
      q1Detail: 'I gave one real detail: a core question we asked and a follow-up.',
      q1Record: 'I said how the interview was recorded and analysed (audio, transcript checked against the recording, then coding or content analysis).',
      q1Ethics: 'I described the ethics we followed (consent to take part and to recording, right to withdraw, code instead of a name, recording deleted within 7 days, debrief).'
    }
  };
  var METHODS = ['experiment', 'observation', 'interview'];
  var CONCEPTS = ['bias', 'causality', 'measurement', 'responsibility', 'change', 'perspective'];
  var CONCEPT_DEF = {
    bias: 'a filter of experience or preference that distorts how data are collected or read',
    causality: 'whether a change in one variable produces a change in another',
    measurement: 'how a behaviour is operationalised so it can be recorded reliably and represented validly',
    responsibility: 'the researcher’s ethical duties to participants and to how findings are used',
    change: 'whether, and how, a study can show behaviour shifting over time or after an intervention',
    perspective: 'the approach and assumptions that frame a study, including whose viewpoint the data capture'
  };

  var DESIGN = {
    experiment: [
      'I wrote an aim on the topic of the practical named, not the topic of my experiment.',
      'I named an IV with two conditions and an operationalised DV (exactly what is counted or timed).',
      'I named the design: true or quasi, independent samples or repeated measures.',
      'I said who the participants are, how many, how they are chosen and how they are put into conditions.',
      'I included controls and standardised instructions.',
      'I included ethics: consent, right to withdraw, debrief, and a reason for any cover story.'
    ],
    observation: [
      'I wrote an aim and named the behaviour to be observed, on the topic of the practical named.',
      'I named the type with a reason: naturalistic or controlled, overt or covert, participant or non-participant.',
      'I defined behaviour categories clearly enough that another observer would record the same thing.',
      'I said where and when, and whether I use time sampling or event sampling.',
      'I said how behaviour is recorded and included an inter-rater reliability check with two observers.',
      'I included ethics: public settings only, no names or images, and a justification for any covert design.'
    ],
    interview: [
      'I named the type of interview with a reason (for example semi-structured, so core questions stay consistent).',
      'I wrote an aim on the topic of the practical named.',
      'I described the sample: technique, reason and number.',
      'I gave two example questions that are open and not leading.',
      'I described recording and transcription, checked against the audio.',
      'I described the analysis (coding into categories or content analysis) and the ethics (consent, recording, withdrawal, codes, deletion, debrief).'
    ]
  };

  var STUDIES = [
    {
      id: 'conformity', context: 'Human relationships',
      title: 'Group identity and online conformity',
      concepts: ['bias', 'causality', 'measurement', 'responsibility'],
      text: [
        'Researchers at a university in the UAE wanted to find out whether students change their opinions to match a group, and whether this depends on how strongly the students identify with that group. They invited 96 first-year undergraduates (all studying psychology, aged 18 to 20, 71% female) to take part in return for course credit.',
        'Before the main task, all participants completed a six-item questionnaire in which they rated statements such as "I am proud to be a student of this university" from 1 (strongly disagree) to 5 (strongly agree). Scores were added to give an identification score from 6 to 30.',
        'Participants were then told that they would join an online group chat with four other students from their university and rate 12 posters for a campus festival from 1 (poor) to 10 (excellent). In reality, the other four "students" were computer-controlled accounts. Participants were randomly assigned to one of two conditions. In the majority condition, the four accounts posted their ratings first, and these were always at least 3 points lower than the average rating the same poster had received in an earlier pilot test. In the control condition, participants rated the posters with no other ratings visible. Conformity was measured as the difference between each participant’s rating and the pilot average.',
        'In the majority condition, ratings were on average 1.9 points lower than the pilot average, compared with 0.2 points lower in the control condition. Within the majority condition, participants with identification scores above the median conformed more (mean shift of 2.4 points) than those below the median (mean shift of 1.4 points).',
        'After the session, all participants were told that the other accounts were computer-controlled and were offered the chance to withdraw their data. Four participants did so. Fourteen participants said they had suspected that the accounts were not real students.'
      ]
    },
    {
      id: 'selftest', context: 'Learning and cognition',
      title: 'Self-testing and memory for a science text',
      concepts: ['bias', 'causality', 'measurement', 'responsibility'],
      text: [
        'Researchers in Abu Dhabi wanted to find out whether testing yourself helps you remember more than rereading. They recruited 64 Grade 10 students from two schools through the students’ science teachers. Parents gave written consent and students gave their own consent. Students were told the study was about "study habits".',
        'All students read the same 600-word text about how coral reefs form. They were then randomly allocated to one of two conditions. In the rereading condition, students read the text again for 10 minutes. In the self-testing condition, students spent 10 minutes writing down everything they could remember without looking at the text.',
        'One week later, all students answered 20 short questions about the text in their classrooms. The researcher who marked the answers knew which condition each student had been in. Students in the self-testing condition scored a mean of 13.1 out of 20, compared with 10.4 in the rereading condition.',
        'Students were debriefed after the final test and told the real aim of the study. The researchers concluded that self-testing causes better long-term memory than rereading and recommended that schools teach it to all students.'
      ]
    },
    {
      id: 'sharing', context: 'Human development',
      title: 'Sharing behaviour in a nursery',
      concepts: ['bias', 'causality', 'change', 'measurement'],
      text: [
        'A research team wanted to find out how sharing develops in early childhood. They observed children at a nursery in Sharjah during free play over four weeks. Children were grouped by age: 3-year-olds (14 children) and 5-year-olds (16 children). Parents gave written consent, and the nursery’s head teacher approved the study.',
        'Two observers sat in the corner of the playroom and recorded every instance of sharing, defined as offering or handing a toy to another child without being asked by an adult, on a checklist. The observers were nursery staff, so the children were used to them being in the room. The two observers agreed on 84% of the instances they both recorded.',
        'Five-year-olds shared on average 6.2 times per session, compared with 2.9 times for 3-year-olds. The researchers concluded that sharing develops between the ages of three and five as children’s understanding of other people grows.'
      ]
    },
    {
      id: 'sleep', context: 'Health and well-being',
      title: 'Sleep and stress among university students',
      concepts: ['bias', 'causality', 'measurement', 'perspective'],
      text: [
        'A researcher wanted to know whether sleep is linked to stress among university students in Dubai. 240 students volunteered after seeing an advert on the university’s social media pages. They completed an anonymous online questionnaire asking how many hours they usually slept on weeknights, and rated ten statements about stress over the past month on a scale from 1 to 5. Participants could skip any question.',
        'Students who reported less sleep tended to report higher stress (r = -0.41). The researcher then interviewed eight of the students with the highest stress scores about their daily routines. The interviews were audio recorded with consent. Several students described staying up late to finish assignments and then feeling anxious the next day.',
        'The researcher concluded that poor sleep contributes to stress, and recommended that the university start a sleep awareness campaign.'
      ]
    }
  ];

  var SECTION_B_CHECK = [
    'I discussed at least two of the concepts listed in the question, and only concepts from that list.',
    'I defined each concept in my own words as it applies to this study.',
    'Every paragraph uses a specific detail from the study (a number, a step, a measure).',
    'I explained why each detail matters for the concept (the "one more question").',
    'I gave a limitation or counterpoint in each paragraph.',
    'I showed how two of the concepts interact at least once.',
    'My conclusion commits to a position about what the study does and does not show.'
  ];

  function pick(a){ return a[Math.floor(Math.random() * a.length)]; }
  function others(m){ return METHODS.filter(function(x){ return x !== m; }); }
  function art(m){ return PRACTICALS[m].a; }
  function joinConcepts(list){
    if(list.length < 2) return list.join('');
    return list.slice(0, -1).join(', ') + ' and/or ' + list[list.length - 1];
  }

  function q1(m){
    var p = PRACTICALS[m];
    return { type: 'Q1', marks: 4, minutes: 8, label: 'Q1 Describe',
      question: 'Describe how you used ' + p.a + ' in your class practical and its aim and procedure.',
      checklist: [
        'I started with our practical, not a general definition of the method.',
        'I stated the aim as a statement or a research question.',
        p.q1Type,
        'I said who took part, how they were chosen, and why.',
        p.q1Detail, p.q1Record, p.q1Ethics,
        'I described what we did. I did not evaluate it or report the findings.'
      ] };
  }
  function q2(m, c){
    c = c || pick(CONCEPTS);
    var p = PRACTICALS[m];
    return { type: 'Q2', marks: 4, minutes: 8, label: 'Q2 Explain a concept', concept: c,
      question: 'Explain the concept of ' + c + ' in relation to the ' + p.name + ' in your class practical.',
      checklist: [
        'I wrote about the ' + p.name + ', the practical the question named.',
        'Define: I explained ' + c + ' in one clear sentence (' + CONCEPT_DEF[c] + ').',
        'Link: I tied ' + c + ' to a real detail of the ' + p.name + ' (a variable, a number, a step, a rule).',
        'Limit: I gave one limitation linked to ' + c + ' and said what it did to the data.',
        'I used method terminology accurately.'
      ] };
  }
  function q3(m, o){
    o = o || pick(others(m));
    return { type: 'Q3', marks: 6, minutes: 12, label: 'Q3 Compare and contrast', other: o,
      question: 'Compare and contrast the research methodology of the ' + PRACTICALS[m].name + ' used in your class practical with the research methodology of ' + art(o) + '.',
      checklist: [
        'Every point names both the ' + PRACTICALS[m].name + ' and the ' + o + '.',
        'I included at least one similarity.',
        'I included at least two differences.',
        'I used at least one real detail from our ' + PRACTICALS[m].name + ' practical.',
        'Each point ends with "this means..." (why the similarity or difference matters).',
        'I wrote point by point, not two separate descriptions.'
      ] };
  }
  function q4(m, o){
    o = o || pick(others(m));
    var list = DESIGN[o].slice();
    list.unshift('I designed ' + art(o) + ', not my ' + PRACTICALS[m].name + ' again.');
    return { type: 'Q4', marks: 6, minutes: 13, label: 'Q4 Design', other: o,
      question: 'Design ' + art(o) + ' to investigate the same topic you investigated in your ' + PRACTICALS[m].name + ' class practical.',
      topicHint: 'Topic of your ' + PRACTICALS[m].name + ' practical: ' + PRACTICALS[m].topic + '.',
      checklist: list };
  }
  function secB(id){
    var st = id ? STUDIES.filter(function(s){ return s.id === id; })[0] : pick(STUDIES);
    return { type: 'B', marks: 15, minutes: 45, label: 'Section B Discuss', study: st,
      question: 'Discuss the following study with reference to two or more of the following concepts: ' + joinConcepts(st.concepts) + '.',
      checklist: SECTION_B_CHECK.slice() };
  }

  function makeQuestion(type, practical){
    var m = practical || pick(METHODS);
    switch(type){
      case 'Q1': return q1(m);
      case 'Q2': return q2(m);
      case 'Q3': return q3(m);
      case 'Q4': return q4(m);
      case 'B': return secB();
      default: return makeQuestion(pick(['Q1', 'Q2', 'Q3', 'Q4', 'B']), practical);
    }
  }
  function sectionA(){
    var m = pick(METHODS);
    var a = q1(m), b = q2(m), c = q3(m), d = q4(m);
    a.practical = b.practical = c.practical = d.practical = m;
    return [a, b, c, d];
  }
  var MODES = {
    full: { label: 'Full paper', minutes: 90, build: function(){ return sectionA().concat([secB()]); } },
    A:    { label: 'Section A only', minutes: 45, build: sectionA },
    B:    { label: 'Section B only', minutes: 45, build: function(){ return [secB()]; } }
  };

  window.P2BANK = { PRACTICALS: PRACTICALS, METHODS: METHODS, CONCEPTS: CONCEPTS, STUDIES: STUDIES,
    makeQuestion: makeQuestion, MODES: MODES, paperName: 'Paper 2', totalMarks: 35 };
})();
