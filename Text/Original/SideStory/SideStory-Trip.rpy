# Trip
# by Howly

label sidestory_trip:

stop music fadeout 3.0
scene bg black
with slow_dissolve

$ renpy.pause(2, hard=True)

$ vol("background", 0.3)
play background "nhysteria.ogg" fadein 10 # volume 0.3

$ renpy.pause(4, hard=True)

$ pan("background2", 0.9)
$ vol("background2", 0.025)
$ vol("sound", 0.2)
play background2 "carbeep.ogg" # volume 0.025
play sound "chasecomes.ogg" # volume 0.2

$ renpy.pause(9.6, hard=True)

$ stop_all_audio(reset=True)
call sidestory_title("October 2014", fade=0) from _call_sidestory_title_8

pause

$ vol("background", 0.3)
play background "crickets.ogg"

$ renpy.pause(2, hard=True)

call sidestory_title("May 2010", fade=0, end=True) from _call_sidestory_title_9
$renpy.pause(1, hard=True)

scene bg trailerinteriornight with slow_dis
show nightoverlay
show Jeremy at center behind nightoverlay

"I let the sugar cube roll around on my tongue, realizing how gross sugar really is without anything to go with it."
"...Or maybe it's just the LSD. Does acid taste like anything?"
"I guess the cube is a little bit bitter, sort of."
"I look over at Jeremy, whose mouth is open, and I can see the sugar cube bounce around on his tongue."
c "\"Are you sure there's anything in this? I don't taste it.\""
jer "\"It doesn't taste like anything.\""
"I let the cube clack against my teeth a few times before it breaks up and starts dissolving a lot faster."
show Jeremy Teasing with dis
"No turning back now. I tap my hoof against the messy floor, making the bed I’m sitting on squeak."
"Jeremy grins at me."
jer "\"Dude, relax.\""
jer "\"Remember, good vibes, otherwise you're gonna trip bad.\""
"Him saying that only makes me more nervous and I put my face in my paws."
c "\"Shit, man, I shouldn't have done this. Can I throw it up?\""
"He laughs at me, but at this point I’m so nervous I can’t be mad at him."
"In a way I’m latching on to him for guidance because I know he’s done this before."
jer "\"No, you can't throw it up. Remember, good vibes. This is about discoverin' yourself.\""
c "\"Couldn't we at least have done this outside? This isn't exactly my idea of a place I'd wanna {i}find{/i} myself in.\""
"I glance around Jeremy’s trailer and wrinkle my nose."
"Now, my room isn’t spotless, but Jeremy’s place is downright nasty; underneath the smell of pot is a layer of mold and rotting food."
"The light is a sickly yellow that turns everything in this 70s-ass trailer into a piss-stained color."
"The walls are paneled wood with missing parts and it’s hard to see through the plates, bottles, and used tissues (gross), to the orange shag carpet underneath."
show Jeremy with dis
jer "\"No, I don't want that bitch cop findin' us. She's already got it out for me.\""
"He lays back on the bed, looking at the ceiling, one of his giant ears folding under his head."
"He lifts his head back up to swat it back into position."
jer "\"You're over your whole anxiety stuff, right?\""
jer "\"I told you this ain't like pot. It's not something you fuck around with.\""
c "\"Well, you saying shit like that is reeeally helping.\""
"I try to keep my voice steady."
"He watches me for a while, then nods to his shitty TV."
jer "\"Wanna watch something while it sets in? Might help ya relax.\""
"That does sound like a good idea, but still I’m not so sure."
"Wasn’t I doing this to \"discover\" myself?"
"Now that I think about it I’m not really sure why I decided to do this in the first place. Maybe to figure out why I’m so goddamn broken?"
"He takes my silence as a yes, though, and goes over to a splintered shelf to pull out a VHS. His TV is so fucking old it's got a VHS player built into it."
show Jeremy Teasing with dis
jer "\"This cartoon got me through a lot of tough times as a kid.\""
play sound "<from 0.15>switch.ogg"
"He turns on the TV and sticks it in."
python:
    vol("music", 0.0)
    vol("music2", 0.6)
    renpy.music.play("cartoon.ogg", "music2", fadein=1, synchro_start=True)
    renpy.music.play("cartoon-trip.ogg", "music", synchro_start=True)
"I watch the white \"PLAY\" letters appear over the blue screen before it flickers to a faded-out picture of a pink feline thing in a diaper."
"Distorted music crackles out of the TV's tiny speakers as the cat starts talking to us in a high-pitched whine."
"I frown."
c "\"This is just creepy.\""
jer "\"Naw, that's just 'cuz I've played it way too many times. Just watch and try to relax.\""
show Jeremy:
    ease 5 alpha 0.0
"Jeremy comes back to the bed and I lean back against the wall while Jeremy curls up next to the pillow."
"I'm not totally sure what the show is about since the TV is kinda quiet and the audio is all fucked up."
"All I can figure out is that the cat thing and his baby bird friend are trying to make something, a cake, I think, but they're making a huge mess."
"It feels like one of those shows that might be fun to make fun of with Leo, or something, or Chase... He always laughs at the stupid shit I say."
"The kitchen they're in is a bright pink that almost stings my eyes and I'm not sure if it's because of the distortion or if it was like that originally."
"It starts to hurt a lot, so I look up at the ceiling."
"I notice a whole bunch of holes in it, and there's one part with wires hanging out and pipes inside."
"Suddenly, I'm really wishing I'm not here."
"I start to grip the bedsheets because things are feeling really light, my body feels light, like a cloud, and now I know it's starting."
"I try to relax because that's what Jeremy said I should do, but now the ceiling is starting to move..."
"...the patterns starting to swirl around that hole, like it's a whirlpool... no, like it's a black hole."
"I don't know what to think."
"It is kinda cool to watch, but that feeling that I'm not connected to anything isn’t really fun, and it's actually kinda scaring me."
"I still feel like I'm floating, like I'm floating up towards that black hole, like it's sucking me in."
"I jolt and take a breath that sounds sloppy because I'm drooling down my chin and I whip my head around to look at Jeremy."
"He's staring at his paw and he looks up and grins at me."
jer "\"{cps=25}Ya alright?\""
"I just stare at him. How long has it been?"
"It's like I just jumped an eon between the time I was staring at the black hole to now as I'm staring at Jeremy's face."
"His eyes are bright white, like marbles burning into me."
"I try to breathe normally, try not to freak out."
jer "\"Hey, watch the TV. It's alright. If it gets too bad you can just pull out one of your joints.\""
show nightoverlayred:
    alpha 0.0
    ease 30 alpha 1.0
$ vol("music", 1.0, 30)
$ vol("music2", 0.0, 35)
"I turn my eyes to the TV and see that pink tiger guy again."
"He's pointing at the oven, talking to the bird."
"It's a green bird, and for some reason the orange on his wings keeps slipping off, like those feathers are a jacket that he can't keep on."
"I'm still not completely sure about what's going on, but now I think I'm starting to realize."
"That tiger wants the bird to get in the oven, to clean it, because there's shit in between the grating, stuff that needs to be cleaned off, because..."
$ pan("music", -0.3, 10)
"...because they don't have anything to put the cake on before they put it into the oven, so the oven needs to be super clean..."
"...but the tiger doesn't really care if the oven is clean."
"He's gonna shut the door as soon as the bird gets inside, then he's gonna turn it all the way up, all the way up to 500 degrees and cook the bird alive."
"Suddenly I'm fucking pissed. Jeremy made me watch this shit to freak me out."
$ pan("music", 0.3, 10)
"He didn't really want me to calm down, he wanted me to lose my mind watching this cartoon horror show."
"I look over at him and glare."
c "\"What the fuck is this?\""
jer "\"Hm?\""
"He doesn't even look up from his paw."
"What else is he planning?"
"If he was willing to be this cruel to me what else is he gonna do?"
"Suddenly I'm really scared and breathing hard."
"I stand up quick and that's when he finally looks up at me."
$ pan("music", 0, 10)
jer "\"Carl?\""
c "\"Dude, just–just leave me alone.\""
jer "\"Carl, what are you seeing?\""
c "\"Stop it!\""
"I turn away and stumble to the door."
jer "\"Carl, whatever it is, it's not real.\""
"He sounds distracted, like he doesn't care."
"He doesn't even get up off the bed to follow me, which is just fine."

scene bg scraptrailernight with dis

$ vol("sound", 1.5)
play sound "dooropen.ogg" # volume 1.5
$ vol("background", 1.0, 0.5)
play music2 "loneliness.ogg" fadein 10
$ vol("music2", 0.5, 0.5)
$ vol("music", 0.8, 0.5)
"I stumble out and gasp as the cool air hits my lungs."
"It feels good because I'm leaving behind whatever bad shit is inside Jeremy's trailer, inside that black hole."
$ pan("music", -0.4, 10)
$ pan("music2", 0.4, 10)
"And now, suddenly, I just feel sad and lonely."
"Why the fuck did I hang out with Jeremy?"
"I stand there for a second, looking around, and that's when I realize I don't even know where I am."
"It's dark and there aren't any lights on the streets."
"How the hell am I supposed to get home?"
"Leo."
"Leo can help me."
$ vol("sound")
$ pan("music2", -0.4, 10)
$ pan("music", 0.4, 10)
"Just thinking about him fills me with a warm feeling, like back when I was seventeen and Dad just told me he'd pay for everything."
"I reach into my pocket and pull out my phone."
"I stare at it, and I stare and stare and stare because I don’t even know what to push."
"The little apps keep swirling around, like the black hole."
"I shut my eyes then push where I know the phone app is supposed to be."
"I open them again and see the keypad and I blow out a sigh of relief, but then as soon as I push the first number all of the numbers change."
"I frown and push the next number, but the numbers change right before I hit it and I spend the next ten minutes..."
$ pan("music2", 0, 10)
$ pan("music", 0, 10)
"twenty..."
"eighty..."
"...two hours? trying to figure it out, but it's no use."
"I keep shaking my phone and swearing, like that's gonna help."
"I finally give up and stumble to my car..."
"...trying to keep my breathing under control..."
play sound "cardoorsecondhalf.ogg"
$ vol("music", 0.1)
$ vol("background", 0.1)
play loop "terrorbelowthesurface.ogg" fadein 30
"...because I'm on the verge of a panic attack and I have a feeling that it's gonna be way worse than the one I had at school."
"For a while I sit there in the seat in the dark and stare out through the windshield."
"I see the beginnings of swirls and whirlpools again so I look down at my hands and that's when I see the fur shifting around, too."
"I close my eyes and just think about how nice the cool leather feels against my thighs."
"It’s the drug, it's the LSD. I'm having a bad trip. I know this, but just knowing that still scares me."
play audio "thud3.ogg"
$ stop_all_audio(fadeout=4, reset=True, subset=["background", "music2"])
$ pan("sound", 0.9)
$ vol("sound", 0.1)
play sound "steps.ogg"
$ pan("sound", -0.9, 3)
"At that moment I hear AND feel something run past the window, then bounce over the hood of my car."
"I whip my head up and stare into the blackness and feel my throat close up."
c "\"{cps=10}Please...\""
"I say it to no one, but everyone at the same time."
"It comes out strangled and whiney because I'm about to start crying."
"Home, I need to get home."
$ pan("sound")
$ vol("sound", 0.3)
play sound "enginestart.ogg"
"I turn on my car, but I'm not really sure where I'm at."
"GPS, that'll help."
"I lean down towards the console, trying to find the right button."
"Again, things are moving around, and the bright blue LED lights are blurring and leaving long trails in my vision."
"I have to close my eyes again and stab at different buttons, scaring the shit out of myself when music starts blaring."
"Psychedelic rock is a lot less fun now."
"That thing is out there and I don't wanna attract it with noise."
$ vol("sound", 0.5)
"I manage to turn the music off{nw}"
play sound "gps.wav"
"I manage to turn the music off {fast}and what seems like an eternity later I hear the words I've been looking for."
"" "{i}{b}\"State your destination.\""
c "\"{cps=25}Home!\""
"I almost sob it out, leaning back in the seat and covering my face, sighing with relief."
"" "{i}{b}\"Navigating to Pueblo. You should reach your destination in three hours and thirty-two minutes.\""
"My eyes fly open."
c "\"NO!\""
"I struggle to remember the stupid name I gave it."
c "\"No! ...Fatass!\""
"For some reason it's only hitting me now how stupid that name is, how unfunny and immature it is."
"How I've been so lazy that I haven't taken the time to change the name of my stupid GPS that I named five years ago."
play sound "metalscratch.ogg"
"Again, I feel the bony, skeletal thing rush by my passenger window, dragging its fingers along the glass."
c "\"Fatass! Navigate home!\""
"" "{b}{i}\"Navigating to The University of Pueblo.\""
c "\"No!\""
"" "{b}{i}\"You should reach your destination in three hours and thirty-nine minutes.\""
c "\"NO!\""
"I slam my fist into the console."
"I'm about ready to run out of the car, into the darkness screaming for help, not just because I'm scared, but because sitting still is almost as bad as being lost."
"I need to MOVE."
"My legs are bouncing up and down, hitting the steering wheel, and it feels like I'm peeing my pants."
"I take a few deep breaths, I can do this, just need to calm down."
c "\"{cps=25}Fatass.\""
"{cps=25}{font=ui/belligerent.ttf}Stupid, immature."
play music2 "nhysteria.ogg" fadein 60
"" "{b}{i}{cps=5}\"Yes?\""
show nightoverlayred:
    alpha 0.0
    linear 120 alpha 1.0
"I pause because I know it's not supposed to do that... or is it?"
"I try to remember what I was gonna say."
"" "{b}{i}{cps=15}\"Ye-es?\""
"The tone is different, taunting, like it knows that it's fucking with me."
"It doesn't wait for me to say anything."
play audio "badradio3.ogg"
stop music fadeout 10
"" "{cps=22}{font=ui/COLONNA.ttf}{i}\"Navigating to the {/i}thing...\""
play audio "badradio.ogg"
"" "{cps=20}{font=ui/COLONNA.ttf}{i}\"You have arrived; your destination is on your left.\""
$ reset_channel("music")
play music "shadowbg.ogg"
"I cower in my seat because I can feel it standing right next to me, outside the window, staring in at me through the glass."
"I cover my face with my paws and I can feel tears leaking through my fingers."
"{cps=25}I stay like that for a long, long, long, long time."
"{cps=25}Hours stretch into weeks stretch into months stretch into infinity, and I fall back into the black hole."
"{cps=25}It stretches my mind, starts pulling it apart along with the rest of my body."
"{cps=22}I start to give in, {cps=17}start to give up..."
play sound "gps.wav"
stop loop fadeout 10
"" "{b}{i}\"Navigating home. You should reach your destination in three minutes.\""
"Slowly, I bring my paws down from my face."
"The clock says 2:23."
"If that's right, it's been two hours since I ate that sugar cube."
"I look out the window and see that the light is still on in Jeremy's trailer. I wonder if he's going through the same thing as me."
"But I'm calm now because I know why the GPS was freaking out earlier."
"It was stupid of me to lose my shit like that, especially now that I know that Chase is in the car, home from spring break."
"He's been fucking with me, trying to get me to go to Pueblo with him."
"I remind him that I'm tripping the fuck out and that messing with me in any way isn't a good idea."
show bg highwaynight2 onlayer screens:
    alpha 0.0
    linear 20 alpha 1.0
show nightoverlayred onlayer screens:
    alpha 0.0
    linear 20 alpha 1.0
play background "carwind.ogg" fadein 10
"I look around and can't see him, but that's okay, it's just nice that he's here."
"I put the car in drive and pull into the road, start driving where the GPS is telling me to go."
"I'm chill now, but I still feel like something's following me."
"It makes me feel better that Chase is telling me about school, how much he misses me."
"I think I feel him caress one of my horns, which is okay because it feels nice."
"My car rolls along down the road and over time things start to blur together."
"Again time stretches and distorts, but it's okay because Chase is talking to me, but then his tone gets more urgent."
"He's trying to warn me about something."
"I frown, dread starting to roil in my gut again."
"What now?"
"I think about looking into my rearview mirror."
play loop "nhysterialoud.ogg" fadein 5
"I don't want to, but I do and as soon as I do I'm screaming; red, bony, with black holes for eyes, then something grabs my neck."
"I let out a long, strangled moan of horror, and my hoof slams the gas."
"That moment stretches, distorts, alters and changes just like the VHS Jeremy had shown me that lifetime ago."
"I go back and forth."
"I repeat and loop, the thing killing me forever."

$ vol("sound", 0.4)
play sound "<from 1>driveby.mp3" fadein 0.4 # volume 0.4
window show
$ renpy.pause(0.7, hard=True)
$ renpy.scene(layer="screens")
scene bg black with {"master" : Fade(0.01, 0.025, 0.01, color="#f1f1f1")}
$ vol("sound", 1.5)
play sound "carcrash.ogg" # volume 1.5
play audio "carwindowsmash.ogg" # volume 1.5
play audio "catchfire.ogg"
play audio "<from 0.1>thud8.ogg"
# play audio "<from 0.15>honkhonk.ogg" # volume 0.3
$ stop_all_audio(reset=True, subset=[x for x in sidestory_audio_channels if x != "loop"])
#$ vol("music", 0.1)
#play music "ringing.ogg" # volume 0.1

window auto show
"I'm lifted out of my seat and my head slams into something, sending white light flashing through my eyes."

$ pan("background2", 0.4)
play background2 "carbeep.ogg" fadein 10

"An explosion hits me in the stomach and chest and now I can't breathe."
stop music fadeout 10
"Little hard pebbles pelt the back of my head as what sounds like sand being poured out onto paper echoes in my ears."
show image "#f0f0f0" with medium_dis
show nightoverlay with medium_dis
"Slowly, I sag back down into my seat and my vision is full of white, a balloon pushing out of the steering wheel."
"On that white are little dark red spots that keep popping up in different spots."
"I cough and then there are a million of them."
"I stare at them, confused, and they start to dance around and whirlpool."

show highwaynight2 behind nightoverlay:# with slow_dis
    alpha 0.0
    linear 5 alpha 1.0
play background "death.ogg" fadein 30
stop background2 fadeout 10

"I crashed the car, I realize, and I also realize that I've killed Chase."
"He'd been sitting in the car with me, trusted me with driving, and he'd hit the windshield without the horns and skull to protect him."
"I start sobbing."
"Liquids run down my face; tears, maybe snot, but it's dark and I realize it's blood... it's probably all three of those things."
play audio "badradio2.ogg"
"{cps=10}Time stretches,{nw}"
"Time stretches,{fast} dis{font=ui/belligerent.ttf}torts, {cps=10}loops,{nw}"
"Time stretches, dis{fast}torts, {cps=10}loops, repeats."
show bg mansionnight onlayer screens:
    alpha 0.0
    linear 18 alpha 1.0
show nightoverlayred onlayer screens:
    alpha 0.0
    linear 18 alpha 1.0
show nightoverlay onlayer screens:
    alpha 0.0
    linear 18 alpha 0.0
"Somehow I get home."
"Somehow I ditched the car and I ran up the road all the way to my house."
"The entire way I try to dial 911 on my phone to get Chase some help, but the buttons won't hold still."
"I couldn't look, at the time, but I know he's lying in a bloody heap in the passenger-side foot well."
"As I stumble towards the house, I realize that the thing is still waiting for me."
"He'd jumped out of the car and hidden on the porch."
"I whimper and stare at the shadows, then I run to the house."
"I stumble back and forth, the ground sinking towards the window wells like quicksand, sucking me in."
"I dodge around them, pulling my hooves out of the sinking grass, about to get stuck."
"Once I get to the backdoor I shove my paws into my pockets, but there aren't any keys because I left them in the ignition."
"I sob again and look around desperately."
"The longer I hold still the deeper I sink into the ground."
"Again, I almost give in, but then I see the treehouse."
stop loop fadeout 20
"Like my legs are made of lead I stumble across the yard, feeling the thing crawling after me."
"I leap up and cling to the ladder before scurrying up, my hooves slipping on the wood as I feel the tree start to sink as well."
hide highwaynight2
hide image "#f0f0f0"
show bg mansionnight onlayer screens:
    linear 5 alpha 0.0
"I fumble up through the opening, breaking through cobwebs and snorting up dust."
"I crawl to a corner and curl up, covering my eyes and facing the wall."
"I beg Chase to forgive me because now I can't get him help, because now I'm stuck on this sinking ship with a monster."
"I curl up tighter and tighter, so tight that I become my own source of gravity, my own black hole, sucking up everything around me..."
"...stretching it thin..."
"...then tearing it apart."
"It's only then that everything settles."

$ renpy.scene(layer="screens")
scene bg black

$ stop_all_audio(reset=True)
$ renpy.pause(3, hard=True)

show carlsroomred
"My parents found me three hours later after someone had reported the accident to the cops a few hours after I'd left."
"My dad took responsibility for it so I wouldn't get tested for anything."
"He made up some excuse about walking to the house because he forgot his cell phone."
"I guess they didn't wonder why blood was everywhere and why my dad had no injuries."
pause 2
"I realize what happened was just a bad trip, but I don't have any plans to try it again."
"I guess it helped me discover things about myself... "
"...things I'd rather not have found out."
"Even now, irrational fears get the better of me, and I'm still paranoid as fuck, like everyone's keeping a big secret from me."
"Sometimes I'm positive they're hiding the fact that they found a dead otter in the car."

window auto hide
hide carlsroomred
$ renpy.pause(2, hard=True)
$ renpy.end_replay()
