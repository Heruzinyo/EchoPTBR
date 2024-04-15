label saturday:



############################################
stop music fadeout 3.0
scene bg black
with slow_dissolve
play loop "nhysteria.ogg" fadein 20.0
$ renpy.pause(2.0, hard=False)
window show
unk "{cps=22}{font=ui/belligerent.ttf}I knew you'd be back..."
unk "{cps=15}{font=ui/belligerent.ttf}You all come back eventually..."
unk "{cps=15}{font=ui/belligerent.ttf}Why do you try to run away in the first place...?"
unk "{cps=15}{font=ui/belligerent.ttf}It doesn't matter..."
scene bg saturday0
with slow_dis
unk "{cps=15}{font=ui/belligerent.ttf}Even though you're here you're going to try and run again..."
unk "{cps=15}{font=ui/belligerent.ttf}Just stop..."
unk "{cps=15}{font=ui/belligerent.ttf}Because just like this town..."
unk "{cps=15}{font=ui/belligerent.ttf}You're only moving in circles..."
play background "highway.ogg" fadein 6.0
stop loop fadeout 9.0
window hide
scene bg saturday1
with dissolve
$ renpy.pause(2.0, hard=False)

stop music fadeout 10.0
$ renpy.pause(2.0, hard=True)
scene bg route93 with opening_fade


window show
m "\"Yeah mom, I brought it.\""  
m "\"No, no I've got everything.\""
m "\"No, TJ's with us, we picked him up yesterday...\""
m "\"No I...I {i}did{/i} call you yesterday, there was no answer.\""
m "\"Fine. Yeah, I'll try more than once next time.\""
m "\"So I'm...Of course they're clean!\""
m "\"Listen, I'm driving right now, so—\""
m "\"Yeah, so I shouldn't be on the phone, should I? I'm gonna hang up.\""
m "\"Okay, love you, too... bye.\""
"I sigh and finally hang up the phone, dropping it on my lap."
"TJ, next to me in the passenger seat, stretches back and scratches behind his ear."
t "\"Aww, that's cute. It's been a while since I've seen your mom. How is she?\""
"I shrug."
m "\"Fine, I think. She wouldn't tell me if she wasn't, anyway.\""
"TJ taps a foot against the dashboard before yawning."
t "\"Wow, it feels like we've been driving for daaays.\""
"Normally TJ wasn't one to whine, but the long drive was obviously getting to him."
"It was getting to all of us, honestly."
"I look over at him."
m "\"We're almost there. Why don't you listen to some music, or something?"
t "\"My phone's been dead for the past two hours. I didn't know it would take us eight hours to get there.\""
"I sigh."
"Whether that dig was purposeful or not, I still feel a little embarrassed."  
"I'll admit, I got us lost for a few hours. Route 93 is hard to find, even with the GPS."
"It's no wonder that Echo's in the state it's in."
j "\"You should have brought a book, those don't run out of batteries.\""
"I look up into the rearview mirror and see Jenna hold up a hefty book titled 'Cognition'."
"TJ sighs."
t "\"All of my books are on my phone...\""
m "\"Why don't you listen to the radio?\""
"TJ starts to reach for the dial."
j "\"Don't bother, all we get out here are hick stations. I have some music on my phone, though."
j "\"Do you have an AUX cable, Chase?\""
m "\"In this clunker? No, but like I said, we're almost there.\""
"Just having the three of us here is a little awkward...unbalanced."  
"I wonder if completing our little group will bring back that old chemistry."
"Thinking about seeing Carl, Flynn, and Leo again makes my heart skip a beat."
play sound "gps.wav"
"GPS" "\"Take exit 127 onto Flint Road.\""
"I jerk back to the present and press on the brakes as I swerve onto the exit ramp."

scene bg flint with dissolve

t "\"Whoa!\""
m "\"Sorry! Sorry...\""
# Swerve sound and image change
t "\"Chase! Come on, pay attention.\""
"TJ adds a little giggle to lighten the chastisement, but my face gets hot anyway."
m "\"Hey, me and Jenna went three hours out of our way to pick you up from CCU, you could have taken the bus.\""
t "\"No, no, I'm grateful. I'd just rather this not be the place I die, haha.\""
"We continue down Flint road for about fifteen minutes in silence while I avoid the ever-increasing number of potholes in the road."
"I think we're all a little nervous now as we get closer to our destination."
"Unsurprisingly, there isn't another car in sight."
j "\"You guys excited?\""
"I look in my rearview mirror again and see that Jenna has put down her book, staring out the window."
"I actually haven't given a whole lot of thought as to how I feel about the whole thing."
menu:
    "\"Yeah\"":
            $ Trip_Mood = "good"
            m "\"It'll be great to see everyone again. It's been way too long.\""
    "\"Not really.\"":
            $ Trip_Mood = "bad"
            m "\"Meh, I'm assuming we'll all just pick up where we left off.\""
    "\"I'm nervous.\"":
            $ Trip_Mood = "nervous"
            m "\"I dunno, it's been a while since we've all been together. Think things will be the same?\""
j "\"I meant Echo. Are you excited to go back?\""
m "\"Oh.\""
"I didn't really know how to answer that."
"Is excited the right word?"
"It's sure as hell stressful."
t "\"As long as we can go for a hike.\""
t "\"I don't wanna be sitting around in the motel all day.\""
j "\"Well it beats having a heat stroke in the desert. Are you seriously hiking the trail?\""
t "\"Oh come on, it'll be fun! At least I know Chase'll come.\""
"TJ smiles at me, raising his brows."
"It's too hard to say no to such an eager face...at least right now."
m "\"Yeah, yeah, of course.\""
j "\"Anyway, it sounds like you've only got the boys on your mind, Chase.\""
j "\"...Leo, maybe?\""
play sound "gps.wav"
"GPS" "\"Make a slight right onto Lake Emma Road.\""
"I ignore Jenna, pretending to be distracted with adjusting the GPS."
"A few more minutes of silence pass before Jenna speaks up again."
j "\"Soo, this news thing you're making, what's it about, exactly?\""
"I swerve a little to avoid another pothole."
m "\"A news packet.\""
m "\"If you remember there was that one crazy thing that happened here in the early 1900s.\""
m "\"I read a little bit about it and it's pretty fucked up.\""
t "\"Come on, Chase, language.\""
m "\"Just thought I'd do a little more digging.\""
m "\"Honestly, though, I just need to make something that looks good enough to pass with.\""
j "\"Well that sounds kinda fun.  Are you going to have enough time to hang out? I know Leo made some plans.\""
"This whole thing was Leo's idea, actually." 
"When I told him that I'd be coming down to Echo for spring break he suggested we all use it as an excuse to have a reunion."
"He says it hasn't been the same since the three of us left."  
m "\"Yeah, I should. I just need some b-roll and shots of the old, creepy locations.\""
m "\"Shouldn't take too long.\""
"I catch a flash of blue and see the lake to our right."
"The conversation dies down a bit and pretty soon we're all lost in our own thoughts."
"Finally, we round a bend and I start to catch some glimpses of the town."
"The tall, rusted signs for the gas station and motel loom over the rest of the old community."
"Lake Emma Road merges right onto Main Street, where the motel is at."
"Soon enough we're turning into the parking lot."

scene bg parkinglotday with dissolve

"There are only a few other cars in the parking lot."
stop background fadeout 3.0
play sound "engineoff.mp3"
"I park in the closest spot next to the door and switch off the ignition, relieved to be done with the driving."
"I sit back for a moment, rubbing my eyes."
m "\"Uuugh. I hope you're grateful, TJ. I never wanna drive that long again.\""
t "\"Thaaaanks, Chase!\""
play sound "cardoor.mp3"
"TJ hops out of the car, clearly happy to be out."
play music "neutral.ogg"
show TJ Sheepish with dissolve
t "\"Eeeuuuuugghhh!\""
"TJ puts his paws to his back and stretches out from toes to ear tufts, and I hear a few cracks."
t "\"Gosh, it feels good to be out of there.\""
"I smile as I follow him out and stretch as well, though less flamboyantly. It's good to see TJ reverting back to his old, cheerful self."
show Jenna Neutralhips behind TJ at right
with easeinright
j "\"Alright, I made the reservations, so I'll check us in.\""
j "\"You boys wanna bring in our stuff?\""
t "\"Sure!\""
hide Jenna
hide TJ 
with dissolve
"Me and TJ head around to the trunk of the car, getting our bags and camera equipment while Jenna heads inside."

scene bg motelfull with fade

"I'm pleasantly surprised."
"While it's a bit musty, the room is spacious and generally clean, a lot more than I was expecting from a town like Echo."
"Although I've lived in the town for most of my life, I've never actually been in the motel."
show TJ at left with dissolve
t "\"Hey, this is nice! And two double beds?\""
show Jenna at right with dissolve
j "\"Yeah, thought I'd get one of the nicer rooms, since everything here is dirt cheap.\""
"TJ sets his bags down on the bed."
t "\"So I guess this'll be me and Chase's bed.\""
t "\"Jenna can have her own, obviously.\""
j "\"That's...nice of you, TJ. Anyway, here are your keycards.\""
"She hands us both our keycards, which I slip into my back pocket."
t "\"So, when we gonna eat? I'm starving!\""
"My stomach grumbles. We haven't eaten since breakfast and it's late afternoon at this point."
"I pull out my phone, checking over my texts with Leo."
m "\"Leo said he's gonna get us some sandwiches from the diner.\""
t "\"Did you tell—\""
m "\"Yes, I told him to substitute the bread with lettuce for yours, TJ.\""
t "\"Nice!\""
j "\"Alright, well, I've texted everyone that we're here. Let's at least unpack.\""
j "\"It's going to get crowded and I don't want all our stuff in the way.\""
hide Jenna
hide TJ
with dissolve
scene bg motelbeds
with fade
"Half-an-hour later we've got all our stuff packed away in the motel drawers."
"Now, I'm sitting on the bed, toying with my camera equipment while TJ watches TV and Jenna organizes her school work."
t "\"You know you're on vacation, right?\""
t "\"And didn't you already get into grad school?  You should relax.\""
j "\"That's exactly why I need to be keeping up.\""
play sound "doorknock.mp3"
"There's a knock at the door and, being the closest, I get up to answer it."
m "\"I'll get it!\""
scene bg moteldoor with dissolve
"I look through the peephole excitedly and see a beanie cap with a pair of some very familiar horns poking through it."
"I grin as I unlock the door and swing it open."
show Carl at center with dissolve
m "\"Carl!\""
c "\"Chase!\""
"I slap paws with him and pull him into a hug."
"...and immediately get a whiff of the pungent scent of pot."
"Despite that, his embrace is warm and plush, and his belly squishes against my body like a pillow through his jacket."
"There is an underlying sturdiness, though, and I feel his biceps bulge around my shoulders."
"Had he been working out?"
"I put my paws on his shoulders and push him back, looking him over."
"He's changed a bit since I've last seen him. He's definitely bulkier, and the fur on his face is a bit shaggier."
"His eyes are a little red, and his expression is a little glazed, like he's daydreaming about someplace far away from here."
m "\"Still getting blazed, huh?\""
c "\"You know it.\""
"His jokey nature drops a bit as he gives me a genuine smile."
c "\"It's good to see you again.\""
"I feel warm inside as I smile back."
m "\"You too.\""
j "\"Is that Carl I hear?\""
hide Carl with dissolve
"Carl and I step back into the room, the ram remaining slouched as we do."
scene bg motelfull
show Carl at right with dissolve
show Jenna Smiling at center with easeinleft
c "\"Hey Jenna.\""
j "\"Carl! How've you been?\""
c "\"Not bad, just livin' life, like I'mma be...\""
"It sounds like he's starting to sing the lyrics to a song, but he trails off as we all look at him expectantly."
"He just smiles back."
m "\"Huh?\""
show TJ behind Jenna at left
with easeinleft
c "\"Hey, is that TJ?\""
t "\"Hi!\""
"Though he's smiling happily, TJ is outright crinkling his nose."
t "\"Still up to your old habits, huh?\""
"Carl shrugs."
"I'm starting to remember that it's something he does a lot. It's his answer to almost everything."
"It gets quiet for a moment, then I clap my paws together."
m "\"So, what have you been up to, Carl?\""
m "\"You're not online that often.\""
"Carl shrugs."
c "\"Oh, you know...just hangin' out.\""
show Jenna Smilinghips with dis
j "\"Must be kinda boring, considering it's Echo.\""
c "\"Not going outside helps, haha.\""
t "\"You been able to find a job? I know they closed the old Corner Market you used to work at.\""
show Carl Neutral with dis
c "\"Yeaah, been kinda hard since pretty much everything's closing around here.\""
c "\"On top of that I still don't have a car that can get me to Payton.\""
t "\"Oof, that's right.\""
t "\"You crashed the one your parents got you.\""
show Carl Depressed with dis
"TJ's grinning sympathetically, but Carl hunches further into himself, looking sulky."
show Carl Annoyed with dis
c "\"Man, don't kill my vibe.\""
j "\"What about school, been thinking about going back?\""
show Carl Rejected with dis
c "\"N-not really, maybe...\""
"Carl's starting to lose that faraway look as he narrows his eyes."
show Jenna Smiling with dis
j "\"You should! You went for what, a semester?\""
j "\"That's not really enough time to tell if you're really cut out for college.\""
j "\"Classes get easier to handle once you get used to it.\""
c "\"Yeah, well, it wasn't exactly the school work that was the problem.\""
t "\"You cooouuld try smoking less weed, that might help.\""
show Carl Surprised with dis
c "\"Wh—wha…?\""
show Carl Surprised at farright with easeinright
c "\"Is this—was I set up for an intervention, or something?\""
"Carl looks over at me, as if asking for help."
m "\"Hey, don't look at me. I had to deal with them for the past ten hours.\""
c "\"Yeah, guess I just forgot how naggy they can be.\""
t "\"That's because we care about you, Carl!\""
j "\"Anyway, I'm pretty sure Chase has been missing you ever since you left school.\""
"Carl and I were in the same class throughout school. As a result, we entered college together."
"We even roomed together for that one semester, which was a lot of fun. Of course I had missed him."
"Carl seems pretty eager to get off the topic, though."
show Carl with dis
c "\"Speaking of school, didn't you get accepted into Weston, Jenna?\""
j "\"Yep! Going into experimental psych. I start in the fall.\""
c "\"That's pretty cool, congrats.\""
"Carl turns back to me."
c "\"And you're into...journalism, right?\""
"He looks over the equipment, looking confused."
c "\"What's all this?\""
#pic of cam equipment on bed?
m "\"Oh! Yeah, one of the reasons why I'm out here.\""
m "\"I'm doing a news segment on Echo.\""
c "\"Sounds like the feel-good movie of the year, Chase.\""
m "\"That's what you get out of the feel-good town of the century, Carl.\""
c "\"Hehe, yeah.\""
"Carl scratches his muzzle before turning to TJ."
c "\"And you're doing...what again?\""
c "\"Sports...something...Bible olympics?\""
t "\"Athletic training, but yes, it's a Christian school.\""
"Carl gives a thumbs up."
c "\"Super. So we gonna eat? I'm hungry as hell.\""
t "\"Hell is a little extreme, there, Carl.\""
t "\"Not even YOU can be that hungry, hehe.\""
c "\"Mhm, sure. Where's Leo, he's bringing the sandwiches, right?\""
j "\"He actually just texted me that he's here. He was picking up Flynn.\""
t "\"So we're all gonna be here! Just like old times.\""
"TJ almost looks like that little kid lynx again, his ears twitching around with excitement."
play sound "doorknock.mp3"
stop music fadeout 2.0
c "\"Ooh, there they are.\""
hide Carl
with moveoutright
scene bg motelbeds
with dissolve
"I grip the bedspread and watch as Carl moves around the corner to open the door."
"I hear it open, followed by the distinctive deep, brassy voice of Flynn."
play music "comeover.ogg" fadein 3.0
f "\"Hey, why are YOU getting the door, fatty?\""
c "\"To get my sandwiches, dickface. I've got the munchies like a mother.\""
c "\"Er...where are they?\""
f "\"Leo has them...here he is.\""
l "\"Hey, they all in there?\""
"My heart skips a beat and my tail thumps the bed as I hear Leo's high baritone."
"There's some bustling before they start coming around the corner, bringing me face-to-face with the rest of my childhood friends."
show Flynn at center
with dissolve
"Flynn comes first, slinking in casually, his posture loose and relaxed, slouching."
"Unlike Carl, though, his slouch makes him look like he just doesn't give a fuck, as opposed to just trying to make himself seem smaller."
"He wasn't a shy guy, as evidenced by his open shirt."
f "\"And who you callin' a dickface?\""
"Flynn knocks Carl on the head, which made a loud thunking sound, but Carl just grins throughout."
f "\"Hey Jenna, TJ, Chase.\""
"He nods to each of us in turn, rubbing his knuckles."
hide Flynn
with moveoutleft
show Leo at center
with moveinright
"Immediately following him, his arms wrapped around two big, brown, paper bags, is Leo."
"He smiles over the tops of the bags, sweeping the room with his eyes along with his tall rectangular ears."
"He pauses on Jenna, then TJ, before finding me."
"His face immediately breaks into a full-on grin as he walks over to the bed I'm sitting on, setting down the bags."
"As he comes to a stop in front of me I reach out my paw to slap his, like I did with Carl."
"Instead, he grabs it to yank me up right into a tight bearhug, nearly squeezing the air out of me."
l "\"Chase!\""
l "\"Man, I missed you...\""
"Just like Carl, it seems like Leo's gotten bigger, and stronger. He lifted me up without even trying."
"The tension I've been feeling in my chest melts away like an ice cube on an Echo sidewalk."
"Everything's fine."
"All of that worry about how he was going to react was for nothing."
"...The hug IS lasting kinda long, though."
"I can feel everyone else looking at us."
j "\"And just like that he forgets we exist.\""
"Leo finally does pull back, then, smacking me on the shoulder before turning to greet Jenna and TJ."
hide Leo with dissolve
"I shakily sit back down, feeling a whole lot better now that the introductions are out of the way."
scene bg motelcouch with dissolve
show Flynn Annoyed at left with dissolve
f "\"Fuck, leave Carl in a room for five seconds and it smells like a goddamn skunk sauna.\""
f "\"The weed is just oozin' out of your pores at this point.\""
"Flynn theatrically plugs his nostrils as he pulls the window open a crack."
show Carl Neutral at right with dissolve
"Carl rolls his eyes, slouching further and jamming his paws in his pockets."
c "\"Oh shut up. I think everyone here agrees that my smell is a lot better than your shedding.\""
c "\"Nothing like leaving a big pile of lizard dust on the couch for the next person.\""
c "\"And by the way, dude, that skunk comment was speciesist.\""
f "\"And that lizard comment wasn't?\""
show Flynn with dis
"Flynn turns to me,  fanning air in from the outside with his hand."
f "\"What's worse, Chase: Carl's smell, or my...dustin' off?\""
show Carl with dis
c "\"Ha! Dusting off? That's not a thing!\""
c "\"Try saying 'white flakes that chip off of me with every step I take...except when I scratch my ass, then it's like a fucking blizzard of dead skin\""
c "\"...and some of it might land in your mouth.'\""
c "\"That's what you should call it!\""
f "\"Hey, you furballs do it too...it's just less noticeable.\""
f "\"Either way, it's hot in here!\""
c "\"Aren't you cold-blooded?\""
f "\"Someone turn down the goddamn thermostat!\""
show Carl Neutral with dis
show TJ at center
with dissolve
t "\"Somebody turn down your language, haha!\""
"TJ says it to him like a cheerful kindergarten teacher pep-talking a student into using his words."
f "\"...\""
t "\"...\""
"They stare at each other for about five seconds, Flynn's expression like a stone, while TJ slowly loses his smile."
show TJ Sheepish with dis
t "\"Uh...\""
f "\"Well Jesus butt-fucking Christ, I'll be sure to watch that.\""
t "\"Flynn!\""
show Flynn Happy
show Carl 
with dis
"TJ actually looks pretty upset, but Flynn just reaches out and yanks him into a choke-hold, the much shorter lynx easily dwarfed by the lizard."
f "\"Ah, shut up ya priss, I'm just kiddin'!\""
"TJ half-heartedly fights the hold."
"I guess TJ thought he'd get some respect, now that we're all adults."
t "\"Hey, ow!\""
t "\"Y—you still said it!\""
"Normally I might step in to help, but its been a while since I've seen Flynn and TJ go at it."
"It's just too funny to stop."
f "\"Look, no lightnin'! So much for your almighty go—OOF!\""
"TJ jabs his elbow back into Flynn's stomach, doubling the lizard over for a second."
t "\"Ha! See? God works in mysterious wa—OW!\""
"Flynn reaches up and grabs at one of the tufts on TJ's ears and yanks, earning a yowl from the feline."
c "\"Foul! Species features!\""
"Species features was something we made up to make our tussles a little more fair."
"It involved any distinct physical difference between our species that might pose as a disadvantage like my tail, Jenna's ears, or TJ's ear tufts."
"Carl was especially keen on it. Being a ram his horns were often used as leverage against him."
j "\"TJ! Come get your sandwich.\""
"TJ finally yanks himself out of Flynn's grasp, smoothing down his fur as he tries to look as dignified as possible."
t "\"Well, I can see things haven't changed...\""
"With that, TJ walks over to the table to get his food."
hide TJ with dissolve
"I can't help but laugh."
m "\"Hehe, I think TJ won that one by technicality.\""
c "\"Or did he? He might have fouled, too.\""
c "\"Flynn's got a soft lizard belly, haha.\""
"Flynn snorts, rubbing his stomach."
f "\"Oh, don't even try to tell me about soft, asshole. It looks like you swallowed a beach ball.\""
c "\"Speaking of which, food!\""
stop music fadeout 3.0
scene bg motelbeds with fade
"We all pass the bags around to get our food."
"A chicken sandwich for Jenna and TJ, roast beef for me and Leo, and three large veggie burgers that almost take up their own bag for Carl."
play music "neutral.ogg" fadein 3.0
"Flynn, as usual, isn't eating anything. I think it's a lizard thing."
"I keep my seat on the bed as I unwrap the foil around my sandwich."
"The smell wafts up from the beef, making my mouth water, and bringing some memories up with it."
"We'd all spent many nights at the old diner. I can remember the night me and Carl graduated."
"Leo took us all straight from Payton High to the diner, skipping out on the all-night graduation party for sandwiches and milkshakes."
"I take a huge bite and a yellow bell pepper slips out the other end, landing back in the foil."
l "\"Whoah! Slow down, you're going to choke.\""
"Suddenly, I'm almost falling over to the side as something heavy plants itself next to me on the bed."
show Leo at center with dissolve
"I quickly grab a napkin and bring it to my muzzle, wiping away the grease."
m "\"Ey, Leo...\""
"Leo chuckles at my embarrassment and unwraps his own sandwich."
l "\"Sorry if the bread is a little soggy. {i}Garrobo{/i} over here took his sweet time getting to the car.\""
scene bg motelcouch
show Flynn at left
with dissolve
f "\"Hey! Working in the town hall is serious business.\""
f "\"I don't have a family business I can just waltz out of, like you.\""
show Carl at right with dissolve
c "\"Hey, Flynn. I'll bet you that I can eat this whole burger in one minute.\""
f "\"...\""
f "\"Is that a fucking joke? Of course you can.\""
c "\"Hahahahaha! Yeah...But what about TWO burgers?\""
scene bg motelbeds
show Leo
with dissolve
l "\"Don't choke, Carl.\""
"I decide to keep the conversation on Leo's job, since that's the whole reason why he's still here."
m "\"Is business still pretty good?\""
l "\"Yes! Payton's getting bigger, so is the number of customers.\""
m "\"I guess it's a good thing your dad moved it out of Echo, huh?\""
l "\"For sure. The place is turning into a ghost town.\""
l "\"It probably will be in another decade or two.\""
m "\"By some standards it already is.\""
"I take another bite of my sandwich, biting right into another bell pepper."
"I'd forgotten how good the diner food is."
scene bg moteltable
show Jenna Smilinghips at left
show TJ Rejected at center
with dissolve
"I notice TJ sitting next to Jenna at the table, picking unhappily at his lettuce wrapped chicken."
"Jenna seems to as well as she leans towards him."
j "\"What's wrong, TJ?\""
t "\"It's just...nevermind, it doesn't matter.\""
j "\"Are you sure?\""
t "\"It's just the mayo, I forget they put it on everything here, hehe.\""
"Jenna lifts up the bun on her sandwich, inspecting its contents."
j "\"Hmm, none of the mayo really got on my chicken. Here—\""
t "\"No, you don't have—\""
"Jenna picks up TJ's sandwich and swaps out his grilled chicken."
"She rips off the layer of mayo-tainted lettuce from his lettuce bun before swapping her chicken in.\""
j "\"There! How's that?\""
t "\"Th—thanks...\""
show TJ Sheepish with dis
"It's then that TJ looks up and sees Leo and I staring at him. I see his ears flatten in embarrassment."
t "\"What!?\""
l "\"Hehe, nothing TJ, nothing.\""
scene bg motelbeds
show Leo at center
with dissolve
m "\"So are your parents still letting you live in the house here in Echo?\""
l "\"Yes, we actually tried to sell it last year, but of course no one bought.\""
l "\"I think two people came to look, but took off once they saw the town.\""
l "\"Anyway, my parents are living in Payton in a house twice as big as the old one.\""
m "\"Well, it must be pretty cool living in your own house.\""
l "\"My parents aren't constantly breathing down my neck so that's, you know, nice. \""
"Leo's already finished his first sandwich, and now he's unwrapping the second."
"He sure could eat a lot."
m "\"How many people are still here, anyway? In the town, I mean.\""
"Leo takes another bite and I hear the crunch of the peppers through his muzzle. He chews thoughtfully for a moment before swallowing."
l "\"Hmm, not too sure.  Of course I know almost everyone here, but most don't actually live here anymore.\""
l "\"Most everyone's turned their old house into a sort of vacation home, now.\""
m "\"Really, why?\""
"I can't imagine anyone coming here for a vacation..."
"...unless your hobbies are meth or dying of heat stroke."
l "\"Well, they've all got their old houses here, and it's cheap to build.\""
l "\"And the town is actually trying to turn that old lake into a recreational thing.\""
m "\"Lake Emma?\""
l "\"Yeah. They're putting in docks and stuff.\""
m "\"Huh...\""
"Lake Emma is the old reservoir just a few minutes outside of town. As kids, we used to play around there all the time."
"It was generally an ugly place; dead fish on the banks, a terrible smell, and mosquitoes everywhere."
"Then again, it could have changed since then. I haven't been there in...twelve years now. None of us have."
"Thinking about the lake is making my stomach tighten again, forcing away my appetite in the process."
"It's been so long at this point, I need to learn to get over things..."
"Actually, that reminds me."
"The others are pretty deep in their own conversations, but I lower my voice anyway, leaning into Leo."
m "\"Hey, Leo.\""
l "\"Mmmh?\""
"Leo turns to me. He had been in the middle of a massive bite and now he has a bell pepper half hanging out of his muzzle."
"That throws off my train of thought for a second."
m "\"Uuuh...oh yeah. So I wanted to get some shots of the lake for my project.\""
"Leo ducks his head to pull out the pepper from his muzzle, only to shove it back in a second later."
"He chews for a while, but his ears are still tipped towards me, so I go on."
m "\"It's kind of important to Echo's history. Anyway, you told me that on Monday everyone's free during lunch.\""
"I can tell by the set of Leo's ears that he knows where I'm going, and he's not too into the idea."
"I quickly go on."
m "\"Of course, we don't have to, but it's been a long time, and if the town is making it look better, it could be fun...\""
l "\"Listen, Chase...\""
"I feel my face burn a little under the fur."
m "\"Sorry, it was a dumb idea...\""
l "\"No no, Chase, if it were up to me, I'd definitely do it, it's just...\""
"Leo looks towards Flynn, and I do as well, finding him still bantering with Carl."
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "\"It doesn't matter how fucking fast you eat, I'm not gonna be impressed.\""
"He's got that classic Flynn look on his face where he's pressing his lips together, trying not to smile."
c "\"What if I ate all THREE?\""
f "\"You've already eaten most of the first one, so that's not gonna happen now, is it?"
scene bg motelbeds
show Leo at center
with dissolve
"I look back down at my sandwich."
"I suddenly feel really guilty. Here I am, back after three years, just assuming that I know how everyone feels."
"Now I'm kinda feeling like an impostor."
"Leo notices, like he always did, and he nudges me with his shoulder."
l "\"Hey, don't worry about it, it's not your fault.\""
"Suddenly, Leo's ears perk up, and I know he's suddenly had an idea."
"His ears made him easily readable, just as reading people came easily to him."
"It made it all the more impressive that he was able to tell what most of us were thinking, considering my short, stubby ears."
"...Or Flynn's lack thereof."
l "\"Listen, there's a cool little spot by the river that's actually pretty close to the lake.\""
l "\"We could have lunch and you could walk over and get your shots!\""
"The idea makes me feel a bit better."
m "\"Alright, that could be fun. Also, this motel doesn't have a pool, so it'll be really nice to swim in something.\""
l "\"Heh, otters and their waters. Anyway, I'll have to ask Flynn, but I think he'll be okay with it.\""
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "\"What would REALLY impress me is if you didn't eat the rest.\""
c "\"...\""
c "\"You're a funny guy, Flynn.\""
"Carl goes right back to shoving the next burger into his mouth as Flynn looks on in mild disgust."
"He suddenly notices us watching him and he gives us an odd look, but that slowly morphs into a smirk as he focuses on Leo."
f "\"You're lookin' pretty happy there, Leo. Not like you've been for the past three years.\""
scene bg motelbeds
show Leo at center
with dissolve
"I furrow my brow in confusion and look up at Leo. I see him shift and he's giving Flynn a look that I don't quite understand."
l "\"Well of course I'm happy to see us all back together again.\""
"I look from Leo to Flynn, and it's pretty easy to imagine a bolt of electricity between them."
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "\"You should have seen him, Chase. He'd go days without smiling.\""
c "\"Agreed, Leo's been kind of a dick ever since you guys left.\""
f "\"Isn't Jenna a counselor? Hey, you should have a session with Leo.\""
scene bg moteltable
show Jenna at left
show TJ Neutral at center
with dissolve
j "\"Um, I'm still an undergrad. I'm not going into counseling, anyway.\""
j "\"That would just make me sad.\""
"TJ is busy trying to hold his sandwich together and eat it at the same time, not very successfully, but he looks up as well."
t "\"Leo depressed? It's hard to imagine you NOT smiling. You seemed fine online.\""
j "\"Has something been going on, Leo?\""
scene bg motelbeds
show Leo Rejected at center
with dissolve
"For the first time since he's arrived, Leo looks truly uncomfortable."
"You don't see him like that very often."
"Flynn, on the other hand, has his trying-not-to-smirk face on."
show Leo Embarassed with dis
l "\"Wh-I-I...\""
"Leo pauses, pinned down by everyone's eyes in the room, then he takes a frustrated breath."
l "\"Can't people be sad sometimes? Yes, things have been more...have been harder, but I'm fine.\""
l "\"I think it's pretty clear that FLYNN-\""
"Leo flicks his long muzzle at the lizard."
l "\"-Is just trying to get some reactions.\""
scene bg motelcouch
show Flynn Teasing1 at center
with dissolve
f "\"Suuure, I'm just sayin' you're back to your old self. But seriously, it's great...\""
scene bg motelbeds
show Leo Neutral at center
with dissolve
"Leo makes a snorting sound."
"I'm about to ask Leo what's so stressful when he lifts his paw up again to take a bite of his almost-finished sandwich."
stop music fadeout 2.0
"I go quiet as I look at his paw."
"A silver anchor, tied around his wrist with leather. The word otter is etched into the shank of the anchor, the name Chase is engraved into the stock."
"Why was he still..."
t "\"CHASE!\""
"I jump as TJ's voice breaks through my trance, bouncing on the bed once I come down."
"Leo looks at me as the bed wobbles, an eyebrow raised."
scene bg moteltable
show TJ at center
with dissolve
"TJ puts a paw to his muzzle."
t "\"Oops! Sorry, you were just kinda staring off into space.\""
m "\"Yeah, uh, just thinkin' about stuff. What's up?\""
t "\"We were just talking about {i}The Last Game{/i}. Didn't you tell me that you saw that movie on the drive here?.\""
stop music fadeout 3.0
scene bg motelcouch
show Carl Annoyed at center
with fade
play music "banter.ogg" fadein 3.0
c "\"I really don't get you right now, TJ...{i}The Last Game{/i} was the WORST Lion's Brigade movie!\""
scene bg moteltable
show Flynn at center
with dissolve
f "\"You're just mad 'cuz they didn't follow the comics.\""
scene bg motelcouch
show Carl Neutral at center
show TJ at farleft
with dissolve
t "\"Yeah, Carl, as a movie it was just better...I'm sure the comics are great too, though, hehe.\""
scene bg moteltable
show Flynn at center
with dissolve
f "\"Naw, the comics are shit. Carl tried showin' 'em to me once.\""
scene bg motelcouch
show Carl Annoyed at center
show TJ at farleft
with dissolve
c "\"Bwah!!??\""
c "\"See?  This is the problem.  They never follow the source material and no one cares because they have no respect for the originals, man.\""
scene bg motelbeds
show Leo at center
with dissolve
l "\"You're waaay too picky, Carl. {i}The Last Game{/i} was a great movie!\""
c "\"Not you too, Leo!\""
scene bg motelcouch
show Carl Annoyed at center
show TJ at farleft
with dissolve
t "\"I don't know, I think Lion's Brigade was always a bit too violent for me, what with all the shooting and punching.\""
t "\"I've always liked the Trinity Weasel.  She's the thinking man's superheroine.\""
"Carl waves his paw dismissively."
c "\"The Trinity comics have always been pretty lame. They're jerk-off fodder for lonely nerds...and so's the movie.\""
l "\"Ha! You mean like yourself?\""
show Carl Rejected with dis
c "\"Hey...\""
scene bg moteltable
show Flynn Teasing1 at right
with dissolve
f "\"Hold up, we're talking about Trinity now? Julia Blasco...She's hella fine!\""
f "\"Never seen an ass like hers on a weasel before.\""
scene bg motelbeds
show Leo at center
show Jenna at farleft
with dissolve
j "\"That's because it's fake.\""
scene bg motelcouch
show Carl Neutral at center
show Flynn at farright
show TJ at farleft
with dissolve
t "\"N—no, I just like the story.\""
t "\"It's really kind of deep, if you think about it.\""
f "\"It was hard to think about when half the shots are slo-mo and she's doing all these flips and backbends and shit.\""
scene bg motelbeds
show Leo at center
show Jenna at farleft
with dissolve
j "\"Hmm? I didn't think that was your sort of thing anyway, Flynn?\""
"Flynn doesn't have time to retort before Jenna shifts her attention, seemingly coming to TJ's defense."
j "\"Come on, Trinity DOES have more story going on than your average superhero movie.\""
j "\"I think it's great that you like her character over all the meat-heads.\""
l "\"Yeah, they just stuck in all the boob shots to reel in the dummies.\""
scene bg motelcouch
show Carl Neutral at center
show Flynn at farright
show TJ at farleft
with dissolve
f "\"Of course that's easy for someone like {i}you{/i} to say. Besides, I see what's going on here.\""
f "\"Maybe you should watch {i}Luche Lobo{/i}, TJ. He's shirtless the whole time.\""
show TJ Sheepish with dis
"TJ's ears go flat, tufts pointed at the ground."
show Flynn Teasing1 with dis
f "\"I'd better stop it with all this saucy talk. The only way this could get any more awkward is if ya got sprung!\""
"We all groan in unison, but TJ shoots right back:"
show TJ Annoyed with dis
t "\"And knowing you, that's {i}exactly{/i} what you want to happen, isn't it, Flynn?\""
show Carl 
show Flynn Surprised
with dis
"That gets a few surprised chuckles."
c "\"Daaaamn TJ, where'd that come from?\""
"It isn't that it is a particularly good joke. It's that it came from TJ that makes it so funny."
"I don't think I've ever heard him talk like that."
show Flynn Happy with dis
"Even Flynn can't keep from grinning a little bit."
scene bg motelwindow with slow_dissolve
"We talk late into the afternoon."
"At this point all of my worries have disappeared, leaving a happy, warm feeling in its place."
"It seems silly that I'd been so nervous earlier. In fact, I'm starting to look forward to the rest of the week."
scene bg motelbeds
show Leo at center
with dissolve
l "\"Alright, alright.\""
"Leo steps forward, indicating that we should all shut up."
l "\"Now, we all need to remember that Chase is here to do his school project, so that comes first.\""
l "\"But! I did make a few other plans for things that we can do on his off time.\""
l "\"I'm pretty sure all of us know that we're going to Southwest Adventures tomorrow, so I'll pick these two up—\""
"He jerks his head towards Flynn and Carl."
l "\"—then swing by the motel to get you guys at 9, alright?\""
j "\"Sounds good.\""
l "\"Then I was thinking about doing some stuff in Payton towards the end of the week, but we'll make those plans later.\""
l "\"In between those times we should find time to hang out as well, make the most of this.\""
"Leo looks about done, but suddenly snaps his fingers, as if remembering something."
l "\"Oh yeah! Chase, I saw you had a camera.\""
l "\"Think you could get a pic of us? It would be nice for all of us to have something that isn't camera phone quality.\""
m "\"Oh, sure. I was messing with the self-timer earlier.\""
m "\"Should be able to get it to work.\""
scene bg motelfull
with dissolve
"After a few minutes of me adjusting the tripod, and Leo adjusting everyone at the end of one of the beds, we manage to get into position."
m "\"Aaaalright, here goes...\""
"I set the timer and fast-walk to the spot Leo saved for me."
play sound "camera.mp3"
window hide
scene groupphoto with transition_fade
$ renpy.pause(3.0, hard=False)
stop music fadeout 4.5
scene black with slow_dissolve
$ renpy.pause(1.0, hard=False)
play loop "crickets.ogg" fadein 1.0
window show
"For the next two hours we watch a movie on TV, not really paying attention, mostly catching up with each other on how we'd been."
"It's good to be back and it feels like we're all just picking up where we left off three years ago."
"It's really nice."
"Finally, at about 10, Leo, Carl, and Flynn head out."
"I spend the next twenty minutes tinkering with the equipment, making sure it's all in order for shooting the next day."
"Once TJ finishes getting ready for bed in the bathroom, I do as well before getting into bed, head-to-toe with TJ."
"There's a soft glow from the corner as Jenna sits at the table reading something."
"I lay in bed, staring at the ceiling, waiting for her to go to sleep..."
stop loop fadeout 10.0
scene bg creepylake
with opening_fade
play music "meeting1.mp3" fadein 10.0
"There's a chain attached to my ankle as I walk away from the lake, my legs and feet caked in mud."
"I look back, seeing the chain snaking back around the rocks and reeds before disappearing into the water."
"Looking ahead again, I see Leo. He's smiling, waving at me."
"I walk towards him and the chain stays slack, pulling easily out of the water."
"\"There's an anchor in the lake,\" I say."
"I stare at him, but he doesn't say anything and just keeps on smiling."
"I crouch on the rocks, wrapping the chain around my wrist a few times."
"Leo kneels next to me, rubbing my back and sticking out his arm to compare our \"bracelets\", saying that everyone gets one."
"He seems happy, but now I'm stuck here. I can't even stand up to walk."
jump wideshot