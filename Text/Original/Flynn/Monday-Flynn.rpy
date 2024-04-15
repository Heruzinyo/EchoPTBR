label goafterflynn:
stop music fadeout 3.0
"I look back at Flynn as he winds his way down the trail towards the road."
"I sigh angrily, starting towards him."
c "\"Chase, I wouldn't—\""
m "\"Someone's gotta talk sense into that idiot. He thinks he can just get away with this shit?\""  
c "\"You know how he is...\""
play background "trailsteps.ogg"
"I keep walking."
scene bg deserttrail
with dissolve
play loop "reststop.ogg" fadein 3.0
"He's moving pretty slow, so it's easy to catch up with him."
"He's got his hands jammed into his pockets as he walks along, his head down."  
m "\"Hey, Flynn!\""
"He jerks his head up, then looks back around at me."
"He's chewing on a toothpick, which he promptly pulls out of his muzzle."
f "\"The hell? What the fuck you think you're doing, Chase?\""
f "\"Go back.\""
m "\"Yeah, right! You think you can just walk away from me after saying shit like that?\""
show Flynn at center with dissolve
"He stops walking and turns around fully to face me."
stop background fadeout 3.0
"I step up right in front of him, just a few feet away."
"He looks me over and, for some reason, I can see a smile threatening to crack his face as he tries to keep it hidden."
f "\"Yeah? And what are you gonna do about it?\""
"I shrug."
m "\"Talk?  We were having a good time. Why do you have to go and turn everything good—\""
"He suddenly steps up close, thrusting his chest out into me. It hits me around the neck and I stumble back."
f "\"NOT in the mood.\""
"He sticks the toothpick back in his muzzle before he turns and starts walking away again."  
hide Flynn with dissolve
f "\"Go back to the river so you can all talk about what an asshole I am...\""
m "\"What?\""
"I watch him go for a bit."
"I'm not TOO worried about Flynn actually beating me up."
"I'd annoyed him pretty bad before, but he hadn't ever actually hurt me, at least not maliciously."
"On top of that, he'd have Leo to answer to if he ever did anything like that, and he knows how that would end up."  
"Still, he did look pretty angry when he stepped towards TJ, more than I'd ever seen him, probably."
"Now might not be the best time to do this..."
menu:
    "Turn back.":
        "Definitely not worth it."
        "I really don't wanna make things worse than they already are."
        "I sigh, watching the broad shoulders of the Gilaian get smaller and smaller before I turn back."
        "One of the others probably need my company more than Flynn."
        scene bg yeeyaw
        with dissolve
        menu:
            "Find TJ.":
                jump findtj
            "Follow Jenna and Leo":
                jump leoandjenna
            "Sit with Carl.":
                jump sitwithcarl
    "Keep going.":
        "Screw him."
"Once again, he thinks the act of an asshole can just brush off whoever he doesn't want to talk to."
"Well, I'm about to show him exactly why that doesn't work when it's a stubborn otter he's up against."
play background "trailsteps.ogg"
"I start following again, doing a little jog to catch up."
"This time, Flynn hears me and whirls around, pulling the toothpick out of his mouth again."
show Flynn Annoyed at center with dissolve
f "\"Your ears filled with water? I said FUCK OFF!\""
stop background fadeout 3.0
"I flinch a little under his yelling, but I square my shoulders and walk up to him, standing my ground."
"Now I'm only three feet away."
m "\"Or what, you gonna hit me?\""
m "\"Really?\""
m "\"Go on, try it.\""
"I look him in the eye and immediately I know I have nothing to worry about."
"This is Flynn after all, one of my best friends."
"Whether or not he'd ever admit to it, our little group is family, no matter how many stupid fights we get into."
"He's trying to scare me though, with the way he's leaning over me, glaring."
"I just smirk up at him and, pretty soon, I see his façade crack."
"He slumps down, letting out one massive sigh, deflating like a life-size lizard balloon."
f "\"Fuckin' otters. What do you want?\""
m "\"I want you to stop being a dick.\""
"Flynn looks right back at me and glares, some of the posturing coming back."
f "\"What!?\""
m "\"Oh Christ, you heard me.\""
f "\"That is NOT a good thing to say to me right now.\""
"Flynn starts leaning over me again and I lean right back, almost bumping muzzles."
m "\"Yeah, well, EVERYTHING you said back there was NOT a good thing to say.\""
"I see the corner of one of his eyes twitch."
"We're so close I can smell the beer on his breath. I see that smirk tug at his muzzle again."
f "\"Comin' in for a kiss?\""
"He presses even closer and I feel my muzzle flush, but I'm not backing down."
f "\"I see how it is; you're bored with Leo and now you want some lizard action, eh?\""
m "\"No, I just want an explanation—\""
"He raises a brow and leans back a little."
m "\"—of why you're being such a dick when we're all supposed to be having fun...\""
f "\"Actually, I think I know exactly what this is. You're trying to prove me wrong.\""
f "\"Well, being an obnoxious twit doesn't suddenly mean you've got a personality.\""
f "\"Anyway, they told me to speak my mind. I did.\""
hide Flynn with dissolve
play background "trailsteps.ogg"
"He turns away again and starts walking. I quickly catch up and start walking alongside him."
m "\"That's not an answer.\""
m "\"Besides, even if something's true, it doesn't mean you have to point it out in the middle of everyone's vacation!\""
"Flynn keeps walking, opting to glare at the dusty trail."
m "\"Do you really think I'm just looking to bone all of you? I'm not!\""
"Flynn laughs and, for once, it's not cynical, it's genuine."
f "\"I think what you're doing right now isn't helpin' your case, Chase.\""
m "\"What!? I'm just trying to figure out what the hell is wrong with you, Flynn.\""
play sound "phonebuzz.ogg"
$ renpy.pause(1, hard=False)
"My phone buzzes and I pull it out."
call text_chase("leo") from _call_text_chase_14
call text_0("", "Are you okay?") from _call_text_0_13
""
#l "\"{i}Are you okay?{/i}\""
"It's a text from Leo."
#$ renpy.pause(1, hard=False)
play sound "texting2.ogg"
$ renpy.pause(1.5, hard=False)
call text("m", "Everything is fine and I'm just trying to talk to Flynn.") from _call_text_16
""
#"I type out a quick reply that everything is fine and that I'm just trying to talk to Flynn."
"Flynn snorts right in my ear, making me jump." 
call text_end from _call_text_end_14
"I jerk my phone away as I realize he's been reading over my shoulder."
f "\"What, wolfy-boy thinks I'm gonna clock you for being annoying?\""
m "\"You almost hit TJ.\""
f "\"Almost.\""
scene bg lakeemma with dissolve
"At this point we're walking along Lake Emma Road, the trail winding between it and the reservoir itself."
"There's a little guardrail on the lakeside, but it's rusty and I seriously doubt that it would stop any car from going over into the lake."
"Another ten minutes and we'll reach the motel."
play sound "phonebuzz.ogg"
$ renpy.pause(1, hard=False)
"My phone buzzes again as I get a response from Leo."
call text_chase("leo") from _call_text_chase_15
call text_0("", "If he does anything, call me.") from _call_text_0_14
""
#"\"{i}If he does anything, call me.{/i}\"" 
"Flynn sighs again."
call text_end from _call_text_end_15
stop background fadeout 3.0
show Flynn Depressed at center with dissolve
"He stops, and I turn to face him. He looks sad, for once, staring hard at the ground."
stop loop fadeout 3.0
play music "loneliness.ogg"
f "\"I just sort of blacked out for a second. I was angry...\""
m "\"Uh, that's what murderers say after they kill their exes.\""
show Flynn with dis
f "\"Jesus, Chase.\""
show Flynn Depressed with dis
f "\"Well.. okay, I fucked up.\""
m "\"Yeah, no shit.\""
f "\"It's just—it's just something that's been fucking with me ever since it happened.\""
f "\"That.. he's not telling the truth.\""
"Flynn looks up at me sharply."
show Flynn Annoyed with dis
f "\"You KNOW he isn't!\""
"Flynn's staring at me hard as if he's looking for something, and this time I do look away."
m "\"W—well, what if he is?\""
f "\"No.. no, you SAW him right after it happened, how scared he was, how he couldn't look at any of us...\""
"I have no idea what to say. Flynn never talks about this."
"Before today the last time I'd heard him mention Sydney was like, six years ago."
f "\"It just.. it really fucked me up...\""
f "\"And that we thought we could just come back to this stupid fuckin' lake.\""
"He kicks his foot across the ground towards the reservoir, some pebbles falling over the steep drop and plopping into the water."
"It fucked us all up, but Flynn most of all."
m "\"Look, Flynn. Maybe something DID happen, something he doesn't want to tell us.\""
m "\"But it's TJ, you KNOW what kind of person he is.\""
f "\"And that's what makes this so fuckin' shitty...\""
m  "\"But we were kids. He was like, ten years old. We're different people now—\""
"Looking behind Flynn, I see Leo's van coming up the road."
"Flynn waits for me to go on, but sees me looking back and does so himself."
"As soon as he sees the van he folds his arms and turns his head to look out across the lake."
play loop "engine.ogg" fadein 3.0
"As it pulls up alongside us the window rolls down, and I see Jenna in the passenger seat, Leo next to her."
l "\"Hey, we're heading back. Wanna get in?\""
"Flynn doesn't say anything, instead choosing to continue staring at the lake."
"I decide that it's probably a good idea for me to walk with him instead of making him do it alone."
m "\"Naw, that's alright. We're just talking.\""
"Leo shifts his gaze to Flynn, studying him before turning back to me."  
l "\"Alright. Text me later, okay?\""
m "\"Okay.\""
stop loop fadeout 3.0
stop music fadeout 5.0
"The window rolls back up as the van pulls away, kicking up some dust from the roadside as it does."
play loop "reststop.ogg" fadein 3.0
"I turn back to Flynn, who's still looking at the lake, chewing slowly on his toothpick."
"That's when his stomach growls so loudly it almost makes me jump."
"I snort and Flynn fixes me with a glare."
f "\"What? I didn't get to eat.\""
m "\"Neither did I...which is your fault.\""
hide Flynn with dissolve
play background "trailsteps.ogg"
"Flynn grunts and keeps walking up the trail toward Echo, the town's windows and rusted signs glinting in the desert haze."
"I skip up alongside him."
m "\"Hey, why don't we go to the diner? It's just a few minutes away.\""
"Flynn grimaces."
f "\"I can't eat that shit anymore.\""
m "\"What? When's the last time you ate there?\""
f "\"Few years ago.\""
m "\"Wow. What DO you eat, then?\""
"Flynn laughs."
f "\"I go to Payton where they actually have grocery stores.\""
m "\"Oh, okay.\""
"A few moments of silence pass before Flynn speaks up again."
f "\"I guess it wouldn't hurt to eat there again, for old time's sake.\""
stop background fadeout 3.0
stop loop fadeout 3.0

scene bg diner
with fade
play music "neutraldiner.ogg"
"As we walk into the diner, my senses are assaulted by nostalgia."
"Everything looks and smells the same, from the faded, patched stools, to the smell of burgers and fries."
"Out of habit, I start walking towards the corner booth, the one we always used to sit at."
show Flynn at right with dissolve
f "\"Where you goin'?\""
m "\"Huh?\""
"I look back at Flynn who's standing near the counter, looking ready to sit on one of the stools."
m "\"Oh come on, Flynn, those are uncomfortable. Besides, it'll be easier to talk.\""
"Some of the patrons are starting to look up from their meals."
"Flynn looks around, clearly embarrassed and shoves his hands into his pockets, making his way over to me."
f "\"Fine.\""
"I slide into the booth, into my usual spot on the right-hand side. Usually Leo would sit next to me."
show Flynn at left with easeinleft
"Flynn sits opposite me, leaning back, eyes half open."
m "\"Tired?\""
f "\"Yup.\""
"I wait for him to elaborate, but he doesn't go on."
m "\"Up late?\""
"Flynn reaches up and rubs his eyes."
f "\"Yeah.\""
"The long breath he takes in before he says that tells me he's starting to get annoyed, so I drop it."
"Luckily, that's when Janice, the old diner waitress, comes over to our table."
show Janicenotepad Happy at right with dissolve
ja "\"Chase!? My goodness, what are you doing here?\""
m "\"Hi Janice. Just doing a school project.\""
ja "\"Oh really? I wonder what sorta schoolin' might be here for ya?\""
m "\"I'm actually just getting some film of the town—\""
"Flynn's covering both his eyes with his hands now, as if that's going to make him invisible."
ja "\"And you Flynn, can't say I've seen you at all, recently.\""
"Flynn makes a low, grunting sound, not taking his hands away."
"Janice keeps talking, though, unphased."
ja "\"Well, anything you'd like to drink while you're decidin' on your meal?\""
f "\"Water.\""
ja "\"Chase?\""
menu:
    "Water":
        m "\"Just water, thanks.\""
    "Coke":
        m "\"I'll have a coke.\""
    "Root beer":
        m "\"Root beer, please.\""
    "Root beer float":
        m "\"Can I get a root beer float, please?\""
    "Strawberry shake":
        m "\"I'll have the strawberry shake.\""
ja "\"Sure thing!\""
"Flynn does move his hands at this point and looks at me."
"His expression is odd, like he wants to say something."
"I look back and raise my brows, but he just shuts his muzzle and looks out the window."
ja "\"Alright, I'll be right back with you.\""
hide Janicenotepad with dissolve
"As Janice moves on to some other patrons, I look back at Flynn."
m "\"Were you gonna say something?\""
"Flynn shakes his head, folding his arms on the table and hunching forward."
f "\"No.\""
"Somehow his mood is even darker than it was earlier."
"I sigh, frustrated. It's so damn hard to understand Flynn. His mood-swings are absolutely ridiculous."
"I lean back and fold my arms, scowling."
f "\"What?\""
m "\"You know exactly what. I'm trying to be friendly, here.\""
"Flynn shrugs, a bewildered expression on his face."
f "\"I dunno what to say, Chase. It's been a shitty day.\""
"I don't say anything and just look out the window like Flynn."
"Again, there's a tense silence between us."
"I just listen to the clatter of silverware from the two other people in the diner, along with the old rockabilly music playing over the crackly speakers."
show Flynn Depressed with dis
"Finally, Flynn sighs. I decide that's his signature expression, like Carl's shrug."
f "\"Sorry. I'm just...like I said, it's been a shitty day.\""
m "\"It's fine...\""
show Janicenotepad at right
show Flynn
with dissolve
"That's when Janice brings over our drinks before taking a notepad out to take our orders."
ja "\"Alright, what'll you have?\""
f "\"The tuna melt. Onion rings.\""
ja "\"Uh-huh, and you, Chase?\""
menu:
    "Roast beef sandwich":
        m "\"I'll get the roast beef sandwich, please.\""
    "Bacon cheeseburger":
        m "\"The bacon cheeseburger sounds good.\""
    "Tuna melt":
        m "\"I'll get the tuna melt, too.\""
ja "\"Alrighty. And what'll you have on the side?\""
menu:
    "Fries.":
        m "\"Fries, please.\""
    "Onion rings.":
        m "\"Onion rings, please.\""
"Flynn is staring at me in a weird, squinting sort of way, as if he's trying to see something."
ja "\"Great! I'll have it right over. Sit tight!\""
hide Janicenotepad with dissolve
"As Janice bustles away, I look to the side, then back at Flynn."
m "\"What!?\""
"Flynn keeps squinting, his face incredulous, now."
f "\"Do you really not...\""
"He doesn't finish and instead shakes his head."
f "\"Nevermind.\""
m "\"Seriously! You're kinda freaking me out...\""
"Flynn chuckles and covers his eyes again, rubbing."
f "\"Same.\""
"What the hell is he talking about? I'm opening my mouth to ask again, but he cuts me off."
f "\"Listen, I've got the day off tomorrow. Do you, uh, do you wanna do somethin'?\""
"I stare at him, at a loss for words."
"First he's acting like a complete douche, then he tells me I'm scaring him, and now he's inviting me to hang out with him?"
"Is he, what do you call it...bipolar?"
m "\"I—I guess...?\""
f "\"Alright, I'll come by sometime after noon, maybe with Carl. He doesn't do shit so he should be free.\""
m "\"Okay. I guess I could use a break from working on the project for a bit.\""
"Flynn goes on to tell me that he and Leo often go out to fish on their days off and that it's actually a lot of fun."
"I'm still trying to get used to the shift in conversation when Janice shows up with our food."
"Flynn stares down at his giant, greasy sandwich while I take a giant bite of mine."
f "\"Fuck, I'm gonna regret this.\""
m "\"Why? Tastes great.\""
f "\"Well, you're lucky. This kinda food fucks up my stomach.\""
m "\"Do you make your own food?\""
f "\"Yup.\""
"I snort and Flynn looks up sharply."
m "\"S—sorry, it's just hard to imagine—\""
f "\"Hey, I'm a real good cook.\""
show Flynn Teasing1 with dis
"I guess the expression on my face is showing I don't buy it because he smirks back at me."
f "\"Fine, sometime this week you're comin' over. I'll show ya then.\""
"I shrug, even though I feel like I've won some kind of secret battle we were having."
m "\"Deal.\""
stop music fadeout 3.0

scene bg creepylake
with opening_fade
play music "meeting1.mp3" fadein 10.0
"Flynn pulls me over rocks and boulders."
"I stumble along, trying to keep my balance."
"Flynn's insistent, though, almost angry."
"We reach the edge of the lake and he throws me down."
"I stare at the wet sand, then back up at Flynn."
"He points and tells me to dig."
"I start digging."
"I don't know what I'm looking for, and I ask, but Flynn doesn't say anything."
"Water keeps filling the hole, it's hard to keep sand from sliding back in."
"Finally, I reach in deep and someone grabs my paw."
"I stay like that for a long time."

jump flynntuesday