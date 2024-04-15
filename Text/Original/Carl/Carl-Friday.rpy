label carlfriday:
stop music fadeout 3.0
stop loop fadeout 3.0
scene bg friday
with transition_fade
$ renpy.pause(3.0, hard=True)
scene bg crawlspace with dissolve
play loop "floodlight.ogg" fadein 5.0
show Raven at center with dissolve
window show
ra "\"Hey, is this useful?\""
"I look over at Raven as he holds up what looks like a porcelain canine doll of some kind."
m "\"Uhh, maybe? Again, just set aside the stuff you think might be interesting enough for me to take pictures of.\""
ra "\"Okay.\""
"He puts it to the side and starts digging through the tub (rather carelessly) again."
hide Raven with dissolve
"I sigh and turn back to the binder."
"I really wish Carl had agreed to come down."
"Again, he declined to help me, even after Raven arrived."
"But now I guess I have my answer as to why."
"More stuff is missing from the tubs...and I know it can't be anyone else except Carl."
"The containers were turned the opposite way when I got down to the crawlspace earlier this morning."
"On top of that there were two more loose wrappers in the tub, along with..."
"I trace a paw up the torn edges of a missing page in the \"John Begay\" section."
"The question, of course, is why he would be doing this."
"There's absolutely no reason for it."
"And the bizarreness of the situation makes it pretty much impossible for me to confront him on it."
"It's his house, after all, though if he didn't want me going through it why would he have shown it to me in the first place?"
"And he isn't even trying to cover his tracks."
"In fact, I practically caught him in the act just a few nights ago. He must know now that I'd be able to put that together pretty quick."
"I close the binder, deciding that this will be the last time I'll be going through this stuff."
"If Carl doesn't want me digging up info on his family's history then I'm not gonna pry any further."
show Raven Happy at farleft with dissolve
ra "\"Hey look at this!\""
"Raven holds up a wooden train."
ra "\"Bet this was probably the shit back in the day.\""
"I sigh."
m "\"Probably.\""
play sound "phonebuzz.ogg"
$ renpy.pause(1.0, hard=False)
"My phone buzzes."
"I take it out, my notifications telling me I have a text from Leo."
#chat history
call text_chase("leo") from _call_text_chase_35
#call text_0("", "hangin' with u was great. looking 4ward to chillin more in future :) :)")
call text_0("", "met me @ diner 4 lunch,  just u") from _call_text_0_36
""
"For a moment I feel a pang of guilt."
"He'd told me how excited he was to hang out with me this week, yet I've spent almost all of my time here with Carl."
"Though, from what I've gathered in texts, Leo's been spending most of his time with TJ and Jenna since the lynx is apparently still feeling down."
"At least he had that to keep him occupied."
"My excuse that Carl has all the info I need for my project made my decision to spend most of my time here a little less weird."
#l "\"{i}Meet me at the diner for lunch, just you{/i}\""
#"I text back what time and what does he mean by just me."
play sound "texting3.ogg"
$ renpy.pause(1.0, hard=False)
call text("m", "What time? And what do you mean by just me?") from _call_text_48
""
call text_end from _call_text_end_35
m "\"Hey, Rave? I'm gonna go out to meet with some friends, could you keep Carl company?\""
ra "\"Okay, sure.\""
"Raven seems busy pushing the train across the ground while attaching more cars."
m "\"And make sure you keep that together; I wanna get a picture of it later."
play sound "phonebuzz.ogg"
$ renpy.pause(1.0, hard=False)
#"Leo texts back."
call text_chase("leo") from _call_text_chase_36
call text_0("", "now. need to talk in privato") from _call_text_0_37
#l "\"{i}Now. Need to talk in private{/i}\""
""
call text_end from _call_text_end_36
"I sigh and put my phone away, patting my pocket for my keys as I head up the crawlspace steps."
stop loop fadeout 3.0

scene bg diner
with fade
play loop  "roomtone.ogg" fadein 3.0
"Leo waves at me as I walk into the diner."
"I'm surprised to see that the diner is completely empty."
"There's almost always SOMEONE in here."
"Something else is amiss, too, and I don't notice it until I've sat down across from the wolf."
"It's eerily quiet."
"The usual rockabilly tracks aren't playing from the jukebox."
show Leo Neutral at center with dissolve
l "\"Hey.\""
m "\"Hey man. What's up?\""
"The atmosphere is unreasonably awkward and I blame most of that on the strange state of the diner."
l "\"Um, so apparently we have to go up to the counter to order; Janice isn't here.\""
m "\"Oh...why's that?\""
"Leo shrugs as he sips on a milkshake."
l "\"Dunno. Sick, I guess.\""
"It's then that I remember the story Flynn had told us about Janice and her...incident."
"Though I'm not gonna bring that up because I'm sure that's what Leo's thinking as well."
m "\"Well, I'm not really hungry anyway...what was it you wanted to talk about?\""
show Leo Depressed with dis
"Leo swallows slowly, then looks down at the table."
l "\"So you probably know this whole...thing...didn't go as I'd planned.\""
"I look at the collection of condensation on his glass before I speak up."
m "\"Yeah, sort of.\""
"Leo frowns, as if he'd hoped I would have tried to deny it."
l "\"Well, it's mostly my fault. I should have done a better job at resolving shit.\""
"Now I frown."
m "\"Hey...\""
show Leo Neutral with dis
"I wait until he takes his eyes off the table to look at me."
m "\"You know...you're not our big brother anymore.\""
show Leo Depressed with dis
"He looks back down at the table."
m "\"We're adults, believe it or not. We make our own decisions now.\""
m "\"Everything we're doing right now is our decision, our fault, not yours.\""
show Leo with dis
"Leo's eyes get shiny, but he smiles."
l "\"Heh, yeah, you're right. Guess I just want to go back, is all.\""
m "\"Hey, we're still young. You're talking like my grandpa.\""
"Leo laughs and leans back."
l "\"Mine, too.\""
show Leo Questioning with dis
"Leo jerks his head, as if he just remembered something."
l "\"So what the hell happened between Jenna and Carl?\""
m "\"I was actually hoping YOU could have told me that. I have no idea.\""
l "\"She keeps going on about him not participating. I told her it was fine, but she can't seem to let it go.\""
m "\"Yeah...well, it's really weighing on Carl, I think.\""
"Leo swigs his milkshake, forgoing the straw."
show Leo Neutral with dis
"He wipes away the cream from his muzzle as he brings it back down onto the table with some resolve."
play sound "setdownglass.ogg"
l "\"Well, I'm not letting it end like this.\""
m "\"Hmm? Let what end like this?\""
play music "loneliness.ogg" fadein 10.0
l "\"Our group.\""
l "\"You realize this might be the last time we're all together?\""
"That sentence immediately forms a lump in my throat."
m "\"Yeah...\""
l "\"So I'm not gonna let it end like this; Flynn pissed at TJ, Jenna pissed at Carl, you and me...\""
"He lets that hang and, when I don't say anything he coughs."
show Leo Depressed with dis
l "\"So I planned something.\""
m "\"What?\""
"His hesitant tone is making me nervous."
show Leo Neutral with dis
"He looks me in the eye and squares his shoulders."
l "\"We're going to the lake tomorrow.\""
"He lets that sink in as I turn his words over in my head."
"I had suspected that this is what he was getting at."
"I consider my words for a moment, not wanting to say the wrong thing."
m "\"I...I don't know if that's—\""
show Leo Rejected with dis
"Leo puts up a paw."
l "\"I've thought this over real hard, Chase.\""
l "\"That day, what happened to Sydney, it fucked us all up. Changed us all.\""
l "\"Not for the better, either. It took something from us.\""
"Leo pauses, looking to the side as if searching for words."
l "\"Flynn, Sydney was his best friend.\""
l "\"And Carl, he's been depressed ever since.\""
"I feel the need to speak up."
m "\"I don't know if you can pin all of that on what happened. Maybe we would have turned out the same—\""
"He presses on."
l "\"TJ, he saw Sydney die, saw him drown. Can you imagine that at eight years old?\""
l "\"And Jenna, has she ever been happy since?\""
"I shake my head."
m "\"I always felt like that experience helped her, in a weird way. She decided to go to school, leave Echo.\""
"He doesn't seem to be listening to me."
l "\"And you...I love you, but you did change the day it happened. You're practically a different person.\""
"I don't have anything to say to that..."
show Leo Depressed with dis
l "\"And me...I—\""
"His voice catches in his throat and I close my eyes."
m "\"Leo...\""
l "\"I—I was supposed to be watching all of you. I was supposed to take care of—\""
"Leo stops talking and I keep my eyes on the table while he grabs one of the brown napkins and wipes his eyes."
"When he speaks again his voice is thick and cracks with emotion."
l "\"His parents never said but...they trusted me with Sydney, and I think they blamed me—\""
m "\"No, Leo.\""
"He falls silent."
"For a while we both sit there and share the feeling of being weighed down by eleven years of baggage."
"A good five minutes goes by, Leo staring out the window."
"The afternoon sun turns his normally red fur almost orange."
l "\"We can't do this anymore...and this might be our last chance to find some kind of closure.\""
"I take a deep breath, swallowing past the lump."
m "\"Okay.\""
show Leo Neutral with dis
"He looks up at me, relief all over his face."
l "\"So you'll go?\""
"I smile reassuringly at him."
m "\"Of course. Have you told anyone else?\""
show Leo Rejected with dis
"He lowers his ears."
l "\"No...\""
m "\"Oh, God...Are you going to tell them?\""
l "\"I dunno...\""
m "\"Leo.\""
"He does his signature shrug, paws out."
l "\"I really don't know how else to get them to go.\""
m "\"Then there's no way this isn't gonna be a disaster.\""
l "\"Hey, we gotta try.\""
stop music fadeout 10.0
m "\"I guess...\""
l "\"So can you bring Carl with you?\""
"I think for a moment."
m "\"Oh shit, Carl has an interview.\""
l "\"What time?\""
m "\"Uh, 10, I think.\""
#chat history
l "\"Well, we'll plan around it. Text me the actual time, okay?\""
play music "comeover.ogg" fadein 5.0
show Leo Neutral with dis
l "\"Anyway, I invited you out here to talk about more than shitty stuff.\""
show Leo with dis
l "\"What have you been up to the past three years?\""
"And so we talk for the next two hours, catching up on everything."
"It feels good and I regret not spending more time with Leo this past week."
scene sunset
show Leo
with dissolve
"As we part in the small parking lot, Leo surprises me with a hug."
l "\"I have a good feeling about this. It'll be hard, but we'll be better for it.\""
"I hug back, hoping with all my heart that he's right."

jump carlsaturday