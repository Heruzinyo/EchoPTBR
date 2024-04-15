# Date

label sidestory_date:

stop music fadeout 3.0
scene bg black
with slow_dissolve
play background "roomtone.ogg" fadein 5
pause 1
call sidestory_title("January 2010") from _call_sidestory_title
pause
call sidestory_title("January 2010", end=True) from _call_sidestory_title_1

"What makes a good date?"
"Chase told me dinner and a movie."
"Personally, I felt like having the dinner half of the date at my house would have been really nice."
"I mean, it's cleaner than any restaurant you might find in Payton, and my mom's a great cook."
"Still, I can tell by the way Heather has her head down that she's really unhappy."
"I feel a sort of sinking feeling in my chest."
"It's sorta set the mood for the night so far."

scene bg route93
play background "highway.ogg"

"Mom drives us to the movie theater and I start to get restless, noticing how late we are."
"The movie is supposed to be really good and it takes place in space, which is my favorite."
"Mom tells me not to worry, though, since previews usually fill the first fifteen minutes."

show bg theaterext with dis
play background2 "reststop.ogg" fadein 5
stop background fadeout 7
"Finally, we park and I hop out and hold the door open for Heather."
"I notice that she’s taking her time getting out, so I wait for her as Mom goes in to get the tickets."
show Heather at center with dis
h "\"Why's your mom coming?\""
"Her voice is a whisper."
"I reach out to shut the door, but she does it herself, a little harder than she needed to."
"I stand there for a second, not sure what to say."
t "\"Um... well, it's really hot out. Staying in the car would be too-.\""
h "\"Never mind.\""
hide Heather with dis
"Heather stalks ahead of me and I feel that sinking feeling again."
stop background2 fadeout 10
"It’s only now hitting me that bringing Mom was a bad idea. Not that I told her to come; Mom sort of just invited herself."
"Chase gave me a bunch of tips on how to make the date go well, but he never said anything about parents."
"Maybe it was so obvious that he didn’t think he had to tell me. That thought just makes me shrink into myself even more and I can feel my face get hot."
play background2 "roomtone.ogg" fadein 10
"I push my paws into my pockets and follow after her, trying to keep my ears upright."

scene bg theater with medium_dis
python:
    vol("music", 0.05)
    pan("music", 0.2)
    vol("background", 0.1)
    pan("background", -0.2)
play music "adastratheme.ogg" fadein 10
play background "adastrasfx.ogg" fadein 10

"Mom's really nice and sits about five rows behind us, but Heather still seems pretty angry about it."
"She keeps moving her sitting position, folding her arms and making pouting faces."
"Each time she sighs I feel myself cringe just a little more inside and now I can’t even focus on the movie."
"After about thirty minutes, she adjusts her sitting position again and knocks some popcorn into my lap. I lean over to her, whispering."
t "\"What's wrong?\""
"She shrugs, keeping her eyes on the movie."
"I lean back in my seat, again trying to keep my ears up, especially with Mom behind us."

$ stop_all_audio(reset=True)

scene bg highwaynight
play background "highway.ogg"

"The drive back home is pretty awkward."
"Mom goes on and on about the movie and what she thought of it, which is fine, because I can tell Heather isn't in the mood  to talk and I have no idea what to say."
"As we drive back into Echo, Mom looks back at us."
mom "\"Alright, Heather, would you like me to drop you off at your house?\""
h "\"Actually, me and TJ wanted to talk about a few things. Would it be alright if I stayed over for a little while longer?\""
mom "\"Sure thing!\""
"I look over at Heather, but she doesn’t look back at me."
"I have no idea what she's talking about, and I think I'd rather not find out."
"There's nothing I can do, though, so when we pull over in the drive way, I quietly get out and follow Heather into the house."

play background2 "roomtone.ogg" fadein 3
stop background fadeout 5

scene bg tjdiningroom with medium_dis

dadg "\"How was the movie?\""
"He says it without looking up from the TV."
h "\"Oh, it was great, Mr. Hess, really cool.\""
"She's using that weird, sweet voice she puts on for my parents."
t "\"Uh, yeah, a lot of fun.\""
"I follow after her."
dadg "\"Good, good.\""
"He doesn't even try to sound interested as he keeps watching the hockey game."
show bg tjbedroom with dis
show Heather at left with dis
"Heather's already sitting on my bed when I walk through the doorway."
"She's got her legs crossed, paws resting back behind her on the bed."
"I stand there awkwardly, trying to figure out what to do as she just sits there and doesn’t say anything."
t "\"Uh, do you want to listen to some music?\""
"I turn to my dresser, grabbing my small stack of CDs and shuffling through them."
"I skip over the Christian rock albums, feeling my ears burn a little at the thought of her seeing those."
"I end up picking out a Cherryloom album my dad gave me a few years ago when he was trying to get me into classic rock."
"Heather still hasn't said anything and I feel myself sweating a bit as I put the CD in and turn it down low."
$ vol("music", 0.4)
$ pan("music", -0.2)
play music "Country3.ogg"
"Finally, I turn around, and see that Heather hasn't moved from her spot on the bed. She's just been watching me the whole time."
"I twitch an ear and scratch behind my head, laughing to cover my nervousness."
t "\"Uh, hehe. What's up?\""
show Heather Happy with dis
"She gestures with her hand towards the doorway."
h "\"Shut the door.\""
t "\"Um, okay.\""
hide Heather with dis
"I know my mom would probably get mad, but I do it anyway, trying to close it as softly as possible so my parents don't hear it."
play sound "rustle.ogg"
show Heather Happy at center with dis
"That's when I hear the bed squeak behind me. I turn around and Heather is right in front of me."
t "\"Oh!\""
"I jump back and bump against the door. Heather giggles and moves closer, and I can feel her breath on my face."
"She reaches out and rests her paws on my waist, then slides them up, pushing up my shirt, her paws on my bare fur now."
t "\"Oh, wow, okay, uh...\""
"I have no idea what to say, or what to do."
"Heather just giggles at me again, pressing her fingers through the fur to my skin, and I can feel her paw pads against me."
"I look down and see that she has my shirt pushed up above my belly button and she's starting to rub at the white fur that's been exposed."
"No one's ever touched me like this before, and I know I'm supposed to like it...but I don't."
"It’s almost like I’ve jumped into ice-cold water and now I can’t breathe."
"I open my mouth and I think I'm about to ask her to hold on, but that's when she kisses me."
show Heather Happy:
    ease 0.4 alpha 0.0
"It's awkward and her bottom lip presses up against my teeth while she pushes me back, banging my head against the door."
"I can taste the butter from the popcorn still on her lips."
"She huffs into my mouth excitedly as she pulls me away from the door, then pushes me down on the bed."
t "\"Wait, Heather.\""
"My voice is quiet as she pushes me all the way down so I'm flat against the bed, my legs dangling off the side."
"She's really excited, and it kind of scares me, her eyes wide and her breathing coming in loud huffs."
"I grab at her wrists as she pushes my shirt up again, but this time she does it all the way to my neck."
"She leans down and I gasp as she presses her cold nose up against my stomach."
"She's so...confident about what she's doing. Has she done this before?"
"She nuzzles lower, then presses a paw against my crotch. I sit up fast and push her back."
t "\"Heather! Let's... let's stop.\""
"I quickly push my shirt back down."
"Heather stares at me, then awkwardly stands back up, folding her arms."
show Heather Sad:
    ease 0.1 alpha 1.0
h "\"You weren't enjoying it.\""
"I keep pretending to adjust myself, having no clue about what I should say."
t "\"N-no, it was okay. I just-. I'm just not ready, is all.\""
"I know that sounds really cliché, but it’s the truth."
"I finally lose the battle with my ears and they lilt off to the sides of my head as Cherryloom plays softly in the background."
h "\"Alright, I should probably get going anyway.\""
"But she doesn't move. She stands there, like she's waiting for something."
"I'm still too stunned to really know what to say."
t "\"Do you need a ride home?\""
"That's the best I can manage."
"She sighs again before turning to the door."
h "\"No, it's alright. It's only a few minutes away. See you on Monday.\""
hide Heather with dis
t "\"O-okay.\""
"I get up awkwardly to walk her to the door, but she's already gone."
"I sit there on the bed for a while, hearing the rumble of my dad’s voice for a bit before I hear the front door open and close."
"Then I hear some footsteps up the stairs and my mom sticks her head around the door frame."
mom "\"Everything okay? Why aren't you walking her home?\""
t "\"I, uhm, she told me she wanted to walk alone.\""
"I feel my ears droop lower."
mom "\"Oh, alright.\""
"Mom's about to leave, but then she pokes her head back around the door frame."
mom "\"Well, your father and I are watching TV. Why don't you come down and join us?\""
"That actually sounds nice, and my ears perk up a little."
t "\"Sure, I'll be there in a minute.\""
mom "\"Okay.\""
"She smiles at me, before pulling back from the doorframe."
$ vol("sound", 0.4)
play sound "switch.ogg" # volume 0.4
stop music fadeout 0.1
"I watch the doorway for another minute, then sigh and lay back again."
"I cover my face with both paws, rubbing my forehead. I’m so bad at this stuff, why did I even try?"
"That's when my phone buzzes and I take it out to see a text."
"" "{b}Chase:\n{i}hows the daaattee ;)"
"I stare at it for a second, then, on a whim, press the call button with my thumb. He picks up after the second ring."
m "\"Hey, bee-otch. Your date over already?\""
t "\"Hey, Chase...\""
m "\"What's up?\""
"I can hear him adjust the phone, and his voice drops the lisp."
"I hear Leo's voice in the background, muffled."
l "\"That TJ?\""
"I start to massage the bridge of my nose, closing my eyes against the room's light."
t "\"Yeah, the date's over. It was... okay, I guess?\""
m "\"Are you asking me? How was it?\""
"I wait a while, listening to white noise on the other end. I can hear some music in the background. I wonder if they're in Leo's car."
t "\"Chase... how did you know you're gay?\""
"There's some silence on the other end before I hear a burst of laughter."
"I flatten my ears, feeling my face blush all over again. I don't say anything, though, and just wait for him to get it out of his system."
l "\"What did he say?\""
"Leo sounds really close now, like his muzzle is right up against Chase’s. I hear some more adjusting of the phone going on before Chase finally reponds."
m "\"Sorry, sorry. I just didn't expect that. Are you on your computer?\""
t "\"Uh, yeah.\""
"I get off my bed and walk over to my desk, waking my computer up."
$ vol("sound")
play sound "click.ogg"
play background "comphum.ogg" fadein 3
m "\"Okay, go to the website Thickfur.\""
"I type it into the URL and press enter."
"Immediately a buff fox with no clothes on pops up."
"He’s got his paws on his privates and he’s sort of pushing them up."
"There are a bunch of other pictures, too, but I don’t have time to process them as I jump and close the browser."
"I dart my eyes behind me, half expecting to see Mom and Dad staring around the corner, their eyes wide in horror."
t "\"Chase!\""
m "\"Hehe, so are you hard?\""
t "\"Wha-? No!\""
m "\"Then you probably aren't gay, TJ. You like looking at boobs, don't you?\""
"I pause."
t "\"Well-.\""
m "\"Wait a minute, don't you?\""
t "\"Well... not really, I guess.\""
m "\"This isn't you being all... Christian, right?\""
t "\"No, I'm fine with this stuff. I just haven't really given it much thought, I guess.\""
m "\"I guess you could be asexual–ah! Leo, stop it!\""
"I can hear the phone getting bumped around again and I think I know what's going on."
l "\"What are you guys talking about?\""
"His voice is playfully accusatory and I can hear some more shuffling with the phone as, I assume, Chase tries to move it away from the wolf."
m "\"Alright, TJ, I'd better get going. I'll talk to you more about this on Monday, okay?\""
t "\"Okay.\""
l "\"Laaater, Teej!\""
"Leo's voice is muffled, like he has something in his muzzle."
m "\"And listen, TJ-.\""
"He sounds strained."
m "\"Heather is... well, she's not that... it's just not a big deal, alright? Okay, I'm gonna go. Talk to you later!\""
t "\"See ya.\""
"I hear Chase start to snap something at Leo before he hangs up."
"I drop my phone on the bed next to me and close my eyes, tempted to just fall asleep right then and there."
"I feel better, though. Chase always had a way of making things seem alright."
"He offered doing a double date with us, but Heather didn't want to, so it didn't happen. It would have made things a whole lot better."
"I start to wonder what Chase and Leo might have been doing."
"He was probably nibbling Chase's ear, Leo does that a lot. In front of us, too, sometimes."
"I actually think it’s kind of cute..."
"My paw drifts down to my crotch and for the first time in the past few hours I feel something hard."
mom "\"TJ?\""
"I jump as I hear my mom call from downstairs, jerking my paw back."
t "\"Coming!\""
"I quickly sit up and slide off the bed, going downstairs to watch the rest of the game with my family."
$ stop_all_audio(2, reset=True)
$ renpy.pause(0.2, hard=True)
show bg black with medium_dis
$ renpy.pause(2, hard=True)
$ renpy.end_replay()
