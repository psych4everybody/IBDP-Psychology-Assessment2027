from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, ai_card

P = Page("CRM-07", "07", "Sampling, Correlational Studies and Case Studies",
         "Who takes part, and what can you conclude when you cannot run an experiment?")
S = P.slot

P.topic("start", "Sampling, Correlations and Case Studies", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to choose and justify a sampling technique, explain what a correlation can and cannot tell you, explain when a case study is the right tool, and design a study of your own with every choice justified.</p>
{checklist("CRM-07-goals", [
 "I can explain target population, sample, representativeness and sampling bias.",
 "I can describe the five sampling techniques in the guide, with a strength and limitation of each.",
 "I can explain what a correlation coefficient shows, and the two reasons a correlation does not show cause.",
 "I can explain what a case study is, with its strengths and limitations.",
 "I can design a study for a research question and justify the method, sampling, procedure and ethics.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (sampling techniques; research methods: correlational studies and case studies).</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 2 Section A (sampling in Questions 1 and 4; Question 4 is a design task); Paper 2 Section B (unseen studies are often correlational or case studies); Paper 3 for HL students (correlation coefficients and scatterplots); the IA (Criterion B, sampling)</p>
{chips("bias", "causality", "measurement")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p>A company that makes a mindfulness app paid for a study of its own app. It emailed all 3,400 registered users to invite them to a four-week study. Of those who chose to take part, 290 completed an anxiety questionnaire at the start and the end. 87% showed lower anxiety scores after four weeks. The company's advert says: \"Our app reduces anxiety in 87% of users.\"</p>")}
<p>1. What is the target population, and what is the actual sample? Why are they different?</p>
{S("W", 2)}
<p>2. Give two problems with how participants were recruited.</p>
{S("W", 2)}
<p>3. Even if the 87% figure is accurate, did the app cause the change? Give one other explanation.</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>Populations, samples and sampling bias</h2>
<p>The <b>target population</b> is the whole group a researcher wants to draw conclusions about, for example Grade 11 students in the UAE. The <b>sample</b> is the smaller group that actually takes part. A sample is <b>representative</b> when it reflects the population on the characteristics that matter for the research question, such as age, gender, nationality, language or school type. The more representative the sample, the more confidently findings can be <b>generalised</b>.</p>
<p><b>Sampling bias</b> occurs when the sample differs from the population in a systematic way, so the findings are distorted in a predictable direction. In the warm-up, the people who chose to join the app study were already users who had kept the app and who were willing to spend four weeks on a study: they were probably more motivated and more positive about the app than users in general.</p>""", "Populations and samples")

P.card("rd-2", f"""<h2>The five sampling techniques</h2>
{table(["Technique", "How participants are chosen", "Strength", "Limitation"], [
 ["Random", "Every member of the target population has an equal chance of being chosen, for example by a random number generator from a full list", "Least sampling bias; most likely to be representative", "Needs a complete list of the population; people chosen may decline, which reintroduces bias"],
 ["Stratified", "The population is divided into subgroups (strata) that matter, such as year group or gender, and people are chosen randomly from each in the same proportions as the population", "Every important subgroup is represented in the right proportion", "Needs detailed knowledge of the population; time-consuming"],
 ["Opportunity", "Whoever is available and willing at the time, such as one class. Also called convenience sampling.", "Quick, easy and cheap; the most common technique in practice", "Those available may differ systematically from the population"],
 ["Self-selected", "People volunteer, for example by answering an advertisement", "Participants are willing and likely to complete the study", "Volunteers may be more motivated, curious or affected by the topic than others"],
 ["Snowball", "Existing participants recruit further participants from people they know", "Reaches hard-to-find groups, such as people with a rare experience; builds trust", "The sample comes from linked social networks, so it is unlikely to be representative"],
])}
<p>Researchers in qualitative studies often describe <b>purposive</b> sampling: deliberately choosing people who have the experience being studied. It is not one of the five techniques in the guide, so if you use the term, explain it.</p>
<p>Remember from CRM-03: <b>random sampling</b> (who is in the study) is different from <b>random allocation</b> (which condition they are placed in). A class can be an opportunity sample that is then randomly allocated to two conditions.</p>""", "The five sampling techniques")

P.card("rd-3", """<h2>Correlational studies</h2>
<p>A <b>correlational study</b> measures two or more variables, called <b>co-variables</b>, as they already are, without manipulating either, and tests whether they are related. The strength and direction of the relationship are given by a <b>correlation coefficient</b> (r), which runs from -1 to +1.</p>
<ul>
<li><b>Positive correlation</b> (r above 0): as one variable increases, so does the other, for example hours of revision and test scores.</li>
<li><b>Negative correlation</b> (r below 0): as one increases, the other decreases, for example hours of sleep lost and memory test performance.</li>
<li><b>No correlation</b> (r close to 0): no consistent straight-line relationship.</li>
</ul>
<p>The closer r is to +1 or -1, the stronger the relationship. As a rough guide, about 0.1 is weak, 0.3 moderate and 0.5 or above strong, though what counts as strong depends on the field. Correlations are shown on a <b>scatterplot</b>, which can also reveal curved relationships that r would miss (CRM-09).</p>
<p>A correlation does not show cause, for two reasons:</p>
<ul>
<li><b>Bidirectional ambiguity:</b> if exercise and good mood go together, exercise may improve mood, or people in a good mood may exercise more, or both.</li>
<li><b>The third variable problem:</b> ice cream sales and sunburn are positively correlated, but hot, sunny weather causes both.</li>
</ul>
<p>Correlational studies are still valuable. They can study variables that cannot be manipulated ethically, such as stress or screen time over years, and they show which relationships are worth testing with experiments.</p>""", "Correlational studies")

P.card("rd-4", """<h2>Case studies</h2>
<p>A <b>case study</b> is an in-depth investigation of a single person, group, organisation or event, often over a long period. Case studies usually combine several methods: interviews, observations, psychological tests, medical records and documents. The case is often unusual, which is exactly why it is studied.</p>
<ul>
<li><b>Strengths:</b> rich, detailed data; the only way to study rare conditions or events; can challenge an accepted theory with a single clear counter-example; generates hypotheses for later research.</li>
<li><b>Limitations:</b> findings from one case may not generalise; much information may be retrospective and depend on memory; the researcher's interpretation plays a large role; anonymity is hard to protect when the case is unusual and well known.</li>
</ul>
<p>Correlational studies and case studies are both research methods in the guide, and they often appear as unseen studies in Paper 2 Section B. They are <b>not</b> class practical methods and cannot be used as the method for your IA, which must be an experiment, observation, survey/questionnaire or interview.</p>""", "Case studies")

P.card("rd-5", f"""<h2>Key study: H.M., a case study of memory</h2>
{table(None, [
 ["Background", "In 1953, a young man known in research as H.M. (Henry Molaison) had surgery to treat severe epilepsy. Parts of the medial temporal lobes on both sides of his brain, including most of the hippocampus, were removed."],
 ["What was found", "His epilepsy improved, but he was left with severe difficulty forming new long-term memories of facts and events, while his short-term memory, his intelligence and many older memories were largely intact. Later testing by Brenda Milner showed that he could improve at a new motor skill, mirror drawing, over several days without remembering having practised it."],
 ["Methods used", "Researchers studied H.M. for decades, using memory tests, observation, interviews and, later, brain scans."],
 ["Conclusion", "Different kinds of memory depend on different brain systems: the hippocampus is needed to form new memories of facts and events, but not to learn skills."],
 ["Use it for", "This chapter (case studies); biological factors in memory (CL-07); localization of function."],
 ["Evaluate it with", "<b>Causality:</b> because the surgery is documented, the cause of his memory loss is unusually clear for a case study. <b>Bias:</b> one person, with a history of epilepsy and its treatment, may not represent how memory works in everyone. <b>Responsibility:</b> H.M. could not remember giving consent to each session, so consent and his privacy had to be protected by others."],
])}""", "Key study: H.M.")

P.card("rd-6", f"""<h2>Real life: samples and correlations in the news</h2>
{tip('''<ul>
<li><b>Online polls.</b> A website poll with 10,000 replies can be less representative than a random sample of 1,000, because only people who visit the site and care about the topic answer.</li>
<li><b>Health headlines.</b> "People who drink coffee live longer" comes from correlational data. Coffee drinkers may differ in income, health and lifestyle.</li>
<li><b>App statistics.</b> "Students who use our revision app score higher" says nothing about whether the app causes it if students chose whether to use it.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example and explain the problem using the correct term (sampling bias, bidirectional ambiguity or third variable).</p>
{S("D", 2)}""", "Real life")

P.card("rd-7", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies"], [
 ["Bias", "Sampling bias limits how far findings can be generalised. Self-selected and opportunity samples are especially at risk."],
 ["Causality", "Correlations show relationships, not causes, because of bidirectional ambiguity and third variables. Case studies may suggest causes but cannot test them."],
 ["Measurement", "Co-variables must be measured validly; a correlation is only as good as the measures behind it."],
 ["Perspective", "Case studies give an in-depth, individual view; large correlational samples give a broad, general view. Each sees something the other misses."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. Explain the difference between a target population and a sample, using the app study in the warm-up.</p>
{S("C", 2)}
<p>2. A researcher wants a sample that matches the proportions of Grade 9 to 12 students in a school. Which technique should she use, and how would she do it?</p>
{S("C", 2)}
<p>3. A study finds r = -0.45 between late-night phone use and morning alertness. Describe what this shows, and give two reasons it does not show cause.</p>
{S("C", 3)}
<p>4. Give one strength and one limitation of the case study of H.M.</p>
{S("C", 2)}
<p>5. Why can correlational studies and case studies not be used as the method for your IA?</p>
{S("C", 2)}""", "Check yourself")

P.topic("exam", "Exam practice", "Paper 2 practice: designing a study, and evaluating a correlational study.")
P.card("ex-1", f"""<h2>Paper 2, Section A, Question 4 style [6 marks]</h2>
<p><b>Design a study using a method of your choice (experiment, observation, survey/questionnaire or interview) to investigate whether listening to music while studying affects academic performance in secondary school students.</b> [6]</p>
<p class="small">Any of the four methods can be defended; the marks come from a clear, detailed and justified design. Plan first, then write in continuous prose.</p>
{slot_list(["Method, and why it suits this question", "Target population, sampling technique, and one limitation", "Procedure: what participants do, what is measured and how", "Two ethical considerations, and how each is handled"])}
{S("Q4", 5)}
{S("Q4", 6)}
{earns("CRM-07-Q4", ["My design uses the method I chose and stays on the research question.", "I give an aim and enough procedure (participants, sampling, materials, steps) for someone to carry it out.", "I explain key choices, such as how responses would be recorded and analysed, and one ethical step.", "I use research methods terms correctly."])}""", "Paper 2, Section A, Question 4 style [6 marks]")
P.card("ex-2", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
{tip("<p><b>Study (invented for practice):</b> 156 students at one private school in a large city were recruited by opportunity sampling. They reported the average number of hours a week they spent in organised activities such as sports teams, music groups or clubs. Their most recent end-of-year grade average was taken from school records, with parental consent. There was a moderate positive correlation (r = 0.41, p &lt; .01): students who spent more time in activities tended to have higher grades. The researchers suggested that taking part in activities may improve grades by building time-management and goal-setting skills.</p>")}
<p><b>Evaluate this study with reference to the concepts of causality and measurement.</b> [6]</p>
<p class="small">Read the final sentence carefully before you begin.</p>
{S("S", 7)}
{earns("CRM-07-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "Give me five research scenarios, one at a time, and ask me which sampling technique is being used and one limitation of it. Wait for my answer.",
 "Give me three correlations from everyday life. For each, ask me to suggest a third variable and explain the possible direction of cause.",
 "Here is my design for a study on music and studying. Ask me three questions an examiner might ask about my sampling and procedure. Do not rewrite it.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA starter", "Criterion B asks you to justify your sampling. For a proposal on sleep and memory in Grade 12 students in the UAE, compare an opportunity sample from your school with a stratified sample across several schools. Which would you choose, and what would you have to admit as a limitation?"],
 ["EE question workshop", "Turn \"Does screen time harm teenagers?\" into a focused question, and note which of the studies you find are correlational and which are experimental."],
 ["HL link", "<b>Technology:</b> social media platforms hold data on millions of users. What would a huge correlational dataset gain in sample size, and what would it still be unable to show?"],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>1. Complete the sentence about your design in Question 4: "My sampling technique is ___, so my findings can or cannot be generalised to ___ because ___."</p>
<p>2. What would a researcher gain by combining the correlational study above with your design? What is combining methods like this called?</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-07.html", "w").write(P.render())
print("ok", P.counts)
