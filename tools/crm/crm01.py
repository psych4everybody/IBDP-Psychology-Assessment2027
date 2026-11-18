from lib import Page, checklist, earns, chips, table, slot_list, tip, frame

P = Page("CRM-01", "01", "The Six Concepts",
         "What are the big ideas that frame everything we do in this course?")
S = P.slot

# ---------------- START ----------------
P.topic("start", "The Six Concepts", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will know what makes psychology a science, how the course fits together, and what each of the six concepts asks you to think about. You will also be able to use a concept to examine a real study.</p>
{checklist("CRM-01-goals", [
 "I can explain what psychology studies and why it relies on evidence rather than common sense.",
 "I can describe how concepts, content and contexts fit together in this course.",
 "I can explain each of the six concepts (bias, causality, change, measurement, perspective, responsibility) and give an example of each.",
 "I can explain why perspective and bias are not the same thing.",
 "I can explain a concept in relation to a specific study, using details from that study.",
])}
<p class="progress"></p>
<p class="small">Part of the course: the six concepts. They are not a topic you finish. You will use them in every chapter, in every context, and in most exam answers.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 1 Section C (every essay is built around one concept); Paper 2 Section A Question 2 (explain a concept in relation to your class practical); Paper 2 Section B (discuss an unseen study using two or more concepts); Paper 3 for HL students</p>
{chips(*["bias", "causality", "change", "measurement", "perspective", "responsibility"])}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
<p>Read this personality profile as if it had been written just for you. Then answer the questions.</p>
{tip("<p><i>You want other people to like and respect you, but you are often harder on yourself than you need to be. You have some weaknesses, though you usually keep them under control. Sometimes you wonder whether you made the right choice. You can look calm and confident on the outside while feeling unsure on the inside. You like to think for yourself and you do not accept what people tell you without good reason.</i></p>")}
<p>1. On a scale of 0 (does not describe me at all) to 5 (describes me perfectly), how well does the profile describe you? Then compare your score with two classmates. What do you notice?</p>
{S("W", 2)}
<p>2. The same profile was given to everyone in your class. Why might so many people still feel it describes them?</p>
{S("W", 2)}
<p>3. What would you need to know before deciding that a personality profile really tells you something about you in particular?</p>
{S("W", 2)}""", "Warm-up")

# ---------------- READ ----------------
P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", """<h2>What is psychology?</h2>
<p><b>Psychology</b> is the scientific study of behaviour and mental processes. Behaviour is what people do and say, which others can observe. Mental processes are what goes on inside: memory, attention, perception, emotion, thinking and decision-making. These cannot be seen directly, so psychologists have to find ways to study them through behaviour, through what people report, or through measures of the body and brain.</p>
<p>Psychology counts as a science because it is <b>empirical</b>: claims are tested against evidence that is collected systematically, through observation and research, rather than accepted because they sound right, because they are traditional, or because someone important said so. The aims of psychological research are usually described in four steps: to <b>describe</b> behaviour, to <b>explain</b> it, to <b>predict</b> it and, where it helps people, to <b>change</b> it.</p>
<p>Why not just use common sense? Because common sense often contradicts itself ("birds of a feather flock together", but "opposites attract") and because our intuitions are easily fooled. The warm-up showed one way this happens: a vague, flattering description feels personal even when it is not. Research gives us ways to check our intuitions, and the six concepts in this chapter give us ways to check the research.</p>""", "What is psychology?")

P.card("rd-2", f"""<h2>How the course fits together</h2>
<p>The course has three parts that are meant to be studied together, not one after another.</p>
{table(["Part", "What it is", "Examples"], [
 ["Concepts", "Six big ideas used to examine any topic: bias, causality, change, measurement, perspective and responsibility.", "Is this study biased? Does it show cause and effect? How was memory measured?"],
 ["Content", "The approaches psychologists take (biological, cognitive and sociocultural) and the research methodology they use. Content gives you the terms and theories.", "Neuroplasticity, schema theory, conformity; experiments, interviews, sampling"],
 ["Contexts", "Four real-world areas where the content is applied.", "Health and well-being, human development, human relationships, learning and cognition"],
])}
<p>A simple way to remember it: <b>content</b> is what you know, <b>contexts</b> are where it is used, and <b>concepts</b> are the lenses you look through. A Paper 1 Section C question brings all three together: one context, one area of study from that context, and one concept. For example, a question might ask you to evaluate research on memory through the lens of measurement.</p>
<p>Three rules about concepts are worth knowing from the start:</p>
<ul>
<li><b>Exam questions use only the concept word.</b> A question will say "causality", never a related term such as "reductionism". The related terms in this chapter are there to help your thinking.</li>
<li><b>Any idea can link to any concept, if you explain the link.</b> Reductionism, for example, can be argued as a problem of bias, of causality or of perspective. What earns marks is the explanation of the link.</li>
<li><b>Concepts are not about memorising study details.</b> Studies are useful evidence, and one well-used study is plenty, but the exam rewards how well you think about them, not how many dates and sample sizes you remember.</li>
</ul>""", "How the course fits together")

P.card("rd-3", f"""<h2>Bias</h2>
<p class="small"><b>The question it asks:</b> in what ways might our knowledge of behaviour be distorted?</p>
<p>A <b>bias</b> is a systematic error: something that pushes thinking or findings away from the truth in one particular direction. Compare two faulty kitchen scales. One gives slightly different readings each time you weigh the same bag of rice, sometimes a little high and sometimes a little low; that is <b>random error</b>, and it tends to cancel out over many measurements. The other always reads 200 grams too heavy; that is <b>bias</b>, and weighing the bag a hundred times will not fix it. Bias is dangerous precisely because repeating the research does not remove it.</p>
<p>Bias shows up in three places.</p>
<ul>
<li><b>In research.</b> <i>Researcher bias</i>: the researcher's expectations shape how data are collected or interpreted. <i>Participant bias</i>: participants change their behaviour because they are being studied, for example by guessing the aim (demand characteristics) or giving answers that make them look good (social desirability). <i>Sampling bias</i>: the people studied do not represent the people the conclusion is about. <i>Confirmation bias</i>: noticing evidence that fits what you already believe and overlooking evidence that does not. <i>Publication bias</i>: studies with striking results are more likely to be published than studies that found nothing, so the published picture can look stronger than the truth.</li>
<li><b>In theories.</b> A theory can lean too heavily towards one kind of explanation, for example explaining all behaviour through genes (biological determinism) or through upbringing (environmental determinism), or reducing a complex behaviour to one simple cause (reductionism). Gender and cultural bias can also affect how disorders are diagnosed and counted.</li>
<li><b>In everyday behaviour.</b> People take mental shortcuts (heuristics) when time, information or motivation is short. These shortcuts usually work, but they also produce systematic errors called <b>cognitive biases</b>, such as anchoring on the first number you hear.</li>
</ul>
<p>Researchers use <b>controls</b> to reduce bias: random sampling, keeping the aim hidden until the debrief, having two observers check each other (inter-rater reliability), and reflecting on their own assumptions (reflexivity). Spotting a bias is only the first step. The skill that earns marks is explaining how the bias could change the findings or the conclusion.</p>""", "Bias")

P.card("rd-4", f"""<h2>Causality</h2>
<p class="small"><b>The question it asks:</b> how can we know what causes a behaviour?</p>
<p><b>Causality</b> is the relationship in which one variable produces a change in another. To claim that X causes Y, a researcher needs three things: X and Y must change together; X must come before Y; and other possible causes must be ruled out. The research method designed to do this is the <b>experiment</b>, where the researcher changes one variable (the independent variable), keeps everything else as constant as possible, and measures the effect on another (the dependent variable). You will study experiments in CRM-03.</p>
<p>Much research in psychology cannot do this. It measures two things and finds that they go together, which is a <b>correlation</b>. A correlation alone does not show cause, for two reasons:</p>
<ul>
<li><b>Bidirectional ambiguity:</b> the direction is unclear. Students who sleep more get better marks. Does sleep improve learning, or do students who are on top of their work sleep better because they are less worried?</li>
<li><b>A third variable:</b> something else may cause both. Countries that eat more fish report lower rates of depression, but wealth, climate, diet as a whole and the way depression is diagnosed all differ between those countries too.</li>
</ul>
<p>Human behaviour is also <b>complex</b>. Often there is no single cause but several factors that interact: a gene may raise risk only in a stressful environment. Good answers about causality ask how strong the evidence for a cause is, what has been controlled (for example with a placebo, a double-blind design or a waiting-list group), and whether a cause found in a laboratory would still operate in everyday life. That last point is about <b>internal validity</b> (did the study show what caused what, inside the study?) versus <b>external validity</b> (does the finding hold outside it?).</p>
<p>A note on <b>statistical significance</b>, because it is often misunderstood. A result with p &lt; .05 means that if there were really no effect, results this strong would turn up less than 5% of the time. It does not mean there is a 95% chance the hypothesis is true, and it does not tell you how large or important the effect is.</p>""", "Causality")

P.card("rd-5", f"""<h2>Change</h2>
<p class="small"><b>The question it asks:</b> how and why does behaviour change, and can we change it on purpose?</p>
<p><b>Change</b> is about how behaviour, mental processes and the brain shift over time. It comes in two main kinds in this course.</p>
<ul>
<li><b>Change that happens naturally:</b> development and maturation, such as a child's language growing, the brain reorganising after experience (neuroplasticity), or a person adapting to a new culture.</li>
<li><b>Change that is the result of an intervention:</b> a treatment for a disorder, a programme to prevent a health problem, a strategy to improve memory, or a technique to persuade people.</li>
</ul>
<p>Change can be gradual or sudden, planned or unplanned, lasting or short-lived. The concept also raises one of psychology's oldest debates: how far do we freely choose our behaviour (<b>free will</b>, sometimes called agency), and how far is it shaped by biology and environment (<b>determinism</b>)? Psychologists also study <b>barriers to change</b>, the reasons people keep doing something even when they want to stop.</p>
<p>Studying change needs the right design. A <b>longitudinal</b> study follows the same people over months or years; a <b>repeated measures</b> design tests the same people before and after an intervention. Change can also be measured across whole populations, for example how the <b>prevalence</b> of a health problem rises or falls over time or differs between countries. A useful question for any finding: is this change the result of the intervention, or would it have happened anyway?</p>""", "Change")

P.card("rd-6", f"""<h2>Measurement</h2>
<p class="small"><b>The question it asks:</b> how can we turn complex mental processes into something we can observe and record?</p>
<p>Many things psychologists study, such as intelligence, stress, memory or loneliness, are <b>constructs</b>: ideas that cannot be seen directly. To study them, researchers must <b>operationalise</b> them, which means stating exactly how they will be measured. "Memory" is a construct; "the number of words recalled from a list of 20 after a 30-second delay" is an operationalised variable. Every choice of operationalisation includes some parts of the construct and leaves others out.</p>
<p>Two qualities make a measurement trustworthy:</p>
<ul>
<li><b>Reliability:</b> it gives consistent results, for example when the test is repeated or when two observers score the same behaviour.</li>
<li><b>Validity:</b> it measures what it claims to measure. A test can be reliable without being valid: a scale that is always 200 grams heavy is perfectly consistent and always wrong.</li>
</ul>
<p>Measurements can be <b>direct</b> (counting how often a child shares a toy) or <b>indirect</b> (inferring brain activity from changes in blood flow in a brain scan, or inferring stress from a hormone level). Data can be <b>quantitative</b> (numbers) or <b>qualitative</b> (words and meanings), and they can be self-reported, observed or recorded by instruments. Each kind has strengths and weaknesses, which is why researchers often combine methods, known as <b>triangulation</b>, to check that different measures point the same way. Measurement is not only about numbers: deciding how to code interview transcripts into themes is a measurement decision too.</p>""", "Measurement")

P.card("rd-7", f"""<h2>Perspective</h2>
<p class="small"><b>The question it asks:</b> what different ways are there of explaining the same behaviour?</p>
<p>A <b>perspective</b> is a coherent way of looking at behaviour, built on its own assumptions about what matters and how to study it. The course uses three broad approaches:</p>
{table(["Approach", "What it focuses on", "Typical evidence"], [
 ["Biological", "The brain, nervous system, hormones and genes", "Brain imaging, twin studies, animal research"],
 ["Cognitive", "Mental processes such as memory, thinking and perception", "Experiments on memory and decision-making, cognitive models"],
 ["Sociocultural", "Other people, groups and culture", "Observations, interviews, cross-cultural comparisons"],
])}
<p>No single approach explains behaviour fully on its own. Take a student who becomes very anxious before exams. A biological explanation might point to the body's stress response; a cognitive one to the way the student interprets the exam ("if I fail, everything is ruined"); a sociocultural one to family expectations and comparison with classmates. Each is coherent, each captures something real, and together they give a fuller picture than any one alone.</p>
<p>Perspective also covers different theories and models of the same behaviour, <b>alternative explanations</b> of the same finding, <b>inductive</b> research (starting from the data and building a theory) versus <b>deductive</b> research (starting from a theory and testing it), and <b>emic</b> versus <b>etic</b> approaches: studying a culture from the inside, in its own terms, versus applying the same measures across many cultures to compare them. It also includes the perspectives of Indigenous peoples, whose understandings of mind and well-being may differ from those built into most published research.</p>""", "Perspective")

P.card("rd-8", f"""<h2>Responsibility</h2>
<p class="small"><b>The question it asks:</b> what do psychologists owe to the people they study and to society?</p>
<p>Psychologists study people, and their findings shape treatments, school policies and public opinion. That gives them power, and <b>responsibility</b> is about using it well: during research, when reporting results, and when results are applied.</p>
<p><b>During research</b>, ethical guidelines protect participants: informed consent; the right to withdraw, including withdrawing their data; anonymity and confidentiality; protection from harm; avoiding deception unless it is essential and harmless; and a full debrief afterwards. Researchers weigh costs against benefits: is the knowledge gained worth any discomfort caused? Extra care is needed with children, with research in public places where people are observed without being asked, and with animals, where researchers try to replace animals with alternatives, reduce the numbers used and refine procedures to minimise harm.</p>
<p>Ethics can also <b>affect the results</b>. Asking for informed consent may tell participants enough to change how they behave. The right to withdraw may mean the people who stay are different from those who leave. Anonymity can make people more willing to answer honestly.</p>
<p><b>After the research</b>, responsibility continues: reporting findings honestly, including their uncertainty; thinking about how a finding on a sensitive topic might be used, for example to stigmatise a group; and, where research shows something could help people, sharing it with those who make decisions.</p>""", "Responsibility")

P.card("rd-9", f"""<h2>Perspective is not bias, and concepts connect</h2>
<p>This is one of the most common mistakes in exam answers, so it gets its own section. A <b>perspective</b> is a coherent framework that can be partly right: a biological and a sociocultural explanation of anxiety can both be valid. A <b>bias</b> is a distortion that pushes findings away from the truth. Calling a perspective "biased" because it only looks at one kind of cause confuses the two. The accurate point is usually that relying on one perspective alone can lead to a <i>reductionist</i> explanation, which you can then argue as a limitation.</p>
<p>The concepts also connect, and showing a connection is a sign of strong thinking. Some examples:</p>
<ul>
<li><b>Bias and perspective:</b> a sample drawn from one culture limits how far a finding can claim to show something universal.</li>
<li><b>Measurement and causality:</b> if the measure of the outcome is not valid, an experiment cannot show that the treatment caused a real change.</li>
<li><b>Responsibility and bias:</b> letting participants withdraw is the right thing to do, and it can also leave a biased sample.</li>
<li><b>Change and causality:</b> people improve after a treatment, but would they have improved anyway?</li>
</ul>""", "Perspective is not bias")

P.card("rd-10", f"""<h2>Key study: Forer (1949), the fallacy of personal validation</h2>
{table(None, [
 ["Aim", "To show how readily people accept a vague, general personality description as an accurate account of themselves."],
 ["Participants", "39 students in Bertram Forer's introductory psychology class in the USA."],
 ["Procedure", "Students completed a personality test and were told that each of them would receive a personal description based on their answers. A week later every student was given the same description, made of 13 general statements that Forer had taken largely from a newsstand astrology book. Students rated how well it described them on a scale from 0 (poor) to 5 (perfect). Only after the ratings were collected did Forer reveal that the descriptions were identical, and he used this to discuss the problem with the class."],
 ["Findings", "The mean accuracy rating was 4.26 out of 5. Most students gave a 4 or 5, and nobody gave lower than 2."],
 ["Conclusion", "People tend to accept vague, generally positive statements as personally meaningful, especially when they believe the statements come from an expert or a test about them. Forer called this the fallacy of personal validation. It is now usually called the Barnum effect, a name suggested by Paul Meehl in 1956."],
 ["What happened next", "The effect has been found many times since, which matters for anyone who uses personality tests: a client saying a description \"fits\" is not evidence that the test works."],
 ["Use it for", "Practising concepts (this chapter); Paper 2 Section B (evaluating a study with concepts); a link to cognitive biases in CL-05."],
 ["Evaluate it with", "<b>Bias:</b> participants wanted the result to be about them, and they rated a description given by their own teacher, which may have raised scores. <b>Measurement:</b> a single 0 to 5 rating of \"accuracy\" is a simple measure of a complex judgement. <b>Responsibility:</b> students were deceived; the deception was mild and was explained in the same lesson."],
])}""", "Key study: Forer (1949)")

P.card("rd-11", f"""<h2>Real life: concepts in the headlines</h2>
{tip('''<p>Three claims you might see this week. Each is invented for practice.</p>
<ul>
<li>A news site: <i>"Students who own more books at home have bigger vocabularies, so buying books makes children smarter."</i></li>
<li>An app advert in the UAE: <i>"9 out of 10 users say our focus app improved their grades."</i></li>
<li>A social media post: <i>"This personality quiz knew me better than my friends do. It must be scientific."</i></li>
</ul>''', "Real life")}
<p>During the reading: for each claim, which concept is most useful for questioning it, and what one question would you ask?</p>
{S("D", 3)}""", "Real life")

P.card("rd-12", f"""<h2>The six concepts at a glance</h2>
{table(["Concept", "The question it asks", "Ideas linked to it"], [
 ["Bias", "How might our knowledge be distorted?", "Researcher, participant, sampling, confirmation and publication bias; gender and cultural bias; determinism; cognitive biases; reflexivity"],
 ["Causality", "How can we know what causes a behaviour?", "Correlation vs causation; bidirectional ambiguity; controls; internal and external validity; significance; complexity"],
 ["Change", "How does behaviour change, and can we change it?", "Development and maturation; interventions and their effectiveness; prevalence; longitudinal designs; free will vs determinism; barriers to change"],
 ["Measurement", "How do we observe and record what we cannot see?", "Constructs and operationalisation; reliability and validity; direct and indirect measures; types of data; triangulation"],
 ["Perspective", "What other ways are there to explain this?", "Biological, cognitive and sociocultural approaches; theories and models; emic and etic; inductive and deductive; alternative explanations"],
 ["Responsibility", "What do psychologists owe participants and society?", "Consent, withdrawal, anonymity, harm, deception, debrief; cost-benefit; animals; children; stigma; reporting findings"],
])}
<p class="small">These lists are guidance, not a checklist to memorise. You can link a concept to any idea, as long as you explain the link.</p>""", "The six concepts at a glance")

# ---------------- CHECK ----------------
P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. What makes psychology a science rather than common sense?</p>
{S("C", 2)}
<p>2. Explain the difference between random error and bias, using an example of your own.</p>
{S("C", 2)}
<p>3. Give two reasons why a correlation does not show that one variable causes the other.</p>
{S("C", 2)}
<p>4. What does it mean to operationalise a variable? Operationalise "stress" in one sentence.</p>
{S("C", 2)}
<p>5. Why is it a mistake to call a perspective a bias?</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Concepts in action</h2>
<p>Each scenario below connects most directly to one concept. For each, name the concept and explain the link in one sentence. Use a detail from the scenario, not a definition.</p>
<ol>
<li>A sports psychologist tests whether motivational coaching improves performance, using players from the team he coaches. Two coached players score below average, so he leaves their results out because he thinks they were unwell on the day.</li>
<li>A survey finds that countries where people eat more fish report lower rates of depression. A magazine headline says: "Eating fish prevents depression."</li>
<li>A researcher records the vocabulary and grammar of the same thirty children every year from age two to age twelve.</li>
<li>Two teams study well-being in teenagers. One uses a 20-item questionnaire; the other counts each student's close friendships. They reach very different conclusions about which students are doing well.</li>
<li>A student with severe exam anxiety is seen by two specialists. One focuses on the body's stress response; the other on how the student thinks about failure and on family expectations. Neither thinks the other's account is complete.</li>
<li>Volunteers in a study are asked to describe a road accident they once witnessed. Two become upset and ask to stop. The researcher reminds them that they agreed to take part and asks them to carry on.</li>
</ol>
{slot_list([f"Scenario {i}: concept, and the link in one sentence" for i in range(1, 7)])}
{S("C", 6)}
<p>Now choose one scenario and explain, in three or four sentences, how the concept applies. Refer to specific details from the scenario.</p>
{S("C", 4)}""", "Concepts in action")

# ---------------- EXAM ----------------
P.topic("exam", "Exam practice", "Paper 2 practice: explaining a concept in relation to a study.")
P.card("ex-1", """<p class="small">In the exam, Paper 2 Section A Question 2 asks you to explain a concept in relation to <b>your own class practical</b>. Here you practise the same move on a published study, Forer (1949). The skill is identical: say what the concept means in research, then tie it to specific features of the study.</p>""")
P.card("ex-2", f"""<h2>Paper 2, Section A, Question 2 style [4 marks]</h2>
<p><b>Explain the concept of bias in relation to Forer (1949).</b> [4]</p>
<p class="small">There is more than one kind of bias in this study. Choose the one you can explain most clearly and use details from the key study.</p>
{slot_list(["Bias, defined in one sentence", "The kind of bias, and the feature of the study that shows it", "How it could have affected the ratings", "What this means for the conclusion"])}
{S("Q2", 4)}
{S("Q2", 5)}
{earns("CRM-01-Q2", ["I explain what the concept means in research, accurately.", "I link it to specific features of the study, not to research in general.", "I explain the effect: how it helped or limited what the study could show."])}""", "Paper 2, Section A, Question 2 style [4 marks]")
P.card("ex-3", f"""<h2>Now try a second concept [4 marks]</h2>
<p><b>Explain the concept of responsibility in relation to Forer (1949).</b> [4]</p>
<p class="small">Think about what students were told, what they were not told, and what happened afterwards. Would the study be allowed today?</p>
{S("Q2", 5)}
{earns("CRM-01-Q2b", ["I explain what the concept means in research, accurately.", "I link it to specific features of the study, not to research in general.", "I explain the effect: how it helped or limited what the study could show."])}""", "A second concept [4 marks]")

# ---------------- MORE ----------------
P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", """<div class="sec-label">Using AI to learn</div><h2>Make AI question you, not write for you</h2>
<p>Try one of these after you have attempted the chapter yourself:</p>
<ul><li><i>"Give me six short descriptions of psychology studies, one at a time. For each, ask me which of the six IB Psychology concepts fits best and why. Wait for my answer, then tell me if another concept could also work."</i></li>
<li><i>"I will explain the difference between perspective and bias. Ask me two follow-up questions that test whether I really understand it. Do not give me the answer."</i></li>
<li><i>"Here is my paragraph on bias in Forer (1949). Tell me which sentences use details from the study and which are general. Do not rewrite it."</i></li></ul>
<p><b>Remember:</b> check every study an AI tool names against this chapter or your textbook, because these tools sometimes invent studies and figures. Do not use AI to draft or mark your IA or EE.</p>""", "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA link", "Your IA proposal will ask you to think about how your own background and assumptions could shape the way you design a study. Start now: write down one assumption you hold about teenagers and phones, and how it could sneak into the questions you would ask."],
 ["EE question workshop", "A psychology EE uses published research only. Turn \"Do personality tests work?\" into a focused question, for example \"To what extent can self-reported accuracy ratings show that a personality test is valid?\" Find one study that supports a test and one that challenges it."],
 ["CAS idea", "With a teacher, set up a \"Check the claim\" board in your school where students post an advert or headline and others label the concept that best tests it. CAS cannot be part of your course requirements, so treat this as an idea to take beyond class."],
 ["HL link", "<b>Technology:</b> online personality quizzes and horoscope apps reach millions of people. What would Forer predict about how users rate them, and what would you need to measure to test that? <b>Culture:</b> would people in every culture rate a vague, individual-focused profile as highly, or does it suit some cultures more than others?"],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>"Psychology is just common sense in scientific language. We already know stress affects performance and children need secure relationships. Why do we need research?"</p>
<p>1. How would you answer this claim? Use at least one of the six concepts.</p>
{S("L", 4)}""", "Last check")

open("../../ws-crm-01.html", "w").write(P.render())
print("ok", P.counts)
