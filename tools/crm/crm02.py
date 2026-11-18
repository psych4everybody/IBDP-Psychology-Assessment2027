from lib import Page, checklist, earns, chips, table, slot_list, tip, frame

P = Page("CRM-02", "02", "Writing with Concepts",
         "How do you write about a concept so that it could only belong to your answer?")
S = P.slot

LP = ("In Loftus and Palmer (1974), students watched short films of car crashes and were then asked how fast the cars were going. "
      "The only thing that differed between groups was one verb in the question.")

# ---------------- START ----------------
P.topic("start", "Writing with Concepts", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to test your own sentences with the swap test, and use the five rungs to turn a general comment about a concept into analysis that belongs to one study and one question. Every Concept Workout in this site uses these rungs.</p>
{checklist("CRM-02-goals", [
 "I can explain what the swap test checks, and use it on my own sentences.",
 "I can name the five rungs and say what each one trains.",
 "I can decode a Paper 1 Section C question into its context, area of study, concept and command term.",
 "I can turn a general sentence about a concept into one that is specific to a study.",
 "I can write a conclusion sentence that names a condition.",
])}
<p class="progress"></p>
<p class="small">Part of the course: the six concepts, and how to write about them. This is a skills chapter: it teaches the method you will practise in every Concept Workout.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 1 Section C (every concept-based essay); Paper 2 Section B (discussing an unseen study using concepts); Paper 2 Section A Question 2 (explaining a concept in relation to your class practical)</p>
{chips("causality", "measurement", "bias")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
<p>{LP} Two students wrote one sentence each about this study.</p>
{tip("<p><b>Sentence A:</b> This study has low ecological validity because it was done in a lab, so the results may not apply to real life.</p><p><b>Sentence B:</b> Watching short film clips in a classroom is not the same as seeing a real crash, so the effect of the word \"smashed\" on speed estimates may be smaller for a frightened eyewitness who is questioned by police days later.</p>")}
<p>1. Which sentence could be pasted into an answer about almost any laboratory study?</p>
{S("W", 2)}
<p>2. Which words make the other sentence belong to this study only?</p>
{S("W", 2)}""", "Warm-up")

# ---------------- READ ----------------
P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>Why general sentences do not earn marks</h2>
<p>Two exam tasks are built around concepts: the Paper 1 Section C essay and the Paper 2 Section B evaluation of an unseen study. In both, the marks rise as your links between the concept and the content become more relevant, more developed and more specific to the question. At the top of the range, examiners want analysis that is clearly about <i>this</i> study or <i>this</i> area of study, and a conclusion that follows from your argument.</p>
<p>The trap is the general sentence. "Experiments can show cause and effect." "Lab studies lack ecological validity." "More research is needed." Each is true, and each could appear in almost any answer, which is exactly the problem: it shows you know the vocabulary, not that you can think with it. General sentences <b>describe</b>. Specific sentences <b>analyse</b>.</p>
<p>Remember from CRM-01: exam questions use only the concept word, any idea can be linked to any concept, and it is the explanation of the link that earns the marks. This chapter gives you a routine for building those explanations.</p>""", "Why general sentences do not earn marks")

P.card("rd-2", f"""<h2>The swap test</h2>
<p>Before you keep a sentence about a concept, try to swap the study or topic in it for a different one. If the sentence still works, it is too general. A sentence <b>passes</b> when it could only belong to this answer, because it uses a detail of this study, this topic or this question.</p>
{table(["Fails the swap test", "Passes the swap test"], [
 ["The sample was biased, so the results cannot be generalised.", "All 39 participants were students in Forer's own class, rating a profile handed out by their teacher, so they may have rated it more generously than strangers reading it online would."],
 ["This was an experiment, so it shows cause and effect.", "Because the groups in Loftus and Palmer saw the same films and differed only in the verb, the difference in speed estimates can be put down to the wording of the question."],
 ["The study used self-report, which may not be valid.", "Students rated the profile's accuracy on a 0 to 5 scale, which measures how much they liked the description as much as how well it fitted them."],
], keycol=False)}
<p>Notice what the passing sentences add: a <b>detail</b> from the study, and a <b>consequence</b> for what the study can or cannot show.</p>""", "The swap test")

P.card("rd-3", f"""<h2>The five rungs</h2>
<p>The five rungs are a ladder from understanding the question to committing to an answer. Do them in order. In every Concept Workout on this site, each rung has guiding questions that point the way without giving you the answer.</p>
{table(["Rung", "What you do", "What it trains"], [
 ["1. Decode", "Break the question into its context, area of study, concept and command term.", "Answering the question that was asked"],
 ["2. Define", "Define the topic and the concept in one sentence each, as they apply to this question.", "Accurate knowledge and terminology"],
 ["3. Upgrade", "Rewrite a sentence that fails the swap test so that it passes.", "Relevant, specific links between the concept and the content"],
 ["4. One more question", "Take a finding and ask one more question before you accept it.", "Critical analysis"],
 ["5. Commit", "Write a conclusion sentence that names a condition.", "A reasoned, clearly stated conclusion"],
])}
<p>For Paper 1 Section C, the workouts ask you to write plans, not full essays. A plan you can explain is worth more in revision than an essay you have memorised.</p>""", "The five rungs")

P.card("rd-4", f"""<h2>Rung 1: Decode</h2>
<p>A Section C question is built from four parts. Find all four before you write anything.</p>
{table(["Part", "What to look for", "Example"], [
 ["Context", "One of the four contexts, usually at the start: \"In the context of...\"", "learning and cognition"],
 ["Area of study", "A topic from that context's table in the guide. Only the main areas are used, never the subheadings that group them.", "schema theory"],
 ["Concept", "One of the six concepts, named exactly.", "causality"],
 ["Command term", "Evaluate (weigh strengths and limitations), discuss (offer a balanced review with a range of arguments) or to what extent (consider the merits of a claim and reach a judgement).", "to what extent"],
])}
<p>Then ask one more thing: which idea from another chapter sits close to this question but is <i>not</i> what it asks? Writing about the wrong neighbour, for example describing a memory model when the question asks about schema theory, is one of the most common ways to lose marks.</p>""", "Rung 1: Decode")

P.card("rd-5", """<h2>Rung 2: Define</h2>
<p>Define the topic and the concept in one sentence each, <b>as they apply to this question</b>. A dictionary definition of causality ("one thing causing another") is accurate but does no work. A working definition sets up your argument: "Causality here means whether research can show that activating a schema changes what people remember, rather than only showing that the two go together."</p>
<p>A good test: could your definition only appear in an essay on this question? If yes, it is doing its job.</p>""", "Rung 2: Define")

P.card("rd-6", f"""<h2>Rung 3: Upgrade</h2>
<p>This is the swap test in action. Take a sentence that fails and rebuild it in four moves:</p>
<ol>
<li><b>Name the concept and the idea you are using</b>, for example causality and the role of a control group.</li>
<li><b>Point to the exact feature of the study</b> that raises it, for example "the groups saw identical films and heard different verbs".</li>
<li><b>Explain the consequence</b> for the conclusion, for example "so the wording, not the film, explains the difference in estimates".</li>
<li><b>Connect to a second concept</b> if you can, for example "but this only shows a change in the estimate participants gave, which is a measurement question".</li>
</ol>
{frame("Weak: Experiments control variables, so this study shows causality.<br>Upgraded: Because the only difference between the groups in Loftus and Palmer was the verb in one question, the higher speed estimates after \"smashed\" can be attributed to the wording; whether the wording changed the memory itself, or only the answer, is a separate question about what was measured.")}""", "Rung 3: Upgrade")

P.card("rd-7", f"""<h2>Rung 4: One more question</h2>
<p>Strong analysis does not accept a finding at face value. Before you accept a conclusion, ask one more question. Each concept suggests its own kind of question:</p>
{table(["Concept", "One more question to ask"], [
 ["Bias", "Who took part, who was left out, and who interpreted the results?"],
 ["Causality", "What else changed at the same time? Which way does the arrow point?"],
 ["Change", "Would this change have happened anyway? Does it last?"],
 ["Measurement", "What exactly was counted or rated, and is that the same as the thing we care about?"],
 ["Perspective", "How would a different approach explain the same finding?"],
 ["Responsibility", "Who could be harmed by this research, or by the way its findings are used?"],
])}
<p>Then <b>link it</b>: most good questions about one concept turn out to raise another. That link is often the most impressive sentence in an answer.</p>""", "Rung 4: One more question")

P.card("rd-8", f"""<h2>Rung 5: Commit</h2>
<p>A conclusion must take a position, and the strongest positions name a <b>condition</b>: when, for whom or in what way the claim holds.</p>
{frame("Research can establish causality in the study of schema theory when [condition], because [reason].")}
<p>Some conclusions are ruled out because they do not commit to anything:</p>
<ul>
<li>"Experiments show cause and effect." (Which experiments? Shown how strongly?)</li>
<li>"It depends." (Unless you say on what.)</li>
<li>"More research is needed." (What research, and what would it show?)</li>
</ul>""", "Rung 5: Commit")

P.card("rd-9", f"""<h2>The study used in the workout: Loftus and Palmer (1974)</h2>
{table(None, [
 ["Aim", "To find out whether the wording of a question asked after an event changes what people report about it."],
 ["Experiment 1", "45 university students in the USA watched seven short films of traffic accidents. Afterwards they answered questions, including the critical one: \"About how fast were the cars going when they ___ each other?\" Groups of nine heard different verbs: smashed, collided, bumped, hit or contacted. The mean speed estimate was 40.8 mph for \"smashed\" and 31.8 mph for \"contacted\", with the other verbs in between."],
 ["Experiment 2", "150 students watched one film of a crash. One group was asked the speed question with \"smashed\", one with \"hit\", and a control group was not asked about speed. A week later all were asked whether they had seen any broken glass. There was none in the film. 16 of the 50 in the \"smashed\" group said yes, compared with 7 in the \"hit\" group and 6 in the control group."],
 ["Conclusion", "Information given after an event can change what people report, and possibly what they remember. This is often explained with schema theory: the word \"smashed\" may activate a schema of a violent crash, which then fills in details, such as broken glass, that were never seen."],
 ["Use it for", "Practising the rungs (this chapter); the experiment as a research method (CRM-03); schema theory (CL-03)."],
])}""", "Loftus and Palmer (1974)")

P.card("rd-10", f"""<h2>Common traps</h2>
{table(["Trap", "What it looks like", "Fix"], [
 ["Concept-dropping", "The concept word appears once, in the first line, and never again.", "Keep returning to the concept in every paragraph, with a detail and a consequence each time."],
 ["Listing related terms", "\"This links to bias: sampling bias, researcher bias, confirmation bias...\"", "Choose one idea and explain it properly. One developed link beats five names."],
 ["Perspective called bias", "\"The biological approach is biased because it ignores culture.\"", "Say that relying on one perspective can give a reductionist explanation, and explain what it leaves out."],
 ["The universal limitation", "\"The sample was small, so the findings cannot be generalised.\"", "Say who the sample was, who the conclusion is about, and why the difference matters for this finding."],
 ["The empty conclusion", "\"Overall, there are strengths and limitations.\"", "Name a condition: when, for whom, or in what way the claim holds."],
])}""", "Common traps")

# ---------------- CHECK ----------------
P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. In your own words, what does the swap test check?</p>
{S("C", 2)}
<p>2. Name the five rungs in order and say in a few words what each one trains.</p>
{S("C", 3)}
<p>3. Decode this question: <i>"In the context of human development, evaluate measurement in research on attachment."</i></p>
{slot_list(["Context", "Area of study", "Concept", "Command term, and what it asks you to do"])}
{S("C", 4)}
<p>4. This sentence fails the swap test: <i>"The study is unethical because it used deception."</i> Rewrite it about Forer (1949) so that it passes.</p>
{S("C", 3)}
<p>5. Why is "It depends" a weak conclusion, and how can you make it a strong one?</p>
{S("C", 2)}""", "Check yourself")

# ---------------- WORKOUT ----------------
Q = "In the context of learning and cognition, to what extent can research establish causality in the study of schema theory?"
P.topic("workout", "Concept workout: Causality", "A full workout, done together. The guiding questions point the way; they do not give you the answer.")
P.card("wo-1", f"""<p class="small">This is the first full workout, so do it together in class. Use the Loftus and Palmer summary in the Read tab as your evidence.</p>
<p><b>{Q}</b> [15]</p>""")
P.card("wo-2", f"""<h2>Rung 1: Decode</h2>
{slot_list(["Context", "Area of study", "Concept", "Command term, and what it asks you to do"])}
{S("R", 4)}
<p>Which words in the question point to causality, and which point to research?</p>
{S("R", 1)}""", "Rung 1: Decode")
P.card("wo-3", f"""<h2>Rung 2: Define</h2>
<p>Schema theory, in one sentence:</p>
{S("R", 2)}
<p>Causality, as it applies to this question, in one sentence:</p>
{S("R", 2)}
<p class="small">Ask yourself: what would a researcher have to rule out before saying that a schema caused people to remember something differently?</p>""", "Rung 2: Define")
P.card("wo-4", f"""<h2>Rung 3: Upgrade</h2>
<p>This sentence fails the swap test.</p>
{frame("Experiments can show cause and effect because they control variables, so Loftus and Palmer shows causality.")}
<ol>
<li>Which variable did Loftus and Palmer change between groups, and which did they measure?</li>
<li>What stayed the same for every group, and why does that matter for a causal claim?</li>
<li>Cause of what, exactly: a change in the memory itself, or a change in the speed estimate participants reported?</li>
</ol>
<p>Rewrite the sentence so it could only belong to an answer about causality in research on schema theory:</p>
{S("R", 4)}""", "Rung 3: Upgrade")
P.card("wo-5", f"""<h2>Rung 4: One more question</h2>
<p><b>The finding:</b> In Loftus and Palmer (1974), participants who heard "smashed" gave higher speed estimates than participants who heard "contacted".</p>
<p><b>A first reaction:</b> <i>"So leading questions change what people remember, because they activate a schema."</i> Before you accept that, ask one more question.</p>
<ul>
<li>Did the verb change the memory, or only the answer participants gave when they were unsure of the speed?</li>
<li>In the second experiment, participants were asked a week later about broken glass. What does that add to the causal claim?</li>
<li>The study measured what people said. Did it measure a schema at all, or is the schema an explanation added afterwards?</li>
</ul>
{S("R", 4)}
<p><b>Link it.</b> This started as a causality question. Which other concept does it become a problem for, and why?</p>
{S("R", 2)}""", "Rung 4: One more question")
P.card("wo-6", f"""<h2>Rung 5: Commit</h2>
<p>Write one conclusion sentence for the Rung 1 question. It has to name a condition.</p>
<p><i>Research can establish causality in the study of schema theory when [condition], because [reason].</i></p>
<p><b>Ruled out:</b> "Experiments show cause and effect."   "It depends." (unless you say on what)</p>
{S("R", 3)}
<p class="small"><b>Check your rungs.</b> <span class="tickbox"></span> Swap test: none of my sentences above could be pasted into an answer on a different topic.   Rungs I could do without the guiding questions: <span class="tickbox"></span> Decode  <span class="tickbox"></span> Define  <span class="tickbox"></span> Upgrade  <span class="tickbox"></span> One more question  <span class="tickbox"></span> Commit. Record them in your Concept Moves Tracker (Beyond tab).</p>""", "Rung 5: Commit")

# ---------------- EXAM ----------------
P.topic("exam", "Exam practice", "Paper 1 Section C: your turn, on your own.")
P.card("ex-1", f"""<h2>Paper 1, Section C [15 marks]: plan only</h2>
<p><b>In the context of learning and cognition, discuss measurement in research on schema theory.</b></p>
<p class="small">Same study, different concept. Run all five rungs on your own, then write the plan. A plan you can explain is worth more in revision than an essay you have memorised.</p>
{slot_list(["Rung 1: context, area of study, concept, command term", "Rung 2: schema theory and measurement, one sentence each", "Line of argument (one sentence)", "Point 1: what was measured in Loftus and Palmer, and what was assumed", "Point 2: a sentence that passes the swap test", "Link to a second concept", "Conclusion that names a condition"])}
{S("P", 5)}
<p class="small">The Section C markband is in the self-check box on your answer sheet.</p>""", "Paper 1, Section C [15 marks]: plan only")

# ---------------- MORE ----------------
P.topic("more", "Beyond the chapter", "Your tracker, AI prompts and a last check.")
P.card("mo-tracker", f"""<div class="sec-label">Keep this all year</div><h2>Concept Moves Tracker</h2>
<p>Log every Concept Workout you complete, in any chapter. Tick each rung you managed <b>without</b> the guiding questions. Keep the tracker at the end of your CRM-02 answer sheet and add a row each time. Over the year it shows you which rungs are becoming automatic and which still need the scaffolding.</p>
{table(["Chapter", "Concept", "Decode", "Define", "Upgrade", "One more question", "Commit"], [
 ["CRM-02", "Causality", "", "", "", "", ""],
 ["", "", "", "", "", "", ""],
 ["", "", "", "", "", "", ""],
])}""", "Concept Moves Tracker")
P.card("mo-ai", """<div class="sec-label">Using AI to learn</div><h2>Make AI question you, not write for you</h2>
<p>Try one of these after you have attempted the chapter yourself:</p>
<ul><li><i>"Here are five sentences I wrote about a psychology study. For each one, tell me whether it passes the swap test (could it be pasted into an answer about a different study?). Do not rewrite them."</i></li>
<li><i>"Give me a Paper 1 Section C style question for IB Psychology. Ask me to decode it into context, area of study, concept and command term, then tell me if I missed anything."</i></li>
<li><i>"I will give you a finding from a study. Ask me one more question about it, linked to one of the six concepts, and wait for my answer."</i></li></ul>
<p><b>Remember:</b> check every study an AI tool names against this chapter or your textbook, because these tools sometimes invent studies and figures. Do not use AI to draft or mark your IA or EE.</p>""", "Using AI to learn")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>1. In your own words, what does the swap test check?</p>
<p>2. Write one sentence about bias in Forer (1949) that passes the swap test.</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-02.html", "w").write(P.render())
print("ok", P.counts)
