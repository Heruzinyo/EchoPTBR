# Metaphor (revised)
# by Zeke

label sidestory_metaphor:

stop music fadeout 3.0
scene bg black
with slow_dissolve

play background "warehouse.ogg" fadein 10
$ renpy.pause(1, hard=True)
call sidestory_title("September 2014") from _call_sidestory_title_2
pause
call sidestory_title("September 2014", end=True) from _call_sidestory_title_3

scene bg warehouseint with medium_dis


show Flynn Annoyed at center
"Scales glistening with perspiration, seen through his open button-down shirt, Flynn hefts some boxes down the roller conveyor."
"The gila briskly walks over to his pallet jack, pumping it vigorously."
"He drags the stacked-up pallet of fifteen packs of twenty-four count spring water bottles across the stockroom to the truck's trailer."
"Dumping the pallet in, he drags the jack back out, haphazardly abandoning it mid-walk as he gets to the clerical counter."
show Flynn with dis
"He picks up a clipboard, checking off the work he just did, examining the list intently."
"His tail whips back and forth, the orange splotch patterns looking metallic in the sparse, incandescent light."
"He's been working overnights at this distribution center for nearly eight years, and for some reason, he hasn't grown numb to it."
"Flynn plops the clipboard onto the counter, patting his pockets with his scaled claws, and pulls out a pack of cigarettes and a lighter."
"Sean, an armadillo, sees him walking toward the side exit."
se "\"Where do you think you're going?\""
f "\"Taking my break.\""
"Sean rubs his face with both paws."
se "\"Okay. You're really doing this tonight? You know we still got four trailers left to fill, right?\""
"Flynn pops a cigarette between his lips."
f "\"Yeah, and we still got five hours in the fuckin' shift. I'll be back.\""
se "\"You're shift lead.\""
f "\"You know where to find me.\""

scene bg warehouseext with {"master": Fade(0.5, 0.1, 0.3)}
show nightoverlay
show Flynn at left behind nightoverlay

play background2 "parkinglotnocarts.ogg" fadein 5
stop background fadeout 8


"Flynn leans against the building, unlit cigarette in his mouth, fidgeting with the lighter."
"It sparks, over and over again, never igniting."
"He sighs, slipping the lighter back into his pocket and switching it out with his phone."
$ vol("loop", 0.5)
play loop "engine.ogg" fadein 3
"He scrolls through a few posts on social media, checking his messages, staring idly at his homescreen."
$ vol("loop", 1, 3)
"He perks up at some distant revving."
"He picks out the familiar pickup truck from across the parking lot, greeting it as it pulls up."
stop loop fadeout 3
show Flynn:
    ease 0.6 xalign 0.1
f "\"About time. Were you too busy fapping at the moon?\""
show Leo behind nightoverlay with medium_dis:
    xalign 0.95
    yalign 1.0
l "\"You'd like that.\""
l "\"You're just lucky I happened to be up, otherwise you'd have no one to talk shit to.\""
show Flynn Teasing1 with dis
"Flynn chuckles."
show Leo Neutral with dis
"Leo nods his head towards the gila's snout."
l "\"Thought you don't smoke anymore?\""
show Flynn Surprised with dis
"Flynn takes the cigarette out of his mouth."
show Flynn with dis
f "\"Ah. Yeah, I don't.\""
show Leo Questioning with dis
l "\"...So what, you just like chewin' on them?\""
"Flynn clears his throat."
f "\"Uh... Yeah, actually.\""
l "\"...Alright, man. It's great if you quit, but you know I don't care what you do, right?\""
show Flynn Annoyed with dis
f "\"No-. Aw, for-.\""
show Flynn with dis
"He lets out a breath."
show Flynn Sheepish with dis
f "\"I'm serious, I quit. I don't light them.\""
f "\"It's like... you keep the thing that kills you between your teeth, or whatever. It's from a movie.\""
show Leo with dis
l "\"...That's really fucking cheesy, man.\""
show Flynn with dis
"Flynn pockets the cigarette and shrugs."
f "\"Yeah. I dunno, I guess I just liked it.\""
"Leo rolls his eyes, letting out a sighing laugh. He puts his paws behind his head and leans back against the building next to Flynn, looking up at the full moon."
"He reaches over, running his paw softly over the gila's head spines."
show Flynn Happy with dis
"The reptile closes his eyes for a moment, humming at the touch."
"He looks over the glinting piece of silver on the wolf's wrist, shining in the moonlight."
"Leo looks too, their eyes locking briefly."
show Flynn Teasing1 with dis
"Flynn snickers."
f "\"Your eyes are weird as hell.\""
f "\"You say they're brown, but they always look red in the light.\""
l "\"Ha. Yeah, I've been told that before.\""
"Leo pulls his paw back."
f "\"Tsk. Why'd you stop? You know I like having my spines petted.\""
show Leo Surprised with dis
l "\"Oh, uh, my bad?\""
f "\"I'm just messing with you.\""
show Leo with dis
l "\"You're in a really good mood.\""
show Flynn Happy with dis
f "\"Heh. Yeah, uh, just touch-starved, I guess.\""
show Leo Wry with dis
l "\"Aw. You need me that bad, huh? You want to make cuddles at work a regular thing?\""
show Flynn Teasing1 with dis
f "\"Settle down. I can get better tail than you whenever I want.\""
show Leo with dis
l "\"Fuck you.\""
f "\"Name the time and place.\""
"They laugh for a while."
"They fall into a comfortable silence, listening to the sounds, looking at the sky."
show Flynn with medium_dis
f "\"So.\""
f "\"He's graduating in a about a year now, right?\""
f "\"We're supposed to be having some sort of reunion?\""
"Leo leans back against the building."
l "\"Mhm! Jenna and Teej, too.\""
l "\"Exciting, right? We'll be a crew again, just like back then.\""
f "\"Sure.\""
"Flynn takes the cigarette back out and rolls it around in his fingers for a bit before returning it to his mouth."
show Leo Neutral with dis
l "\"You don't seem all that excited.\""
"Flynn keeps it in his mouth as he speaks."
f "\"We've had separate lives these past few years, Leo.\""
f "\"And a lot has happened, too, some of it... well, you know. Some of it's fucked.\""
f "\"Just don't be surprised if it's not the same.\""
show Leo Depressed with dis
"Leo sighs."
l "\"Maybe.\""
l "\"Either way, though. It'll at least be nice to see everyone again.\""
f "\"For sure.\""
show Flynn Depressed with medium_dis
"Flynn takes the empty lighter back out."
"He strikes it once, twice, like the many times he has before, when he was feeling nervous, or just needed something to do with his hands."
"He watches the sparks dance and die, searching desperately for gas, never finding any."
"He lifts the cigarette out of his mouth, eyes falling away from the wolf."
"He inhales."
f "\"And I need to know where we stand, Leo.\""
f "\"I don't wanna get caught in the middle of that shit again. None of us do.\""
"The red wolf's shoulders ease down as he lets out a ragged sigh."
"He runs a paw up his snout, rubbing his eyes with his finger and thumb, then he looks back at the towering reptile."
show Leo Neutral with dis
l "\"I love you and Chase as {i}friends.{/i} Very good friends.\""
show Flynn with dis
l "\"That's good enough for me.\""
"Flynn studies the determined look on Leo's face."
"He puts the cigarette back into his mouth."
"When he speaks again, it's level, almost monotone."
f "\"I guess that's okay."
f "\"If that's all you want.\""
l "\"What do you mean?\""
"Flynn shrugs."
f "\"Nothing.\""

$ stop_all_audio(reset=True)
scene bg black
$ renpy.pause(2.5, hard=True)
$ renpy.end_replay()

# # Metaphor (original)
# # by Zeke
#
# September 2014
#
# Scales glistening with perspiration, seen through his open button down shirt, Flynn hefts some boxes down the roller conveyor. The gila reptile then briskly walks over to his pallet jack, pumping it vigorously before dragging the stacked up pallet of fifteen packs of twenty-four count spring water bottles across the stockroom to the truck’s trailer. He dumps the pallet in, then drags the pallet jack out, haphazardly abandoning it mid walk as he gets to the clerical counter under the incandescent bulbs. Flynn picks up a clipboard, checking off the stock he just put on the trailer, going over the list intently. His tail flicks to and fro, the orange splotch patterns looking metallic in the sparse light. He’d been working overnights at this distribution center for nearly eight years, and for some reason hadn’t grown numb to it. Like most things, he normally would. After a while Flynn would stop caring so much about something so routine, and either stop putting so much effort into it, or
# stop doing it altogether. “In fact…” Flynn plops down his clipboard onto the counter, patting his pockets with his scaled claws. He reaches into either side pocket, pulling out a full pack of worn out cigarettes from one pocket, and a zippo lighter from the other. “…Time for a break”, Flynn says under his breath, then walks toward the side exit. Sean, an armadillo, sees him. He sets down a box, walking toward the reptile, “Hey Flynn, where you think you’re going?”
#
# “I’m on break. I’ll be back… Whenever”
#
# Sean rubs his face with both paws, sighing heavily, “Okay; You’re really doing this tonight? You know we still got four trailers left to fill right?”
#
# Flynn pops a cigarette between his lips, “Yeah and we still got five hours in the fuckin’ shift. I’ll be back”
#
# He continues to walk to the door. Sean steps forward a few steps, calling after Flynn, “But you’re the shift lead!” The gila monster continues his journey through the door, turquoise eyes glinting in the dark as he goes through, “You know where to find me.” The metal door closes behind him.
#
# Cigarette dangling from his lip, Flynn futilely tries lighting it with the zippo. It sparks, over and over again, never igniting. He sighs, slipping the lighter back into his pocket, and in return his paw comes back with a cell phone in hand. He checks his messages, scrolling through a few posts on his social media. He perks up at some distant revving, his forked tongue darting out past his unlit cigarette.
#
# “There he is. Fucker”
#
# A rusty pickup truck pulls up near Flynn, who haughtily greets it, “About time. Were you too busy fapping at the moon, slut wolf?”
#
# Leo steps out of the truck, a slightly annoyed smile on his muzzle, “Psh, you’re one to talk about ‘slut’, lizard. You’re lucky I just so happened to be up, otherwise you’d have no one to shit talk to”
#
# Flynn chuckles, pulling out his lighter again as Leo leans against the wall space beside him. The timber wolf raises a brow. “Thought you gave up smoking?”
#
# “I did”, he said holding the lighter. He pulls out the tattered pack of cigarettes “This lighter; it’s empty. This pack; it’s the same one from back then”
#
# Leo gives the reptile a look of awe, “That old!? Jeez… But why? If you really did quit, then why keep those around?”
#
# Flynn puts away the pack and the lighter, taking the cigarette out of his mouth. He turns to Leo holding the cigarette up “As a reminder.”
#
# The wolf tilts his head to the side, “Que?”
#
# Flynn continues “It’s to serve as a reminder of my past, and show that I’m in control. I could smoke these any time if I really wanted, but I quit cold turkey, and made that addiction my bitch”
#
# Leo, turns up his mouth, raising a brow as he looks at Flynn. Flynn chuckles again, “It’s something I saw from a movie a while back. I thought it was kinda deep, meaningful. Figured it wouldn’t hurt to try. Turns out it helped me.”
#
# Leo snorts shaking his head, “Well it sounds either really pretentious or really gay, even for you”
#
# “Why can’t it be synonymous?”
#
# The red wolf rolls his eyes, letting out a sighing laugh. He puts his paws behind his head leaning back against the building, looking up at the full moon. “Why do we even hang out if all our conversations end up like this?”
#
# Flynn rolls the cigarette around his lips, “Conversations are a two-way street, Leo. I didn’t exactly twist your arm to come here. For me, maybe it’s like this cigarette.”
# They stand in silence for a few seconds, looking up at the night sky. Leo reaches over smoothing a paw over Flynn’s head spines, “I dunno Flynn. It just sounds like you’re hanging onto the past.”
#
# The reptile closes his eyes for a moment, then looks over at the glinting piece of silver on the wolf’s wrist. That anchor shining in the moonlight. Leo looks too, their eyes locking briefly, turquoise staring into red. Flynn snickers a bit, “Your eyes are stupid. You say they’re brown, but they always look red in the light.”
#
# “Ha, yeah. I’ve been told that before…” Leo slowly pulls his paw back.
#
# Flynn looks over the wolf,clicking his tongue “Tsk… why’d you stop? You know I like having my spines petted.
#
# Leo’s ears stand on end, then lower slightly “Oh! Well uh… I figured I’d just stop? I dunno…”
#
# The reptile smirks, “I’m just messing with you, slut wolf.”
#
# “Dammit, Flynn. Will you stop calling me that?”
#
# “Maybe. So he’s graduating in about a year now right? We’re supposed to be having some sort of reunion?”
#
# Leo smiles, going back to his recline against the building, “Mhm! Exciting right? We’ll be a crew again, just like back then.”
#
# Flynn scoffs, “And you said I’m the one holding on to the past”
#
# “Fuck you, lizard”
#
# “Name the time and place”
#
# “Épale!” Leo pushes off the wall, standing to face Flynn, “What’s with you tonight? I came to keep you company on your break and-”
#
# Flynn stands from the wall as well, squarely facing Leo. The gila monster has a few inches on the wolf, and it always gave Leo some pause, but never fully intimidated him. They’d done their share of physical squabbles, and while Flynn is a force to reckon with, Leo was clearly more capable. Flynn pulls the cigarette from his maw, “I need to know where we stand, Leo. I don’t wanna get caught in the middle of that shit again. None of us do”
#
# The red wolf’s shoulders ease down as he lets out a ragged sigh. He smooths a paw up his snout, rubbing his eyes with his finger and thumb, then looks back at the towering reptile, “I love you and Chase as friends. Very good friends. That’s good enough for me.”
#
# Flynn rubs his scaly chin, studying the determined look on Leo’s face, “I guess that’s okay. If that’s all you want”
#
# Leo’s ears perk and twitch “Que? What do you mean?”
#
# “Nothing,” Flynn flicks at his lighter again, then puts it away, pulling out another. This time it’s a standard gas station disposable lighter, orange casing. He flicks it, and it immediately ignites. Taking the cigarette out of his mouth he slips it away, patting his khaki pockets, “Damn. Left my loud. Really coulda used that.”
#
# Leo looks at Flynn in disbelief, folding his arms. Flynn shrugs, putting the lighter away.
# “Hey, I said quit smoking cigarettes.”
