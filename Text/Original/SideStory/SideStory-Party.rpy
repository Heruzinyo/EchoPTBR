# Party
# by Gausk

label sidestory_party:

stop music fadeout 3.0
scene bg black
with slow_dissolve

play background "roomtone.ogg" fadein 3
pause 1
call sidestory_title("October 2012") from _call_sidestory_title_6
pause
call sidestory_title("October 2012", end=True) from _call_sidestory_title_7

scene bg uni6 with dissolve

m "\"Carl, do you know where the keys are?\""
play music "neutral.ogg" fadein 2
stop background fadeout 5
"I dig through my pockets again, but my fingers only rake the grocery shopping list I made and some chump change from the soda I bought earlier."
"I brief hope, a glimmer of salvation bubbles to the surface when I feel something metal and pointy."
"When I bring it out, though, it's just an old keychain I won at the fair and never bothered to take out."
"It's even still got a sticker on it."
c "\"Didn't you leave them on your desk?\""
"His voice is barely audible over what I can only imagine are the ten-year-olds he's playing his shooter with."
c "\"I thought I saw them on your desk.\""
m "\"I already checked, they're not.\""
"I open the closet drawer. It's filled to the brim with old comics, but still no keys."
c "\"Maybe they got thrown in the trash by accident?\""
m "\"Why would-?\""
"I rub the bridge of my snout."
"I'm in no rush to get out today, because the party won't start for an hour and a half, at least, but I won't get anywhere without the car keys."
"Our dorm isn't the largest, but right now it still feels like I'm trying to find a needle in a haystack."
"A haystack that's usually very well organized. As per usual, I blame Carl."
c "\"What do you n-NN-?\""
"I hear the sound of a rocket launcher going off."
"Carl follows up with a stream of swear words the likes of which I haven't heard since we were twelve and hanging out with Flynn after school."
c "\"...What do you need them for, anyway? I got the groceries this morning.\""
m "\"Weed. You got weed this morning, Carl. I can smell it from here.\""
"I hear an awkward chuckle."
c "\"You know how it is. Healthy greens. Anyway, where are you going?\""
"I scour another drawer. This one's full of greeting cards. Old ones, by the looks of it, congratulating Carl and me for getting into college."
"I flip each one over before shutting it again."
m "\"I'm heading to Vincent's place, remember? I thought I told you.\""
"I lift one of the vases Carl's mom gave him when we left town."
c "\"You're actually going?\""
# "Carl's voice becomes a bit more clear when I step into the living room. Not by much, however – the voices are still overpowering his by a mile."
c "\"I thought you said you were going to study tonight.\""
m "\"Nah, I got invited, and a couple of my friends'll be there, so I'm going.\""
"I spot the keys, and let out a sound which, once it's out of my mouth, I realize resembles a deflating balloon."
m "\"They're right here, Carl, Jesus!\""
"They're sitting on the shelf, right next to the TV. I pick them up."
"I almost feel like doing a little victory dance at this point – I've been looking for these damn things for a solid hour already."
show Carl Neutral at center with dis
"Carl's still as stone-faced as ever. I don't know if he's had weed or if he's just in a bad mood. Maybe both."
"I sit on the bed with him."
"It's a far more comfortable mattress than the ones that come with the dorm. I think Carl's parents had it specially ordered when he left town."
"Carl doesn't tear his eyes off the game."
c "\"Dude. Get off my back. I didn't mean to-.\""
show Carl Annoyed with dis
c "\"Shit...\""
"The round's over."
"The cacophony of voices that has served as the backdrop for our conversation abruptly dies out, replaced by the most generic orchestral music I've ever heard."
"Carl's got the worst score on the board."
$ vol("sound", 0.6)
play sound "plasticimpact.ogg" # volume 0.6
"I don't even have time to say anything before he tosses the controller off to the side."
$ vol("sound")
"It's a small miracle it doesn't break on impact, considering how hard he's tossing it around."
"I cross my arms behind my head and get comfortable."
m "\"You alright man? You seem kinda mad.\""
show Carl Neutral with dis
c "\"Eh.\""
"Carl's hands go to the pockets of his ripped jeans."
c "\"I could be better.\""
m "\"Really?\""
"I absentmindedly draw a finger over the keychain of my car keys. The one with a picture of Leo on it."
"I think it's the first picture I'd ever taken with my own camera."
show Carl with dis
"Carl notices from the corner of his eye, and playfully smacks my paw away, though it seems to remind him of something, as he turns to me and opens his muzzle."
show Carl Neutral with dis
c "\"How are you holding up? With the whole Leo thing going on, I mean.\""
"I have to ponder that for a moment, myself."
"Leo doesn't cross my mind a lot these days, but when I do think of him, I feel empty, hollow."
"To the point where I wonder, somewhere in the back of my mind, if leaving Echo's been the right choice."
"In the end, however, I shake my head to snap out of it – as I always do when asked about Leo."
"I've done it for my parents, I've done it for my friends. And I've done it for myself when looking in the mirror all alone late at night."
m "\"It's better this way, you know?\""
"I mimic Carl's sitting position, thrusting my hands down my jean pockets."
"I smirk, inching closer to him."
m "\"Besides, I've got all the man I need right here.\""
show Carl with dis
"It's a poor way to lighten the mood, but Carl falls for it hard, making a mock face of disgust."
show Carl Teasing with dis
c "\"Ew, pardon, but I don't associate with no queers.\""
"He does his best Southern drawl."
show Carl with dis
"I snort."
m "\"So those last, what, nine years, that was just you letting me down gently?\""
c "\"Exactly!\""
"He notices the way I'm sitting, shifts his legs around, and pulls his hands out of his pockets."
c "\"I'm glad you finally got it after all this time. It's a weight off my shoulders.\""
m "\"And here I thought we had something special.\""
"We laugh together. Almost enough to make me forget about Echo for a moment. Almost."
c "\"So, this Vincent guy. It is a date, or...?\""
"I roll my eyes."
m "\"It's just a party. Geez. Nothing's gonna happen.\""
show Carl Neutral with dis
c "\"If he tries anything funny, just give me a call.\""
"Carl takes a large swig from the two-liter soda bottle sitting next to him."
"It's almost captivating to watch him down it all in the span of roughly an hour. I think his record's at 45 minutes."
c "\"I'll come pick you-\""
"He cuts himself off with a burp."
c "\"-pick you up.\""
m "\"It's a five-minute drive. I'll be fine. Thanks, though.\""
c "\"You mom made me promise to look after you, man.\""
"He slams the bottle down a bit too hard. Soda erupts from the bottle and stains his pants."
show Carl Annoyed with dis
c "\"Well, fuck.\""
show Carl Neutral with dis
"I laugh."
m "\"Sounds like you need more help than I do.\""
show Carl with dis
"He wags a finger at me."
c "\"Shut it. Can you pass me the towel?\""
m "Don't wanna come with?"
"I toss him the towel hanging over the back of his chair."
m "\"He invited you, too.\""
show Carl Neutral with dis
c "\"Nah, you know me, Chase. I'm no good at parties.\""
"He's vigorously rubbing at the stain, but it won't come out no matter how much pressure he applies. Hell, I don't even think it's really drying."
show Carl Rejected with dis
"When he realizes it, he shoots me a pleading glance. There's just a tiny hint of despair in his eyes."
"It's a look he's given me many times since we were kids, and I know exactly what it means."
m "\"Nope. You're on laundry duty today, Carl, remember?\""
"I fold my arms over my chest."
show Carl Neutral with dis
m "\"And you're cooking tomorrow. I've got a lecture in the afternoon. Something about the importance of composition in photography.\""
"He groans and stretches."
c "\"Composition in photography? Sounds pretty interesting.\""
m "\"It {i}is{/i} pretty interesting.\""
"I eye one of the magazines sitting on the table. It's from a few months back, before we even got here."
"A layer of dust is starting to form on them."
m "\"What about your classes?\""
c "\"Hm?\""
"The way he's looking at me, you'd think I said something offensive."
c "\"My what?\""
"I drag a finger through the dust, then bring it to my face."
"My paw pad's all gray now, and the dust my paw's kicked up is almost enough to give me a coughing fit."
m "\"Your classes. How are they?\""
show Carl Depressed with dis
c "\"Oh, I've, uh...\""
"He shrinks back into his seat, like he's trying to hide behind his hoodie."
show Carl Neutral with dis
"He finally just shrugs."
c "\"Okay, I guess. Not bad.\""
"I raise an eyebrow."
m "\"Just okay?\""
c "\"It's... it's a business major, Chase.\""
"He's given up on rubbing the stain."
c "\"Not much going on besides numbers, numbers, and more numbers.\""
"He snorts."
c "\"I don't even know how my mom can keep track of all of them. So many numbers...\""
"I chuckle."
m "\"Almost sounds like college.\""
show Carl Depressed with dis
c "\"Maybe I should've stayed in Echo. I'm not really cut out for this stuff.\""
"I gently squeeze his shoulder."
"He pulls his beanie down to the point it's almost covering his eyes. I can see him nodding under there. I think."
"I let it sit there. I don't want to make Carl uncomfortable. His parents put enough pressure on him as is."
"Instead, I just put a hand on his shoulder."
"He leans into the touch, a smile appearing on his face again."
show Carl with dis
"He picks up the controller once more, and starts a new game. He hastily points towards a second controller."
c "\"You still have time, right?\""
"I look at Carl's pleading grin, then at my watch."
"Indeed, I still have another hour until I really need to leave, and I've already freshened up and everything."
"Before I've even managed to grab the controller - almost tripping over the clothes and trash on the floor in the meantime - Carl's already started a match."
"The voices start up again. There's accusations and shit-slinging abound already."
m "\"I'm gonna be playing online?\""
c "\"Of course you're playing online. The bots are way too easy.\""
m "\"I thought we could just do a versus match or some-.\""
"My character gets taken down with a headshot almost as soon as I'm in. There's some shrieking on the other end."
c "\"C'mon, Chase, get it together.\""
"I'm not used to these controls."
"I've played one of the older games in the series before."
"Mostly back in Echo, during the summer, when it was so hot you couldn't even go outside without spontaneously combusting."
"This one's got an entirely different control scheme, and I only manage to get a grip on it after dying a few times. If Flynn were here, I'm sure he'd have a jab ready."
m "\"I'm better at sidescrollers, you know.\""
"I get stabbed ten times in the chest by a guy whose nickname leaves a lot to be desired."
m "\"And fighting games.\""
c "\"You suck at fighting games, too.\""
"I grin at him."
m "I do not suck at fighting games."
m "\"I beat your ass last time, remember?\""
c "\"Only because you used the cheapest character and kept spamming the same move.\""
"It stings just a little, but he isn't lying, now that I think about it."
"I remember reading somewhere that the character I used isn't allowed in tournaments because of how broken he is. Naturally, he ended up being my favorite."
"Didn’t help that he was cute, too."
m "\"Well, you could've dodged it after the fifth time I used it.\""
c "\"Seriously?\""
"He takes another swig from his bottle. Some droplets fall on his hoodie."
c "\"That was a bullshit combo and you know it.\""
"Somehow, I manage to land a headshot on the guy who killed me, and Carl lets out a war cry that sounds like a dying frog."
show Carl Neutral with dis
"A bit too soon, as I stand out of cover a bit too long, which earns me a rocket to the face from the player who was standing right next to said guy."
show Carl Annoyed with dis
"I swear through gritted teeth, but I persevere. After I get killed by a guy who's blatantly shooting me through walls, however, I just give up."
c "\"Cheater.\""
show Carl with dis
m "\"It's whatever, I guess.\""
"I shift on the bed, kicking up my legs."
m "\"How about a couple levels in Claws of Destruction? I think I'm done with this one for now, if that's okay.\""

$ stop_all_audio(1.5)

scene bg unisunset with Fade(1, 0.3, 0.8)
play background "carwind.ogg" fadein 3

"After grabbing a granola bar from the kitchen cabinet, I'm finally on my way to the party."
"Only half of my mind's actually focusing on the road. The other half can't stop grumbling about the heat."
"I probably should've put on something other than jeans. Maybe shorts? Or would that look silly?"
"Vincent's place is near the other side of campus. It's a short drive, but in this heat it feels like miles."
"My parents' old car doesn't have air conditioning. It'll make visiting them back in Echo torture if I ever do decide to go back there."
"Perhaps one day. For now, I'm pretty content where I am."
play background2 "reststop.ogg" fadein 2
stop background fadeout 10
"Even though I've seen it often, I'm always struck by how gorgeous the campus looks at sunset."
"Echo's got some nice views, but Pueblo just kicks it to the curb in every aspect."
"It looks exactly like what the brochures make it out to be, which I've heard is pretty impressive for a place like this."
"I'm just happy it's got indoor and outdoor pools. I wouldn't be able to survive a week without those."
"Just driving in this weather is making me seriously long for air conditioning."
"There's a couple of cars on the parking lot in front of the building already. Mine looks out of place next to all the newer models."
"Then again, I suppose I'm a bit less affluent when compared to most of the other students here, with their muscle cars and scholarships."
"Didn't stop me from getting in, at least!"
python:
    vol("music", 0.3)
    vol("music2", 0.0)
    renpy.music.play("BGkitworth.ogg", "music", fadein=5, synchro_start=True)
    renpy.music.play("BGkitworthtrip.ogg", "music2", synchro_start=True)
"Some of the people I recognize from my class wave at me as I pass them, others ignore me and keep on smoking just out of sight."
"Judging by the smell, it's weed. I shouldn't be surprised. People seem to be a lot more lax about that here than they are back home."
"It might be one of the reasons Carl's mom had him go to this university."
"It takes me a couple of rings to realize the doorbell's busted - even longer to notice the tiny slip of paper stuck to the door telling me to go around the back."
$ vol("music", 0.5, 5)
"When I do, I'm met with the jovial grin of a wolf who already looks like he's had one too many."
"Vincent walks towards me, arms spread open wide."
"He's wearing a plain white shirt and the most casual shorts. Looks like I did put on too many layers."
"When I return the awkward hug he tries to give me, I can smell cheap liquor on his breath. A far cry from the diligent student he usually is during classes."
vi "\"Chase! How are you, man?\""
m "\"Doing just fine, thanks. Nice, uh, party you've got going on here. Lots of people.\""
"He chuckles, patting my back."
vi "\"There's more inside. Way more. Come on in, I'll show ya.\""
stop background2 fadeout 5
play background "roomtone.ogg" fadein 4
"I follow him into the building, through some small hallways."
"I notice Jenna standing at the other end when we turn a corner. It looks like she's busy reading something."
"I call out to her, but it doesn't seem like she can hear me. Just when I'm about try again, Vince tugs me into his room."

scene bg univincent with dis

play sound "dooropen.ogg"
$ vol("music", 1.2, 0.1)

"It's spacious, I'll give him that much. Busy, too. There's tons of people in the living room area alone."
"Some of them are playing beer pong, others are chatting - well, it's more like they're shouting to each other over the loud music."
"A girl from my class I've been working together on a project with - Lana - sits in a corner, playing with her phone."
"She's wearing a rather eye-catching, revealing red dress, one I'm pretty sure violates some university dress code. Sometimes, she giggles to herself."
"When I catch her eye, she immediately puts it away and steps over to me."

la "\"There you are, Chase! It's not like you to be this late.\""
"She grins from ear to ear, displaying her almost eerily white teeth."
"I lean against a wall, eyeing the crowd from a distance with her."
m "\"I had trouble finding a good parking spot. How's the party? Anything crazy going on?\""
la "\"It's been pretty routine so far. We were just getting to the good part.\""
"She smiles, tipping her muzzle towards a table."
la "\"The drinks are over there.\""
m "\"The good part?\""
"Next to me, Vincent nods, then tilts his muzzle toward the kitchen. His ears perk up."
vi "\"Lana and I went out and got something special for the guests.\""
"Part of me already knows what it's going to be. Probably booze or something."
"From what I've heard, it's what college parties are all about. I don’t know. This is the first one I’ve ever been to."
m "\"Something... special, huh? What is it?\""
la "\"You'll see.\""
"She grabs her phone again, tapping away on it like she's writing a novel."
la "\"It's going to be good.\""
"I kick back and enjoy the party for a bit."
"This \"good thing\" sounds pretty questionable, even more-so once Lana disappears into the kitchen before returning with a big silver tray."
"She passes it from person to person, everyone taking something from it. I try not to think about it too much."
"By the looks of it, it's not just the usual party snacks. It takes her a while to get through everyone, so I just grab a can of soda from the cooler on the table."
"It’s an off-brand. I guess the booze is more important."
"Finally, Lana thrusts the tray in front of my face with the widest of smiles."
"Her enthusiasm only leaves me disappointed when I find nothing but blueberry muffins."
"Blueberry muffins that smell kind of funny, like they've been out for a few days already. It's like those cakes Janice tried selling at the diner a few years back."
"I scratch the back of my head."
m "\"They're... they're just muffins. What's the big deal?\""
"A large lion with a long, braided mane pipes up behind her."
unk "\"Special recipe, man. They're edibles.\""
"I've seen the lion around campus before, but I don't know his name, just his face. Think he's in Carl's class."
m "\"Like, drugs?\""
"I take one of the muffins from the tray, and bring it up to my nose. Up close, it just smells awful."
"I narrow my eyes."
m "\"You'd better not be pulling a prank on me.\""
la "\"No prank. You should try one, Chase.\""
"She grins at me. She seems honest enough – not that I think she's trying to poison me."
"Now that I think about it, Carl told me about edibles once. About a year ago, I think?"
"Time's been ticking by way too fast ever since I graduated from high school."
"I can't remember what he told me about them, specifically. Something about not being able to get high from them?"
"Then again, Carl's probably used to stuff that's a lot heavier."
"Around me, people are already popping them in their muzzles like it's no big deal."
"This probably isn't a prank, then, unless they laced just one of them and this is some weird \"Russian Roulette, but with muffins\" kind of thing."
"Should I do this? I mean, I promised my parents I'd try and be responsible while away from home, but I don't think this would hurt."
"If it does, I can always just leave."
"Everyone's eyes are on me when I stick it in my mouth. This peer pressure makes the fur on the back of my neck stand on end."
"It's not as gross as I expected it to be, at least, thank God. I can still taste a bit of the blueberry in there."
"The weed part, though... well, I've never used weed, so I don't know what it tastes like. If this is it, it's nothing special."
"Hell, I don't even feel anything."
"Lana sets the tray down on the coffee table. A sheep sitting on the couch takes a muffin from it as soon as she leaves it alone."
la "\"How is it? You okay?\""
"I shrug my shoulders and drink my soda."
m "\"I don't really feel anything.\""
"Her lips stretch into a thin line, and she looks down at the tray again with a frown."
la "\"Huh.\""
"The lion speaks up again, taking a swig from the beer bottle he's holding."
unk "\"Maybe his wasn't all that strong.\""
vi "\"I sure as hell felt it when I ate mine. Maybe he's just immune to it or something.\""
"I shake my head."
m "\"Maybe I am, maybe I'm not. Maybe it just hasn't kicked in yet.\""
"Vince gives my back a smack."
$ vol("music2", 1, 10)
stop music fadeout 20
vi "\"Maybe. Didn't think you'd be such a heavyweight, Chase.\""
"It's a compliment I don't quite know how to take, or even comprehend."
stop background fadeout 10
"In fact, even standing feels difficult to grasp at the moment, and I find myself wobbling on my feet once he pulls back his hand."
show bg univincent as dorm at sidestory_trip with slow_dis
"Lightheaded doesn't even begin to {cps=25}describe it."
"Dizzy, nauseous, about to barf, that's a more apt description."
"I stumble back and forth to keep myself upright, try clinging to the nearest flat surface, but it doesn't really help. The ground is moving underneath my feet."
"Where there were two people before, I now see four, swaying from side to side as everything spins around me."
"It’s like I’m out on a raft in the middle of the ocean."
"Twenty minutes into the party, and I'm already completely out of it. This is probably setting all sorts of party records."
"Is this what being high feels like? What the hell was in those things?"
la "\"Shit! Chase!\""
"I recognize her voice, but when I turn to look at Lana she's just a blur, a featureless blob of red and white, ever shifting."
la "\"Chase, are you okay?\""
unk "\"What's wrong with him?\""
"Someone’s tugging at my arm, but gravity’s currently working against me in every possible way."
unk "\"Hold on. C'mon, get up.\""
show bg black onlayer screens:
    alpha 0.0
    block:
        ease renpy.random.randint(5, 7) alpha 0.5
        ease renpy.random.randint(5, 7) alpha 0.3
        repeat
"The moment I let go of that cabinet, I fall to the floor. Any moment now, I’m gonna sink through it. Where I’ll end up, I don’t know."
"My head hurts. My stomach hurts."
"The empty muffin liner is on the floor next to me. I can still make out the pink frills."
la "\"Someone call 911!\""
"The despair in her voice is almost palpable. She takes a hold of my wrist. My hand just flops around once she moves it."
unk "\"And get arrested? Fuck no.\""
la "\"Fucking shit, I don't know what to do. What do I do?\""
"I want to comfort her, tell her that I’ll be fine, even if it’s a lie, but no sound comes out of my muzzle."
"I try to sit and push myself off the ground, but my back just ends up hitting the floor again, followed by my ass."
"I hope I’m not being filmed right now."
"I just lay there."
"With my brain and body in complete disarray like this, there’s no way I’m getting up anytime soon."
"And despite the screams, despite the loud music, despite everything, I feel my eyelids grow heavier and heavier."
"The world goes dark before my very eyes, and the last thing I think about before I’m out like a light is how comfortable the cold floor is."

$ stop_all_audio(4)

scene bg black with Dissolve(2)
$ renpy.scene(layer="screens")
unk "\"Chaaase!\""

$ vol("background2", 0.3)
play background "roomtone.ogg" fadein 5
play background2 "dryer.ogg" fadein 5
"I return to the land of the living with a long gasp for air. The scent of very strong coffee fills my nostrils."
"As soon as I realize I have control over my body again, I thrash in the sheets, which only leaves me tangled when I settle down."
"My breathing is still harsh, uneven, but I’m okay. I’m okay."
"Sheets. I'm in a bed. Not the floor."

scene bg uni6 with slow_dis

"My paws shoot up to my eyes. I rub them before opening them. There’s a lot of gross shit in them. I’ve probably been out for quite a while."
"I can only imagine how bad I must be reeking right now.  I’m still wearing the clothes I was wearing last night, too. Fuck."
"The clock says it’s just past nine. How I managed to get back here, I have no idea."
"When I try to think about what happened last night, my head just starts hurting more."
show Carlu Pants at center with dis
"Carl waltzes in like it’s no one’s business, wearing nothing but pajama pants that look a few sizes too big even for him."
"There’s a piece of toast in his mouth and two mugs of coffee in his paws."
c "\"Ooh, you're up. Here, I made coffee.\""
m "\"I can see that. Thanks, though.\""
"He sits down next to me, exhaling through his nostrils, just eating his toast."
"We made rules about only eating at the table, but right now, I’m just glad to be awake and in good health."
"I speak up once my mug's half empty."
m "\"So what happened? How'd I get back here?\""
"Carl noisily swallows the last bits of toast."
c "\"Well, a few guys and one girl dropped you off here a few hours after you left.\""
"A shit-eating grin slowly spreads across his face."
c "\"You were completely zoned out, man. Talking about random shit and giggling like a kid. It was kinda funny to watch.\""
"I glare at him and fold my arms."
m "\"I'm sure it was.\""
"I'm honestly just glad all I got from it was a headache."
"I might not be invited to future parties, but I'd rather have that than end up dead because I couldn't handle a muffin."
c "\"I got you some water and put you in bed.\""
"He takes a large gulp of coffee and chuckles."
c "\"See? I can be responsible sometimes.\""
m "\"Sure.\""
"I set the mug down on the nightstand and wipe the rest of the sleep out of my eyes."
m "\"Goddamn, I feel terrible.\""
c "\"So, your turn to answer my question.\""
"He tucks his legs in like a kindergartener."
c "\"What happened last night? Did you really get drunk, or...?\""
m "\"Or?\""
c "\"Y'know...\""
"He mimics taking a drag from a cigarette."
m "\"No!\""
"My shakily-uttered denial's not the most convincing, but Carl doesn't seem to pick up on it, thank God."
m "\"Hell no. I was just... I just had a couple too many, that's all.\""
c "\"Even if you did try some, no fur off my back. I mean, look at me. I think I'm past just a little experimenting.\""
"I fall quiet. It’s a bit awkward to admit to doing something I used to tease Carl for, especially when I fainted almost immediately after trying it."
"Maybe I’ll tell him later. Preferably when we’re done with college, so it’ll be just one of many escapades."
"I do hope future escapades won’t leave me feeling this much like I got hit by a train, though." # lmfaoo
"I finally sit up. God, my back’s stiff as can be."
m "\"What have you been up to while I was out?\""
c "\"Studying, believe it or not. That and laundry.\""
"He stack the two cups and stands up."
hide Carlu with medium_dis
c "\"I washed your stuff, too. Should be done by the time you're done with your shower. You got a lecture to go to, right?\""
"Oh shit, yeah, the lecture."
"I bury my face in my paws and rub at my temples."
"I should be able to make it if I hurry. Looks like I woke up just in time. And surprisingly enough, I have Carl to thank for it."
m "\"Hey, Carl.\""
"He turns around, nearly dropping one of his coffee cups."
c "\"Hm?\""
"I shoot him a smile."
m "\"Thank you.\""
m "\"Wanna play some more Claws of Destruction when I get back?\""
c "\"You're on.\""
window auto hide
show bg black with medium_dis
$ renpy.pause(1, hard=True)
$ stop_all_audio(2, reset=True)
$ renpy.pause(2, hard=True)
$ renpy.end_replay()
