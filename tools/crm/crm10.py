from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, ai_card

P = Page("CRM-10", "10", "Synthesis and Design",
         "The IA in miniature: everything from the Foundations chapters, applied to one real problem.")
S = P.slot

P.topic("start", "Synthesis and Design", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will design a complete, justified research proposal, the same kind of thinking the IA asks for, and evaluate unseen studies by choosing the most relevant concepts yourself, finishing with a full Paper 2 Section B answer.</p>
{checklist("CRM-10-goals", [
 "I can explain how the decisions in a study connect, from research question to conclusion.",
 "I can describe what the IA asks for and the four criteria it is marked on.",
 "I can design a proposal with a focused aim and a justified method, sample, procedure and ethics.",
 "I can explain what a different method would add to the same research question.",
 "I can choose the two most useful concepts for an unseen study and apply them with specific evidence.",
 "I can plan and write a full Paper 2 Section B response in about 40 minutes.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology, brought together with all six concepts. This chapter closes the Foundations section.</p>
<p class="small"><b>Where this appears in the exams:</b> the IA (all four criteria); Paper 2 Section A Question 4 (design); Paper 2 Section B (the full 15-mark task)</p>
{chips("bias", "causality", "change", "measurement", "perspective", "responsibility")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p>A self-help article for teenagers says: <i>\"Studies show that deleting all social media for 30 days improves mood in 90% of teenagers.\"</i></p>")}
<p>Before believing this, what would a psychologist want to know? List five questions about the study behind the claim, and for each say in one sentence why it matters.</p>
{slot_list([f"Question {i} and why it matters" for i in range(1, 6)])}
{S("W", 5)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", f"""<h2>How the decisions in a study connect</h2>
<p>Every study is a chain of decisions, and each one limits what the next can achieve. The Foundations chapters each covered one link.</p>
{table(["Decision", "The question to ask", "Chapter"], [
 ["Research question and aim", "What exactly do I want to find out, about whom?", "CRM-03, CRM-10"],
 ["Method", "Do I need to test a cause (experiment), describe behaviour (observation), measure how common something is (survey), or understand experiences (interview)?", "CRM-03 to CRM-06"],
 ["Sample", "Who is my population, and which sampling technique gives me a sample I can justify?", "CRM-07"],
 ["Procedure and measurement", "How will I operationalise and record the key variables, and how will I keep things consistent?", "CRM-03, CRM-05, CRM-08"],
 ["Ethics", "How will I protect participants, and how might that affect the data?", "CRM-04"],
 ["Analysis", "Which statistics, graphs or themes fit my data?", "CRM-09"],
 ["Conclusion", "What can my design actually support, and for whom?", "CRM-01, CRM-02, CRM-08"],
])}
<p>When you evaluate any study, you are checking these links one by one: is each decision justified, and does the conclusion stay within what the chain can support?</p>""", "How the decisions connect")

P.card("rd-2", f"""<h2>The IA in brief</h2>
<p>The internal assessment is a <b>research proposal</b>: you design a study to investigate a real-life problem for a <b>population of interest</b>, such as students in your school or a group in your community. You do <b>not</b> collect data. The task is about justifying your decisions.</p>
{table(["Feature", "What the guide sets"], [
 ["Method", "One of the four class practical methods: experiment (true or quasi), interview (structured, semi-structured or focus group), observation, or survey/questionnaire"],
 ["Length and time", "A maximum of 2,200 words, and about 20 hours of class time"],
 ["Marks and weighting", "24 marks across four criteria of 6 marks each; 30% of the final grade at SL and 20% at HL"],
 ["Criterion A: Introduction", "A focused aim, the problem and its impact on the population, and two relevant studies with clear links to the proposal"],
 ["Criterion B: Research methodology", "The method and why it suits the aim; the procedure, including sampling, sample, design, setting and process; ethical considerations specific to the study"],
 ["Criterion C: Data collection", "One data collection tool with at least five items (a copy in the appendix), the decisions behind it, and the challenges you expect"],
 ["Criterion D: Discussion", "Potential findings and their implications for policy or practice, your own possible bias, and one other method that would add understanding"],
])}
<p>The proposal must be one that an ethics committee would approve. Some topics are not allowed at all, such as abuse or self-harm, and your teacher will advise on topics that are sensitive here in the UAE. Safe, popular directions include sleep and memory in exam season, screen time and attention, learning in a second language, belonging for newly arrived students, and peer influence on study habits.</p>""", "The IA in brief")

P.card("rd-3", f"""<h2>Choosing a method</h2>
<p>There is rarely one right method, but there is always a <i>justified</i> one. Match the method to what the question needs:</p>
{table(["If the question asks...", "A good fit", "What you give up"], [
 ["Does X cause a change in Y?", "Experiment (true if you can randomly allocate; quasi if groups already exist)", "Often realism; sometimes ethics limits what you can manipulate"],
 ["What do people actually do in a situation?", "Observation", "The reasons behind the behaviour; cause and effect"],
 ["How common is a behaviour or attitude, and how does it relate to other variables?", "Survey/questionnaire", "Depth; accuracy of self-report; cause and effect"],
 ["How do people experience something, and what does it mean to them?", "Interview or focus group", "Sample size and generalisability; comparability across participants"],
])}
<p>Criterion D asks for one other method that would add understanding. The best answers say exactly <i>what</i> the second method would reveal that the first cannot, for example "interviews would explain <i>why</i> students check their phones at night, which the survey only counts". Combining methods to check findings from different angles is <b>triangulation</b>.</p>""", "Choosing a method")

P.card("rd-4", f"""<h2>Paper 2 Section B: the full task</h2>
<p>Section B gives you an unseen study and asks you to <b>discuss</b> it with regard to two or more concepts, chosen from at least four listed in the question. It is worth 15 marks; plan for about 5 minutes and write for about 40.</p>
<ol>
<li><b>Read the study twice.</b> The second time, underline every detail that raises a concept: the sample, how participants were placed in groups, how variables were measured, who did the analysis, what the conclusion claims.</li>
<li><b>Choose your concepts.</b> Pick the two (or three) that the details support most richly. Two concepts discussed in depth and two or more discussed for breadth are both acceptable approaches.</li>
<li><b>Plan each point</b> with the rung 3 moves (CRM-02): the concept and the idea, the exact detail, the consequence for the conclusion, and a link to another concept.</li>
<li><b>Show concepts interacting.</b> For example, how participants were allocated (causality) and who was sampled (bias) together limit what the conclusion can claim.</li>
<li><b>End with a conclusion</b> that answers the question and follows from your points, ideally naming a condition (rung 5).</li>
</ol>
<p>The marks rise with how well you understand and engage with the concepts in relation to <i>this</i> study, how developed your links are, how accurate your terms are, and how specific your references to the study are.</p>""", "Paper 2 Section B")

P.card("rd-5", f"""<h2>The Foundations at a glance</h2>
{table(["Chapter", "The skill you need from it"], [
 ["CRM-01 The Six Concepts", "Tell perspective from bias; apply any concept to a specific study"],
 ["CRM-02 Writing with Concepts", "Write sentences that pass the swap test; plan with the five rungs"],
 ["CRM-03 The Experiment", "Describe an experiment precisely; explain what supports and weakens a causal claim"],
 ["CRM-04 Quasi and Natural Experiments, and Ethics", "Classify designs; explain ethics in relation to a specific study"],
 ["CRM-05 The Observation", "Design categories and sampling; explain inter-rater reliability"],
 ["CRM-06 Surveys and Interviews", "Write neutral items; compare surveys and interviews"],
 ["CRM-07 Sampling, Correlational Studies and Case Studies", "Justify a sample; explain why correlation is not cause"],
 ["CRM-08 Research Considerations", "Use reliability, validity, credibility and transferability accurately"],
 ["CRM-09 Data Analysis and Interpretation", "Read statistics and graphs; describe before interpreting"],
])}""", "The Foundations at a glance")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself: one question per skill</h2>
<p>1. A biological psychologist explains exam anxiety through the body's stress response; a cognitive psychologist explains it through how students interpret exams. A student writes: "The biological psychologist is biased against cognitive explanations." Is "biased" the right word? Explain in two sentences.</p>
{S("C", 2)}
<p>2. A researcher compares students at schools that introduced a mindfulness programme with students at schools that did not. Name the design and one confounding variable.</p>
{S("C", 2)}
<p>3. A survey item reads: "How much has late-night phone use damaged your sleep?" Name the problem and rewrite the item.</p>
{S("C", 2)}
<p>4. A researcher recruits 18 interviewees by snowball sampling, starting with two members of a school chess club. Can the findings be generalised to all teenagers? Answer in two sentences using the word "therefore".</p>
{S("C", 2)}
<p>5. A study of 800 teenagers finds that users of a study app score 2.1 points higher out of 100 on a test than non-users (p = .001). Should every school buy the app? Use the concepts of measurement and causality.</p>
{S("C", 3)}""", "Check yourself")

P.topic("exam", "Exam practice", "A mini-IA design, a concept-choice warm-up and a full Paper 2 Section B task.")
P.card("ex-1", f"""<h2>Mini-IA design challenge</h2>
{tip("<p><b>The context:</b> a school counsellor in the UAE notices that many Grade 10 students say they feel tired in morning lessons, and several mention using their phones late at night. She wants to investigate how late-night phone use relates to sleep and morning alertness among Grade 10 students at her school.</p>")}
<p>Design a research proposal for this problem. Write in prose, not bullet points. Each part below mirrors part of the IA.</p>
<p><b>1. Aim</b> (like Criterion A): a focused research question about this population, and a hypothesis.</p>
{S("I", 2)}
<p><b>2. Method and why</b> (Criterion B): one of the four methods, with three or four sentences on why it suits this question and what data it produces.</p>
{S("I", 3)}
<p><b>3. Procedure</b> (Criterion B): enough detail for someone else to carry it out, including how the key variables are measured or recorded.</p>
{S("I", 4)}
<p><b>4. Sampling</b> (Criterion B): your technique, target population, why it fits, and one limitation for generalisability.</p>
{S("I", 3)}
<p><b>5. Ethics</b> (Criterion B): at least three considerations specific to this study, each with the steps you would take.</p>
{S("I", 3)}
<p><b>6. Another method</b> (Criterion D): what a different method would add to the same question.</p>
{S("I", 2)}
<p class="small">A practice rubric for this task (not the IA criteria) is in the self-check box on your answer sheet.</p>""", "Mini-IA design challenge")

P.card("ex-2", f"""<h2>Paper 2, Section B warm-up: choose your concepts [6 marks]</h2>
{tip("<p><b>Study (invented for practice):</b> Researchers used semi-structured interviews to explore how students aged 14 to 17 experience comparing themselves with others on social media, and how this affects their confidence. Twelve participants were recruited by snowball sampling, starting with two volunteers from a psychology class. Each was interviewed one-to-one for about 40 minutes. The lead researcher had previously published two studies arguing that social media harms teenagers' self-esteem, and carried out the thematic analysis alone. Four themes were reported: comparing with carefully edited posts, seeking approval through likes, awareness that online lives are not real, and limiting use as a way of coping. The researchers concluded that social media is a major cause of low confidence in teenagers and recommended compulsory media-literacy lessons in all secondary schools. Participants gave written consent and were debriefed. Two participants said during their interviews that they felt the questions were steering them towards particular answers.</p>")}
<p><b>Evaluate this study with reference to two concepts of your choice from: bias, causality, change, measurement, perspective and responsibility.</b> [6]</p>
<p class="small">Spend a minute deciding which two concepts the details support most richly. The choice is part of the task.</p>
{S("S", 7)}
{earns("CRM-10-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Choose your concepts [6 marks]")

P.card("ex-3", f"""<h2>Paper 2, Section B [15 marks]</h2>
{tip('''<p><b>Study (invented for practice): screen time, sleep and memory</b></p>
<p>Researchers wanted to know whether reducing evening screen time improves memory in teenagers. They invited all Grade 10 students at two secondary schools in Dubai to take part; 64 volunteered, with written consent from their parents. Students at School A (n = 33) joined a four-week programme in which they agreed to stop using phones and tablets one hour before bed. Students at School B (n = 31) carried on as normal. Students were allocated by school, not as individuals.</p>
<p>Each morning, students recorded their screen use and hours of sleep in an online diary. At the start and end of the four weeks, all students took a 20-word free recall test in their classroom, supervised by their own teachers, who knew which school was in the programme. Six students in the programme group stopped completing their diaries and were removed from the analysis, leaving 27.</p>
<p>The programme group's mean recall rose from 11.2 to 13.1 words. The comparison group's mean rose from 11.4 to 11.9 words. The researchers concluded that limiting screen use before bed improves memory, and recommended that all UAE schools introduce the programme.</p>''')}
<p><b>Discuss this study with regard to two or more of the following concepts: bias, causality, measurement, responsibility.</b> [15]</p>
<p class="small">Plan for about 5 minutes: for each concept, the detail you will use, the point you will make and a link to another concept. Then write for about 40 minutes, ending with a conclusion that follows from your points.</p>
{slot_list(["Concept 1: detail, point, link", "Concept 2: detail, point, link", "Concept 3 (optional)", "Conclusion in one sentence"])}
{S("X", 4)}
{S("X", 12)}
{earns("CRM-10-X", ["I show a clear understanding of each concept I use, in relation to this study, not in general.", "My analysis is developed: each point says what the detail is, why it matters and what it means for the conclusion.", "I show how concepts interact, for example how allocation and sampling together limit the causal claim.", "I use accurate terms and refer to specific details of the study throughout.", "I argue to a clear conclusion that follows from my points."], "Our plain-language guide. The official Section B markband is in the self-check box on your answer sheet.")}""", "Paper 2, Section B [15 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, a forward look and a self-check.")
P.card("mo-ai", ai_card([
 "I am designing an IA proposal on sleep and memory in Grade 12 students. Ask me one question at a time about my aim, method, sample, tool and ethics, the way a supervisor would. Do not suggest answers.",
 "Here is my Paper 2 Section B plan. Tell me which concept is best supported by specific details and which is weakest. Do not rewrite it.",
 "Give me a short invented study and ask me which two concepts I would choose to evaluate it, and why.",
]), "Using AI to learn")
P.card("mo-l-1", f"""<div class="sec-label">Looking ahead</div><h2>Last check: which method?</h2>
<p>Each context has a recommended class practical method. For each research question, name the method you think fits best and justify it in one sentence.</p>
<ol>
<li>Health and well-being: does an eight-week mindfulness programme reduce exam anxiety in Grade 11 students?</li>
<li>Human development: how does adolescents' sense of identity change between 14 and 18?</li>
<li>Human relationships: how do young adults in different cultural settings describe what makes a close friendship?</li>
<li>Learning and cognition: does spaced practice lead to better long-term memory than massed practice?</li>
</ol>
{slot_list([f"Question {i}: method and justification" for i in range(1, 5)])}
{S("L", 4)}""", "Last check")
P.card("mo-self", f"""<div class="sec-label">Self-check</div><h2>How ready are you for Paper 2?</h2>
<p>Tick the skills you are confident about. Revisit the chapter for any you leave unticked.</p>
{checklist("CRM-10-ready", [
 "I can tell perspective from bias and apply both to unseen studies (CRM-01).",
 "I can describe a class practical in the Question 1 format with full detail (CRM-03 to CRM-06).",
 "I can explain ethics in relation to a specific practical (CRM-04).",
 "I can classify a study as a true, quasi or natural experiment and justify it (CRM-04).",
 "I can compare a survey with an interview on at least four points (CRM-06).",
 "I can design a study with the method, sampling, procedure and ethics justified (CRM-07, CRM-10).",
 "I can read descriptive statistics and keep description separate from interpretation (CRM-09).",
 "I can evaluate a study with any two concepts, using specific evidence (CRM-02, CRM-10).",
])}""", "Self-check")

open("../../ws-crm-10.html", "w").write(P.render())
print("ok", P.counts)
