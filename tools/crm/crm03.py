from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, practice_note, ai_card

P = Page("CRM-03", "03", "The Experiment",
         "How do psychologists use experiments to establish cause and effect?")
S = P.slot

P.topic("start", "The Experiment", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to take any experiment apart into its variables, design and controls, explain how it supports a claim about cause and effect, and spot what weakens that claim.</p>
{checklist("CRM-03-goals", [
 "I can identify and operationalise the IV and DV in an experiment, and write a research hypothesis and a null hypothesis.",
 "I can explain independent measures, repeated measures and matched pairs designs, with a strength and a limitation of each.",
 "I can explain random allocation, and how it differs from random sampling.",
 "I can explain how extraneous and confounding variables, demand characteristics and researcher effects threaten a causal claim, and how they are controlled.",
 "I can compare laboratory and field experiments, and explain the trade-off between control and ecological validity.",
 "I can evaluate an experiment using the concepts of causality and bias.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (research methods). The experiment is the class practical method set for learning and cognition, so you will meet it again in CL-11.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 2 Section A (all four questions when your practical is the experiment, and Question 3 or 4 when another method is compared with it); Paper 2 Section B (evaluating an unseen experiment); the IA (Criterion B, research methodology)</p>
{chips("causality", "bias", "measurement")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p>A news site reports: <i>\"Students who own more books at home score higher on vocabulary tests. More books means a bigger vocabulary.\"</i> The researchers asked 500 families how many books they owned and compared this with their children's vocabulary scores. The more books, the higher the scores.</p>")}
<p>1. What kind of relationship did the researchers find?</p>
{S("W", 2)}
<p>2. Does this show that owning books causes a bigger vocabulary? Give one other explanation for the pattern.</p>
{S("W", 2)}
<p>3. How could you change the study so the headline's claim would be better supported?</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>What makes a study an experiment?</h2>
<p>An <b>experiment</b> is a research method in which the researcher deliberately changes one variable, keeps other variables as constant as possible, and measures the effect on a second variable. That combination of <b>manipulation</b> and <b>control</b> is what makes experiments the method best suited to testing cause and effect.</p>
<ul>
<li>The <b>independent variable (IV)</b> is the variable the researcher changes. It is the presumed cause. Each version of it is called a <b>condition</b>.</li>
<li>The <b>dependent variable (DV)</b> is the variable the researcher measures. It is the presumed effect.</li>
<li><b>Controlled variables</b> are kept the same in every condition, such as the room, the instructions, the materials and the time allowed, so that only the IV differs.</li>
</ul>
<p>Back to the warm-up. The books study measured two things and found that they go together, but it changed nothing. Families with more books may also have parents who read aloud more, more money, more time and more education, and any of these could raise vocabulary. To test the headline, you would need to give books to some families and not to others, with families placed into the two groups by chance, and then compare vocabulary scores later. That would be an experiment.</p>
<p>Some experiments have an <b>experimental group</b> that receives the treatment and a <b>control group</b> that does not, which gives a baseline for comparison. Others compare two or more versions of the IV, for example studying with music versus in silence, with no "no treatment" group at all.</p>""", "What makes a study an experiment?")

P.card("rd-2", """<h2>Operationalising variables and writing hypotheses</h2>
<p>A variable is <b>operationalised</b> when you say exactly how it will be changed or measured. "Memory" is a construct; "the number of words correctly recalled from a list of 20 in 60 seconds" is an operationalised DV. "Music" is vague; "a recording of instrumental music played at the same volume throughout the task" is an operationalised IV. Operationalising matters for two reasons: another researcher can repeat (replicate) the study exactly, and readers can see what the results do and do not tell them. Any operationalisation leaves part of the construct out, which is always worth an evaluation point.</p>
<p>A <b>research hypothesis</b> is a testable prediction about the effect of the IV on the DV, written with both variables operationalised.</p>
<ul>
<li>A <b>directional</b> (one-tailed) hypothesis says which way the difference will go: "Participants who study a list of 20 concrete words will recall more words in 60 seconds than participants who study 20 abstract words."</li>
<li>A <b>non-directional</b> (two-tailed) hypothesis predicts a difference but not its direction: "There will be a difference in the number of words recalled..."</li>
<li>The <b>null hypothesis</b> states that the IV will have no effect on the DV, and that any difference found is due to chance.</li>
</ul>
<p>Researchers usually choose a directional hypothesis when earlier research points one way, and a non-directional one when it does not.</p>""", "Operationalising and hypotheses")

P.card("rd-3", f"""<h2>Experimental designs</h2>
<p>The <b>design</b> is how participants are used across the conditions of the IV.</p>
{table(["Design", "What it means", "Strength", "Limitation"], [
 ["Independent measures", "Different participants in each condition", "No order effects; participants see only one condition, so they are less likely to guess the aim", "Participant variables (ability, mood, motivation) may differ between groups; needs more participants"],
 ["Repeated measures", "The same participants do every condition", "Participant variables are the same in each condition; needs fewer participants", "Order effects: practice, boredom or fatigue; seeing both conditions may reveal the aim"],
 ["Matched pairs", "Participants are matched on a variable that matters (for example prior test scores), then one of each pair goes into each condition", "Reduces participant variables without order effects", "Matching takes time and is never perfect; if one person drops out, the pair's data is lost"],
])}
<p>Order effects in repeated measures can be reduced by <b>counterbalancing</b>: half the participants do condition A first and half do condition B first, so any practice or fatigue effect is spread evenly across conditions. Some studies cannot use repeated measures at all, for example when the same word list cannot be learned twice, or when knowing about one condition would change behaviour in the other.</p>""", "Experimental designs")

P.card("rd-4", """<h2>Random allocation is not random sampling</h2>
<p>These two terms sound alike and are confused in exams more than any other pair.</p>
<ul>
<li><b>Random sampling</b> is about <i>who takes part</i>: every member of the target population has an equal chance of being chosen. It affects how far the results can be <b>generalised</b>. It is rare in practice.</li>
<li><b>Random allocation</b> is about <i>which condition</i> each participant is placed in, for example by drawing names from a container or using a random number generator. It spreads participant variables across conditions by chance, so no group is systematically different at the start. It affects whether the study can claim <b>cause and effect</b>.</li>
</ul>
<p>A study can have one without the other. A teacher who randomly allocates the students in one class (an opportunity sample) to two conditions has random allocation but not random sampling. Random allocation does not make the groups identical, especially in small samples; it only removes systematic differences. When participants are not randomly allocated, the study is a quasi-experiment, which you will meet in CRM-04.</p>""", "Random allocation vs random sampling")

P.card("rd-5", """<h2>What threatens a causal claim?</h2>
<p>An <b>extraneous variable</b> is anything other than the IV that could affect the DV: noise, time of day, how tired participants are, how the instructions are read. If an extraneous variable changes <i>along with</i> the IV, it becomes a <b>confounding variable</b>, and the researcher can no longer tell which of the two caused the change in the DV. If the music group did the task in the morning and the silence group after lunch, time of day is a confound.</p>
<p>Two further threats come from the people in the study.</p>
<ul>
<li><b>Demand characteristics:</b> cues that tell participants what the study is about, so that they change their behaviour, often to help (or sometimes to spoil) the result.</li>
<li><b>Researcher effects:</b> the researcher's expectations influence the results, for example through tone of voice when giving instructions, or through how ambiguous answers are scored.</li>
</ul>
<p>Researchers use <b>controls</b> against these threats:</p>
<ul>
<li><b>Standardisation:</b> the same instructions, word for word, the same materials, the same timing and the same room for everyone.</li>
<li><b>Random allocation</b> to deal with participant variables.</li>
<li><b>Single-blind</b> procedures, where participants do not know which condition they are in, and <b>double-blind</b> procedures, where the researcher running the session does not know either.</li>
<li>A <b>placebo</b> condition in treatment studies, so that the effect of simply expecting to improve can be separated from the effect of the treatment.</li>
<li>A <b>pilot study</b>: a small trial run that finds problems with instructions, timing or materials before the real study.</li>
</ul>
<p>Three conditions must be met for a causal claim: the IV is <b>manipulated</b>, extraneous variables are <b>controlled</b>, and the change in the IV <b>comes before</b> the change in the DV.</p>""", "What threatens a causal claim?")

P.card("rd-6", f"""<h2>Laboratory and field experiments</h2>
{table(["", "Laboratory experiment", "Field experiment"], [
 ["Setting", "An artificial setting the researcher controls", "A natural setting, such as a school, shop or street"],
 ["Control", "High: extraneous variables can be kept constant", "Lower: many things vary that the researcher cannot control"],
 ["Do participants know?", "Usually yes", "Often not, which reduces demand characteristics but raises ethical questions"],
 ["Ecological validity", "Often low: tasks may be short and artificial", "Usually higher: behaviour happens where it normally does"],
])}
<p>This is the central trade-off of experimental research. <b>Internal validity</b> asks whether the study really showed that the IV caused the change in the DV. <b>Ecological validity</b> asks whether the findings apply to real-life settings. Tighter control usually raises internal validity and lowers ecological validity. Neither kind of experiment is "better": the right choice depends on the question being asked.</p>""", "Laboratory and field experiments")

P.card("rd-7", f"""<h2>Key study: Loftus and Palmer (1974), leading questions and memory</h2>
{table(None, [
 ["Aim", "To find out whether the wording of a question asked after an event changes what eyewitnesses report about it."],
 ["Experiment 1", "45 university students in the USA watched seven short films of traffic accidents, each between 5 and 30 seconds long. After each film they answered questions, including the critical one: \"About how fast were the cars going when they ___ each other?\" Groups of nine heard different verbs: smashed, collided, bumped, hit or contacted. This is an independent measures design with five conditions."],
 ["Findings 1", "Mean speed estimates rose with the strength of the verb: 40.8 mph for \"smashed\", 39.3 for \"collided\", 38.1 for \"bumped\", 34.0 for \"hit\" and 31.8 for \"contacted\"."],
 ["Experiment 2", "150 students watched one film of a crash. 50 were asked the speed question with \"smashed\", 50 with \"hit\", and 50 (a control group) were not asked about speed. A week later, without seeing the film again, all were asked: \"Did you see any broken glass?\" There was no broken glass in the film."],
 ["Findings 2", "16 of the 50 in the \"smashed\" group said yes, compared with 7 in the \"hit\" group and 6 in the control group."],
 ["Conclusion", "The wording of a question can change what people report. The second experiment suggests it may also change the memory itself: the verb added information that was then remembered as part of the event."],
 ["Use it for", "This chapter (variables, conditions, control groups); CRM-02 (the worked Concept Workout); schema theory (CL-03); Paper 2 Section B practice."],
 ["Evaluate it with", "<b>Causality:</b> the groups saw identical films and differed only in the verb, so the wording can be identified as the cause of the difference. <b>Measurement:</b> speed estimates may show uncertainty more than memory, which is why the broken-glass question matters. <b>Bias:</b> all participants were university students watching films in a calm setting; real eyewitnesses are frightened and may be questioned days later."],
])}""", "Key study: Loftus and Palmer (1974)")

P.card("rd-8", f"""<h2>Real life: experiments outside the laboratory</h2>
{tip('''<ul>
<li><b>Medicine trials.</b> New medicines are tested in randomised controlled trials: patients are randomly allocated to the medicine or a placebo, often double-blind, before a medicine is approved for use in the UAE or elsewhere.</li>
<li><b>Apps and websites.</b> A food delivery app shows two versions of its checkout screen to users chosen at random and compares how many complete an order. This is an independent measures field experiment, often called an A/B test.</li>
<li><b>Schools.</b> A school in Sharjah wants to know whether a ten-minute retrieval quiz at the start of lessons improves end-of-unit scores. Classes cannot be randomly reshuffled, so the comparison may be weaker than it looks.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example. What is the IV, what is the DV, and what is one variable that would need to be controlled?</p>
{S("D", 3)}""", "Real life")

P.card("rd-9", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies to experiments"], [
 ["Causality", "Manipulation, control and random allocation are what allow an experiment to claim cause and effect. Confounding variables are what break that claim."],
 ["Bias", "Demand characteristics, researcher effects and unrepresentative samples can all push results in one direction. Blind procedures and standardisation are controls against bias."],
 ["Measurement", "The DV has to be operationalised. Whether the operationalisation captures the construct (does a speed estimate measure memory?) is a validity question."],
 ["Responsibility", "Field experiments and hidden aims raise questions of consent and deception. Participants must be debriefed and allowed to withdraw their data."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. A researcher tests whether a breathing exercise before a test reduces anxiety in Grade 11 students, measuring anxiety with a 10-item questionnaire. Identify the IV and DV and operationalise each.</p>
{S("C", 3)}
<p>2. Write a directional research hypothesis and a null hypothesis for the study in question 1.</p>
{S("C", 2)}
<p>3. The same students do the test once with the breathing exercise and once without. Name the design, give one limitation, and say how it could be reduced.</p>
{S("C", 2)}
<p>4. Explain the difference between random sampling and random allocation. Which one matters more for a causal claim, and why?</p>
{S("C", 2)}
<p>5. What is a confounding variable? Give an example that could occur in the study in question 1.</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Practice study: word type and memory</h2>
{practice_note("experiment", "CL-11")}
<p><b>Research question:</b> does word type (concrete or abstract) affect the number of words recalled? Concrete words name things you can see or touch (table, river); abstract words name ideas or feelings (honesty, idea). One explanation for a difference is <b>dual coding</b> (Paivio, 1971): concrete words can be stored both as words and as mental images.</p>
<ol>
<li>Your teacher places you in the concrete or the abstract condition.</li>
<li>Study your list of 10 words silently for 30 seconds.</li>
<li>Filler task: count backwards from 200 in threes until your teacher says stop. This stops you rehearsing the words.</li>
<li>Write down as many words as you can remember in 60 seconds, then count your correct words.</li>
<li>Your teacher collects the class results and shares the mean for each condition.</li>
</ol>
{slot_list(["My condition", "My score (out of 10)", "Class mean: concrete", "Class mean: abstract"])}
{S("C", 4)}
<p>Was this a true experiment? Explain using how participants were placed into conditions. Then name one controlled variable and one extraneous variable that was not fully controlled.</p>
{S("C", 3)}""", "Practice study")

P.topic("exam", "Exam practice", "Paper 2 practice: describing an experiment, and evaluating one with concepts.")
P.card("ex-1", """<p class="small">These tasks use the practice study and Loftus and Palmer. In the exam, Paper 2 Section A asks about your own class practical; the experiment practical for your class is in CL-11.</p>""")
P.card("ex-2", f"""<h2>Paper 2, Section A, Question 1 style [4 marks]</h2>
<p><b>Describe how an experiment was used in the practice study, including the aim and procedure.</b> [4]</p>
<p class="small">Include the aim, the IV and DV (operationalised), the design, how participants were placed into conditions, and the procedure in enough detail to repeat it.</p>
{slot_list(["Aim (one sentence)", "IV and DV, operationalised", "Design and allocation", "Procedure in three or four steps"])}
{S("Q1", 4)}
{S("Q1", 5)}
{earns("CRM-03-Q1", ["I name the method and its type (for example a true experiment, a naturalistic observation or a semi-structured interview).", "I state the aim of the study.", "I describe the procedure in order, with enough detail that someone could repeat it.", "I use research methods terms correctly (for example operationalised variables, sampling, consent)."])}""", "Paper 2, Section A, Question 1 style [4 marks]")
P.card("ex-3", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
<p><b>Evaluate Loftus and Palmer (1974) with reference to the concepts of causality and bias.</b> [6]</p>
<p class="small">The real Section B is 15 marks and asks you to discuss an unseen study using two or more concepts from a list. This shorter task practises the core move: apply each concept to specific features of the study and explain the consequence.</p>
{S("S", 7)}
{earns("CRM-03-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "Describe five short studies, one at a time. For each, ask me to name the IV, the DV and the design. Wait for my answer each time.",
 "I am going to explain why random allocation is not the same as random sampling. Ask me two questions that would show whether I really understand the difference.",
 "Here is my evaluation of Loftus and Palmer (1974). Tell me which sentences pass the swap test and which could be pasted into any study. Do not rewrite it.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA starter", "Population of interest: Grade 11 students in the UAE who revise with their phone nearby. Sketch an experiment comparing recall of a word list after a two-minute break spent either scrolling a phone or sitting quietly. Write the IV, DV, design and one control. The IA is a proposal: you do not collect data."],
 ["EE question workshop", "A psychology EE uses published research only. Turn \"Are eyewitnesses reliable?\" into a focused question, for example \"To what extent do leading questions alter eyewitness memory rather than only the answers eyewitnesses give?\""],
 ["HL link", "<b>Technology:</b> would the music-versus-silence experiment give the same result with earphones and a streaming playlist the student chose? <b>Motivation:</b> if participants were offered a reward for each word recalled, which group might it help more?"],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>1. Loftus and Palmer used filmed accidents in a classroom. What would be gained, and what would be lost, by studying real eyewitnesses to real accidents? Name the concept that captures what you would lose.</p>
<p>2. The participants were university students. Which concept does this connect to most directly, and why?</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-03.html", "w").write(P.render())
print("ok", P.counts)
