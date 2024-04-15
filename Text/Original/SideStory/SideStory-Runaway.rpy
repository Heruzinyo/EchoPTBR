# Runaway
# by Gausk

label sidestory_runaway:

stop music fadeout 3.0
scene bg black
with slow_dissolve

pause 1
play background "fan.ogg" fadein 7
pause 2
call sidestory_title("May 2010") from _call_sidestory_title_4
pause
call sidestory_title("May 2010", end=True) from _call_sidestory_title_5

scene jashouse2 with medium_dis

"The sun has begun to set. If I want to avoid Dad and Jeremy, I'll have to leave soon."
"I take another look around my room, just to make sure I haven't missed anything."
"With my bookshelf empty and all the clothes packed away, it feels a little bleak, gloomy."
"If not for the posters still hanging on the walls, you'd be forgiven for thinking no one had lived here at all."
"It reminds me of one of those TV shows where they explore abandoned, haunted buildings."
"And while this place isn't particularly haunted – at least, as far as I know – plenty of terrifying things have happened here."
"Part of the reason I want nothing more than to leave it all behind me."
"I zip up the duffel bag - not particularly easy with my paws trembling so much - and I take my phone out of my purse, reading Chase's messages again."
"He says he'll be waiting at the diner."
"When I ask if Leo will be coming along, he replies with an emoticon shaking its head. Figures."
"I hoist the duffel bag over my shoulder and waddle towards the door, snagging my necklace – the one Jeremy gave me – off the nightstand along the way."
"I put my ear to the door and listen for any signs of my family before even thinking of opening it."
"Usually, I can tell when they're home by the shouting and screaming of Dad and Jeremy's daily arguments, but I want to be sure."
"Once I'm sure the coast is absolutely clear, I open the door and start walking."
"First out of my stuffy room, then out of the hallway, then out of the house."

scene bg neighborhood with medium_dis

play audio "dooropen.ogg"
play background2 "eveningcall.ogg" fadein 0.2
stop background fadeout 0.3
"I lock the door and put the key under the doormat, looking over my shoulder at the house where I've spent the past seventeen years of my life."
"It's just a house to me. Not a home. Hell, school feels more like a home than this place does."
"I expected to feel regret setting in about now, but I can only grin like an idiot."
"Simply walking out that door feels like an achievement – I don't think I've ever felt this kind of rush before."
"I'm free!"
"I'm not gonna become another Janice, working a mindless, soul-sucking job while sighing to everyone who'll hear–"
"–not listen, because people in Echo never listen–"
"–about what could and should have been."
"I'm going to college, on the other side of the state, far away from this dusty, dried-up shithole."
"I'm aware of the consequences, of the potential problems that could await me, yet the pros far outweigh the cons."
"I run a finger over the gemstone in the necklace, and feel a pang of guilt in my stomach."
"Jeremy will have to deal with Mom and Dad all on his own now."
"And while he certainly hasn't made my life any easier, he doesn't deserve that. Nobody does."
"If it hadn't been for Clint, he might've turned out alright."
"But I’ve made up my mind."

scene bg nightroad with medium_dis
play background "dirtroadwalk.ogg"

window show
"And so I head towards the diner, struggling to keep myself upright, duffel bag in one paw, my purse in the other."
"And while people walking around with shifty-looking bags at night isn't an uncommon sight in Echo, I stick to the shadows regardless."
"I try to resist the urge to look over my shoulder every three steps."
"Jeremy could be hiding in every shadow, or so my mind tells me. I feel like a child again."
"I really shouldn't have packed this much, these bags are way too heavy."
"After nearly tripping over several rocks, I can finally breathe a sigh of relief when the familiar lights of the diner come into view."
"On the other side of the road stands the motel, a lone car parked in its parking lot."
"Even as a dot in the distance, I recognize it instantly – it's Chase's parents' car."
show bg parkinglotdusk with dis
"I walk over as fast as I can on these heels."
show Chasey N with dissolve
"Chase is leaning against his car, his face illuminated by the light of his phone."
"Once he notices me walking towards him, he slides it into his pocket. With his paws still in his pockets, he walks to the edge of the parking lot."
stop background fadeout 1
"The motel's parking lot is quiet and dark, but not unpleasant."
"It's cooled down considerably – not quite to the point where I'd be worried about catching a cold, but cool enough to not get heat stroke after taking ten steps."
m "\"Lemme handle this.\""
"He hunches over with a grunt as he lifts my duffel bag from my paws."
show Chasey Disc with dis
m "\"{i}Shiiit,{/i} Jas, did you fill this thing with bricks?\""
"I giggle at the sight of him, folding my arms."
jas "\"Just the necessities, really. Clothes, a toothbrush, something to read...\""
show Chasey N with dis
"He grins."
m "\"All your manga, too?\""
jas "\"Most of it. Just the issues I haven't gotten around to reading yet.\""
play sound "cardoorsecondhalf.ogg"
stop background2 fadeout 0.1
"Maybe I should've filled it with bricks. It would've made for a nice prank."
$ vol("sound", 0.7)
hide Chasey with dissolve
play sound "enginestart.ogg" # volume 0.7
play background2 "engine.ogg" fadein 3
"Once we get seated, my duffel bag in the trunk and my purse between my legs on the floor, I look out the window, to the road I took to get here."
"I catch Chase's eye."
m "\"Ready to go?\""
"He puts a paw on my shoulder."
"It's warm, and his paw pads are a little damp with sweat, but it's the most comforting thing I've felt all day."
"I melt into the touch, just a little."
"I nod."
jas "\"As ready as I'll ever be.\""
"I lean forward to turn on the radio."
play audio "switch.ogg"
$ vol("music", 0.5)
$ pan("music", -0.35)
play music "emo.ogg"
"One of Chase and Leo's songs, or as Flynn likes to call them, {i}\"emo garbage with shitty lyrics\", starts playing.{/i}"
"Probably explains why the car reeks of Leo's cologne."
"While I don't particularly like the music, it's still miles better than the country music that usually plagues the local radio stations, so I leave it on."
"Chase raps his fingers on the steering wheel in time with the beat."
"When he notices I'm looking, he quickly averts his gaze, messing with the rearview mirror instead."
"I chuckle."
"He's cute."
"A different brand of cute than TJ, but cute."
$ vol("sound") # reset channel
jas "\"Where is wolf boy, anyway? Out with the pack?\""
m "\"His parents needed him at the shop. He said it was urgent.\""
jas "\"I thought his parents' place closed at six?\""
"He shrugs."
m "\"They call him at the weirdest times. I've gotten used to it.\""
"Still, he glances at his anchor bracelet, eventually straightening it out so the tiny anchor rests on top of his wrist."
"It's a habit of his I've noticed ever since they went out to buy those things."
jas "\"You guys okay?\""
"He sighs."
m "\"We've been better.\""
m "\"I feel like... like we've got different ideas about our future, where we're gonna take this... this thing we have, once we're done with school.\""
"I had a hunch. Well, less of a hunch, and more noticing they weren't eating each other's faces last time I saw them."
jas "\"Do you want to talk about it?\""
m "\"It's no big deal. We'll work it out eventually.\""
jas "\"It sure {i}sounds{/i} like a big deal to me. Have you mentioned it to him?\""
"He tilts his head back."
m "\"It's not just something you can bring up out of the blue, Jas.\""
jas "\"If it's bothering you, you should do something about it. It'll just get worse if you don't.\""
play background "highway.ogg" fadein 10
stop background2 fadeout 12
m "\"I'll ask him about it when I see him.\""
"He says it with a tone of finality."
"The anchor drops from the top of his wrist again."

scene sunset with medium_dis

"We're on the road now, moving further and further away from the diner and the motel until they're just blots in the distance."
show nightoverlay onlayer screens:
    alpha 0.0
    ease 60 alpha 1.0
"If there's one good thing about Echo, I suppose it's the spectacular sunsets."
"It reminds me of all the evenings I spent at TJ's house, sitting in the backyard with his family, just to watch the sun slowly sink."
"Sometimes, his mother would pull out a photo album, and tell me all about where they came from, what nature there was like."
"Chase looks at me from the corner of his eye."
m "\"We can stop, if you'd like.\""
m "\"If you want to say goodbye-.\""
jas "\"I'm fine.\""
"My response is a little snippier than I would've liked. I make the effort to soften my voice."
jas "\"You... you can keep driving, Chase.\""
m "\"Alright. I'll have to stop for gas when we get to Payton, though. I promised my mom I'd fill up the tank.\""
jas "\"I don't mind.\""
"I reach into my purse to grab my wallet, but he raises his paw."
m "\"I'll pay. Don't worry about it.\""
jas "\"Are you sure? I mean, you're going all the way out there for me.\""
"He smiles."
m "\"Seriously, don't sweat it.\""
"It's hard to do, given the gravity of the situation, but it's a smile I gladly return."
jas "\"Thanks, Chase.\""
$ vol("loop", 0.3)
play loop "phonebuzzlong.ogg"
m "\"It's what friends are for, right?\""
$ vol("loop", 0.6, 0.2)
"I take my phone out of my purse. Dad's calling."
"He probably got home and noticed I wasn't there."
$ vol("music", 0.2, 10)
"The fur on the back of my neck prickles as I look at the screen. I'm tempted to pick up."

show bg highwaynight onlayer screens:
    alpha 0.0
    linear 18 alpha 1.0
# show nightoverlay onlayer screens:
#     linear 18 alpha 0.0

"The song playing on the radio has stopped registering. All I can hear is buzzing."
stop loop fadeout 0.3
"Finally, I shake my head and hit the ignore call button, thrusting the phone back into my purse, taking out a manga instead."
"I'm not listening to anything he has to say anymore."
m "\"What was that about?\""
jas "\"Dad called.\""
m "\"You haven't even been gone that long.\""
"He stops rapping his fingers on the steering wheel and eyes me nervously."
"It reminds me of TJ a little, the way his fur bristles whenever something catches the lynx off guard."
m "\"You think he knows?\""
"I flip through my manga, taking out my bookmark."
jas "\"I don't know. And I don't really care.\""
stop background fadeout 10
"I start reading."
"In a town as dull as Echo, manga and anime have always filled the void pretty nicely."
"They've been an escape for me, a gateway to cultures and countries beyond this nothing town, places where I don't have to deal with my family."
"Strangely enough, I never got into Western comics much."
"Carl got me one of those collector's edition comics for my birthday once, but I sort of gave up on it when I hadn't finished it after a year."
"Mental note to get back to that one soon."

$ vol("background", 0.4)
$ vol("background2", 0.2)
play background "restroomamb.ogg" fadein 10
play background2 "lightbuzz.ogg" fadein 3 # volume 0.5

stop music fadeout 5

hide sunset
hide nightoverlay onlayer screens
show bg highwaynight onlayer screens:
    linear 2.0 alpha 0.0
scene bg conveniencenight with Fade(2.0, 0.1, 1.5)

$ renpy.scene(layer="screens")


# "Chase taps my shoulder."
# m "\"We're here.\""
"The gas station between Echo and Payton is a perfect representation of the miserable state Echo is in."
"It's old and decrepit, to say the least, and what little staff it has consists mostly of junkies saving up for their next fix."
"Usually, they get it from the dealers that show up at night around here."
"If the gas wasn't the cheapest around, I doubt it'd see any customers at all. Most people already try to avoid it whenever they can."
m "\"This place gives me the creeps. Looks like it came straight out of a horror movie.\""
jas "\"It does.\""
"I smirk at him."
jas "\"Do you think there's any spiders around?\""
"He turns to me, an interesting mixture of fear and frustration etched on his face as his muzzle opens, only to close again, like a fish trying to get some air."
m "\"Don't even {i}joke{/i} about that!\""
jas "\"There's probably some really big ones...\""
"I walk my fingers up his arm to the back of his neck, then pinch him."
jas "\"{i}Boo!\""
m "\"Jasmynn!\""
"He swats my paw away with a yelp."
m "\"Stop it!\""
"I laugh."
jas "\"I swear, TJ keeps it together better than you, sometimes.\""
"He snorts."
m "\"Only because you go easy on him.\""
"He's not wrong."
"The one time I played a Chase-caliber prank on TJ, he'd spent hours crying in his room afterwards."
"It was the only time I'd ever seen his mother legitimately angry, a stark contrast to her usual sunny disposition."
"Not much scares me, but that was a frightening experience."
jas "\"Hey, he's been through a lot already. I don't want to scar him for life.\""
"He raises a brow."
m "\"But {i}I'm{/i} fair game?\""
jas "\"Well, I get the best reactions out of you.\""
"He sighs."
m "\"Foxes.\""
"I always feel a little guilty about playing into Chase's arachnophobia (or \"Chase's little spider problem\", as his mom always calls it)."
"But he's just so damn fun to tease."
"My greatest moment has to be when we emptied an entire bag of those tiny rubber spiders in his backpack while he was changing for gym class."
"I can still remember the look on his face when he opened it to get his lunch. Priceless."
jas "\"Aw, did I offend you, {i}chula?\""
"I give him a playful pat on the back. He pulls back almost instantly, as if he's afraid I'll do something."
jas "\"Want me to call Leo so he can kiss you all better?\""
"The exasperated look on his face is pure gold. If it wasn't so dark, I'd be filming right now."
m "\"Don't-. Jasmynn...\""
"He starts fiddling with his bracelet again."
jas "\"I think there's only hillbilly serial killers 'round these parts, anyway. Nothing to worry about.\""
"After getting another look from him, I lay off, completely satisfied."
"Chase gets out of the car to pump gas. I look out the window again, to the convenience store."
"There are a few truckers here, but not much else."
"This place could use a clean. Shame that most likely won't ever happen – and probably hasn't since, what, the 50s?"
"The most recent addition to the building is a poster for the Trinity Weasel movie starring Julia Blasco... which came out about two years ago."
"I think TJ was the only one who really liked that movie, come to think of it."
"My stomach rumbles when I notice the sandwiches set out on the counter."
"I eye the clock. It's about 8, and I haven't had dinner."
"While I could've grabbed something at the diner, I didn't want to risk Janice seeing me and calling my parents."
"The sandwiches they sell at the gas station may not be as fresh or as tasty, but they'll have to do."
$ vol("loop", 0.3)
play loop "phonebuzzlong.ogg"
"I make a grab for my wallet again, catching my phone mid-buzz."
$ vol("loop", 0.6, 0.3)
"Grumbling to myself, I take it out of my purse."
stop loop fadeout 0.2
$ reset_channel("loop", delay=0.2)
"Fifteen missed calls since the last one I saw. Fourteen from Dad, one from Jeremy."
"I don't know whether to laugh or cry, to be honest. I can only shake my head in disbelief."
"Not even half an hour into my little escape attempt and they're already trying to drag me back to the madhouse."
"As long as they didn't follow me here, I have nothing to worry about."
"But I can't shake the thought, the possibility, of them just showing up, or calling the police..."
"...or a thousand other things they'd never actually do."
"I don't feel like leaving the car anymore."
"I don't feel all that hungry anymore, either. Something light will do."
"I tap the window to get Chase's attention, then roll it down."
jas "\"Mind grabbing something from the store for me, Chase?\""
m "\"'Course not. What do you need?\""

scene bg conveniencenight with Fade(0.5, 0.2, 0.5)

play audio "<from 0.6>cardoorhalf.ogg"
$ vol("background", 0.8, 0.3)
$ vol("background2", 0.8, 0.3)
"I look up from my manga when he comes back, carrying a small plastic bag with the gas station's logo on it."
m "\"One for {i}you...\""
play audio "cardoorsecondhalf.ogg"
$ vol("background", 0.3, 0.2)
$ vol("background2", 0.3, 0.2)
"He says it in a sing-song voice, dangling a strawberry-flavored popsicle in front of me, which I greedily snatch from his paw."
m "\"And one for me.\""
"These popsicles come from Carl's mom's company. I've seen and eaten them more times than I can count."
"Back when we were kids, Carl used to boast that we were paying for his pocket money whenever he caught us eating one."
"Considering Carl's mom would always give us entire bunches of them for free whenever we visited, though, we never had to buy all that many ourselves."
jas "\"You remembered I liked strawberries? That's sweet of you, Chase.\""
"I take a whiff of the familiar, sugary, way too chemical scent."
m "\"Well, it was the only flavor left in stock – I mean, yeah, I did!\""
m "\"Better check the expiration date. It might be older than we are.\""
jas "\"The rest of this place certainly is.\""
"I take a little bite."
jas "\"I think it's safe. I'm not dead yet, at least.\""
"He laughs, unwrapping his own before producing two cans of soda from the plastic bag and handing one to me."
m "\"That's a relief.\""
"Eating popsicles and drinking soda in the parking lot of a run-down gas station. It sounds rather silly in my mind, but this is really happening."
"I take another bite."
jas "\"So. Have you figured out what you're going to do once you're done with high school?\""
"He fiddles with his bracelet again."
m "\"I don't know. Leo's dad said he might have a job for me, but I don't think I'd make a good mechanic. I've got two left paws.\""
m "\"I think I'd just destroy any car that came into the shop.\""
jas "\"Why don't you apply for college?\""
m "\"You mean the one in Pueblo?\""
"He gives me a quick sidelong glance."
m "\"That's really far away, isn't it? I dunno, Jas, I can't just leave Leo behind.\""
jas "\"You've got your phone! Long distance relationships are a thing, you know.\""
"I crumple up the popsicle wrapper, putting it down in the ashtray."
jas "\"They're actually all the rage these days. I've got this friend who has a boyfriend who lives on the other side of the planet.\""
"I turn and look at him."
jas "\"You know, I think you'd be a good fit for college, actually. Smart, motivated...\""
m "\"Really? I mean, I'm, not... I'm not all that good at anything, really. I don't know what I'd go for.\""
jas "\"Maybe journalism or something? I mean, you were in charge of the school paper last year. You like filming and taking pictures, right?\""
jas "\"And having a degree is always good.\""
m "\"What are you going to major in?\""
"He finishes his popsicle, tossing the stick in the plastic bag."
jas "\"I'm going for psychology.\""
m "\"Oh, like, the inner workings of the mind and stuff?\""
"He pantomimes while talking, yelping when he hits his elbow on the steering wheel."
"I giggle."
jas "\"I suppose. Minus the bruised elbow.\""
jas "\"I want to find out what makes people do things the way they do.\""
m "\"So what made you do the thing you're doing {i}right now?\""
"His expression takes a turn for the serious."
m "\"Why'd you decide to run away?\""
"For a moment, I'm speechless, all the heat drawing from my body as we look right at each other."
"I thought he was okay with me leaving when I told him, but now, his tone is almost accusatory."
"It reminds me of Leo. I shudder, remembering the stink eye he'd given me when I told HIM I was leaving."
jas "\"A lot of things.\""
"I brush the fur out of my eye."
jas "\"And I'm sorry, Chase, but most of them are none of your business.\""
m "\"I'm the one driving you to your new place. I think I deserve to know what's going on.\""
"He frowns."
m "\"What did they do to you? Did they hurt you or something?\""
jas "\"None of your business.\""
"I grit my teeth."
jas "\"Can - can we just keep driving, Chase. Please?\""
m "\"Jasmynn, please. I want to know.\""
m "\"If you need someone to talk to, someone who can help... me, Leo, my parents – we'll do whatever it takes.\""
m "\"You don't {i}have{/i} to do this, you can keep living in-.\""
jas "\"Is that what this is all about?\""
"I gesture to the soda cans, the empty popsicle wrappers, and the gas station."
jas "\"Are you just stalling so you can convince me to stay?\""
m "\"Jasmynn.\""
"He puts a paw on my shoulder."
m "\"I know how you feel, but running away – running away isn't-.\""
jas "\"You don't know how I feel.\""
"I smack his paw away."
jas "\"You don't know the slightest thing about my situation, Chase.\""
jas "\"You don't know what it's like to live in poverty, what it can do to people.\""
jas "\"And you don't know how it feels when no matter how hard you try to crawl out of that hole, your family will keep piling on even more dirt.\""
"I take a deep breath, realizing I'm clenching my fists."
jas "\"I want to live for myself, Chase. I want to go to college, I want to have a future.\""
jas "\"I can't do that in Echo.\""
jas "\"It's not the place for me. It never was.\""
m "\"It's not the place for any of us.\""
"He shrugs."
m "\"But it's home, y'know?\""
jas "\"It's home for you. It's hell for me.\""
"I put my seatbelt back on."
jas "\"Adam's dead. Jeremy's huffing whatever the fuck he can get his paws on.\""
jas "\"And my parents-.\""
"I cut myself off. I feel nauseous just talking about them."
jas "\"My parents just keep blaming other people for their own ineptitude. Carl, his great-great-grand-whatever, you, Leo, everyone's fair game.\""
jas "\"I'm sick of it.\""
"Chase gently puts his paw on mine. This time I don't push him away."
"I feel drained, exhausted. I'd cry on his shoulder, but I don't even have the energy to do that."
m "\"What'd they say about Carl?\""
m "\"I mean, Leo and I aren't exactly Echo's darlings, but Carl's... he's harmless.\""
jas "\"Apparently his family's the reason we're so poor. Never mind the fact that my dad can't hold a job. Hell, he can't hold {i}anything{/i} save for a beer bottle.\""
m "\"Shit... I didn't even know your families had a history together.\""
jas "\"We go way back. It's complicated.\""
"The story I'd always been told was that one of Carl's ancestors had his business partner – one of my ancestors – lynched for sodomy to cover up his own crimes."
"My parents always conveniently left out the part where they were gay lovers, of course, but a trip to library cleared that one up for me."
"Not that they cared."
"My breath slows. I've stopped clenching my teeth."
"I'm not trembling anymore, at least, which makes drinking my soda a lot easier."
"Finally, Chase smiles at me."
m "\"Sorry about all that. I just... wanted to look out for you, you know? Everyone's been really worried.\""
jas "\"I know, and I'm sorry, too. I shouldn't have lashed out like that.\""
jas "\"Did you tell your parents that I was – that you're helping me?\""
m "\"I told them I'd be taking Carl and TJ out to see the new Lion's Brigade.\""
"He puts the keys back in the ignition."
m "\"My mom's been asking about you, though.\""
"That warms my heart a little. Chase's mother is one of the nicest people I know."
jas "\"What'd she say?\""
m "\"Just wanted to know how you're doing, if you're eating okay, that kinda stuff. She wants you to come over for dinner sometime.\""
"He laughs."
m "\"Maybe she's still hoping I'll go straight someday, huh?\""
play audio "enginestart.ogg"
play loop "engine.ogg" fadein 3
$ stop_all_audio(5, reset=True, subset=["background", "background2"])
"He backs us out of the parking lot."
"When I look behind me, I see a group of employees crowding around a rather shady-looking wolf. I guess we're leaving just in time."
scene highwaynight with medium_dis
play background "highway.ogg" fadein 10
stop loop fadeout 15
jas "\"Do you parents not like that you're with Leo?\""
m "\"My dad {i}adores{/i} him. I think my mom still wants grandkids, eventually, but she's been pretty supportive. She just wanted me to be safe.\""
"I chuckle."
jas "\"Grandkids? I can't really picture you as a dad.\""
m "\"Gee, thanks.\""
"He rolls his eyes dramatically."
m "\"You're as sharp as a boxcutter sometimes, you know that?\""
"I give his snout a playful poke with my finger."
jas "\"Just saying what's on my mind, otter boy. Don't take it too personally.\""
"There's a moment of silence before he speaks again."
m "\"Hey, um, not to change the subject, but like, won't your family be able to find you over there?\""
jas "\"They won't. I've thought of something.\""
m "\"What is it?\""
jas "\"I'm going to get my name changed when I can, once I'm 18."
jas "\"It won't make it impossible to find me, but hopefully it'll keep them off my tail until I can move to Pueblo.\""
"As long as I can remember, even before I started thinking about running away, I’ve wanted to change my name."
"Jasmynn's a name, yeah, but it’s never felt like a name that was really my own. It's the one my parents picked for me."
"I’ve always felt like it was one of those names you usually associate with trash living in a small rural village – a citizen of Echo."
"It's not a name you’d really expect or want to see on the front page of a magazine, or a research paper."
m "\"Really? Huh.\""
jas "\"Yeah. I want something a little more...\""
"I bite my lip."
jas "\"A little more {i}me,{/i} I guess.\""
m "\"What kind of name are you thinking of?\""
"In the past I've considered the names of actresses and singers, from CEOs to scientists."
"Now, though, I just blurt out the first thing that comes to mind."
jas "\"How about Jenna?\""
"It seems like a good enough name."
m "\"Jenna?\""
"He chuckles."
m "\"Thought you'd go for something more ostentatious.\""
jas "\"Well, I don't want to draw too much attention to myself. And to be fair, {i}anything's{/i} better than Jasmynn.\""
m "\"Definitely. It's just... well, it's gonna take some getting used to.\""
"He stares off into the distance, at the empty stretch of barren land next to the road."
m "\"Jenna.\""
jas "\"Doesn't sound half bad, right?\""
m "\"Hey, it's your name.\""
jas "\"What's {i}that{/i} supposed to mean?\""

scene bg paytonnight with opening_fade

$ stop_all_audio(4, reset=True)
play background2 "parkinglotnocarts.ogg" fadein 5
show Chasey N with dissolve
m "\"Shoot me a message once you've unpacked, okay?\""
"Chase lifts the duffel bag out of the trunk with a grunt. I wobble on my feet once I grab it, rescued by Chase giving me a hug."
"I struggle to reciprocate it until I drop the bags."
"It's a little uncomfortable with both our shirts stuck to our fur and it still being warm out. But it's not unwelcome."
"I nod."
jas "\"Drive safe.\""
m "\"Really?\""
"He chuckles, pulling back."
m "\"Seriously? Do you {i}see{/i} a dent in this car?\""
jas "\"Sure, that's what you said about your bike, too, right before you fell flat on your-.\""
m "\"That was five years ago!\""
m "\"Five! Years!\""
"We laugh together."
show Chasey Sad with dis
m "\"It's gonna be different without you around.\""
jas "\"I'll still be around, you dip, just in a different town.\""
"I chuckle."
jas "\"Maybe we can go do something together sometime? We could go bowling.\""
show Chasey N with dis
m "\"Sounds like fun. I'd like that. But only if you promise not to cheat again.\""
jas "\"Hey, I beat you fair and square last time.\""
m "\"Of course you did, Jas-.\""
m "\"Jen.\""
jas "\"Fine.\""
"I fold my arms."
jas "\"I'll go easy on you.\""
"He steps back towards the car."
"After a short pause, he turns around to wave."
"I walk up to him once again."
play music "jennastheme.ogg"
j "\"Wait.\""
"I take Pueblo University's brochure out of my purse."
j "\"For you.\""
"He looks at it for a second, dumbfounded."
stop background2 fadeout 10
show Chasey Sp with dis
"Summoning some of my courage, and a little stupidity, I lean in and give him a peck on the cheek for good measure."
"If Leo were here, he'd toss me through a wall."
j "\"Thanks, Chase. For everything. You've been a big help.\""
"He just stands there, jaw agape, glancing down at the brochure before looking up at me again."
m "\"U-um, I guess I'll see you around?\""
j "\"Bye, otter boy.\""
hide Chasey with dissolve
"I grab the bags again, unable to keep myself from giggling softly as he stumbles to the car door, a confused look of bewilderment still etched on his face."
"He clutches the brochure tightly, and I catch a glimpse of him reading through it before he drives away."
"When he honks the horn, I do my best to wave in spite of the bags, smiling to myself, all alone in Payton in the middle of the night."
"Chase might be the only game Leo ever beat me at, but the odds can still change."
"With the bags in my paws, I waddle to the old, beat-up door, and wait for the door to my future to open."
window auto hide
$ stop_all_audio(fadeout=5.2, reset=True)
show bg black with slow_dis
$ renpy.pause(5.4, hard=True)
$ renpy.end_replay()
