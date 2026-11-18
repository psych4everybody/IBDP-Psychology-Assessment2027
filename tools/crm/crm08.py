from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, ai_card

P = Page("CRM-08", "08", "Research Considerations: Reliability, Validity and Credibility",
         "How do we decide whether a study's findings can be trusted, and how far they reach?")
S = P.slot

P.topic("start", "Research Considerations", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will have the vocabulary examiners expect when you judge the quality of a study: reliability, five kinds of validity, generalisability, researcher and participant bias, and, for qualitative research, credibility, transferability and reflexivity.</p>
{checklist("CRM-08-goals", [
 "I can explain reliability and the ways it is checked.",
 "I can explain internal, external, content, face and construct validity, with an example of each.",
 "I can explain generalisability and why it depends on the sample and the setting.",
 "I can explain researcher and participant biases and how they are controlled.",
 "I can explain credibility, transferability and reflexivity in qualitative research, and strategies for each.",
 "I can use these terms to evaluate a specific study, not just define them.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (research considerations). These terms are listed in the guide's table of research methodology terms, and they run through every evaluation you will write.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 2 Section B (judging an unseen study); Paper 2 Section A Question 2 (explaining a concept in relation to your practical); Paper 3 for HL students (Question 3 asks about credibility, bias or transferability in qualitative research); the IA (Criteria C and D)</p>
{chips("measurement", "bias", "causality")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p>An online quiz claims to measure \"how good your memory is\". It asks ten questions such as \"Do you often forget where you put your keys?\" and \"Are you good at remembering birthdays?\" You take it on Monday and score 7 out of 10. You take it again on Friday and score 4.</p>")}
<p>1. What does the change from 7 to 4 suggest about the quiz?</p>
{S("W", 2)}
<p>2. Does the quiz measure memory, or something else? What would a better memory test look like?</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>Reliability: consistency</h2>
<p>A measure is <b>reliable</b> if it gives consistent results. Reliability is checked in different ways depending on the method:</p>
<ul>
<li><b>Test-retest reliability:</b> the same people take the same test on two occasions; their scores should be similar if the thing measured has not changed. The quiz in the warm-up fails this test.</li>
<li><b>Inter-rater (inter-observer) reliability:</b> two or more researchers score or code the same behaviour independently and agree (CRM-05).</li>
<li><b>Replication:</b> other researchers repeat the whole study, ideally with new participants, and find the same result. A finding that replicates in many samples is far more trustworthy than one striking result.</li>
</ul>
<p>Reliability is improved by standardisation (the same instructions, materials and procedure every time), clear operational definitions and training. But reliability is not enough on its own: a bathroom scale that always reads 2 kg heavy is perfectly reliable and always wrong.</p>""", "Reliability")

P.card("rd-2", f"""<h2>Validity: measuring what you claim to measure</h2>
<p><b>Validity</b> is about whether a study measures what it claims to measure, and whether its conclusions are justified. The guide lists five kinds:</p>
{table(["Kind", "The question it asks", "Example"], [
 ["Internal validity", "Did the IV, and nothing else, cause the change in the DV?", "A confounding variable, such as testing one group in the morning and the other after lunch, lowers internal validity."],
 ["External validity", "Do the findings apply beyond this study, to other people, settings and times?", "A memory effect found with university students learning word lists may not hold for older adults remembering real events. Ecological validity (real-life settings) is one part of it."],
 ["Content validity", "Does the measure cover the whole of what it should, and only that?", "An anxiety questionnaire that asks only about physical symptoms misses worrying thoughts."],
 ["Face validity", "Does the measure look, on the surface, as if it measures what it claims to?", "Asking \"How stressed do you feel?\" has face validity for stress. Face validity is the weakest kind: looking right is not the same as being right."],
 ["Construct validity", "Does the measure really capture the underlying construct, as theory describes it?", "Does a speed estimate in Loftus and Palmer measure memory, or uncertainty and the wish to give a sensible answer?"],
])}
<p>A useful way to remember the difference: <b>reliability</b> is hitting the same spot every time; <b>validity</b> is hitting the right spot. A measure can be reliable without being valid, but it cannot be valid without being reasonably reliable.</p>""", "Validity")

P.card("rd-3", """<h2>Generalisability</h2>
<p><b>Generalisability</b> is the extent to which findings can be applied beyond the sample and setting of the study. It depends on:</p>
<ul>
<li><b>The sample:</b> how well it represents the population the conclusion is about (CRM-07). Much published psychology has relied on university students in Western, educated, industrialised, rich and democratic countries, sometimes shortened to "WEIRD" samples, who are a small and unusual slice of humanity.</li>
<li><b>The setting:</b> whether behaviour in a laboratory or online task reflects behaviour in daily life.</li>
<li><b>The time:</b> whether a finding from the 1970s still applies now, for example before and after smartphones.</li>
<li><b>The measures:</b> whether the same measure means the same thing in a different culture or language.</li>
</ul>
<p>A strong evaluation point names exactly <i>who</i> was studied, <i>who</i> the conclusion is about, and <i>why</i> the difference matters for this particular finding, rather than simply saying "the sample was small".</p>""", "Generalisability")

P.card("rd-4", f"""<h2>Researcher and participant biases</h2>
{table(["Bias", "What happens", "Controls"], [
 ["Researcher bias (researcher effects, observer bias)", "The researcher's expectations influence how the study is run or how data are interpreted, often without the researcher noticing.", "Standardised procedures and instructions; double-blind designs; precise coding schemes; more than one coder; reflexivity."],
 ["Confirmation bias", "Noticing and reporting evidence that supports the hypothesis while overlooking evidence against it.", "Stating hypotheses and analysis plans in advance; reporting all results, not just the striking ones."],
 ["Demand characteristics", "Participants guess the aim and change their behaviour to fit (or spoil) it.", "Keeping the aim general until the debrief; independent measures designs; single-blind procedures."],
 ["Social desirability", "Participants present themselves in a good light, especially in self-report.", "Anonymity; neutral wording; checking self-report against other measures."],
 ["Sampling bias", "The sample differs systematically from the population.", "Random or stratified sampling; describing the sample honestly and limiting conclusions to match."],
])}""", "Researcher and participant biases")

P.card("rd-5", """<h2>Quality in qualitative research</h2>
<p>Interviews, focus groups and unstructured observations produce words and meanings, not numbers. Their quality is judged with related but different terms.</p>
<ul>
<li><b>Credibility:</b> do the findings genuinely reflect what participants experienced and meant? Strategies: <i>triangulation</i> (checking findings across different methods, sources or researchers); <i>member checking</i> (asking participants whether the summary of their interview is accurate); spending enough time with participants; and a clear record of how codes and themes were reached.</li>
<li><b>Transferability:</b> could the findings apply to other people or settings? Qualitative studies do not claim to generalise in a statistical sense. Instead, researchers give a <i>thick description</i> of the participants and context, so that readers can judge for themselves whether the findings fit another setting.</li>
<li><b>Reflexivity:</b> researchers think about, and report, how their own background, beliefs, expectations and relationship to participants may have shaped the questions they asked and how they interpreted the answers. It does not remove bias, but it makes it visible. The IA asks you to do exactly this about your own proposal.</li>
<li><b>Bias</b> in qualitative research is reduced by open, non-leading questions, reflexivity, triangulation, transparent reporting and, in some approaches, having a second researcher code part of the data.</li>
</ul>
<p>There is a useful parallel: credibility is close to internal validity, transferability to external validity, and checking codes with a second researcher is close to inter-rater reliability.</p>""", "Quality in qualitative research")

P.card("rd-6", f"""<h2>Key study: Open Science Collaboration (2015), can psychology's findings be repeated?</h2>
{table(None, [
 ["Aim", "To estimate how many published findings in psychology can be reproduced when the studies are run again."],
 ["Procedure", "Around 270 researchers worked together to repeat 100 experimental and correlational studies published in 2008 in three leading psychology journals, following the original methods as closely as possible and often consulting the original authors."],
 ["Findings", "97% of the original studies had reported statistically significant results. Only 36% of the replications did. The effects found in the replications were, on average, considerably smaller than the original effects."],
 ["Conclusion", "Many published findings are less reliable than they appear. Possible reasons include small samples, publication bias (journals favouring significant results) and flexible analysis choices."],
 ["What happened next", "The project helped spark reforms: researchers increasingly register their hypotheses and analysis plans before collecting data, share their data openly, and publish replication studies."],
 ["Use it for", "This chapter (reliability and replication; publication bias); the concept of bias (CRM-01); evaluating any single study."],
 ["Evaluate it with", "<b>Bias:</b> publication bias means the published record overstates effects. <b>Measurement:</b> a replication can fail because the original effect was not real, or because the new sample or setting differed. <b>Responsibility:</b> researchers have a duty to report findings, including null results, honestly."],
])}""", "Key study: Open Science Collaboration (2015)")

P.card("rd-7", f"""<h2>Real life: judging claims</h2>
{tip('''<ul>
<li><b>A single study in the news.</b> One striking result is weaker evidence than a finding that has been replicated many times by different teams.</li>
<li><b>Personality quizzes.</b> A quiz that gives you a different "type" each time you take it has low test-retest reliability.</li>
<li><b>Job interviews.</b> Structured interviews, with the same questions and scoring rules for every candidate, are generally more reliable than informal chats, which leave more room for interviewer bias.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example and name the research consideration it illustrates, with one sentence of explanation.</p>
{S("D", 2)}""", "Real life")

P.card("rd-8", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies"], [
 ["Measurement", "Reliability and the five kinds of validity are the core of measurement: is the tool consistent, and does it measure the right thing?"],
 ["Bias", "Researcher and participant biases, sampling bias and publication bias all push findings away from the truth. Reflexivity makes the researcher's own bias visible."],
 ["Causality", "Internal validity is the extent to which a study can support a causal claim; external validity is how far that claim reaches."],
 ["Perspective", "Quantitative and qualitative research judge quality in different terms, which reflects different views of what good evidence is."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. Explain the difference between reliability and validity, with an example where a measure is reliable but not valid.</p>
{S("C", 2)}
<p>2. Name the kind of validity in each case: (a) a study's findings do not hold in other countries; (b) a test of "social skills" asks only about making friends online; (c) a confounding variable explains the result.</p>
{S("C", 2)}
<p>3. What is reflexivity, and why does the IA ask you to show it?</p>
{S("C", 2)}
<p>4. Give two strategies for improving the credibility of an interview study.</p>
{S("C", 2)}
<p>5. Why did the Open Science Collaboration (2015) matter for how we judge single studies?</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Name the consideration</h2>
<p>For each short description, name the research consideration and suggest one improvement.</p>
<ol>
<li>Two observers coding playground behaviour agree on only 55% of intervals.</li>
<li>A questionnaire on exam stress asks only about sleep.</li>
<li>An interviewer who strongly believes phones harm teenagers interviews teenagers about phones.</li>
<li>A study of leadership in one company in Dubai is used to make claims about leadership everywhere.</li>
<li>A qualitative study gives no detail about who its participants were or where it took place.</li>
</ol>
{slot_list([f"Description {i}: consideration and improvement" for i in range(1, 6)])}
{S("C", 5)}""", "Name the consideration")

P.topic("exam", "Exam practice", "Paper 2 practice: measurement, and evaluating a qualitative study.")
P.card("ex-1", f"""<h2>Paper 2, Section A, Question 2 style [4 marks]</h2>
<p><b>Explain the concept of measurement in relation to the practice study on word type and memory (CRM-03).</b> [4]</p>
<p class="small">Use at least one kind of validity and one kind of reliability, each tied to a specific feature of the study.</p>
{S("Q2", 5)}
{earns("CRM-08-Q2", ["I explain what the concept means in research, accurately.", "I link it to specific features of the study, not to research in general.", "I explain the effect: how it helped or limited what the study could show."])}""", "Paper 2, Section A, Question 2 style [4 marks]")
P.card("ex-2", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
{tip("<p><b>Study (invented for practice):</b> A researcher who had recently moved to the UAE herself wanted to understand how newly arrived secondary students experience their first term. She interviewed 12 students from one international school, using a semi-structured schedule, in English. Interviews were recorded and transcribed, and she coded them into three themes: missing old friends, confusion about school routines, and the importance of one welcoming classmate. She did not report the students' nationalities or first languages. She concluded that schools should assign every new student a \"buddy\".</p>")}
<p><b>Evaluate this study with reference to the concepts of bias and measurement.</b> [6]</p>
<p class="small">Think about the researcher's own position, how the data were collected and coded, and who the findings could transfer to.</p>
{S("S", 7)}
{earns("CRM-08-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "Describe a study in three sentences. Ask me which kind of validity is most at risk and why. Wait for my answer, then tell me if another kind also applies.",
 "I will explain the difference between credibility and transferability. Ask me one follow-up question about each.",
 "Here is my evaluation paragraph. Tell me where I have only named a research term without explaining how it affects this study. Do not rewrite it.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA link", "Criterion C asks you to discuss challenges such as the validity of your data collection tool, and Criterion D asks about your own possible bias. Write two sentences for an imagined proposal: one on the content validity of your questionnaire, and one on how your background could shape your interpretation."],
 ["EE question workshop", "Turn \"Why do some famous findings fail to replicate?\" into a focused question, and find one replication that succeeded and one that failed."],
 ["HL link", "<b>Paper 3:</b> Question 3 asks about credibility, bias or transferability in a qualitative study. For the invented study above, write one sentence on each."],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>1. In one sentence each, explain internal validity, external validity and construct validity.</p>
<p>2. Which research consideration would you check first in a study you saw reported in the news, and why?</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-08.html", "w").write(P.render())
print("ok", P.counts)
