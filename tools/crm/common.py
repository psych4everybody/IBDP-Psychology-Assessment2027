EARN_S = [
    "I apply each concept to specific features of the study, not to research in general.",
    "I explain the consequence of each point: what it means for the conclusion the study can draw.",
    "I use details from the study as evidence, and my sentences pass the swap test.",
    "I cover both concepts, and develop each one rather than only naming it.",
]

PRACTICAL_CH = {"experiment": "CL-11", "observation": "HD-09", "interview": "HW-11", "survey": "the Paper 2 page"}


def practice_note(method, chapter):
    where = f'<a href="ws-{chapter.lower()}.html">{chapter}</a>' if chapter.startswith(("CL", "HD", "HW")) else '<a href="paper2.html#pr-sur">the Paper 2 page</a>'
    return (f'<div class="callout c-scope"><strong class="tag">Practice study</strong><p>This is a short practice study to learn the method. '
            f'It is not one of your class practicals for Paper 2. Your class practical for the {method} is in {where}.</p></div>')


def ai_card(prompts):
    lis = "".join(f'<li><i>"{p}"</i></li>' for p in prompts)
    return ('<div class="sec-label">Using AI to learn</div><h2>Make AI question you, not write for you</h2>'
            '<p>Try one of these after you have attempted the chapter yourself:</p>'
            f'<ul>{lis}</ul>'
            '<p><b>Remember:</b> check every study an AI tool names against this chapter or your textbook, because these tools sometimes invent studies and figures. '
            'Never paste in your class data or anyone\'s name, and do not use AI to draft or mark your IA or EE.</p>')
