label findtj:
stop music fadeout 5.0
play background "river.ogg" fadein 5.0
"I'm really worried about TJ."
"He's a sensitive guy and, after a tongue-lashing like that from someone like Flynn.. I can't imagine what state he's in."
"I don't see him anywhere as I scan the area, but I do see some trees and bushes further up along the riverbank."
"Since there's really no other place to hide, I assume that's where he's at."
scene bg riverbank
with dissolve
"Sure enough, I see him immediately. He's sitting down, knees drawn up with his arms folded on top of them."
"He's got his forehead resting on top of his arms, staring down at the sand between his legs."
"I stand there for a moment, wondering if it will just be better to leave him alone."
"After a few seconds I finally decide to sit down next to him, cross-legged."
show TJ Rejected with dissolve
"His ears flick in my direction and he turns his head to the left, away from me."
"I notice a few wet spots between his feet."
"Maybe he just wants to be left alone now?"
menu:
    "Say something...":
        "I decide that I need to break the silence."
        m "\"Heeey, TJ...\""
        "He doesn't say anything, or move."
        m "\"You know how Flynn is...he's a dick.\""
        "Again, silence."
        m "\"Everyone knows he's a dick. No one's mad at you.\""
        "He does move, then, sliding his legs out straight and leaning back on his paws."
        "He's still looking away from me, rubbing his face on his shoulder."
        m "\"You wanna go back and eat?\""
        "Finally..."
    "Say nothing...":
        "I decide to let TJ talk when he's ready."
        "In the meantime, I pick up a dry twig and start toying with it, snapping it in half, then snapping the other halves in half."
        "I can see that his ears are still swiveled in my direction, probably wondering what the hell I'm doing."
        "I think I'm getting on his nerves because finally he talks."
        t "\"What do you want, Chase?\""
        "I throw the pieces of the twig into the river."
        m "\"Just wondering where you went. You wanna go back and eat?\""
        t "\"No.\""
        "We sit there for a while longer as I watch the twig pieces float down the river."
        "Finally..."
    "Leave him be...":
        "Definitely not worth it."
        "I really don't wanna make things worse than they already are."
        "I'm not exactly graceful with this sort of thing, especially with TJ."
        "For now, I should probably just go talk to one of the others."
        scene bg yeeyaw
        with dissolve
        menu:
            "Go after Flynn.":
                jump goafterflynn
            "Follow Jenna and Leo.":
                jump leoandjenna
            "Sit with Carl.":
                jump sitwithcarl
        
        
t "\"I can't believe he did that...in front of everyone.\""
"I'm not sure what to say, so I stay quiet."
"After a minute, TJ finally turns his head, looking into the river."
"The wind picks up, reflections from the river highlighting motes of dust that swirl up around us."
"His face fur is a bit mussed up, spiked up in a few places from being wet."
"It's an unusual sight to see his fur unkempt."
t "\"I mean, what the ffh—\""
t "\"...what the heck?\""
"TJ; unable to curse even though it would probably be the best thing for him."
"He adjusts his legs to sit cross-legged, like me, and wipes his face again."
t "\"D—did you know...what he was talking about?\""
"I take in a breath, unsure about how I should approach this."
m "\"I {i}think{/i} so?\""
"TJ's ears lower."
m "\"Listen, no one else thinks anything happened. We were so little, especially you.\""
m "\"I mean, I can't believe he's doing this...\""
"I trace a claw through the dirt, drawing some wavy patterns as I try to make sense of all this myself."
m "\"I think it's just because he was such good friends with Sydney, and he just wants more than the truth.\""
"I look sideways at TJ."
"He's just sitting there, looking at the ground."
m "\"And I guess you were the only one that saw him...saw what happened...so he only has you to go after.\""
t "\"I saw him drown.\""
"I don't say anything, but I feel myself cringe inwardly." 
"Pretty soon tears are running down TJ's face, but he doesn't bother to wipe them away."
"He's not just sad, though; he's angry. I hear it in his voice as he goes on."
t "\"I saw Sydney drown and Flynn thinks he's the only one that hurts?\""
t "\"He thinks that he's the only one that feels like he's in a nightmare?\""
t "\"Well maybe...\""
"His voice cracks and he looks away from me again, wiping at his face."
t "\"...Maybe I haven't told him everything because I don't want him to have those images in his head.\""
"TJ takes a moment to steady his voice, working to get his breathing back to normal."
t "\"I just...I just wish I could go back to that day.\""
m "\"TJ...there's nothing you could have done.\""
"I know my words are meaningless crap, and I hate myself for saying them."
"But I have to say something."
m "\"Not one of us would have been able to do anything if we were there.\""
t "\"You would have.\""
m "\"Well...\""
t "\"Besides, I already know I couldn't have saved him on my own. That isn't what...\""
"TJ takes a moment to wipe his face again and when he's done he doesn't go on."
"We sit in silence for a long while after that, and I adjust myself so that I can lean back against a rock behind me."
"I pat the ground."
m "\"Sit next to me, Teej.\""
"He's calmed down for the most part and, after a moment, he does crawl over to sit by me."
#enlarge image
"I pick up a few pebbles and toss them into the river."
m "\"Remember when we used to call it Seesaw River?\""
t "\"Yeah...\""
"He leaves it at that, so I drop it."
"I rest my head back and close my eyes, only then realizing how tired I am."
"In some way, I can see why Flynn is so suspicious, or at least why he believes there's more to the story."
"There clearly is."
"But while I do want TJ to tell me more about what happened, I could never bring myself to ask him."
"I honestly feel that if I ever want to help him with his past, I should probably come to terms with it myself."
"I crinkle my brow, toying with the idea of going back..."
"It's something I actively avoid thinking about. We all do."
"But like Jenna said, maybe talking about it, {i}thinking{/i} about it, might actually help."
"I dig my fingers into the pebbles on either side of me."
"The images come in a quick flurry, like someone cycling through a View-Master too fast."
stop background fadeout 3.0
scene bg fb6
show nightoverlay
with opening_fade
play music "drone.ogg" fadein 3.0
"The sky is getting cloudy, the air crisp - autumn."
"TJ sitting in a daze, Jenna running back to town, Flynn pulling me into the water..."
"...Me, grabbing onto neck scruff, pulling back to shore..."
"Carl sitting on a rock, bawling, Leo starts trying to do compressions..."
"And Sydney.. Sydney just stares."
"Sirens, the helicopter rotors, adults everywhere."
"I'm home, mom's holding me. Dad puts on my favorite movie. I watch."
"But still.. Sydney stares."
scene bg riverbank
show TJ Rejected at center
with opening_fade
stop music fadeout 5.0
play background "river.ogg" fadein 3.0
"I open my eyes again and the world is blurred. The light reflecting off the river makes me squint."
"I rub my eyes with the back of my paw and it comes away wet."
"My chest hurts, and so does my head, throbbing and buzzing."
"I look over and, luckily for me, TJ is leaning back with his eyes closed like I was."
"If revisiting that day is so horrible for me, I can't imagine what it's like for him."
"I decide right then and there that I'm not going to press TJ on what happened."
"If he wants to tell me more, he'll do it on his own accord."
"I kind of want to swim again, but at the same time I don't."
"That day really fucked up my view about water."
t "\"He's ruined the whole trip...\""
"TJ speaks suddenly, and I look over at him."
m "\"Flynn? No he hasn't.\""
"TJ does finally look at me, then, and I'm struck by how disheveled and sad he looks."
"I feel anger bloom in my chest, all of it directed at Flynn."
"What a selfish prick, thinking he had the right to ruin everyone's good time just because he felt like shit."
"If he were here right now I'm pretty sure I'd punch him right in the gut."
m "\"Listen, we don't all need to hang out to have fun. We had fun at the park with just you, me, and Carl, remember?\""
m "\"If Flynn wants to be a douchebag then let him, we'll do our own thing.\""
stop background fadeout 3.0
play music "comeover.ogg" fadein 3.0
"TJ sniffs and I see his tufted ears perk up a little."
m "\"Didn't you want to go hike the trail?\""
show TJ Sheepish with dis
"He smiles at that and looks at me."
t "\"You didn't want to hike, I could tell.\""
"I grin."
m "\"That's 'cuz it's so friggin' hot! But seriously, we didn't come here to lay in a motel all week.\""
show TJ with dis
t "\"And we can bring water! Just dump it on yourself every half-hour.\""
t "\"That's how I manage, along with taking plenty of breaks.\""
"TJ leans back and spreads his legs out."
"I can see he's starting to get excited at the prospect of hiking, and that makes me feel better."
m "\"Well, if {i}you're{/i} able to do it, I guess I shouldn't complain.\""
"I look over his fluffy form which, by itself, is enough to make me sweat even more than I am already."
m "\"You know, I always thought you'd go back after you graduated high school.\""
t "\"Hm?\""
m "\"The Great White North.\""
"I say it dramatically, nodding upwards as if that's where it is."
m "\"Your parents did.\""
"TJ's family moved to Echo when he was only six from a small town called Wasatchua."
"His dad got a job in Echo to survey the land, or do something with the wildlife...I can't remember exactly what it was."
t "\"Oh, well...I don't really remember it, but I might after I graduate. They have some things up there that sound really nice.\""
m "\"Free healthcare?\""
t "\"Ha, that I guess...and snow.\""
"For a moment I wonder if snow is to a lynx as water is to an otter."
"A lot of snow did sound kind of exciting to me, though. Here we'd be lucky to see a single dusting of it a year."
t "\"Sooo, you're serious about hiking with me?\""
m "\"Of course! I'm gonna bring some of my equipment, too. I think I wanna get some shots of the canyon.\""
t "\"Okay!\""
"He waggles his furry feet back and forth, and I hide a grin at his enthusiasm."
t "\"Alright, so we're going to have to get up around six.\""
m "\"Oh...\""
t "\"I want to be able to make it to the canyon for lunch where we can rest for an hour or two, then—\""
"You can tell how excited TJ is by how much he talks."
"Well, if anyone's good at planning things out at a ridiculously meticulous level, it's TJ."
"We sit there for another 20 minutes or so and just talk, mostly about school and what our plans are once we graduate."
"I promise TJ that we'll meet up again, before I do."
"That's when I get a text from Jenna asking where we are. I stand up, brushing off my pants before reaching down to help TJ up."
m "\"Welp, we better go back. Guess they're all wondering where we are.\"" 
stop music fadeout 3.0
play background "river.ogg" fadein 3.0
scene bg yeeyaw
with fade
"When we get back, everything's packed up and in the van, along with Carl and Jenna."
"Leo's leaning against the van, waiting for us, his paws in his pockets."
show Leo Questioning at center with dissolve
"He looks at me, then over at TJ, obviously trying to gauge his mood."
l "\"...Everything good?\""
t "\"Yeah.\""
"TJ answers before I can, and whether or not he actually is okay, he sounds happy enough."
l "\"Well, alright then.\""
hide Leo with dissolve
"We get in the van at that point, no one saying anything as we make the short drive back to the motel."
stop background fadeout 3.0
scene bg parkingloteve
with fade
play music "neutral.ogg"
"As we get out Leo tells us all that he's going to have a word with Flynn and, despite the spoiled afternoon, we still had stuff to do over the week."
"I'm not too convinced myself that that will happen. I am convinced that it's gonna be awkward as fuck if we do."
"Leo leaves for work at that point, though Carl does end up coming in with us to the motel room."
scene bg motelfull
with dissolve
"The rest of the day is pretty uneventful; we watch a few movies then go to the diner for dinner."
"Afterwards we just sit in the room and talk, Carl filling us in on how things have been in the town over the past three years."
"It's not long before the conversation drifts back to Flynn and his outburst."
show Carl at center with dissolve
c "\"I think he's just antsy 'cuz he's realizing how shitty it's been without you guys.\""
c "\"Trust me, he's already kicking himself for it right now.\""
show Jenna at right with dissolve
j "\"Even if he is it doesn't mean anything unless he apologizes.\""
c "\"Aww, you know how he is, Jenna. He's sorry even if he won't say it.\""
j "\"I don't care, he's going to have to realize that none of us have to put up with him anymore.\""
show TJ at left with dissolve
t "\"Hey! Why don't we all get some ice cream? I've been wanting to go to Ray's ever since we got here.\""
"It's hard to tell if TJ is just trying to change the subject, or actually wants ice cream...probably both."
c "\"Heh, if you wanna drive half an hour to Payton, sure.\""
show TJ Surprised with dis
t "\"What, why?\""
c "\"They moved it there. It sucks, I haven't had their rocky road for a year now.\""
show TJ Rejected with dis
t "\"Awww...\""
j "\"Well, let's just stop by when we go to Payton next. I assume we aren't staying in Echo for the rest of the trip.\""
show TJ with dis
t "\"Ooh! Chase, can you take us?\""
"I just smile at him from my spot on the couch."
m "\"Sure, why not?\""
t "\"Yes! I love the cookie dough.\""
t "\"What about you, Jenna?\""
"Jenna's busy looking at her phone."
j "\"Hmm? Oh, well I've always enjoyed their butter almond. It's hard to find that flavor anywhere else.\""
"TJ looks at me and I open my mouth to answer."
"But for a moment, I draw a blank, the memories of Ray's hazy and blurred. My head is still buzzing."
m "\"Oh, uh...Vanilla.\""
"I've been feeling pretty shitty ever since I'd had that talk with TJ by the river. I make a mental note to steal some of Jenna's aspirin before I go to bed."
c "\"Well...Flynn was right about one of us, at least.\""
show TJ Surprised with dis
t "\"Carl!\""
m "\"What's wrong with that? Everyone likes vanilla.\""
"I grin even though Carl's comment hurts me more than it should. He's just joking after all."
c "\"But I mean, who loves it, right?\""
"{i}...personality of a rock.{/i}" 
t "\"I think it's a good answer, especially if you put toppings on it.\""
scene bg moteltable
with dissolve
"The buzzing picks up and I feel a dull pulse behind my eyes."
"The three of them continue to talk amongst themselves as I lean my head back against the couch."
stop music fadeout 3.0
"I close my eyes, trying to will away the pounding in my head."
scene bg black
with slow_dissolve
scene bg moteltable
with dissolve
"I open my eyes. The room is dark. Jenna is in her bed, TJ is in his, Carl's wrapped in a blanket on the floor."
"I lurch for my camera bag, then look around wide-eyed."
scene bg black
with dissolve
"I sit on the bed next to TJ and stare at the door..."

scene bg creepylake
with opening_fade
play music "meeting1.mp3" fadein 10.0

"TJ stands at the edge of the lake, staring across to the other side."
"He has one paw in his pocket, the other holding a beer."
"He takes a drink from it...TJ doesn't drink beer."
"He pulls the tab off the top, then flicks it towards the lake."
"It whizzes like a weed cutter, skipping across the water and kicking up spray."
"Suddenly, his ears snap up and he sees something I don't."
"He turns and starts to run."
"He's at a dead sprint when his leg snaps out from under him and he falls to the rocks, beer splashing everywhere."
"A chain is pulled taut from the lake, connected to his ankle."
"I get up, wanting to help, but I can't."
"I look down, my wrist and ankle chained..."

jump tjtuesday