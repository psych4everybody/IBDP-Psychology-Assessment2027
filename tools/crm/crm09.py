from lib import Page, checklist, earns, chips, table, slot_list, tip, frame
from common import EARN_S, ai_card

P = Page("CRM-09", "09", "Data Analysis and Interpretation",
         "What do we do with the data we collect, and what does it actually tell us?")
S = P.slot

P.topic("start", "Data Analysis and Interpretation", P.sub)
P.card("st-goals", f"""<div class="sec-label">Goals</div>
<h2>By the end of this chapter</h2>
<p class="lede">You will be able to summarise numerical data, choose and read the right graph, explain what statistical significance does and does not mean, carry out the first stages of a thematic analysis, and keep describing data separate from interpreting it.</p>
{checklist("CRM-09-goals", [
 "I can calculate and explain the mean, median, mode, range and standard deviation, and choose the right one for skewed data.",
 "I can choose and read bar graphs, histograms, box plots, line graphs, scatterplots and frequency tables.",
 "I can recognise normal and skewed distributions and outliers, and explain what they mean for the statistics.",
 "I can explain what p &lt; .05 means and what it does not mean, and the difference between statistical and practical significance.",
 "I can explain a correlation coefficient.",
 "I can describe the phases of thematic analysis and code a small set of responses.",
 "I can keep describing data separate from interpreting it.",
])}
<p class="progress"></p>
<p class="small">Part of the course: research methodology (data analysis and interpretation). SL and HL students both study this, but it is assessed only at HL, in Paper 3. Everyone needs it for the IA and for evaluating studies.</p>
<p class="small"><b>Where this appears in the exams:</b> Paper 3 for HL students (Question 1, interpreting graphs; Question 2, data analysis; Question 3, qualitative research considerations); Paper 2 Section B (reading a study's results); the IA (Criterion D, potential findings)</p>
{chips("measurement", "causality", "bias")}""", "Goals")

P.card("wu-1", f"""<div class="sec-label">Warm-up</div><h2>Before you read</h2>
{tip("<p><b>\"Students who eat breakfast score 23% higher!\"</b> A study of 2,500 secondary students found that those who reported eating breakfast every school day scored on average 23% higher on standardised tests than those who usually skipped it. The difference was statistically significant (p &lt; .05). The lead researcher said: \"The evidence is clear. Schools should provide breakfast to every student.\"</p>")}
<p>1. What does the 23% difference tell us, and what does it not tell us?</p>
{S("W", 2)}
<p>2. Does a statistically significant result show that breakfast causes better scores?</p>
{S("W", 2)}
<p>3. Rewrite the researcher's quote so that it matches what the data can support.</p>
{S("W", 2)}""", "Warm-up")

P.topic("read", "Read", "Read this before the lesson.")
P.card("rd-1", f"""<h2>Descriptive statistics: summarising numbers</h2>
<p><b>Descriptive statistics</b> summarise a set of scores. They describe the data you have; they do not test anything.</p>
{table(["Statistic", "What it is", "When to use it"], [
 ["Mean", "Add all the scores and divide by how many there are", "Most informative when data are roughly symmetrical; pulled up or down by extreme scores"],
 ["Median", "The middle score when scores are in order (with an even number, halfway between the two middle scores)", "Better than the mean when data are skewed or contain outliers"],
 ["Mode", "The most common score or category", "The only average that works for categories, such as the most popular answer to a survey item"],
 ["Range", "Highest score minus lowest score", "A quick measure of spread, but one extreme score can change it a lot"],
 ["Standard deviation (SD)", "Roughly, the typical distance of scores from the mean", "A small SD means scores cluster near the mean; a large SD means they are spread out"],
])}
<p>Worked example: the scores 12, 14, 14, 16 and 19 have a mean of 15, a median of 14, a mode of 14 and a range of 7. Reporting a mean without any measure of spread hides how much people differed, which is why good results sections give "mean = 15, SD = 2.5" and not just the mean.</p>""", "Descriptive statistics")

P.card("rd-2", f"""<h2>Choosing and reading graphs</h2>
{table(["Graph or table", "Use it for", "Watch out for"], [
 ["Frequency table", "How many people fall in each category or score", "Compare percentages, not raw counts, when groups are different sizes"],
 ["Bar graph", "Comparing separate categories or conditions, such as mean recall in two conditions; bars do not touch", "Bars showing means should have error bars or SDs, or you cannot judge the overlap"],
 ["Histogram", "The distribution of continuous scores, in equal-width bands; bars touch", "The shape tells you about skew and outliers"],
 ["Box and whisker plot", "The median, the middle 50% of scores (the box, from the lower to the upper quartile) and the spread, with outliers shown separately", "A box plot can hide a distribution with two peaks"],
 ["Line graph", "Change over time or across ordered steps, such as recall after 0, 10 and 30 minutes", "Do not join points for unordered categories: the line implies a continuum"],
 ["Scatterplot", "The relationship between two co-variables; each dot is one participant", "In a correlational study there is no IV or DV, just two variables"],
])}
<p>When you read any graph, check the axis labels and the scale first. An axis that does not start at zero can make a small difference look dramatic.</p>""", "Choosing and reading graphs")

P.card("rd-3", """<h2>Distributions and outliers</h2>
<p>A <b>distribution</b> is the shape the scores make when plotted.</p>
<ul>
<li>In a <b>normal distribution</b>, scores cluster in the middle and tail off evenly on both sides, in a bell shape. The mean, median and mode are roughly the same.</li>
<li>In a <b>positively skewed</b> distribution, most scores are low and a long tail stretches to the right. This often happens when a task is too hard (a floor effect). The mean is usually pulled above the median.</li>
<li>In a <b>negatively skewed</b> distribution, most scores are high and the tail stretches to the left, often because a task is too easy (a ceiling effect). The mean is usually pulled below the median.</li>
</ul>
<p>A memory aid: <i>the tail tells the tale</i>. The skew is named after the side the tail is on. A skewed distribution is not "bad data"; it tells you something about the task or the participants, and it tells you to report the median.</p>
<p>An <b>outlier</b> is a score far from the rest. It might be genuine, or it might come from a misunderstood instruction or a recording error. Outliers pull the mean and inflate the SD. One common rule treats a score as an outlier if it lies more than 1.5 times the interquartile range beyond the box. Never remove an outlier just because it is inconvenient: if a score is excluded, the reason must be stated and the decision reported.</p>""", "Distributions and outliers")

P.card("rd-4", """<h2>Inferential statistics and significance</h2>
<p><b>Inferential statistics</b> test whether a difference or relationship found in a sample is likely to reflect a real pattern, or could easily have arisen by chance. The test starts from the <b>null hypothesis</b> (no effect) and produces a <b>p-value</b>.</p>
<p>A p-value is the probability of getting a result at least as extreme as the one found <b>if the null hypothesis were true</b>. In psychology, results with p &lt; .05 are usually called <b>statistically significant</b>: if there were really no effect, results this strong would turn up less than 5% of the time.</p>
<p>Three things significance does <b>not</b> tell you:</p>
<ul>
<li><b>That the IV caused the result.</b> Significance in a correlational study, or in a poorly controlled experiment, does not show cause.</li>
<li><b>That the effect is large or important.</b> With 10,000 participants, a difference of 0.3 points on a 100-point test can be significant but educationally meaningless. The size of an effect is a separate question from whether it is significant.</li>
<li><b>That the result is certain.</b> A <b>Type I error</b> is finding a significant result when there is no real effect; a <b>Type II error</b> is missing a real effect, which is more likely with small samples.</li>
</ul>
<p>Which test is used depends on the design and the data. You do not need to calculate tests by hand, but HL students should be able to read a reported result: for some tests, such as the Mann-Whitney U, a result is significant when the calculated value is <i>smaller</i> than the critical value, so always check the rule for the test.</p>
<p>A <b>correlation coefficient</b> (r) from -1 to +1 gives the direction and strength of a straight-line relationship between two co-variables (CRM-07). It cannot detect curved relationships, and it never shows cause on its own.</p>""", "Inferential statistics and significance")

P.card("rd-5", f"""<h2>Thematic analysis: analysing words</h2>
<p><b>Thematic analysis</b> finds patterns of meaning in qualitative data such as interview transcripts, focus group discussions, open survey answers or diaries, and groups them into <b>themes</b> that answer the research question. A widely used version, set out by Braun and Clarke (2006), has six phases:</p>
<ol>
<li><b>Familiarisation:</b> read and re-read all the data, noting first impressions.</li>
<li><b>Coding:</b> attach short labels (codes) to meaningful pieces of text. "I break big tasks into smaller steps" might be coded "breaking tasks down".</li>
<li><b>Searching for themes:</b> group related codes into possible themes, such as "planning as a way of coping".</li>
<li><b>Reviewing themes:</b> check that each theme fits the coded data and the whole data set, and that themes are distinct.</li>
<li><b>Defining and naming themes:</b> say clearly what each theme captures.</li>
<li><b>Writing up:</b> report each theme with short quotes as evidence.</li>
</ol>
<p>Themes are built by the researcher, not simply found, so two researchers may produce different themes from the same data. This is why credibility, reflexivity and transparency matter (CRM-08). Some approaches have a second researcher code part of the data to check agreement; others treat the researcher's interpretation as part of the method and focus instead on reflexivity.</p>""", "Thematic analysis")

P.card("rd-6", f"""<h2>Describe first, then interpret</h2>
<p>These are two different moves, in the IA and in the exam.</p>
{table(["", "Describing", "Interpreting"], [
 ["What it does", "States what the data show, with numbers and patterns", "Explains what the data mean, in relation to the research question and theory"],
 ["Example", "\"Mean recall was higher in the concrete condition (7.2) than in the abstract condition (4.5).\"", "\"This fits dual coding theory, which predicts that concrete words can be stored as images as well as words.\""],
 ["Common mistake", "Adding \"because...\" too early", "Claiming more than the design allows, such as \"proves\" or \"always\""],
])}
<p>Paper 3 Question 2 rewards exactly this: analyse the data accurately, then draw a conclusion that stays within what the data and the design can support.</p>""", "Describe first, then interpret")

P.card("rd-7", f"""<h2>Real life: numbers in the news</h2>
{tip('''<ul>
<li><b>"Average" salaries.</b> A few very high earners pull the mean salary up, which is why the median is a fairer picture of a typical worker.</li>
<li><b>Exam results.</b> A school reports that its mean grade rose. Without the spread, you cannot tell whether most students improved or a few improved a lot.</li>
<li><b>Graphs on social media.</b> A chart with the y-axis starting at 95% can make a 2% change look huge.</li>
</ul>''', "Real life")}
<p>During the reading: choose one example and explain which statistic or graph feature you would check, and why.</p>
{S("D", 2)}""", "Real life")

P.card("rd-8", f"""<h2>The concepts in this chapter</h2>
{table(["Concept", "How it applies"], [
 ["Measurement", "Choosing the right average, spread and graph is a measurement decision. Skew, outliers and missing SDs change what the numbers can tell you."],
 ["Causality", "Statistical significance is not causation. Only the design (manipulation, control, random allocation) can support a causal claim."],
 ["Bias", "Removing inconvenient outliers, reporting only significant results, or choosing a misleading graph can distort findings. Themes in qualitative analysis can reflect the researcher's expectations."],
 ["Responsibility", "Reporting results honestly, including null results and uncertainty, is part of a researcher's responsibility to the public."],
])}""", "The concepts in this chapter")

P.topic("check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.")
P.card("ck-1", f"""<div class="sec-label">Without looking back</div><h2>Check yourself</h2>
<p>1. For the scores 3, 4, 4, 5, 6 and 20, calculate the mean and the median. Which better describes a typical score, and why?</p>
{S("C", 2)}
<p>2. Which graph would you use for (a) mean recall in two conditions; (b) recall measured after 1, 5 and 20 minutes; (c) the link between hours of sleep and test score?</p>
{S("C", 2)}
<p>3. Most students scored 9 or 10 out of 10 on a test. What shape is the distribution, and what might explain it?</p>
{S("C", 2)}
<p>4. Explain in plain words what p &lt; .05 means, and give two things it does not tell you.</p>
{S("C", 2)}
<p>5. Name the six phases of thematic analysis in order.</p>
{S("C", 2)}""", "Check yourself")

P.card("ck-2", f"""<h2>Practice data: word type and memory</h2>
<p>Use your class results from the practice study in CRM-03. If you do not have them, use these sample results (scores out of 10).</p>
{table(["Condition", "Scores", "Mean", "Median", "Range"], [
 ["Concrete words (n = 10)", "8, 7, 9, 6, 7, 8, 5, 7, 9, 6", "7.2", "7", "4"],
 ["Abstract words (n = 10)", "5, 4, 6, 3, 5, 7, 4, 5, 2, 4", "4.5", "4.5", "5"],
])}
<p>1. Which condition had higher recall, and by how much? Compare the spread of the two conditions.</p>
{S("C", 2)}
<p>2. Describe what a bar graph of these results would look like: label both axes and compare the bars.</p>
{S("C", 2)}
<p>3. A student writes: "This proves concrete words are always easier to remember." Give two problems with this conclusion and write a better version.</p>
{S("C", 3)}
<p>4. Write a short results paragraph for the study: give the key numbers and describe the pattern. Do not explain why it happened.</p>
{S("C", 4)}""", "Practice data")

P.card("ck-3", f"""<h2>Practice: code and theme</h2>
<p>Five students answered the open question: <i>"Describe one strategy you use to manage academic pressure."</i></p>
<ol>
<li>"I break big assignments into smaller steps and do them one at a time. Starting is the hardest part."</li>
<li>"I talk to a close friend or someone in my family about what is worrying me. Saying it out loud makes it feel smaller."</li>
<li>"I go for a walk or play football when I feel overwhelmed. Moving clears my head."</li>
<li>"I make a detailed to-do list and tick things off. Seeing my progress makes me less anxious."</li>
<li>"I remind myself I have prepared as well as I can, and that one exam does not decide my worth."</li>
</ol>
{slot_list(["Codes for responses 1 to 5", "Theme 1: name, responses, and why they belong together", "Theme 2: name, responses, and why they belong together", "Theme 3 (if any)"])}
{S("C", 5)}
<p>Compare with a classmate. Did you reach the same themes? What does that tell you about thematic analysis?</p>
{S("C", 2)}""", "Practice: code and theme")

P.topic("exam", "Exam practice", "Paper 2 Section B practice on a study's results.")
P.card("ex-1", f"""<h2>Paper 2, Section B warm-up [6 marks]</h2>
{tip('''<p><b>Study (invented for practice):</b> 40 Grade 10 students were randomly allocated to a mindfulness group (n = 20) or a control group (n = 20). The mindfulness group attended a one-hour session each week for six weeks; the control group had no sessions. Anxiety was measured before and after with a validated 20-item scale (0 to 80; higher means more anxious).</p>
<ul><li>Mindfulness group: before, mean 38.4 (SD 6.2); after, mean 31.7 (SD 7.1). A drop of 6.7 points.</li>
<li>Control group: before, mean 37.9 (SD 5.8); after, mean 36.1 (SD 6.3). A drop of 1.8 points.</li></ul>
<p>The difference between the groups after six weeks was statistically significant (p = .04). The researchers concluded that the programme is an effective treatment for anxiety in teenagers and recommended it for every Grade 10 class.</p>''')}
<p><b>Evaluate this study with reference to the concepts of measurement and causality.</b> [6]</p>
<p class="small">Look at the standard deviations, the size of the effect and what the control group did, before you begin.</p>
{S("S", 7)}
{earns("CRM-09-S", EARN_S, "Our plain-language guide. A practice rubric is in the self-check box on your answer sheet.")}""", "Paper 2, Section B warm-up [6 marks]")
P.card("ex-2", """<div class="callout c-exam"><strong class="tag">HL students</strong><p>Paper 3 uses these skills directly: Question 1 asks for one issue that limits how the data can be interpreted, and Question 2 asks you to analyse the data and draw a conclusion. Practise with the full sets on the <a href="paper3.html">Paper 3 page</a>.</p></div>""")

P.topic("more", "Beyond the chapter", "AI prompts, optional extensions and a last check.")
P.card("mo-ai", ai_card([
 "Give me a small set of invented scores with one outlier. Ask me to calculate the mean and median and say which is more representative. Do not give me the answer first.",
 "Show me a described graph with a misleading feature. Ask me to find the problem.",
 "Here are my codes and themes for five interview answers. Ask me two questions that test whether my themes really fit the data. Do not suggest new themes.",
]), "Using AI to learn")
P.card("mo-b-1", f"""<div class="sec-label">Optional</div><h2>Beyond the chapter</h2>
{table(["For", "Try this"], [
 ["IA link", "Criterion D asks you to discuss potential findings, including the possibility of no difference or no relationship. For an imagined study on sleep and memory, write one sentence on what each possible result would mean."],
 ["EE question workshop", "Choose a published study and read its results section. Which statistics are reported, and does the discussion claim more than the results show?"],
 ["HL link", "Work through one Paper 3 set and, for Question 2, write the description and the conclusion in two separate sentences."],
])}""", "Beyond the chapter")
P.card("mo-l-1", f"""<div class="sec-label">Five minutes</div><h2>Last check</h2>
<p>A school wants to know whether its new study-skills programme works. Teacher A wants to compare grades before and after: "Numbers don't lie." Teacher B wants to interview students: "Grades don't show what they actually learned."</p>
<p>1. What might grades fail to capture? What risk does the interview approach bring?</p>
<p>2. Suggest a plan that combines both. What is combining methods like this called?</p>
{S("L", 5)}""", "Last check")

open("../../ws-crm-09.html", "w").write(P.render())
print("ok", P.counts)
