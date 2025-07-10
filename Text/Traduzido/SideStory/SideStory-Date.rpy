# Date (Encontro)

label sidestory_date:

stop music fadeout 3.0
scene bg black
with slow_dissolve
play background "roomtone.ogg" fadein 5
pause 1
call sidestory_title("Janeiro de 2010") from _call_sidestory_title
pause
call sidestory_title("Janeiro de 2010", end=True) from _call_sidestory_title_1

"O que torna um encontro bom?"
"O Chase me disse sair para jantar e ver um filme."
"Pessoalmente, eu senti que ter o jantar na metade do encontro na minha casa seria bem agradável."
"Quer dizer, é mais limpo do que qualquer restaurante que você encontraria em Payton, e minha mãe é uma ótima cozinheira."
"Mesmo assim, percebo pela maneira que Heather está com a cabeça abaixada que ela está realmente infeliz."
"Sinto um tipo de apreensão em meu peito."
"Meio que define o clima da noite até agora."

scene bg route93
play background "highway.ogg"

"Minha mãe nos leva ao cinema e eu começo a ficar ansioso, percebendo o quão atrasados estamos."
"O filme promete ser muito bom e se passa no espaço, que é o meu tema favorito."
"Porém, minha mãe me disse para não me preocupar, já que os trailers geralmente preenchem os primeiros quinze minutos."

show bg theaterext with dis
play background2 "reststop.ogg" fadein 5
stop background fadeout 7
"Por fim, estacionamos e eu saio e mantenho a porta aberta para a Heather."
"Percebo que ela está demorando para sair, então espero por ela enquanto minha Mãe entra para pegar os ingressos."
show Heather at center with dis
h "— Por que sua mãe tá vindo junto?"
"Sua voz é um sussurro."
"Estendo a mão para fechar a porta, mas ela mesma fecha, com um pouco mais de força do que o necessário."
"Fico ali parado por um segundo, sem saber o que dizer."
t "— Hum... bem, tá muito quente aqui fora. Ficar no carro seria bem–"
h "— Deixa pra lá."
hide Heather with dis
"Heather se adianta a minha frente e sinto aquela apreensão novamente."
stop background2 fadeout 10
"Foi só agora que me dei conta de que trazer minha Mãe foi uma má ideia. Não que eu tenha falado para ela vir; minha Mãe meio que se autoconvidou." # autoconvidou ?
"O Chase me deu várias dicas sobre como fazer o encontro correr bem, mas ele não falou nada sobre os pais."
"Talvez era tão óbvio que ele achou que não precisava me contar. Esse pensamento só faz com que eu me encolha ainda mais e consigo sentir meu rosto ficar quente."
play background2 "roomtone.ogg" fadein 10
"Enfio as patas nos bolsos e sigo atrás dela, tentando manter minhas orelhas erguidas."

scene bg theater with medium_dis
python:
    vol("music", 0.05)
    pan("music", 0.2)
    vol("background", 0.1)
    pan("background", -0.2)
play music "adastratheme.ogg" fadein 10
play background "adastrasfx.ogg" fadein 10

"Minha Mãe é muito simpática e se senta cerca de cinco fileiras atrás de nós, mas a Heather ainda parece bem brava com isso."
"Ela continua mudando sua postura, cruzando os braços e fazendo beicinho."
"Cada vez que ela suspira, me sinto constrangido só mais um pouquinho e agora não consigo nem me concentrar no filme."
"Depois de cerca de trinta minutos, ela volta a ajeitar sua postura e derruba um pouco de pipoca no meu colo. Eu me inclino para ela, sussurrando."
t "— O que foi?"
"Ela encolhe os ombros, mantendo seus olhos no filme."
"Inclino-me para trás no meu assento, novamente tentando manter minhas orelhas erguidas, especialmente com minha Mãe atrás de nós."

$ stop_all_audio(reset=True)

scene bg highwaynight
play background "highway.ogg"

"A viagem de volta para casa é bastante constrangedora."
"Minha Mãe não para de falar sobre o filme e o que achou dele, o que é bom, porque consigo perceber que a Heather não está a fim de conversar e eu não tenho ideia do que falar."
"Enquanto voltamos para Echo, minha Mãe se volta para nós."
mom "— Certo, Heather, você quer que eu te deixe na sua casa?"
h "— Na verdade, eu e o TJ queríamos conversar sobre umas coisinhas. Tá tudo bem se eu ficar por mais um tempinho?"
mom "— É claro!"
"Olho de relance para Heather, mas ela não olha de volta para mim."
"Não tenho a menor ideia do que ela está falando, e eu acho que prefiro não descobrir."
"Porém, não há nada que eu possa fazer, então, quando encostamos na entrada da garagem, eu saio quieto e sigo a Heather até a casa."

play background2 "roomtone.ogg" fadein 3
stop background fadeout 5

scene bg tjdiningroom with medium_dis

dadg "— Como foi o filme?"
"Ele diz sem tirar os olhos da TV."
h "— Ah, foi ótimo, Sr. Hess, muito bom."
"Ela está usando aquela estranha, doce voz que usa para meus pais."
t "— Uh, é, bem divertido."
"Eu a sigo."
dadg "— Bom, bom."
"Ele nem tenta soar interessado enquanto continua assistindo ao jogo de hóquei."
show bg tjbedroom with dis
show Heather at left with dis
"Heather já estava sentada na minha cama quando entrei pela porta."
"Ela está com as pernas cruzadas, patas apoiadas atrás dela na cama."
"Fico ali parado sem jeito, tentando pensar no que fazer enquanto ela permanece sentada e não diz nada."
t "— Uh, você quer ouvir um pouco de música?"
"Vou até a minha cômoda, pegando minha pequena pilha de CDs e procurando entre eles."
"Pulo os álbuns de rock Cristão, sentindo minhas orelhas ferverem um pouco só de pensar nela vendo eles."
"Acabo pegando um álbum de Cherryloom que meu pai me deu há alguns anos atrás quando ele estava tentando me interessar por rock clássico." # Cherryloom é uma referência?
"Heather ainda não disse nada e eu me sinto suando um pouco enquanto coloco o CD e baixo o volume."
$ vol("music", 0.4)
$ pan("music", -0.2)
play music "Country3.ogg"
"Por fim, me viro e vejo que a Heather não se moveu da sua posição na cama. Ela simplesmente ficou me observando o tempo todo."
"Eu contorço uma orelha e coço minha nuca, rindo para disfarçar meu nervosismo." # twitch = contorço ?
t "— Uh, hehe. O que foi?"
show Heather Happy with dis
"Ela aponta com a mão em direção à porta."
h "— Fecha a porta."
t "— Hum, okay."
hide Heather with dis
"Sei que minha mãe iria provavelmente ficar brava, mas fecho mesmo assim, tentando ser o mais suave possível para que meus pais não escutem."
play sound "rustle.ogg"
show Heather Happy at center with dis
"É então que escuto a cama ranger atrás de mim. Me viro e a Heather está bem na minha frente."
t "— Ah!"
"Dou um pulo para trás e me esbarro contra a porta. Heather dá uma risadinha e se aproxima, e consigo sentir sua respiração em meu rosto."
"Ela estende a mão e apoia suas patas em minha cintura, depois as desliza para cima, levantando minha camiseta, suas patas em meu pelo nu agora."
t "— Ah, nossa, ok, uh..."
"Não tenho a menor ideia do que dizer, ou do que fazer."
"Heather apenas ri de mim de novo, pressionando seus dedos através do pelo até minha pele, e consigo sentir as almofadas de suas patas contra mim." # pads = almofadas ?
"Olho para baixo e vejo que ela levantou minha camiseta acima do umbigo e está começando a esfregar o pelo branco que ficou exposto."
"Ninguém nunca me tocou assim antes, e eu sei que deveria gostar... mas não gosto."
"É quase como se eu tivesse pulado em uma água bem gelada e agora não consigo respirar."
"Abro a boca e acho que estou prestes a pedir para ela esperar, mas é aí que ela me beija."
show Heather Happy:
    ease 0.4 alpha 0.0
"É constrangedor e seu lábio inferior pressiona contra meus dentes enquanto ela me empurra para trás, batendo minha cabeça contra a porta."
"Consigo sentir o gosto da manteiga da pipoca ainda em seus lábios."
"She huffs into my mouth excitedly as she pulls me away from the door, then pushes me down on the bed."
t "— Espera, Heather."
"Minha voz é baixa enquanto ela me empurra totalmente fazendo eu ficar deitado contra a cama, com as pernas penduradas na lateral."
"Ela está realmente empolgada, e isso meio que me assusta, seus olhos arregalados e sua respiração em suspiros altos." # huffs = suspiros ?
"Seguro seus pulsos enquanto ela levanta minha camisa novamente, mas dessa vez ela vai até o pescoço."
"Ela se inclina para baixo e eu suspiro enquanto ela pressiona seu nariz frio contra meu estômago."
"Ela está tão... confiante no que está fazendo. Ela já fez isso antes?"
"Ela vai mais abaixo, então pressiona uma pata contra minha virilha. Me sento rapidamente e a empurro para trás."
t "— Heather! Vamos... vamos parar."
"Eu rapidamente baixo minha camiseta."
"Heather me olha fixamente, então se levanta sem jeito, cruzando os braços."
show Heather Sad:
    ease 0.1 alpha 1.0
h "— Você não tava gostando."
"Continuo fingindo estar me ajustando, sem ter ideia do que devo dizer."
t "— N–não, foi bom. Eu só–. Eu só não tô pronto, só isso."
"Sei que isso soa muito clichê, mas é a verdade."
"Finalmente perco a batalha com minhas orelhas e elas se abaixam para os lados da minha cabeça enquanto Cherryloom toca suavemente ao fundo."
h "— Beleza, é melhor eu ir embora de qualquer forma."
"Mas ela não se mexe. Ela fica ali, como se estivesse esperando por algo."
"Ainda estou muito chocado para realmente saber o que dizer."
t "— Você precisa de uma carona?"
"Isso é o melhor que consigo dizer."
"Ela suspira novamente antes de se virar para a porta."
h "— Não, tá tudo bem. É só alguns minutos daqui. Te vejo Segunda."
hide Heather with dis
t "— Ce–certo."
"Me levanto sem jeito para acompanhá-la até a porta, mas ela já se foi."
"Fico sentado na cama por um tempo, ouvindo o barulho da voz do meu pai um pouco antes de ouvir a porta da frente abrir e fechar."
"Então ouço alguns passos subindo as escadas e minha mãe coloca a cabeça pelo batente da porta."
mom "— Tá tudo bem? Por que você não acompanhou ela até em casa?"
t "— Eu, uhm, ela me disse que queria ir sozinha."
"Sinto minhas orelhas se abaixarem ainda mais."
mom "— Ah, certo."
"Minha mãe está prestes a sair, mas então ela coloca novamente a cabeça pelo batente da porta."
mom "— Bem, seu pai e eu estamos assistindo televisão. Que tal descer e vir com a gente?"
"Isso realmente parece legal, e minhas orelhas se levantam um pouco."
t "— Claro, vou já já."
mom "— Certo."
"Ela sorri para mim, antes de sair do batente da porta."
$ vol("sound", 0.4)
play sound "switch.ogg" # volume 0.4
stop music fadeout 0.1
"Observo a porta por mais um minuto, então suspiro e me deito novamente."
"Cubro o rosto com ambas as patas, esfregando a testa. Eu sou tão ruim nisso, por que eu sequer tentei?"
"É aí que meu celular vibra e eu o pego e vejo uma mensagem."
"" "{b}Chase:\n{i}Cmo vai o encooontrroo ;){/i}{/b}"
"Fico olhando a mensagem por um segundo, e então, por impulso, aperto o botão de ligar com meu polegar. Ele atende após o segundo toque."
m "— Ei, vii–aido. Seu encontro já acabou?" # bee-otch = vii–aido ?
t "— Ei, Chase..."
m "— O que foi?"
"Consigo ouvi-lo ajustar o celular, e sua voz deixa de soar rouca."
"Ouço a voz do Leo no fundo, abafada."
l "— Aquele TJ?"
"Começo a massagear o dorso do nariz, fechando os olhos contra a luz do quarto."
t "— É, o encontro acabou. Foi... normal, eu acho?"
m "— Cê tá me perguntando? Como foi?"
"Espero um pouco, ouvindo o som ambiente do outro lado. Consigo ouvir uma música de fundo. Me pergunto se eles estão no carro do Leo."
t "— Chase... como você sabia que era gay?"
"Há um certo silêncio do outro lado antes de eu ouvir uma explosão de risada."
"Abaixo minhas orelhas, sentindo meu rosto corar novamente. Mas não digo nada e fico só esperando que ele se recompor."
l "— O que ele falou?"
"O Leo soa bem próximo agora, como se seu focinho estivesse encostado bem no do Chase. Ouço mais alguns ajustes no celular antes que o Chase finalmente responda."
m "— Foi mal, foi mal. Eu só não esperava isso. Você tá no seu computador?”"
t "— Uh, aham."
"Levanto da cama e vou até a minha mesa, ligando o computador."
$ vol("sound")
play sound "click.ogg"
play background "comphum.ogg" fadein 3
m "— Tá, vai no site Thickfur."
"Eu digito na URL e aperto enter."
"Imediatamente um raposo musculoso sem roupas aparece."
"Ele está com as patas em suas partes íntimas e meio que as pressiona para cima."
"Há um monte de outras fotos também, mas não tenho tempo para processá-las enquanto pulo e fecho o navegador."
"Volto meus olhos para trás, quase esperando ver minha Mãe e meu Pai espiando pela porta, seus olhos arregalados em horror."
t "— Chase!"
m "— Hehe, então cê tá duro?"
t "— Quê–? Não!"
m "— Então você provavelmente não é gay, TJ. Cê gosta de ver peitos, não é?"
"Eu paro."
t "— Bem–"
m "— Pera lá, cê não gosta?"
t "— Bem... não muito, eu acho."
m "— Não é você sendo todo... Cristão, né?"
t "— Não, tá tudo bem pra mim. Eu só não liguei muito pra isso, eu acho."
m "— Acho que você pode ser assexual–ai! Leo, para com isso!"
"Consigo ouvir o celular sendo sacudido novamente e acho que sei o que está acontecendo."
l "— Do que vocês tão falando?"
"Sua voz é brincalhona acusatória e consigo ouvir mais alguns movimentos com o celular enquanto, presumo, Chase tenta afastá-lo do lobo."
m "— Beleza, TJ, É melhor eu já ir indo. Eu falo mais com você sobre isso Segunda, tá?"
t "— Tá bom."
l "— Atééé, Tejinho!"
"A voz do Leo está abafada, como se ele tivesse algo em seu focinho."
m "— E escuta, TJ–."
"Ele soa tenso."
m "— A Heather é... bem, ela não é tão... isso não é nada demais, tá legal? Beleza, já to indo. Falo com você depois!"
t "— Tchauzinho."
"Escuto o Chase começar a xingar o Leo antes dele desligar."
"Largo meu celular na cama ao meu lado e fecho os olhos, seduzido a simplesmente cair no sono naquele exato ponto."
"No entanto, me sinto melhor. O Chase sempre teve um jeito de fazer as situações parecerem boas."
"Ele se ofereceu para fazer um encontro duplo conosco, mas a Heather não quis, então não aconteceu. Isso teria tornado as coisas muito melhores."
"Começo a me perguntar o que o Chase e o Leo poderiam estar fazendo."
"Ele estava provavelmente mordiscando a orelha do Chase, o Leo faz muito isso. Na nossa frente também, às vezes."
"De fato eu acho isso meio fofinho..."
"Minha pata desce até minha virilha e pela primeira vez nas últimas horas, eu sinto algo duro."
mom "— TJ?"
"Dou um pulo quando escuto minha mãe chamando de baixo, tirando minha pata."
t "— Tô indo!"
"Rapidamente me sento e saio da cama, descendo as escadas para assistir ao resto do jogo com minha família."
$ stop_all_audio(2, reset=True)
$ renpy.pause(0.2, hard=True)
show bg black with medium_dis
$ renpy.pause(2, hard=True)
$ renpy.end_replay()
