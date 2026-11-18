from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, practice_note, ai_card

P = Page("CRM-06", "06", "Surveys and Interviews",
         "How do psychologists ask people about their own thoughts, habits and experiences?")
S = P.slot

P.topic("start", "Surveys and Interviews", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to write good survey questions, choose the right kind of interview, explain the biases that affect self-report, and compare surveys and interviews point by point, which is exactly what Paper 2 Section A Question 3 asks.</p>
{checklist("CRM-06-goals", [
 "I can tell closed questions, rating-scale (Likert) items and open questions apart, and explain what data each gives.",
 "I can explain structured, semi-structured and focus group interviews, and when each is the right choice.",
 "I can explain at least three biases that affect surveys and interviews, and how to reduce them.",
 "I can write a short questionnaire with clear, neutral items.",
 "I can compare and contrast a survey with an interview, using similarities as well as differences.",
 "I can evaluate a self-report study using the concepts of bias and measurement.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (research methods: surveys/questionnaires and interviews). The interview is the class practical method set for health and well-being (HW-11) and the survey for human relationships.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 2 Section A (all four questions when your practical is the interview or survey; Question 3 compares methods); Paper 2 Section B; Paper 3 for HL students (qualitative data and thematic analysis); the IA (a questionnaire or interview schedule can be your data collection tool)</p>
{chips("bias", "measurement", "perspective")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p><b>Researcher A</b> wants to understand exam stress in Grade 11. She sends an anonymous 10-item questionnaire to 600 students in 12 schools, with rating scales and two open questions, and gets 587 replies in a week. <b>Researcher B</b> studies the same topic with semi-structured interviews with 14 students and three focus groups of six students. The sessions are recorded and transcribed, and analysis takes six weeks.</p>")}
<p>1. What can Researcher A find out that Researcher B probably cannot? Give a specific example.</p>
{S("W", 2)}
<p>2. What can Researcher B find out that Researcher A probably cannot?</p>
{S("W", 2)}
<p>3. Could both researchers' conclusions be valid at the same time? Which concept does this connect to?</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", f"""<h2>Surveys and questionnaires</h2>
<p>A <b>survey</b> collects self-reported information from people using a fixed set of written questions, the <b>questionnaire</b>. The IB treats the two words as interchangeable. Because every participant gets the same items, surveys are standardised, and they can reach large samples quickly, on paper or online. A survey can be <b>cross-sectional</b> (one snapshot of different people at one time) or <b>longitudinal</b> (the same people surveyed again over months or years).</p>
{table(["Item type", "What it looks like", "Data", "Strength and limitation"], [
 ["Closed question", "Fixed options: \"How many hours do you sleep on a school night? Under 6 / 6 to 7 / 7 to 8 / over 8\"", "Quantitative", "Easy to count and compare; participants cannot explain or add anything"],
 ["Rating scale (Likert) item", "A statement rated on a scale: \"I feel anxious before tests\" from strongly disagree (1) to strongly agree (5)", "Quantitative (ordinal)", "Measures strength of attitude; people may avoid the extremes or always choose the middle"],
 ["Open question", "No options: \"What do you do when schoolwork feels overwhelming?\"", "Qualitative", "Depth and unexpected answers; harder and slower to analyse and compare"],
])}
<p>Good questionnaires use clear, neutral wording; one idea per question (no "double-barrelled" items such as "Do you find homework useful and enjoyable?"); simple, general questions first and more personal ones later; and a <b>pilot</b> with a few people to catch confusing items before the real survey.</p>""", "Surveys and questionnaires")

P.card("rd-2", """<h2>Biases in self-report</h2>
<p>Surveys and interviews both depend on what people say, which brings particular risks:</p>
<ul>
<li><b>Social desirability bias:</b> answering in the way that looks good rather than truthfully, for example under-reporting screen time.</li>
<li><b>Acquiescence:</b> a tendency to agree with statements whatever they say. Mixing positively and negatively worded items helps to detect it.</li>
<li><b>Leading questions:</b> wording that suggests the "right" answer, such as "Don't you agree that phones distract students?"</li>
<li><b>Question order effects:</b> earlier questions shape answers to later ones.</li>
<li><b>Memory limits:</b> people are often poor at recalling how often they did something, especially over long periods.</li>
<li><b>Who replies:</b> if only some people return the survey, the sample may be biased; people who care strongly about a topic are more likely to respond.</li>
</ul>
<p>Anonymity, neutral wording, careful ordering and piloting reduce these problems. None removes them completely, which is why self-report is often combined with other measures.</p>""", "Biases in self-report")

P.card("rd-3", f"""<h2>Interviews and focus groups</h2>
<p>In an <b>interview</b> the researcher asks questions in person, and the interviewer becomes part of the measuring instrument: their wording, tone and follow-up questions shape the data.</p>
{table(["Type", "What it means", "Strength", "Limitation"], [
 ["Structured", "The same questions in the same order for everyone, with no follow-up", "Comparable answers; several interviewers can be standardised", "Little depth; no chance to explore unexpected answers"],
 ["Semi-structured", "A core interview schedule, but the interviewer can probe, follow up and change the order", "Balances comparability and depth; the most widely used type", "Harder to compare across participants; more room for interviewer effects"],
 ["Focus group", "A small group discussion led by a moderator, where participants respond to each other as well as to the moderator. In IB class practicals, groups have three to eight participants.", "Shows shared views, group norms and how people build ideas together", "One person may dominate; people may hold back or follow the group in front of peers"],
])}
<p>Unstructured interviews, with no set schedule at all, are used in some research, but the IB lists only structured, semi-structured and focus group interviews for class practicals. A good interview schedule moves from <b>engagement</b> questions (easy, general openers) to <b>exploration</b> questions (the main topic, with probes) to <b>exit</b> questions (anything else the participant wants to add).</p>
<p>Interviews are usually audio-recorded with consent and <b>transcribed</b>, then analysed with <b>thematic analysis</b> or <b>content analysis</b>: coding the transcripts and grouping the codes into themes (CRM-09). Biases specific to interviews include <b>interviewer effects</b> (the interviewer's reactions influence answers), and in focus groups a <b>dominant participant</b> or pressure to agree. Interviewer training, a piloted schedule and <b>reflexivity</b> help to reduce them.</p>""", "Interviews and focus groups")

P.card("rd-4", f"""<h2>Comparing surveys and interviews</h2>
<p>Paper 2 Section A Question 3 asks you to compare and contrast your practical's method with another method, so you need <b>similarities</b> as well as differences. Write each point about both methods together, and tie it to the study.</p>
{table(["Aspect", "Survey / questionnaire", "Interview / focus group"], [
 ["Similarity: self-report", "Depends on what participants say about themselves", "Also depends on what participants say"],
 ["Similarity: ethics", "Needs informed consent, anonymity and the right to withdraw", "Needs the same, plus consent to record"],
 ["Similarity: bias", "Social desirability and leading questions", "Social desirability and leading questions, plus interviewer effects"],
 ["Data", "Mainly quantitative; open questions add some qualitative data", "Mainly qualitative; analysed by coding into themes"],
 ["Sample", "Large samples quickly, often anonymous", "Small samples; time-consuming to run and transcribe"],
 ["Depth", "Limited: fixed options", "High: probes and follow-ups"],
 ["Researcher influence", "Low: often completed alone", "Higher: tone and follow-ups can shape answers"],
 ["Best for", "How common a behaviour or attitude is, and patterns across groups", "Experiences, meanings and reasons in people's own words"],
])}""", "Comparing surveys and interviews")

P.card("rd-5", f"""<h2>Key study: Hofstede's survey of IBM employees</h2>
{table(None, [
 ["Aim", "To compare work-related values across many countries."],
 ["Procedure", "Between 1967 and 1973, more than 100,000 questionnaires were collected from employees of the multinational company IBM in many countries. Items asked about values at work, such as how people relate to managers and how far they prefer clear rules."],
 ["Findings", "Answers were averaged by country and analysed for patterns, producing four original dimensions on which national cultures differed, including power distance and individualism. Later work added two more."],
 ["Why a survey", "Only a standardised questionnaire could collect comparable answers from so many people in so many countries. The same items, translated, made the comparison possible."],
 ["Use it for", "This chapter (large-scale surveys); cultural dimensions (HR-04); the etic approach."],
 ["Evaluate it with", "<b>Bias:</b> all participants worked for one company, mostly in similar jobs, so they may not represent their countries. <b>Measurement:</b> do translated questions mean the same thing in every language? <b>Perspective:</b> applying the same measure everywhere is an etic approach, which may miss values that matter within a particular culture."],
])}""", "Key study: Hofstede")

P.card("rd-6", f"""<h2>Real life: asking people questions</h2>
{tip('''<ul>
<li><b>Customer feedback.</b> A UAE government service asks you to rate your visit from one to five stars after you finish. Who tends to answer, and what does that do to the average rating?</li>
<li><b>School surveys.</b> A student well-being survey is more honest when it is anonymous and completed on a device rather than handed to a teacher.</li>
<li><b>Focus groups in design.</b> Companies ask small groups to discuss a new product before launch, because the discussion reveals reasons that a rating scale cannot.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example and name one bias that could affect the answers, and one way to reduce it.</p>
{S("D", 2)}""", "Real life")

P.card("rd-7", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies to surveys and interviews"], [
 ["Bias", "Social desirability, acquiescence, leading questions, interviewer effects and who chooses to respond can all push answers in one direction."],
 ["Measurement", "Self-report measures what people say, which may differ from what they do. Item wording, scale design and coding decisions all affect validity."],
 ["Perspective", "Interviews capture people's own meanings and experiences; surveys impose the researcher's categories. Each gives a different view of the same topic."],
 ["Causality", "Surveys usually show relationships between variables, not causes. A link between phone use and focus does not show which causes which."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. Write one closed question, one rating-scale item and one open question on sleep before exams.</p>
{S("C", 3)}
<p>2. What is wrong with this item, and how would you fix it? <i>"Don't you think that teenagers spend too much time on games and social media?"</i></p>
{S("C", 2)}
<p>3. When would you choose a focus group instead of individual semi-structured interviews?</p>
{S("C", 2)}
<p>4. Give two similarities and two differences between a survey and an interview.</p>
{S("C", 3)}
<p>5. Explain social desirability bias with an example, and one way to reduce it.</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Practice study: social media and study focus</h2>
{practice_note("survey", "survey")}
<p><b>Aim:</b> to investigate students' self-reported social media habits and how they think these relate to their focus when studying. The questionnaire is anonymous and completed in class.</p>
<ol>
<li><i>Closed:</i> How many hours a day do you spend on social media on a typical school day? Under 1 / 1 to 3 / 3 to 5 / more than 5</li>
<li><i>Rating scale:</i> When you sit down to study, how often do you check your phone in the first 15 minutes? Never / Rarely / Sometimes / Often / Almost always</li>
<li><i>Rating scale:</i> "Using social media in study breaks helps me refocus." Strongly disagree to strongly agree</li>
<li><i>Rating scale:</i> "I find it hard to concentrate when my phone is nearby." Strongly disagree to strongly agree</li>
<li><i>Open:</i> Describe one strategy you use to manage distractions while studying.</li>
</ol>
<p>Complete it anonymously on paper. Your teacher will tally the class results.</p>
{slot_list(["Most common answer to item 1", "Most common answer to item 2", "Most common answer to item 3", "Most common answer to item 4"])}
{S("C", 4)}
<p>Look at items 3 and 4. Do they point the same way? Why might people agree with both?</p>
{S("C", 3)}""", "Practice study")

P.topic("exam", "Exam practice", "Paper 2 practice: describing a survey, comparing methods, and evaluating self-report.")
P.card("ex-1", f"""<h2>Paper 2, Section A, Question 1 style [4 marks]</h2>
<p><b>Describe how a survey/questionnaire was used in the practice study, including the aim and procedure.</b> [4]</p>
<p class="small">Include the aim, the types of item, how it was given out, how anonymity was protected, the sample, and how results were collected.</p>
{S("Q1", 5)}
{earns("CRM-06-Q1", ["I name the method and its type (for example a true experiment, a naturalistic observation or a semi-structured interview).", "I state the aim of the study.", "I describe the procedure in order, with enough detail that someone could repeat it.", "I use research methods terms correctly (for example operationalised variables, sampling, consent)."])}""", "Paper 2, Section A, Question 1 style [4 marks]")
P.card("ex-2", f"""<h2>Paper 2, Section A, Question 3 style [6 marks]</h2>
<p><b>Compare and contrast the survey used in the practice study with an interview.</b> [6]</p>
{slot_list(["Similarity 1", "Similarity 2", "Difference 1 (think: type of data)", "Difference 2 (think: depth and researcher influence)", "Difference 3 (think: sample size)"])}
{S("Q3", 4)}
{S("Q3", 6)}
{earns("CRM-06-Q3", ["I give at least one similarity and at least one difference.", "Each point is explained, not just listed: I say why the two methods are alike or different.", "I tie each point to the study and to the other method.", "I use research methods terms correctly throughout."])}""", "Paper 2, Section A, Question 3 style [6 marks]")
P.card("ex-3", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
{tip("<p><b>Study (invented for practice):</b> 247 students aged 14 to 18 in three schools completed an anonymous questionnaire in class, with a teacher in the room. One item asked about daily social media use in four categories (under 1 hour, 1 to 3, 3 to 5, more than 5). A validated 10-item scale measured academic self-efficacy, with statements such as \"I am confident I can complete my schoolwork successfully.\" There was a moderate negative correlation (r = -0.52): students reporting more social media use tended to report lower self-efficacy. The researchers concluded that reducing social media use may improve teenagers' academic self-efficacy.</p>")}
<p><b>Evaluate this study with reference to the concepts of bias and measurement.</b> [6]</p>
<p class="small">Look closely at the final conclusion, the conditions in which the survey was completed, and the types of item used.</p>
{S("S", 7)}
{earns("CRM-06-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "Here are five questionnaire items I wrote. For each, tell me whether it is leading, double-barrelled or unclear, and ask me how I would fix it. Do not fix it for me.",
 "Act as a participant in a semi-structured interview about how students prepare for exams. Give short answers so that I have to practise asking probes.",
 "Ask me to compare a survey and an interview on five aspects, one at a time, and tell me if I have given a similarity or a difference.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA starter", "A questionnaire you write yourself, with at least five items, can be your IA tool (an existing published questionnaire cannot). Draft five items on what students in the UAE value most in a friend, mixing rating scales and one open question, and explain one decision behind each item."],
 ["EE question workshop", "Turn \"Can we trust what people say about themselves?\" into a focused question about social desirability in self-report research, and find studies on both sides."],
 ["HL link", "<b>Technology:</b> do online surveys get more honest answers than paper ones on personal topics? <b>Culture:</b> does a five-point agreement scale mean the same thing in every culture, or do some groups avoid the extremes?"],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>"A survey tells you what people say they do. An interview tells you what people think about what they do. Neither tells you what people actually do."</p>
<p>1. Do you agree? Is what people say and think about their behaviour real psychological data in its own right?</p>
<p>2. Which three differences between surveys and interviews would you choose for a Question 3 answer, and why?</p>
{S("L", 5)}""", "Last check")

open("../../ws-crm-06.html", "w").write(P.render())
print("ok", P.counts)
