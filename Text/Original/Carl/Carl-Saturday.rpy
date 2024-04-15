label carlsaturday:
stop music fadeout 3.0
play loop "drone.ogg" fadein 1.0
window hide
scene bg SaturdayCarl
with slow_dissolve
$ renpy.pause(1.0, hard=True)
scene bg SaturdayCarl2 with slow_dissolve
$ renpy.pause(1.5, hard=True)
stop loop fadeout 3.0


scene bg carlsbathroom with dissolve
play music "neutral.ogg" fadein 3.0
window show
c "\"Dudes, I just—I don't know about this.\""
"I peek into the bathroom, watching as Carl stares at himself in the mirror, running his fingers through his hair."
ra "\"You look great!\""
"Raven stands back, grinning with a trimmer in his paws, looking Carl up and down."
ra "\"Tell him, Chase!\""
"Carl looks at me and I have to agree that he looks quite a bit better."
m "\"You look fantastic. A lot cleaner!\""
c "\"Thanks?\""
ra "\"Now take a shower!\""
"Before Carl can say anything Raven shoves the mall bag into Carl's chest before slamming the door in his face."
ra "\"Man, this is going to be great!\""
ra "\"If the interview was based on looks alone he'd get have that job locked!\""
m "\"Yeah, probably.\""
"And so with that we move to the living room and wait..."
scene bg livingroom with dissolve
"Half-an-hour later Carl shuffles in quietly."
"We don't even know he's there until he clears his throat."
show Carlalt Depressed at center with dissolve
c "\"Uh...so—uh, how does it look?\""
"He looks good, but I'm more concerned with the fact that he looks more insecure than I've ever seen him."
"He shifts from hoof to hoof, not making eye contact at all, his fingers pulling at the rolled-up sleeves."
show Raven Happy at left behind Carlalt with dissolve
ra "\"Oh my God. That looks fantastic!\""
ra "\"There's NO WAY you won't get that job now!\""
"Raven sounds genuine enough, but then again, he's always excited."
show Carlalt Rejected with dis
"Carl looks over at me and I give a start, realizing how bad my silence must have seemed."
m "\"You do look great, Carl!\""
show Raven Confused with dis
ra "\"But, uh—\""
show Carlalt Surprised with dis
"Raven chuckles and Carl's eyes widen."
c "\"What!?\""
ra "\"The beanie. Do you always wear that thing?\""
"Carl lifts a paw to it."
c "\"Usually.\""
ra "\"You can't wear that...how do you even get it on?\""
c "\"It's stretchy, and my head fur looks awful.\""
ra "\"Seriously, you can't wear a beanie to an interview.\""
"Carl's getting all fidgety again, so I butt in."
menu:
    "Don't wear it.":
        m "\"Carl, that's a REALLY bad idea for a job interview.\""
        show Carlalt Annoyed with dis
        c "\"Oh, COME ON!\""
        "He looks sad and angry at the same time which gives me pause."
        c "\"I'll wear it if I want. This is my interview.\""
        "After a couple seconds of silence, Raven coughs."
    "Wear it.":
        m "\"Hey, I actually think it looks kinda nice with everything else you've got on.\""
        show Carlalt Rejected with dis
        "Carl glances at me but stops fidgeting with the beanie."
"Raven looks at me, then back to Carl."
show Raven Happy with dis
ra "\"Well, alright.\""
show Carlalt Depressed with dis
"Carl sighs and shifts around again."
"We watch him expectantly."
c "\"Dudes, this just...this feels weird, is all.\""
ra "\"It's new. You'll get used to it!\""
"I pull out my phone to look at the time."
m "\"Alright, we really need to head out. We should get there early.\""
hide Carlalt with dissolve
"As we head to the door, Raven makes as if to follow us."
show Raven Happy at center with moveinright
"I kick myself for forgetting to talk to him earlier."
"I turn around to face him as Carl heads out the door."
m "\"Hey, Raven?\""
show Raven with dis
"He stops."
ra "\"What's up?\""
m "\"So after the interview me and Carl...and our other friends. We're gonna be doing something.\""
show Raven Confused with dis
"Raven raises his brows."
ra "\"Oh?\""
m "\"Oh, it's not that we don't want you to come!\""
"Though I really wouldn't mind having his upbeat attitude present at what will surely be the biggest downer of the week."
m "\"It's just that...it's really personal.\""
ra "\"Oh really?\""
m "\"Yeah. Seriously, you wouldn't wanna come. We're gonna be talking about some heavy shit.\""
show Raven with dis
"Raven seems to perk up a little at that."
ra "\"Oh! Well, I wouldn't want to intrude. I'll just hang out here, then.\""
m "\"Yeah, we'll be back soon, okay?\""
ra "\"Sounds good! But you HAVE to tell me how the interview goes.\""
show Raven Happy with dis
ra "\"I know he's going to do amazing!\""
m "\"I will and he will. See you in a few.\""

scene bg mansion with dissolve
stop music fadeout 3.0
play background "reststop.ogg" fadein 3.0
"Carl looks confused as I come out to the car alone."
c "\"Where's Raven?\""
"I sit down and make a show of buckling my seatbelt."
m "\"Uhh, so, I wanted to tell you this after the interview so you didn't have more to stress out over—\""
c "\"What?\""
"I pause as I back out, pretending to be distracted so I can gather my thoughts."
stop background fadeout 3.0
scene bg flint with dissolve
play loop "highway.ogg" fadein 3.0
m "\"So...Leo wants us to meet up at the lake.\""
c "\"The lake...THE lake?\""
m "\"Yeah...\""
c "\"Why?\""
m "\"Closure, he says.\""
"Carl stays quiet as we drive through Echo and I swerve to avoid all of the potholes."
scene bg route93 with dissolve
"As I'm merging onto the highway he finally speaks up."
c "\"I think that's a good idea. Like, we've been sitting on this for how long?\""
c "\"We should do it while we got the chance.\""
"I nod my agreement."
m "\"I just hope everyone else feels the same.\""
"We fall back into silence, and it stays that way for the remaining twenty minute drive."
"Carl gets more nervous the closer we get."
"I can see his knees bouncing out of the corner of my eye as he stares out the window."
"I reach out and put a paw on his shoulder as we pull into the parking lot of the print shop."
scene bg printshop with dissolve
stop loop fadeout 3.0
play background "parkinglot.ogg"
play sound "engineoff.mp3"
m "\"You look awesome and you're gonna do amazing.\""
"Carl starts taking deep breaths, staring out the windshield."
m "\"Just be yourself. Everyone loves a relaxed employee.\""
c "\"I wish you'd let me have a smoke before we left.\""
m "\"Yeah, go into an interview smelling like pot, great idea.\""
"Carl giggles nervously, but otherwise doesn't move."
m "\"Do you want me to go in with you?\""
"Carl shakes his head quickly, unbuckling his seatbelt as he opens the car door."
c "\"No man, I'll—I'll be fine.\""
m "\"Okay, cool. I'll be waiting!\""
play sound "cardoor.mp3"
"I grin at him, but he just shuts the door and ambles up to the print shop."
"He pushes on the doors and, when they don't move, he pushes harder, shaking the glass."
"I start to open my door to tell him to pull instead, but he seems to figure it out before I have to and disappears inside."
m "\"Oh, Carl.\""
"Then, I sit back and wait."
play music "quiet.ogg" fadein 3.0
"I try to take a nap since I'd been up all night with Raven and Carl gaming, but the heat beating down through the windows becomes too uncomfortable."
"I turn the AC back on, then shuffle through the stations, but I only find twangy country and Mariachi."
"I look at the time."
"10:10 AM"
"If the interview started on time then he was probably almost done with it by now..."
"I sort of want to go inside, but I know Carl wouldn't want me to.."
"I settle back again and close my eyes, trying to get some relief from the failing AC."
"Then the door rattles and I hear haphazard hoof-steps."
stop music fadeout 3.0
"I open my eyes, but...no one's there."
"I do catch some movement disappearing around the side of the store and I lean around to get a better look."
"I wait, but Carl (at least I think it's Carl) doesn't come back from around the corner."
"Looking around, I slowly open my door."
m "\"Carl?\""
"Nothing."
m "\"CARL!?\""
"I yell it, but he still doesn't come out."
"Feeling some dread build up in my stomach, I get out of the car and slowly walk around the side of the building."
"It's an alley, between the print shop and what I think is a laundromat."
"Nothing is in the alley except for a few dumpsters and clumps of garbage."
"I step carefully around puddles covered in oil slick and wonder if maybe he'd just really wanted a smoke."
m "\"Carl?\""
"Something shifts on the other side of one of the dumpsters and I hear sniffling."
"Wordlessly, I walk around the dumpster to the other side."
play music "loneliness.ogg" fadein 3.0
"Carl is bent over, his back to me, paws on his knees."
"His whole body is shaking, and his breaths are ragged."
m "\"Holy shit, Carl!\""
"I'm at his side instantly, rubbing his back."
m "\"What happened? Are you alright?\""
"The stench of vomit hits my nose and I don't need to look closely to know what the puddle between Carl's hooves is."
"Carl makes sure to turn his face away from me, not saying a word."
m "\"Shit.\""
"I dash back to the car and open the passenger door so I can get to the glove box."
"I pull out a few napkins before hurrying back to the ram."
"He takes them from me wordlessly and starts wiping his face."
"The last time I'd seen Carl like this was just last year, when he'd had his panic attack at school."
"I didn't think he'd have that problem now, after all the therapy and time away."
"I try to rub his back comfortingly, in a clockwise motion like my mom would do for me."
"He's at least not hyperventilating."
"He has his horns pressed up against the wall, taking deep breaths as he wipes his face again."
c "\"Why do I suck at everything?\""
"He says it quietly, between gasps, but I can make it out."
m "\"NO, Carl, you're fine. Let's just get you home.\""
"I start to pull on his arm, but he yanks it from me violently."
c "\"Don't touch me!\""
"I'm stunned into silence. I just stare at him, mouth open."
"He glances at me and his eyes are red and, for once, it's not because of weed."
"Carl starts off toward the car on his own, spitting off to the side as he does."
m "\"Carl...Carl, what happened?\""
"He whirls on me."
show Carlalt Annoyed at center with dissolve
c "\"I fucked up! Obviously! Any more fucking questions!?\""
"His voice breaks apart on the last sentence and he turns away from me as his face starts to screw up."
"My stomach feels hollow as I watch Carl get into my car. I've never, ever seen him like this."
show Carlalt Depressed with dis
"He immediately hunches forward, head in his paws."
"I slowly walk up to the driver's side door, feeling like crying myself."
stop background fadeout 3.0
"I sit for a while, waiting to see if Carl is going to say anything."
"He does."
c "\"I'm sorry.\""
"He blurts it out through his fingers."
"I look over at him, scared to say anything in case I say the wrong thing."
c "\"I just...It was a disaster, man.\""
"He takes in a deep, shuddering breath."
c "\"He could tell I wasn't into it right away. I was awkward as fuck.\""
"He leans back and tugs at his shirt."
c "\"This shit, this isn't me, and they knew it and it got me nervous...\""
c "\"I've been nervous ever since I got my clothes, since I got this stupid trim.\""
"At that moment it feels as if I've been punched in the stomach."
"I'm just now remembering the conversation we had on Wednesday."
"I close my eyes for a moment, not wanting to believe I'd become exactly what he said I wasn't, what he liked me for not being."
"We sit in silence for a long, long time until Carl finally looks at me and smiles."
show Carlalt with dis
c "\"Goddammit. We both knew this was gonna happen, didn't we?\""
m "\"I—I dunno, man...\""
c "\"And fuck me very much for taking it out on you.\""
m "\"It is sort of my fault...\""
c "\"Nope, I'm the one that screwed up the interview.\""
"Carl settles back in his seat."
c "\"Now with that fuck-up out of the way, on to the next one!\""
"I force a smile."
m "\"You sure you still wanna go?\""
c "\"Hell no! But I don't think we have much of a choice.\""
"I sigh, looking out at the hazy horizon, in the direction of where I know Echo is."
m "\"Can't wait.\""
stop music fadeout 10.0
"So with that I turn on the ignition and pull out of the parking lot, leaving the print shop and its alley far, far behind us."
show Carlalt Rejected with dis
$ renpy.pause(0.1, hard=False)
scene bg lakeemma with fade
play background "reststop.ogg" fadein 3.0
"Leo, TJ, Flynn, and Jenna are all gathered around a picnic table."
"It's set out neatly on concrete in front of the rocky shore of the lake."
"None of this existed when we were kids. In fact, it didn't exist when I left."
"Echo is trying really hard to stay alive."
"I don't need to get out of the car to gage the mood my friends are in; their shoulders slumped, faces turned away from each other."
"As I park, Leo's ears perk and he turns to wave at us."
"I take a deep breath and turn to Carl."
m "\"You ready?\""
c "\"Nope.\""
"Nevertheless, he opens his door and steps out and I do the same."
"The sun beats down on us, but being this close to the lake cools things down a bit."
scene bg lakeside with dissolve
"As we approach I see Leo with his butt up against the edge of the table while TJ sits next to him."
"Jenna sits next to TJ while Flynn sits across from Jenna."
"When Flynn turns around he immediately zeros in on Carl."
show Flynn Surprised at farleft with dissolve
f "\"What the HELL happened to you?\""
show Carlalt Neutral at center with dissolve
c "\"Drugs, sex, and rock 'n roll.\""
f "\"Out of order, bud.\""
c "\"No, I just put it in the appropriate, descending order.\""
show Flynn with dis
"Flynn rolls his eyes, then looks at me."
f "\"Hey, fuckboy. Maybe you can talk some fucking sense into this idiot.\""
"Leo's ears are flat, but he doesn't look at Flynn."
show Leo Rejected at farright behind Carlalt with dissolve
l "\"Glad you guys could make it.\""
m "\"Sure...\""
show Carlalt Depressed with dis
"Carl sits down next to Flynn and I sit on Carl's other side, across from TJ."
"The silence that follows is possibly the most awkward one of the week."
show Flynn Annoyed with dis
"Flynn snickers."
f "\"See? This is stupid.\""
show Jenna Annoyed at right with dissolve
j "\"How about we let it happen naturally, Flynn, instead of using every moment to take shots at people.\""
"Jenna's tone is icy. She hasn't even acknowledged me or Carl."
show TJ Rejected at farright behind Jenna with dissolve
"TJ, meanwhile, keeps his head down, poking a sharp claw into the soft wood of the table."
"Flynn shrugs and starts to do his trademark \"I don't give a fuck\" lean back pose, but gives a start when he realizes there isn't any backing on the bench."
f "\"Well, we've been sitting here for the past twenty minutes and nothing's happened.\""
show Carlalt Rejected with dis
c "\"Maybe you wanna start us off?\""
"Flynn sighs."
f "\"Well, we could talk about how I never agreed to this shit.\""
show Leo Neutral with dis
f "\"How Leo's a complete fucking idiot for forcing this to happen, and that I wonder what he thought this would accomplish anyway.\""
show Carlalt Depressed with dis
c "\"That's a start, I guess.\""
"Flynn sets his jaw."
f "\"Of course, talk that would ACTUALLY get us somewhere wouldn't be from me, and he's not talkin'.\""
show TJ Depressed1 with dis
"The temperature seems to lower in the impossibly hot air and I don't look at TJ to see how he reacts."
"After a brief silence, Leo speaks up."
show Leo Annoyed with dis
l "\"How about we start with you, Flynn?\""
"Flynn looks at Leo, brows raised."
l "\"How do you feel about what happened?\""
"I see Flynn clench his jaw."
hide Jenna
hide Carlalt
hide TJ
with dissolve
stop loop fadeout 3.0
play music "argument.ogg" fadein 10.0
f "\"What?\""
"His tone sends shivers down my spine and I feel Carl tense up next to me."
"I look out across the lake, the shimmering reflections blinding me."
l "\"You NEVER talked about it. Maybe it'll help?\""
"Sweat pours down the back of my neck, builds up under my arms."
"Even with the wind coming off the lake it's way too hot."
f "\"By telling you how I fuckin' feel? How the FUCK do you think I feel!?\""
"Flynn screams it and TJ jumps in front of me."
l "\"You just gonna keep it buried your whole life {i}Garrobo{/i}?\""
"I think about the time I used to come down to this spot everyday and skip rocks with Jenna and TJ."
f "\"So this is how you plan to fuckin' get us over this? By fuckin' makin' fun of me!?\""
l "\"I'm not making fun of you. I'm trying to help you.\""
f "\"Taunting someone who's felt like shit for a decade is a pretty weird way of helpin'!\""
t "\"Please, guys...\""
f "\"Don't you even fuckin' talk right now!\""
j "\"Don't you dare talk to him like that. We all went through this!\""
l "\"Calm down, Flynn.\""
play sound "mallet.mp3"
"The table shakes as Flynn slams his fist down on the wood, snarling and standing up."
f "\"Tell me to calm down one more fuckin'—\""
stop music fadeout 3.0
show Flynn Surprised
show Leo Surprised
with dis
m "\"Just shut the hell up.\""
"I stand up."
"Everyone turns to look at me, including Flynn."
"I don't say anything, instead I just strip off my shirt."
f "\"The hell are you doin'?\""
"I don't answer him."
"Instead I take off my belt and slide off my pants so that I'm only left in my boxers."
"Without a word, I head to the lake."
hide Flynn
hide Leo
with dissolve
"It's about a hundred yards from the tables to the lake and, while most of the way there is sand, a good stretch of it is pointy rocks."
"I make my way carefully over this section, remembering the numerous cuts I'd gotten as a kid."
play loop "lakesounds.ogg" fadein 5.0
stop background fadeout 3.0
"I don't look back until I'm right at the water's edge and, when I do, I see Leo following me, in the process of taking his own shirt off."
"The rest of them are still sitting at the table, but I don't care because this is really just for me."
"I step into the water and sigh at how cool it is before I wade out further."
"Once I'm waist deep, I dive under the water and pop up several feet further away from shore."
play music "melancholia.ogg" fadein 10.0
"I'm neck deep at this point and, when I look back, I can see Carl now, standing at the lake's edge, paws deep in his pockets."
"Behind him, Jenna is helping TJ across the rocks."
"Only Flynn remains behind at the table, watching us all."
"Leo's up to his chest at this point and I swim in a circle around him before diving under, then popping up right in front of him."
l "\"Gah! Sneaky otter!\""
"He splashes water in my face and I cough."
m "\"Don't be that way.\""
"I swim around him some more and laugh at how he flounders after me."
"He was always a terrible swimmer."
"I dive under the water again and swim up toward the shore, popping up about ten feet away from Carl."
c "\"Having fun?\""
"He's smiling, looking a lot more relaxed than he has all day, probably because we just avoided a situation that could have gotten really ugly."
"To my left Jenna and TJ are sitting on a boulder in the shallows, TJ's slacks rolled up to his knees."
"Him and Jenna seem to be talking, so I decide not to play the same trick on them as I did with Leo."
"Flynn, meanwhile, is standing up, now, arms folded."
"For the next little while, I swim around, occasionally popping up in front of Carl or Leo, sometimes splashing them with my tail."
"There's a freeing feeling about finally swimming in this lake again and having so much space."
"Flynn, after a good twenty minutes, comes out to the shore. He leans against an old, familiar boulder, watching us."
"There's no way for me to know how they're all feeling, if it's liberating like it is for me."
"Flynn is right, in a way."
"We can't just talk about it because there's nothing to really say."
"What happened, happened and no amount of talking can fix it."
"What we can do, or what I can do, at least, is choose to move past it."
"And that's what I'm doing now."
"I just hope that's what they're feeling, too."
"Eventually, I run out of the exhilarating energy that had so consumed me and instead drift to the bottom of the shallows."
scene bg underpond with dissolve
stop music fadeout 10.0
stop loop fadeout 3.0
"I lay on my back against the sand, staring up at the murky glow of the sun."
"I feel my eyelids get heavy and I stretch out against the soft lake bed."
"It is, of course, a bad idea to fall asleep under water."
"If that were to happen, though, I'd probably just try to breathe, get a nose full of water, and immediately wake up."
"Still, I decide that it's best I avoid that, if I can, and force myself to open my eyes again and swim to the surface."
"Except...I can't."
"I'm frozen."
play music "Vanishing_Paradise.ogg" noloop fadein 5.0
"Every nerve in my body is on fire and I struggle not to panic, to not start trying to breathe because that's all my body wants to do."
"I close my eyes, will myself to be calm."
"Sleep paralysis usually only lasts about a minute at most for me. I can hold my breath for eight and I've only been under for..."
"God, I have no idea."
"It FEELS like it's been a while. My chest is already starting to burn and that usually means it's been at least six minutes."
"And this is starting to last a long time."
"Despite my efforts, panic starts to set in, and it sets in quick."
"I start jerking my body around, trying to get something, anything to move."
"I don't understand why I'm not floating to the surface. I'm not trying to stay underwater."
"The seconds turn into minutes and now my lungs are really burning."
"Something has to be holding me down...maybe some kind of vegetation."
scene bg redwater with dissolve
"The water begins to glow red, as if blood has spread across the surface above me."
"I tug and pull, praying that this is all a dream, that I'm back in Carl's room, and that at any moment I'll wake up."
"???" "\"You thought it would be this easy? That's a good one.\""
"I try to turn my head toward the voice which is right in my ear, even though I'm underwater."
"Things go silent again."
"At this point I start to contemplate that I might actually die."
"I can't get my body to move, none of my friends know where I'm at, and now I'm almost out of air."
"Bubbles flow past my lips as my lungs finally give out and blackness starts to crowd in on my vision."
stop music fadeout 6.0
stop loop fadeout 3.0
scene bg black
with transition_fade
$ renpy.pause(10.0, hard=True)
scene bg lakeside with dissolve

t "\"He's waking up!\""
play background "reststop.ogg" fadein 3.0
"My eyes open slowly, painfully, and I'm face to face with a ram, his muzzle wet with tears."
c "\"Oh my god, he is!\""
f "\"Give him room!\""
"I feel some rough paws supporting my back, turning me on my side."
l "\"Can you breathe, Chase?\""
"Leo's voice is ragged next to my ear."
m "\"Y-yeah, no, I'm fine!\""
"I sit up quickly and a wave of dizziness threatens to topple me over again."
"I feel movement behind me, out of my field of vision."
f "\"No...no, no, NO!"
stop background fadeout 3.0
play music "anger.ogg" fadein 10.0
f "\"I can't believe this. I can't fuckin' believe this!\""
"Flynn's voice is torn and ragged. I barely recognize it."
j "\"Calm down, Flynn!\""
f "\"No! We're forced to come here and then THIS shit happens!?\""
t "\"Guys...I have—I need to go...\""
l "\"TJ! Flynn, get over here.\""
"I feel Leo's support leave me."
"Carl is still crouched down in front of me, though."
show Carlalt Surprised at center with dissolve
c "\"Oh my God, dude, what happened?\""
"Carl's gasping, like he's the one that was just underwater."
m "\"I—I don't know.\""
"Carl rubs my back as I rest my head in my paws."
"Vaguely, I can hear more yelling behind me and Carl looks up, too."
t "\"No, no, don't—Leo, help!\""
"Despite my aching head I turn around and see Flynn Chasing TJ, grab him and throw him down onto the rocks."
"Flynn doesn't get any further, though, because Leo tackles him with such force they fly a good five feet before smashing down into the rocks and sand."
"Leo wraps an arm around Flynn's neck and yanks up hard."
c "\"Jesus...\""
"Carl stands up and starts gasping again."
"I try to, but I fall back down on my ass."
"Carl reaches down to help me up."
c "\"Shit, you're not okay.\""
"Carl steadies me, but I'm distracted with trying to see what's happening."
"Leo's leaning down with his muzzle right up against Flynn's head, yelling at him."
"Meanwhile, Jenna's crouched over TJ."
"Carl starts to breathe heavily again, his wheezing picking up speed"
"I look over at him and his eyes are glazed, as if he's watching everything from afar."
m "\"Carl...Carl, what's wrong?\""
"I don't want him having another panic attack."
"I know I should probably stay and try to help, but I feel so fucked up right now."
"Besides, I don't think it will help if Carl has a breakdown."
"I grab his arm."
m "\"Let's...let's get out of here, Carl.\""
"He looks at the scene a while longer, then turns away."
scene bg lakeemma with dissolve
"Without another word, we make our way back to the car. I get in, barely noticing that I'm drenching the seat."
"Looking through the windshield I see that my friends are still in the same position that we left them."
"Except Jenna."
"She watches us as we pull out and keeps watching us until we're out of sight."
stop music fadeout 10.0

scene bg flint with dissolve
play loop "highway.ogg" fadein 3.0
"Carl stays in his glazed state as we make the short drive back to his house."
"I can't give him much of my attention, though."
"I'm more preoccupied with the fact that something terrible just happened."
"Not only to me, but the entire group."
"Maybe this is a dream?"
"Everything feels so surreal right now, like I'm watching all of this happen from a hundred miles away."
c "\"I can't...I don't know—\""
"I look over at Carl, but his expression is still glassy."
"He looks exactly like how I'm feeling."
m "\"What's wrong, Carl?\""
c "\"I don't know.\""
m "\"You don't—\""
"I'm cut off as a large coyote suddenly runs out into the street."
"But she's a good distance down the road so there's no danger of me hitting her."
"I watch as she tears out into the sage brush, zigzagging about, arms flinging out in all directions."
"Carl and I both watch her as we pass, silent."
"Something's happening in this town..."
"...to all of us."
stop loop fadeout 5.0

scene bg kitchen with fade
play music "daze.ogg" fadein 30.0
"Once we get in the house Carl heads straight for the stairs."
m "\"Carl!\""
ra "\"You guys back? How'd it go?\""
"Raven's voice calls from upstairs."
m "\"Ray...something's wrong...\""
ra "\"Huh? What's wrong?\""
"I don't answer as I walk to the stairs Carl just disappeared down."
"Once I get there he's already gone."
"I make my way down the stairs and it's at that point that my headache starts to make a comeback."
m "\"Carl!?\""
scene bg basement with dissolve
"He's not in the basement, either, but I can see the yellow light glowing from the crawlspace."
"Something...I don't know what it is, but something feels incredibly wrong right now."
play sound "drone.ogg"
"Buzzing fills my head, the ground feeling unsteady, as if I'm walking on sand."
stop sound fadeout 2.0
"Once I find Carl we're both going to the hospital."
scene bg crawlspace with dissolve
"I stumble down into the crawlspace and, again, Carl's not there."
"I'm greeted to the familiar row of tubs, but a stack of them have been pulled away from the wall."
play sound "drone.ogg"
m "\"Carl? Carl, what—\""
stop sound fadeout 2.0
"I fall silent because ahead of me is a hole."
"About three feet high and two feet wide."
m "\"What the hell...Carl?\""
"Plaster covers the tarp around it, as if the wall had been bashed violently to create the hole."
"Did Carl go through it?"
"Getting on my paws and knees, I look into it, but the darkness is inky and so black I swear I can touch it."
"As I crawl forward my mind gives a violent jolt and I arch my head back, teeth bared as my face spasms."
"And then I fall."
"And it feels like I fall forever."

scene bg black 
with slow_dissolve
stop music fadeout 10.0
$ renpy.pause(10.0, hard=True)

jump mansion1