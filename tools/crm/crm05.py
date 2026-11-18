from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, practice_note, ai_card

P = Page("CRM-05", "05", "The Observation",
         "How do psychologists watch behaviour systematically, and how do they know they are recording it accurately?")
S = P.slot

P.topic("start", "The Observation", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to design an observation, choose between its options for good reasons, record behaviour with clear categories, check that two observers agree, and explain what observations can and cannot tell us.</p>
{checklist("CRM-05-goals", [
 "I can describe the three dimensions of an observation (setting, awareness, observer role) and the trade-off in each.",
 "I can write behavioural categories that two observers would apply in the same way.",
 "I can explain the difference between choosing participants and sampling their behaviour, and between time sampling and event sampling.",
 "I can calculate inter-rater reliability and explain why it matters.",
 "I can explain the ethics of observation, including when covert observation is acceptable.",
 "I can evaluate an observation using the concepts of measurement and bias.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (research methods: observation). The observation is the class practical method set for human development, so you will meet it again in HD-09.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 2 Section A (all four questions when your practical is the observation; Question 3 or 4 when it is compared with another method); Paper 2 Section B (evaluating an unseen observation); the IA (an observation checklist can be your data collection tool)</p>
{chips("measurement", "bias", "causality")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p>A researcher wants to study how teenagers use their phones at mealtimes. <b>Option A:</b> families agree to have their dinners video-recorded at home for two weeks. <b>Option B:</b> she sits in a busy mall food court and, without anyone knowing, tallies on paper how often teenagers at nearby tables check their phones during a meal.</p>")}
<p>1. How might the teenagers' behaviour differ between Option A and Option B? Why?</p>
{S("W", 2)}
<p>2. Option A gives a camera recording; Option B gives a tally made in the moment. Which data would be easier to check for accuracy, and why?</p>
{S("W", 2)}
<p>3. What ethical question does each option raise?</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>What is an observation?</h2>
<p>In an <b>observation</b>, the researcher watches and records behaviour as it happens, rather than asking people about it or changing anything. Observations are the method of choice when what people <i>do</i> matters more than what they <i>say</i> they do, and when participants cannot easily report on their own behaviour, as with young children.</p>
<p>Observations record what happens, not why. Because the researcher does not manipulate a variable, an observation on its own cannot establish cause and effect. It can describe behaviour in detail, show which behaviours go together, and generate ideas that experiments can then test. Observation is also used <i>inside</i> other methods: an experiment can use an observation checklist to measure its DV. When the method is an experiment, the checklist is a data collection tool, not the research method.</p>""", "What is an observation?")

P.card("rd-2", f"""<h2>Three dimensions of observation design</h2>
<p>Every observation is described on three separate dimensions, so a single study combines one choice from each. A study can be naturalistic, covert and non-participant, for example.</p>
{table(["Dimension", "Option 1", "Option 2"], [
 ["Setting", "<b>Naturalistic:</b> behaviour is watched where it normally happens, without interference. Higher ecological validity, but the behaviour of interest may be rare and many variables are uncontrolled.", "<b>Controlled:</b> behaviour is watched in a setting the researcher has arranged, such as a playroom with set toys. Easier to standardise and repeat, but behaviour may be less natural."],
 ["Awareness", "<b>Overt:</b> participants know they are being watched. Consent can be obtained, but people may change their behaviour (reactivity).", "<b>Covert:</b> participants do not know. Behaviour is more natural, but there is no consent at the time, which limits where it is acceptable."],
 ["Observer role", "<b>Non-participant:</b> the observer watches from outside the group. More detached, but may miss what behaviour means to the group.", "<b>Participant:</b> the observer joins the group. Richer insider understanding, but the observer may lose objectivity, and notes often cannot be taken at the time."],
])}
<p>No option is better in general. The right combination depends on the research question, on what is ethical, and on how much control the researcher needs.</p>""", "Three dimensions of observation design")

P.card("rd-3", """<h2>Deciding what to record: behavioural categories</h2>
<p>An observer cannot record everything, so the behaviour of interest is broken into <b>behavioural categories</b>, also called a coding scheme or checklist. Good categories are:</p>
<ul>
<li><b>Operationalised:</b> defined precisely enough that two observers would classify the same behaviour the same way. "Off task" is vague; "eyes away from the work materials for 3 seconds or more" is operationalised.</li>
<li><b>Mutually exclusive:</b> a behaviour fits only one category at a time.</li>
<li><b>Exhaustive:</b> every behaviour has somewhere to go, which is why many schemes include an "other or cannot classify" category.</li>
</ul>
<p>An observation that uses categories like this is <b>structured</b> and produces quantitative data (counts and frequencies). An <b>unstructured</b> observation records everything that seems relevant in written notes, which produces rich qualitative data but is harder to compare across observers.</p>""", "Behavioural categories")

P.card("rd-4", """<h2>Sampling: who, and when</h2>
<p>An observation involves two separate sampling decisions, and it is worth keeping them apart.</p>
<ul>
<li><b>Choosing participants</b> uses the same techniques as any method: opportunity, self-selected, random, stratified or snowball sampling (CRM-07).</li>
<li><b>Sampling behaviour</b> decides <i>when</i> to record:
 <ul>
 <li><b>Time sampling:</b> at fixed intervals, for example every 30 seconds, the observer records the category the behaviour fits at that moment. This gives a structured record that is easy to compare between observers, but brief behaviours between intervals are missed.</li>
 <li><b>Event sampling:</b> the observer records every time a target behaviour occurs, whenever it happens. This suits behaviours that are rare or unpredictable, such as a child seeking comfort from a caregiver, but it is hard when many events happen at once.</li>
 </ul></li>
</ul>""", "Sampling: who, and when")

P.card("rd-5", f"""<h2>Making observations reliable: inter-rater reliability</h2>
<p><b>Inter-rater reliability</b> is the extent to which two or more observers, watching the same behaviour independently, record the same thing. If they agree, the data do not depend on who happened to be observing. A simple way to calculate it with time sampling:</p>
{frame("Inter-rater reliability (%) = number of intervals where the observers agree ÷ total number of intervals × 100")}
<p>For example, two observers who agree on 8 of 10 intervals have 80% agreement. A figure of about 80% or above is usually treated as acceptable. When agreement is low, researchers sharpen the category definitions, train the observers together and run a <b>pilot</b> observation before collecting real data.</p>
<p><b>Observer bias</b> is the risk that what observers expect shapes what they notice and how they classify unclear behaviour. It is reduced by precise categories, training, observers who do not know the hypothesis, two independent observers, and <b>reflexivity</b>: researchers thinking about how their own background and expectations could affect what they see.</p>""", "Inter-rater reliability")

P.card("rd-6", """<h2>The ethics of observation</h2>
<ul>
<li><b>Overt observation</b> allows informed consent before the study. For children, parents or guardians consent.</li>
<li><b>Covert observation</b> means there is no consent at the time. The general rule is that it is acceptable only in public places where people would expect to be seen by strangers, such as a shopping centre or a park, and never in private places. For class practicals, the IB applies this rule strictly.</li>
<li><b>Recording:</b> in our setting, observers take written notes or tallies only. Do not photograph, film or record members of the public, and check with your teacher and the venue before observing anywhere outside school.</li>
<li><b>Confidentiality:</b> no names or identifying details in the records.</li>
</ul>
<p>Participant observation raises extra questions: if the observer joins a group under false pretences, members are deceived, and the observer may learn private information that the group never agreed to share.</p>""", "The ethics of observation")

P.card("rd-7", f"""<h2>Key study: Ainsworth's Strange Situation, a controlled observation</h2>
{table(None, [
 ["Aim", "To create a standard way of observing the quality of attachment between infants and their caregivers."],
 ["Procedure", "A mother and her infant (about one year old) spend roughly 20 minutes in an unfamiliar playroom, across eight short episodes. A stranger enters, the mother leaves twice and returns twice, so that stress builds a little at a time and attachment behaviour becomes visible. Trained observers watch through a one-way mirror and code specific behaviours, such as seeking closeness, maintaining contact, avoiding and resisting, paying most attention to what the infant does when the mother returns."],
 ["Findings", "Infants were classified into three main types from their pattern of behaviour. In American samples, roughly 70% were classed as secure, 20% as insecure-avoidant and 10% as insecure-resistant."],
 ["Why it is a controlled observation", "The setting, the episodes and their timing are standardised, so every infant meets the same situation and different observers can compare their coding. Observers do not take part (non-participant), and mothers know they are being observed (overt)."],
 ["Use it for", "This chapter (controlled observation, behavioural categories, inter-rater reliability); attachment (HD-05); Paper 2 Section B practice."],
 ["Evaluate it with", "<b>Measurement:</b> coding is precise and reliable, but 20 minutes in a strange room may not capture the relationship at home. <b>Bias:</b> the original samples were American, and the meaning of behaviours such as staying close to the mother may differ across cultures. <b>Responsibility:</b> infants are deliberately but mildly stressed, so episodes are cut short if an infant becomes very upset."],
])}""", "Key study: the Strange Situation")

P.card("rd-8", f"""<h2>Real life: observation outside research</h2>
{tip('''<ul>
<li><b>Classroom observation.</b> When a school leader observes a lesson, a checklist of what to look for makes feedback fairer than general impressions.</li>
<li><b>Sport.</b> Coaches code match footage: every pass, tackle and shot is an event, recorded by category. Two analysts coding the same match is inter-rater reliability.</li>
<li><b>Shops and malls.</b> Retailers observe how shoppers move through a store to decide where to place products. Shoppers in a public space expect to be seen, but not to be recorded.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example and write one behavioural category for it that is properly operationalised.</p>
{S("D", 2)}""", "Real life")

P.card("rd-9", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies to observations"], [
 ["Measurement", "Categories, behaviour sampling and inter-rater reliability are all measurement decisions. If two observers watching the same event record different things, the data cannot be trusted."],
 ["Bias", "Observer expectations can shape what is noticed and how unclear behaviour is coded. Overt observation can cause participants to change their behaviour."],
 ["Causality", "Observations describe and can show which behaviours occur together, but without manipulation they cannot show what caused what."],
 ["Responsibility", "Covert observation removes consent at the time, so it is acceptable only where people expect to be seen by strangers, and recordings of the public are not made."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. Describe an observation that is naturalistic, covert and non-participant. Give one strength and one limitation of that combination.</p>
{S("C", 3)}
<p>2. Turn "being helpful" into two operationalised behavioural categories for observing children in a playground.</p>
{S("C", 2)}
<p>3. When would you choose event sampling instead of time sampling?</p>
{S("C", 2)}
<p>4. Two observers agree on 14 of 20 intervals. Calculate their inter-rater reliability. Is it acceptable, and what would you do next?</p>
{S("C", 2)}
<p>5. Why can an observation not show cause and effect?</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Practice study: study behaviours</h2>
{practice_note("observation", "HD-09")}
<p><b>Research question:</b> what behaviours does a student show during a five-minute revision period?</p>
<p><b>Behaviour codes:</b> A = eyes on the text or work materials; B = writing or typing notes; C = using a phone or device, not for study; D = looking away from the work; E = talking to someone; F = other or cannot classify.</p>
<ol>
<li>A volunteer sits at the front with their notes and revises normally for five minutes. The volunteer has agreed to take part and knows they are being observed.</li>
<li>In pairs, each of you observes independently, without talking to your partner.</li>
<li>Every 30 seconds, when your teacher calls the time, write the code for what the volunteer is doing at that moment (10 intervals in total).</li>
<li>After five minutes, compare your records and calculate your inter-rater reliability.</li>
</ol>
{slot_list(["My codes for the 10 intervals", "My partner's codes", "Number of agreements out of 10", "Inter-rater reliability (%)"])}
{S("C", 4)}
<p>Which behaviours did you and your partner disagree on most, and why? How would you rewrite one category to fix it?</p>
{S("C", 3)}
<p>Describe this observation on the three dimensions (setting, awareness, observer role).</p>
{S("C", 2)}""", "Practice study")

P.topic("exam", "Exam practice", "Paper 2 practice: measurement, and evaluating an observation.")
P.card("ex-1", f"""<h2>Paper 2, Section A, Question 2 style [4 marks]</h2>
<p><b>Explain the concept of measurement in relation to the practice study on study behaviours.</b> [4]</p>
<p class="small">How were behaviours defined, how was behaviour sampled, how was agreement checked, and why does it matter?</p>
{S("Q2", 5)}
{earns("CRM-05-Q2", ["I explain what the concept means in research, accurately.", "I link it to specific features of the study, not to research in general.", "I explain the effect: how it helped or limited what the study could show."])}""", "Paper 2, Section A, Question 2 style [4 marks]")
P.card("ex-2", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
<p><b>Evaluate the Strange Situation with reference to the concepts of measurement and bias.</b> [6]</p>
<p class="small">Link each concept to specific features: the coding system, the setting, the sample and the classification types.</p>
{S("S", 7)}
{earns("CRM-05-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "I am designing an observation of how students use the school library at break. Ask me questions, one at a time, about my categories, sampling and ethics. Do not suggest answers.",
 "Here are my behavioural categories. Tell me which ones overlap or are too vague, and ask me how I would fix them.",
 "Describe four observation studies, one at a time, and ask me to place each on the three dimensions. Wait for my answer.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA starter", "An observation checklist with at least five categories can be your IA data collection tool. Draft one for observing how students in the UAE use their break time on a school day, with an operationalised definition for each category."],
 ["EE question workshop", "Turn \"Is the Strange Situation fair to every culture?\" into a focused question, and find one study that supports and one that challenges using it across cultures."],
 ["HL link", "<b>Technology:</b> could software that tracks eye movements or screen use replace a human observer? What would be gained and lost in measurement and in ethics?"],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>"Observations cannot show cause and effect, so all they give us is description. An experiment always tells us more."</p>
<p>1. Do you agree? Answer in three to five sentences using the concepts of measurement and causality.</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-05.html", "w").write(P.render())
print("ok", P.counts)
