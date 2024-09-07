label tjfriday:
stop music fadeout 3.0
window hide
scene bg friday
with transition_fade
$ renpy.pause(3.0, hard=True)
scene bg motelfull with dissolve
window show
"TJ acorda cedo de manhã e eu caio e volto no sono enquanto ele anda pelo quarto em silêncio." # I fall in and out of sleep = caio e volto no sono
"O chuveiro liga em um determinado momento e eu acho que ouço a voz da Jenna."
"Caio no sono de novo e quando acordo depois vejo a Jenna no canto do quarto, sentada à mesinha e digitando em seu notebook."
"Fico olhando para ela sonolento até que ela me perceba."
show Jenna at center with dissolve
play music "neutral.ogg" fadein 3.0
j "— Bom dia."
m "— Mmmh..."
j "— Ainda tá cansado? Já é quase meio-dia."
"Esfrego meu rosto no travesseiro e bocejo alto." # groan = bocejo alto? 
"Acho que fiquei acordado até mais tarde do que pensava."
"Eu me forço a ficar sentado."
m "— Não tava conseguindo dormir."
j "— Uhum, tá difícil pra mim também. As camas são horríveis."
"Olho em volta."
m "— Cadê o Tejinho?"
j "— Trilha."
m "— Quê?"
j "— Ele foi numa trilha."
"Fico ali sentado, franzindo a testa para a Jenna."
"Ela digita por um tempinho até que finalmente percebe eu olhando e discorda com a cabeça."
j "— Eu não sei, ele queria ir sozinho."
m "— Ele tava pedindo pra gente ir com ele a semana toda."
j "— Eu sei. Acho que tem algo incomodando ele."
"Jenna pausa."
j "— Bem, eu sei que é a gincana. É claro que é isso que tá incomodando ele."
"Fico sentado na beira da cama, esfregando meu rosto com as patas."
m "— Isso foi uma péssima ideia."
"Jenna continua digitando."
j "— Talvez, talvez não. Ele realmente queria fazer. Mas eu vou tentar conversar com ele quando ele voltar."
"Fico olhando para os meus pés por um momento, decidindo se devo ou não só enviar uma mensagem para ele agora."
m "— Jenna, cê acha que tem algo de estranho com a caça ao tesouro?"
"A Jenna nem sequer tira os olhos da tela."
j "— É claro que eu acho. Eu acho que tudo nela é estranho."
m "— Tipo, eu nem sei se o Sydney colocou aquilo tudo lá."
"Jenna finalmente levanta o olhar para mim."
j "— Por que não?"
m "— É só... é só que tudo parece errado."
j "— Quem cê acha que colocou tudo lá, então?"
"Eu levanto os ombros."
m "— Não sei."
"Jenna fica olhando para a tela do computador por um tempo, sem digitar mais."
j "— Bem, todo o motivo de estarmos fazendo isso é por causa do TJ. Isso parece ser o que ele quer fazer."
j "— E mesmo que tenha sido outra pessoa que deixou tudo lá, se isso ajudar ele então eu vou ajudar ele com isso."
"Jenna levanta os ombros."
j "— E no fim é só uma caça ao tesouro. Eu só espero que ela termine na casa."
m "— É."
"Jenna continua digitando, aparentemente encerrando a conversa então eu finalmente me levanto para tomar um banho."
scene bg parkinglotday with dissolve
"O café da manhã já acabou faz tempo quando vou à recepção e o que sobrou foram alguns biscoitos secos."
"Então eu optei por ir à lanchonete ao invés disso enquanto a Jenna optou por ficar no quarto para terminar seu trabalho."
scene bg diner with dissolve
"Sento-me na minha mesa de sempre no canto da lanchonete, folheando o cardápio sem muita vontade."
"Janice veio para anotar meu pedido e minhas respostas curtas às suas brincadeirinhas evitam que ela fale demais."
"Quando acabo de fazer o pedido, me acomodo e olho pela janela, olhando o sol brilhante assar o deserto quente abaixo."
"Imagino o TJ lá fora na trilha, caminhando com dificuldade pelo caminho sob o calor maior que 40 graus."
"Além de me preocupar com o que ele pode estar passando agora, eu também estou preocupado com a possibilidade dele passar mal com esse tipo de clima."
"Eu só posso esperar que ele tenha tido o senso de levar água suficiente e ter certeza de se refrescar, igual ele fez comigo."
"Olho para o meu celular sobre a mesa, de novo considerando se devo ou não ligar para ele."
"Talvez um textinho pelo menos..."
#"I tap out a quick one: Hey man :)"
call text_chase("tj") from _call_text_chase_12
$ renpy.pause(0.5, hard=False)
play sound "texting2.ogg"
$ renpy.pause(1, hard=False)
call text_0("m", "E aí veyr :)") from _call_text_0_11
""
call text_end from _call_text_end_12
"E então coloco meu celular de volta na mesa e espero por uma resposta, me perguntando se eu talvez dirija até a trilha se ele não responder."
"É aí que sinto alguém se aproximar da mesa."
"Eu levanto meu olhar esperando ver Janice, mas me deparo com a imagem de um jovem cervo branco, suas patas segurando um avental azul dobrado."
show Julian at center with dissolve
"Não consigo lembrar do seu nome por alguns instantes e fico com a boca aberta parecendo um idiota."
"Então me lembro."
m "— Ah, Julian. Como vai?"
"Julian sorri."
ju "— E aí... Meu turno acabou agorinha e te vi sentado aqui."
"Eu espero, mas ele não continua."
m "— Ah, uhh..."
"Eu não quero ter que falar, mas parece que ele está esperando, e eu não consigo encontrar uma saída, então..."
m "— Quer sentar?"
ju "— Sim, claro."
show Julian at left with moveinleft
"Julian responde rapidamente e senta no assento à minha frente, colocando seu avental dobrado sobre a mesa."
ju "— Valeu."
m "— Uhum, de boa."
"Me pergunto se estou parecendo um pouco irritado."
"Uma parte de mim espera que sim para que ele se toque, igual a Janice."
"Mas ele continua ali sentado, entrelaçando os dedos e apoiando os antebraços na mesa."
ju "— Como você tá hoje?"
m "— Bem. Você?"
show Julian Rejected with dis
"Julian levanta os ombros."
ju "— Eh, já estive melhor. Esse trabalho tá realmente começando a me sobrecarregar, tá ligado?"
m "— Uhum, já tive uns assim."
"Embora o cervo pareça bem simpático, eu não acho que tive mais do que cinco conversas com esse cara na minha vida inteira."
"Ele era apenas um rosto comum que eu via durante o ensino fundamental e médio, apenas alguém que estava lá."
"Não foi até os últimos anos do ensino médio que eu percebi ele e o TJ saindo, e o TJ foi o único motivo pelo qual brevemente interagimos."
"Então eu tô meio confuso agora pelo porquê dele de repente ter se interessado."
show Julian Confused with dis
ju "— Sério? Com o que você trabalha?"
m "— Uh, bem, eu tô me decidindo sobre trabalhos agora. Eu tô na faculdade mas provavelmente vou trabalhar de repositor durante o verão, igual eu fiz ano passado."
ju "— Então esse trabalho te sobrecarregou?"
m "— Bem... não, mas o meu em fast food sim, aquele que eu tinha no ensino médio. Eu meio que gosto de empilhar caixas e colocar coisas em prateleiras."
ju "— Olha, eu acho que os trabalhos em serviço de alimentação são com certeza os piores, então eu entendo por que estocar pode ser um pouquinho melhor."
show Janice Happy at right with dissolve
"Ele para quando a Janice volta, colocando meu sanduíche de frango na mesa."
ja "— Ah! Você conhece o Chase, Julian?"
ju "— Um pouquinho! Eu conheço ele por causa do TJ."
ja "— Ah! Bem, se você ver o garoto de novo fala pra ele que eu gostaria de conversar com ele!"
hide Janice with dissolve
"Levanto meu olhar e a Janice me dá uma piscadela antes de sair apressada."
"Decido que com certeza não vou contar para o TJ."
show Julian Rejected with dis
ju "— Mas enfim, eu tô na faculdade também, lá em Mesa, e essa lanchonete tem uns horários bem flexíveis. Único motivo pelo qual eu ainda tô aqui."
m "— Pelo menos cês não parecem muito ocupados, até durante o horário de almoço."
"Eu aponto com a cabeça para as outras duas ou três mesas ocupadas."
ju "— Heh, é, é um milagre que ainda estamos em atividade. Provavelmente vai ter que fechar em um ou dois anos."
"Pensar nisso realmente me deixa um pouco triste."
"Olho para o meu sanduíche de frango, sentindo um pouco envergonhado pensando no Julian só me vendo comer, então deixo-o no prato por enquanto."
"Julian se acomoda e olha pela janela."
show Julian Confused with dis
ju "— Então... cadê o Tejinho? Achei que cês tavam saindo juntos?"
"Sinto que esse é o principal motivo pelo qual o Julian está falando comigo."
m "— É, ele saiu numa trilha cedo de manhã. Eu dormi até tarde."
ju "— Ahh, saquei. Ele ainda faz isso muito?"
"Levantos os ombros."
m "— Não sei. Só tamo aqui faz tipo uma semana. Mas ele ama ir em trilhas."
ju "— Tipo, ele faz trilha quando tá UCC?"
"I stare at Julian for a second before I realize what he's talking about."
m "— Ah, não, eu não vou pra UCC. Eu sou da Pueblo."
ju "— Huh, então vocês se encontraram aqui?"
m "— Bem, eu busquei ele e trouxe ele pra cá, junto com a Jenna, mas ela é da Pueblo também..."
"Começo a ficar um pouco irritado por ter que explicar tudo para esse cara."
"Tudo o que eu quero fazer é comer, depois voltar para o hotel e esperar pelo TJ."
ju "— Tendi... bem, o TJ foi meu melhor amigo no terceirão, depois que você e o Carl foram embora. A gente saía sempre. Depois que ele foi pra faculdade a gente meio que perdeu contato." # senior year = terceirão?
m "— Hmm, é, ele não usa tanto redes sociais."
"Eu só vi o TJ postar algumas fotos desde que ele começou as aulas."
"Algumas eram dele no time de futebol da faculdade, e uma era dele em pé em um círculo de oração junto com uma frase inspiracional."
"Mas o Julian revelar que era o melhor amigo do TJ durante o final do ensino médio esfria minha frustração."
"Creio que ele realmente tem um motivo para saber como o TJ está."
ju "— Ele tava meio depressivo logo depois da formatura, então eu fiquei um pouco preocupado com ele."
m "— Depressivo?"
"Isso me surpreende."
"Eu nunca ouvi alguém dizendo que o TJ está depressivo."
"Claro, ele já ficou triste antes, mas não ficou totalmente depressivo, até onde eu sei."
"Talvez eu não saiba muito sobre ele."
ju "— Eu achava que poderia ter a ver com a formatura, mas isso continuou durante o verão inteiro."
m "— Ah... bem, se você quiser conversar com ele eu posso com certeza falar pra ele."
"Faço um gesto para o meu celular sobre a mesa."
"Também faço uma anotação mental para mim mesmo de que deveria conversar com o TJ também... sobre tudo."
show Julian with dis
"Julian sorri."
ju "— Seria ótimo! Por favor. Acho que ele deve ter mudado de número depois de ter ido embora."
m "— Beleza."
"Eu hesito, depois pego o celular e digito a breve mensagem."
hide Julian with dissolve
call text_chase("tj") from _call_text_chase_13
$ renpy.pause(0.5, hard=False)
play sound "texting2.ogg"
$ renpy.pause(1, hard=False)
call text_0("m", "Acabei de encontrar o Julian na lanchonete. Ele queria conversar com vc :)") from _call_text_0_12
""
"O TJ ainda não me respondeu."
ju "— Desde quando cê conhece o TJ?"
call text_end from _call_text_end_13
show Julian at left with dissolve
"Coloco meu celular de volta na mesa e me acomodo no assento."
m "— Desde que ele chegou aqui em 2001, então tipo quatorze anos atrás?"
ju "— Caraaamba, isso é muito tempo."
m "— É, realmente."
ju "— Cês sempre foram bons amigos?"
m "— Em geral sim... já teve momentos em que eu era meio ótario com ele, mas ele sempre foi um bom amigo pra mim."
ju "— Saquei, saquei... É, nós todos estudávamos na mesma escola no fundamental, mas não foi até o segundo ano do ensino médio que eu conheci ele no ensino religioso."
m "— Ah."
"É claro."
ju "— Mas eu sempre sabia sobre vocês, os moleques de Echo."
m "— Uhum, era a gente mesmo. Os esquisitinhos."
show Julian Depressed with dis
"Julian olha em volta antes de abaixar a voz."
ju "— Era algo maldoso de se dizer, mas essa cidade É meio pertubadora. Muitas coisas estranhas acontecem aqui."
m "— Não posso negar isso."
stop music fadeout 10.0
"Julian olha em volta outra vez, mordendo o lábio."
"Então ele abaixa a voz mais um pouquinho."
ju "— Ei, então isso vai ser meio estranho, e eu não quero te ofender, mas isso é algo que vem me incomodando há algum tempo."
"Olho para o Julian com receio."
m "— Sim?"
ju "— O TJ me contou o que aconteceu no Lago Emma um tempo atrás quando távamos conversando sobre a morte e o céu."
"Eu sinto um leve arrepio em minha espinha."
ju "— Bem, ele nunca me contou sobre o que {i}exatamente{/i} aconteceu, mas eu sei que isso realmente afeta ele."
"Julian para, mas eu não digo nada, mantendo meus olhos fixados na mesa."
ju "— Olha, você não precisa me contar, e se isso te deixar desconfortável por favor não–"
ju "— –mas eu sinto que se tiver uma melhor noção do que aconteceu, eu talvez entenda {i}ele{/i} um pouco melhor."
"Julian leva os dedos entrelaçados até o queixo para apoiá-lo."
ju "— Eu não vou pedir a ELE pra me contar, é claro. Eu sei que foi há muito tempo atrás, mas eu sei que essas coisas podem ser carregadas por muito tempo."
ju "— Então se você não estiver bem com isso por favor me fala e eu vou mudar de assunto."
"Fico refletindo sobre isso por um momento, me perguntando se o cervo não está sendo sem noção para perguntar sobre tal coisa."
"Eu decido que ele não está."
"Ele é um dos melhores amigos do TJ, então de certa forma ele está meio que relacionado a isso."
"Então eu acho que ele realmente tem um motivo para saber."
m "— Beleza, mas por favor não fala sobre isso com o TJ. Como cê disse, isso ainda afeta ele muito."
show Julian Confused with dis
ju "— Eu prometo." # never = eu prometo?
"Julian olha para mim com seriedade."
"Penso por um momento, reunindo meus pensamentos."
"Já faz muito tempo que eu não penso na história do começo ao fim."
play music "when_your_arms_were_around_me.ogg" fadein 3.0
m "— Foi por volta de Agosto eu acho, 2003. É meio difícil de lembrar."
m "— O que eu me lembro é que todos nós descemos a rua até o lago pra nadar igual a gente fazia quase toda semana."
m "— Tem um lugarzinho onde a praia meio que faz uma curva e é basicamente só areia e água rasa. Era lá que a gente geralmente ficava e nadava."
m "— Mesmo a água sempre estando meio parada lá, era pelo menos seguro e quente comparado com o resto do lago."
m "— Eu acho que em algum momento um de nós queria ir e jogar pedras na água pra ver qual conseguia ir mais longe." # skip rocks = jogar pedras na água?
m "— A gente tinha que ir mais adiante na costa pra fazer isso, e o TJ tava mais interessado em construir castelos de areia." # parte que usa "up", não sei se realmente tão indo pra cima
m "— Então ele ficou pra trás enquanto o resto de nós foi até a praia pra encontrar as pedras."
m "— Quando você vai lá longe não dá pra realmente ver o lugar mais, então eu não tenho total certeza do que aconteceu."
"Me lembro vagamente de olhar para trás de volta ao TJ enquanto íamos até a praia."
"O lince curvado sobre seu castelo, a parte de trás do seu shorts molhado coberto de areia de quando ele se sentou."
m "— O Sydney veio com a gente, pelo menos eu me lembro disso, mas enquanto a gente tava jogando pedras na água ele só meio que desapareceu."
"Dou uma leve olhada para o Julian por um momento e vejo ele ouvindo atentamente antes de eu voltar a olhar para a mesa."
m "— Enfim, ouvimos uns sons de água e uns gritos do TJ e todos nós fomos correndo e vimos o Sydney boiando no lago..."
m "— Eu nadei até lá e peguei ele. Mas já era tarde demais."
"Não menciono a parte onde o TJ estava agachado em um metro da água, encarando o corpo do Sydney boiando a seis metros de distância dele." # was crouched in three feet of water = a um/em um?
"Não digo a ele que a explicação do TJ para o que aconteceu sempre queria dizer que o Sydney foi longe demais na água."
"Que talvez a correnteza tenha desequilibrado ele e o puxado para o fundo."
"Como ele até disse que quase parecia como se um tubarão invisível havia pegado o Syd e o puxado para o fundo."
"Como nada disso faz sentido nenhum."
m "— Nenhum de nós tem certeza do que aconteceu."
stop music fadeout 15.0
show Julian Depressed with dis
"Mas parece ser o suficiente para o Julian, enquanto ele discorda com a cabeça."
ju "— Eu sinto muito, muito mesmo por ouvir disso, mas obrigado por me contar. Tudo que eu sabia era que um amigo dele tinha se afogado no lago."
ju "— Ele não me disse o quão perto ele tava disso. Faz sentido que isso ainda afete ele profundamente."
m "— Sem problemas."
play music "neutraldiner.ogg" fadein 3.0
"Percebo que o Julian é provavelmente a primeira pessoa que eu contei essa historia fora de Echo."
"Também percebo que não foi tão dificil assim de contá-la."
"Acho que é mais fácil de contar para alguém que não estava relacionado ao incidente, alguém que não tem nenhuma relação com o horror cruel daquele dia."
"Isso, e que muito tempo se passou."
"Talvez eu só tenha superado sem ter percebido."
show Julian Confused with dis
ju "— Mas é, Echo é um lugar bizarro. Cê sabe sobre aquela parada de histeria em massa que aconteceu cem anos atrás? Esse lugar é meio famoso por isso."
ju "— Quase todos os podcasts paranormais que eu escuto tem um episódio sobre."
"Meu coração dispara enquanto eu repentinamente lembro do meu projeto."
"Cubro o rosto com minhas patas."
m "— Merda..."
ju "— O que foi? Eu falei alguma coisa...?"
"Descubro meu rosto e vejo o Julian olhando para mim com certa preocupação."
m "— Não, eu... eu só esqueci um trabalho escolar que eu preciso terminar, um projeto."
"Toda a empolgação com a gincana apagou ele completamente da minha cabeça."
ju "— Ah? Que tipo de projeto?"
m "— Uma reportagem sobre Echo e aquele incidente de histeria em massa. Eu fiz quase nada dele desde que cheguei aqui."
ju "— Ei, isso é legal pra caralho!! Cê precisa de ajuda?"
"Eu pisco, a empolgação do cervo me surpreende."
show Julian Sheepish with dis
"Pela primeira vez eu vejo ele ficar com vergonha, a pele dentro de suas orelhas ficando vermelho escuro."
ju "— Desculpa, é algo que sempre me interessou então eu fiquei um tiquinho empolgado, hehe."
"Dou uma olhada para meu celular e vejo que ainda não recebi uma resposta do TJ, então eu tenho uma ideia."
"Apesar da mimha irritação inicial, eu gosto do quão considerável o Julian foi sobre todo o incidência do lago."
"Eu também quero dar a ele uma chance de ver o TJ antes do fim da nossa viagem."
m "— Bem, na verdade eu queria tirar umas filmagens da mina, ou pelo menos da entrada já que ela tá fechada."
m "— Se você quiser, a gente pode ir até lá pra tirar umas filmagens e ao mesmo tempo procurar pelo TJ. A trilha fica naquela área."
show Julian with dis
"Julian se anima."
ju "— Ei, isso séria incrível pra caramba. Valeu! Cê quer comer primeiro?"
"Olho para meu sanduíche na mesa, então discordo com a cabeça."
m "— Eu vou só comer ele enquanto tiver indo até o hotel."
stop music fadeout 5.0
ju "— Ah, eu tenho uma caminhonete! Eu posso te levar até lá, e tem bastante espaço se você precisar pro seu equipamento."
m "— Ah, beleza. É, valeu. Só deixa eu pedir uma embalagem pra levar e a gente pode sair."

scene bg dirtroad with fade
play background "highway.ogg" fadein 5.0
"Vinte minutos depois e estamos indo pela rua estreita do cânion em direção à mina."
"Eu não estive lá faz anos, mas a rua de terra leva diretamente a ela, então não preciso nem procurar instruções."
"Julian conversa enquanto eu como meu sanduíche morno de uma embalagem de isopor."
"Embora haja uma qualidade quase robótica no cervo com o quão articulado ele é, ele também é muito gentil." # almost robotic quality?
"Consigo certamente ver por que o TJ o considera um amigo."
stop background fadeout 3.0
play loop "engine.ogg" fadein 3.0
"A rua esburacada faz uma curva para cima e finalmente chegamos na mina."
scene bg echomine with dissolve
"Há um largo espaço de terra aberto para estacionar, junto com algumas barreiras de concreto pela beira da calçada." # drop-off = calçada?
"Tem algumas placas de aviso, provavelmente dando uma breve história sobre a mina e ao lado está a mi–" # sign posts = placas de aviso?
"Está o TJ."
"O lince está sentando na abertura da mina, bem na entrada."
"Ele está encostado contra a grade de aço que sela a entrada."
m "— Puta que..."
"Julian para de falar e olha para mim, e então na direção que estou olhando."
ju "— Caramba, é o Tejinho alí?"
"Eu não digo nada porque percebi agora o quão fraco o lince parece, sua cabeça inclinada para trás, suas patas fracamente deitadas no chão."
stop loop fadeout 5.0
play sound "cardoor.mp3"
"Estou fora da caminhonete antes do Julian sequer conseguir estacionar, minha embalagem de isopor caindo bem no cascalho enquanto eu corro até o TJ."
m "— TJ! Ei, o que aconteceu!? Você tá bem?"
"O lince não responde e quando chego até ele vejo que seus olhos estão abertos, mas virados para trás ao ponto que eu só consigo ver branco."
"Me curvo sobre ele, tentar ajudá-lo a melhorar sua postura fica mais difícil por conta de sua mochila pesada atrapalhando."
play background "whispers.ogg" fadein 5.0
"Enquanto ajudo-o, sinto uma corrente de ar frio vindo da mina, passando pelo aço."
"Eu ignoro isso no começo, focado em tentar conseguir uma resposta do TJ, mas então eu percebo que há um som de chiado vindo com ela, como se alguém estivesse expirando."
#"I glance to my left, through the grid, and I come face to face with a blood-red visage of rage."
#"I see piercing yellow eyes, and a row of white, blocky teeth...and then all of the blackness that extends beyond it..."
#unk "\"How long do you think you can keep it hidden? You know someone's onto you.\""
#"A clawed and withered hand sticks out through the bars, resting on TJ's head, ruffing his ears almost affectionately."
#unk "\"How could he ever forgive you?\""
#"I stare back at a different face - increasingly empty eyes, pools of bottomless silence..."
stop background fadeout 5.0
play loop "reststop.ogg" fadein 3.0
"Dou uma olhada pela grade, mas eu não vejo nada."
"Mesmo assim, sinto um calafrio que a abertura está respirando de alguma forma."
show Julian Depressed at right with dissolve
ju "— Ele tá bem!?"
"O grito e a correria do Julian perto de mim faz minha atenção voltar ao TJ."
"Olho para o lince no chão e vejo suas orelhas se contorcendo para os lados." # twitching = contorcendo?
show TJ Neutral at left with dissolve
t "— Uhm, que–?"
"Eu me agacho ao lado dele, colocando uma pata atrás de sua cabeça para lhe dar um pouco de apoio."
m "— TJ, o que rolou? Você tá bem?"
"TJ vira para mim, piscando confuso."
t "— Bem? O que aconteceu?"
"Ele esfrega os olhos com a parte de trás da pata antes de se ajeitar para conseguir se sentar direito."
ju "— Você só tava sentado aí. Quase parecia que você tava–"
"Julian para."
m "— Parecia que você tava desmaiado, ou algo assim."
"TJ finalmente parece focar em nós, o olhar confuso em seus olhos desaparece."
t "— Desmaiado? Ah! Não, eu só tava tirando um cochilinho, haha."
"TJ dá uma risada curta e descansa a cabeça contra a mochila."
m "— Quê? Aqui?"
"Olho de volta para a mina fechada, a escuridão sinistra ainda parecendo estar se abrindo para nós."
m "— Por quê?"
t "— Bem, tá mais quente que o normal hoje, então eu comecei a sentir como se fosse desmaiar. Eu achei que isso poderia ser um mau sinal, então eu decidi descansar quando chegasse aqui."
m "— Cê veio aqui de propósito?"
t "— Uhum, eu vi o cânion com você da última vez, então eu decidi visitar a mina dessa vez."
"TJ sorri de forma preguiçosa para mim enquanto continua a inclinar-se contra sua mochila." # de forma preguiçosa ?  
t "— Desculpa por ter te deixado preocupado e– Ah, Julian!"
"TJ de repente parece perceber que o cervo está aqui."
t "— O que você tá fazendo aqui!?"
"TJ rapidamente se levanta, tirando os braços das alças de sua mochila."
play music "comeover.ogg" fadein 3.0
stop loop fadeout 3.0
show Julian with dis
"Ele abraça Julian, o cervo o abraça de volta com o mesmo entusiasmo."
"O TJ nem sequer me cumprimenta tão... intimamente."
"Acho que eles têm mais passado juntos do que eu pensava..." # more of a history = mais passado juntos ?
ju "— Ei Tejinho. É, eu encontrei o Chase na lanchonete."
ju "— Você não tava respondendo as mensagens, então nós dois decidimos vir aqui e te achar... isso, e o Chase precisa fazer algumas filmagens pro projeto dele."
show TJ with dis
t "— Ah legal! Você precisa de ajuda com isso, Chase?"
"TJ se vira para mim com um sorriso."
"Eu não sei o que é, mas o TJ está agindo com muito mais ânimo do que estava ontem."
"Aquela melancolia quase sombria desapareceu, substituída por sua alegria de sempre."
"Eu preciso sorrir por causa disso, apesar da situação de poucos minutos atrás."
m "— Claro."
"Outra corrente de ar frio parece passar suavemente pelo aço."
"Eu olho de volta para a grade."
m "— TJ, por que que cê dormiria aqui bem lado da mina sinistra?"
show TJ Rejected with dis
"TJ fica sem expressão."
t "— Foi bem agradável."
t "— Tipo, fresco. Eu tava deitado na abertura e senti um arzinho agradável saindo, então eu decidi me encostar ao lado. É uma sensação muito boa."
"TJ caminha até a grade de metal e estende os braços, agarrando-se às barras enquanto pressiona seu rosto contra ela."
t "— Ahhhhh... ergh."
"Ele inclina a cabeça para trás, com uma expressão de desgosto."
t "— Bem, tá com cheiro de mofo bem forte, mas a sensação é ótima!"
m "— Hmm..."
"Olho de volta para a abertura, a escuridão em seu interior causando arrepios na minha espinha."
"Eu me lembro de quando um corpo foi encontrado lá há cerca de cem anos atrás."
"Embora eu saiba que não há nenhum cadáver lá dentro agora, isso ainda me deixa arrepiado pra cacete."
"Tento esconder meu tremor enquanto me afasto, olhando de volta para a caminhonete."
show TJ Neutral with dis
t "— Ei, então a gente vai pra casa antiga do Sydney agora? Foi por isso que vocês vieram me achar?"
"O TJ tá tentando disfarçar, mas eu consigo ouvir a ansiedade em sua voz." # eagerness = ansiedade ?
"Eu me viro para olhar para ele, o lince agora de costas para a mina, encostado contra a grade."
"Eu quero falar para ele sair da abertura, mas eu não conseguiria explicar a ele o porquê."
m "— Bem, deixa eu fazer algumas filmagens primeiro. Eu posso fazer a narração depois, então vai ser rápido."
"Eu seguro uma expressão de vergonha enquanto percebo quanto tempo isso também vai levar." # wince = expressão de vergonha ?
"Meu projeto vai ficar uma merda a essa altura, não tem como evitar."
"Eu só preciso fazer com que seja o menos merda possível."
show TJ with dis
t "— Ah é, desculpa, hehe."
"TJ ri nervoso, e então desvia o olhar."
t "— Desculpa, só tô um pouquinho zonzo por causa do cochilo. Vocês realmente me deixaram surpreso."
m "— De boa. Eu vou ir pegar meu equipamento bem rápido, tá?"
"TJ concorda com a cabeça para mim e vou correndo até a caminhonete estacionada para pegar minha câmera."
hide TJ
hide Julian
with dissolve
"Então o TJ pode ainda estar agindo um pouco estranho, mas estou feliz que ele parece alegre novamente."
"Ver ele do jeito que estava ontem à noite foi... um pouco angustiante para dizer no mínimo."
"Pego a bolsa da câmera na caçamba da caminhonete e volto, diminuindo a velocidade para a de uma caminhada já que o calor já está começando a me afetar."
"Como o TJ conseguiu fazer uma trilha longa-pra-caramba é inacreditável para mim."
"Parece quase insensato."
"Especialmente para alguém como o TJ que sabe o quão perigoso isso pode ser."
show TJ at left with dissolve
show Julian at right with dissolve
"Quando volto para a entrada da mina eu vejo o Julian e o TJ sentados de costas para a abertura um de cada lado, conversando um com o outro."
"Eles estão comendo barras de cereais e o TJ estende uma para mim enquanto me aproximo."
m "— Valeu... Ei, TJ?"
t "— Hum?"
"TJ levanta o olhar para mim inocentemente."
m "— Se você for fazer uma trilha de novo, não se esquece de me trazer na próxima, tá bom? Eu não acho que cê deveria ficar sozinho por aqui."
show TJ Sheepish with dis
t "— Ah... Tá bom, claro."
"Suas orelhas se abaixam um pouco, seu rosto com uma leve expressão de culpa." # frown = culpa ?
m "— Eu só não quero que você se machuque, sabe? Tá muito quente hoje e teria sido realmente terrível se você tivesse desmaiado sozinho."
t "— É, desculpa."
"Largo a bolsa gentilmente no chão antes de me encostar na parede próxima ao lince."
m "— Tá tudo bem. Eu só quero ter certeza de que cê tá bem."
t "— Heh, obrigado. Eu só não queria te acordar hoje de manhã."
m "— A Jenna se ofereceu pra ir contigo, não foi?"
"TJ suspira baixinho, desviando o olhar para a mina."
t "— Foi, mas eu sei que vocês não querem ir. Eu só não quero estragar essa viagem pra vocês mais do que já fiz."
m "— Quê!? TJ do que cê tá falando?"
"TJ fica calado, e então apenas levanta os ombros."
"Talvez ele não tenha voltado ao seu antigo eu antigo afinal..."
ju "— Eu não me importaria de ir contigo, TJ. Eu amo trilha."
"Julian sorri gentilmente para o lince."
"Por algum motivo eu sinto um pequeno aperto de irritação no meu peito."
"É idiota, mas fui eu quem se ofereceu primeiro, e fui eu quem foi com o TJ na primeira vez."
m "— É, nós dois podemos ir. O ponto é que é pra você não ir sozinho na próxima, tá bom Tejinho?"
t "— Aham, okay. Obrigado vocês dois."
ju "— Sem problema."
"Um breve silêncio se estabelece entre nós três até o Julian falar novamente."
ju "— A gente tava falando sobre o nosso antigo grupo de estudo bíblico."
show TJ Neutral with dis
t "— Ugh."
"TJ encosta a cabeça na parede, revirando os olhos."
"É uma expressão que eu não vejo vindo dele com muita frequência."
m "— O que que tem?"
show Julian Happy with dis
ju "— Ah, só o jeito que o TJ sempre levava tão a sério, e mais ninguém não, haha."
"TJ discorda com a cabeça em desaprovação."
t "— É, eu nunca tive nenhum controle sobre aquele clube."
m "— Ah sério? Cê era o responsável?"
"É um pouco estranho pensar no TJ em uma posição de liderança como essa."
"Eu só nunca vi ele sendo quem toma a iniciativa no ensino médio." # I just never knew him to put himself out there in high school
t "— Uhum, eu revivi ele depois que ele ficou meio que desativado por alguns anos. Não era tão popular assim."
"TJ sorri com um certo constrangimento."
ju "— É, a gente tinha tipo, três outros membros sem contar você e eu."
t "— É, e um saiu depois de tipo, dois encontros."
show Julian Wry with dis
"Julian estala a língua."
ju "— Que escola tão sem Deus a gente foi hein."
show TJ Surprised with dis
t "— Ei!"
ju "— Cê sabe que eu tô brincando... na maior parte." # mostly = na maior parte ?
show TJ Neutral with dis
t "— Bem, eu realmente queria que os ateus participassem também, desde que eles não fossem inconvenientes. Eu só queria mostrar a todos o quão agradável poderia ser a experiência–"
t "— –mesmo que você não acreditasse."
"Me lembro bem vagamente do TJ me convidando para ir ao clube e eu dizendo que ia pensar sobre."
"Eu nunca fui, é claro."
t "— Mas acabou não sendo tão espiritual assim."
ju "— É, na maior parte do tempo a gente só conversava e levava comida. Demorou um pouco pro TJ perceber que ninguém queria outra sessão de escola dominical só que na escola."
t "— Uhum. Horas de planejamento jogadas fora."
ju "— Mesmo assim era muito legal. Eu acho que nós quatro ficamos mais felizes com isso."
t "— É, acho que sim."
"TJ parece ter me percebido de repente."
t "— Ah, desculpa Chase, você não saberia muito sobre isso." # you wouldn't know much ?
m "— De boa. É interessante ouvir sobre."
"Novamente, sinto uma pequena pontada de inveja, mesmo sabendo que não é justo."
"Eu tinha escolhido não participar, provavelmente usando aquele tempo para ir para casa e... sair com o Leo."
ju "— Cê não perdeu muita coisa. Só discussões sobre filmes e... assistir uns filmes também."
t "— Ugh, nem pra eles terem um tema religioso pelo menos."
ju "— Graças a Deus."
t "— Ei!"
"Eu rio do quão indignado o TJ está."
t "— Bem, eu tô feliz que você se divertiu pelo menos. Eu saí de lá achando que tudo foi um fracasso." # I came away = eu sai de lá ?
ju "— Eu acho que me lembro de você ter falado que queria que seu amiguinho aqui tivesse aparecido."
show TJ Sheepish with dis
t "— Er... Eu não me lembro muito bem disso."
ju "— É claro que lembra, você sempre falava isso."
"As orelhas do TJ se abaixam e ficam avermelhadas."
m "— Quem, eu?"
ju "— Aham!"
"Julian sorri enquanto o TJ tenta desviar o olhar."
"Mesmo a situação sendo meio engraçada, agora eu me sinto pior ainda sobre nunca ter ido."
m "— Ugh, desculpa Tejinho. Sabe, a gente tava no ensino médio e tals..."
t "— É, eu entendo. Não se preocupa."
ju "— Então, cê começou outro clube na faculdade?"
show TJ with dis
"TJ sorri."
t "— É uma faculdade Cristã, então tem tipo, cinquenta clubes sobre religião."
ju "— Ah? Cê é membro de algum deles? "
t "— Uh, alguns."
m "— Quais?"
t "— Uh... um clube de solteiros."
m "— Solteiros?"
ju "— Um de arranjar alguém?"
t "— Isso."
"Ele desvia o olhar de novo."
"É hilário o quão constrangido ele é sobre esse tipo de assunto."
"Ele tá na universidade; tudo isso deveria ser normal de se conversar, mas não com o TJ."
m "— Você conheceu alguém?"
show TJ Neutral with dis
t "— Ei Chase, você não tem que filmar umas coisas?"
"Ele olha de volta para mim franzindo a testa."
m "— Nooossa, só tava perguntado."
show Julian Happy with dis
"Julian dá uma risadinha baixinho."
"Eu me agacho e começo a pegar meu equipamento, decidindo que algumas filmagens longas com o tripé devem ser suficientes." # long shots = filmagens longas ?
"Enquanto estou estendendo as pernas, o Julian pergunta ao TJ sobre a trilha."
show Julian with dis
ju "— Foi divertido?"
"TJ levanta os ombros, terminando sua última barra de cereal e esfregando as patas para tirar as migalhas."
t "— Foi ok, tava bastante silêncio."
"Eu me retraio enquanto uma das minhas patas fica apertada entre o metal." # I wince = eu me retraio ? pads = patas ?
t "— Meio assustador pra falar a verdade. Eu ia gostar que vocês dois viessem comigo uma hora, se eu for de novo." # sometime = uma hora ?
ju "— É claro."
m "— Sim, com certeza."
stop music fadeout 5.0
play background "reststop.ogg" fadein 3.0
"Durante os 20 minutos seguintes eu posicionei a câmera em três pontos diferentes, conseguindo cerca de um minuto de filmagem em cada um."
"O TJ e o Julian ficam sentados na caminhonete enquanto isso, e sempre que eu dou uma olhada para eles os dois parecem estar conversando alegremente e rindo."
"Quando acabo, eu suspiro e rapidamente coloco o suporte de volta na bolsa junto com a câmera."
"Vejo a minha embalagem de isopor na terra e considero pegá-la... mas não pego."
"Coloco a bolsa na caminhonete de novo antes de ir para o banco do passageiro, deixando o TJ sentado entre nós dois."
stop background fadeout 3.0
"Eles ficam calados quando começamos a sair pela estrada de terra."
scene bg dirtroad with fade
play background "highway.ogg" fadein 5.0
m "— Do que vocês tavam falando?"
ju "— Nada demais. Só sobre o ensino médio."
"TJ concorda com a cabeça."
"Novamente estou começando a me sentir um pouco de fora entre esses dois, tipo como se estivesse segurando vela..."
m "— Então... qual é o plano agora?"
t "— Bem, nós pensamos em ir pra aquela casa agora, depois de buscarmos a Jenna e o Carl."
m "— Beleza."
"Dirigimos em silêncio por um curto período e por algum motivo eu começo a desejar que eu estivesse sentado no meio."
"O jeito que o Julian continua virando o volante força o seu cotovelo a encostar no lado do TJ e–"
"Eu me forço a desviar o olhar, me perguntando que porra eu tô pensando."
"Eu tô tratando o TJ como se ele fosse algo que pertence a mim."
"Nós só saímos recentemente no decorrer dessa semana."
"Eu mal falei com ele nos últimos dois anos."
"Eu me forço a olhar para frente, além do para-brisa."
play sound "phonebuzz.ogg"
"Então o celular do TJ vibra e meus olhos naturalmente vão até a tela enquanto o lince o pega."
"Eu vejo o nome \"Flynn\", e então a mensagem abaixo."
"Eu apenas tenho tempo para ver poucas palavras:"
"\"Tu sabe\" \"dele\" \"PORRA\" \"me conta\""
"TJ puxa o celular de volta para baixo e eu desvio o olhar assim que sinto os olhos do Lince em meu rosto." # jerks = puxa ?
"Eu me pergunto se ele me viu olhando, tenho certeza que sim."
"Mas isso realmente não importa, porque agora estou me perguntando que porra o Flynn acha que tá fazendo."
"Eles têm ficado longe um do outro nos últimos dias obviamente, mas eu acho que o Flynn achou outro jeito de falar com o TJ."
"Que porra ele acha que tá fazendo?"
"Eu me sinto ficando com raiva."
"Eu não sei exatamente o que o lagarto tá falando pro TJ, mas julgando pelo que vi definitivamente não é algo bom."
"Faço uma anotação mental para perguntar ao TJ sobre isso hoje à noite."
stop background fadeout 3.0
"Se ele não me disser então eu vou deixar o Leo sabendo."
"Ele vai dar um jeito."

scene bg sydneyhouse with dissolve
play background "reststop.ogg" fadein 3.0
"Todos nós andamos pela calçada até a antiga casa estilo americano de um só andar."
"Já faz tanto, tanto tempo desde que eu vi esse lugar."
"Mais ainda desde que andei nesse caminho."
"A casa do Sydney é pela estrada de cascalho atrás da \"floresta\"."
"É um lugar um pouquinho estranho, isolado do resto da cidade."
"Foi o melhor possível para nós, eu acho." # It was all the better for us = Foi o melhor possível para nós ?
"É bom não ser lembrado do que aconteceu."
show Carl Rejected at right with dissolve
c "— Galera... eu não sei não. Cês acham que ele vai só deixar a gente entrar numa boa?"
show TJ Neutral at center with dissolve
t "— O que mais a gente pode fazer?"
c "— Uhhh, talvez o Sydney não tava se referindo ao quarto dele?"
t "— Aonde mais ele iria dormir?"
c "— Eu... não sei"
m "— Tipo assim, ele cochilava em lugares aleatorios, se me lembro bem. Tipo, ele já dormiu até no meu sofá."
show TJ Annoyed with dis
t "— Para, Chase. Você sabe que não foi isso que ele quis dizer."
m "— Bem, quem sabe?"
t "— Eu sei. Eu sei onde tá."
"Aquela tensão sombria na voz do TJ está surgindo novamente." # dark edge = tensão sombria ?
show Julian Confused at farright
show TJ Neutral
with dissolve
ju "— Acho que não vai fazer mal nenhum em perguntar."
show Jenna Neutralhips at farright with dissolve
j "— Não dá pra negar que é meio estranho pra cinco jovens adultos de repente aparecerem na sua porta pedindo pra entrarem."
t "— Mas não temos muita escolha, não é?"
show Carl Depressed with dis
"TJ está indo à frente de todos nós, caminhando pelos degraus de concreto sem hesitar antes de imediatamente tocar a campainha."
m "— Eita, espera! A gente nem pensou no que a gente vai falar."
t "— Eu já sei o que eu vou dizer."
show Jenna Rejectedhips with dis
"Ficamos ali perplexos em silêncio por um tempo e eu olho em volta para os outros."
"Carl parece completamente desconfortável, quase enjoado, suas patas enfiadas no fundo dos bolsos enquanto ele olha fixamente para o chão."
"Jenna está olhando para o TJ, suas sobrancelhas franzidas, claramente preocupada."
"Julian apenas fica ali, como se a situação não o incomodasse nem um pouco."
"A porta finalmente abre, revelando um jovem panda vermelho, não muito mais velho do que nós."
"Ele pisca para nós, depois coloca um sorriso no rosto."
unk "— Olá... como eu posso ajudar?"
"Vejo as orelhas do TJ se abaixarem por um momento, sua determinação originalmente firme claramente caindo."
t "— Uh, humm, olá..."
"O panda vermelho olha para o TJ por um momento, esperando atentamente."
"Eu não o reconheço, e tenho certeza de que teria o visto pela cidade se ele tivesse se mudado depois que os pais do Sydney se mudaram."
"Deve ter sido em algum momento recente, há alguns anos atrás."
"Então eu decido que devo intervir para deixar o TJ tentar se recompor."
m "— Opa! Eu sou o Chase, esse é o TJ... o Carl, a Jenna, e o Julian."
"Eu aponto para cada um, sentindo minhas bochechas ficarem quentes."
show Injy at farleft with dissolve
inj "— Oi... pessoal. Eu me chamo... Injy."
"Outro momento de silêncio constrangedor antes de eu tentar pensar em outra coisa para dizer."
"Como caralho você fala que quer revistar a casa de alguém porque ela pertencia ao seu amigo morto?"
"Enquanto estou tentando descobrir como, o TJ fala novamente."
t "— M–meu... nosso amigo morava aqui, há uns doze anos atrás?"
inj "— Ah é mesmo?"
"O panda parece estar pensando."
inj "— Você tá falando sobre um... Cindy?"
t "— Sydney, é, ele era nosso amigo."
inj "— Ah! Eu sinto muito, eu não consegui me lembrar do nome. Eu acho que a tia dele me contou o que aconteceu."
t "— Sim, e uh, ele deixou algo pra trás pra gente, no quarto dele. Tudo bem se entrarmos e procurarmos isso?"
"O olhar originalmente curioso do Injy foi substituído por um olhar de dúvida e definitivamente um pouco de suspeita."
inj "— Ah, todos vocês?"
show Carl Depressed with dis
"Percebo que o Carl ainda está olhando fixamente para o chão, suas patas se revirando em seus bolsos."
t "— Se estiver tudo bem para você."
"Injy olha para todos nós por uns bons dez segundos, fazendo com que até eu olhe para o chão, percebendo o quão idiota isso tudo é."
"Por fim, ele começa a se afastar, fechando um pouco a porta."
inj "— Hum, me desculpa, mas eu não acho que seja uma boa ideia–"
t "— Espera!"
"TJ dá um passo à frente, seu pelo se arrepiando."
"O panda dá um leve pulo, fechando ainda mais a porta até chegar ao ponto em que só consigo ver um de seus olhos."
t "— D–desculpa. É só... talvez eu possa entrar e o resto dos meus amigos pode esperar aqui fora? Vai ser bem rápido. Eu sei exatamente onde procurar."
"O único olho do panda olha de volta para nós."
"TJ se vira e faz um gesto de enxotar com as duas patas." # shooing = enxotar ?
"Há uma pausa, e então vamos um pouco para trás, indo até a calçada." # down the steps onto the sidewalk ?
"Meu rosto queima de novo de vergonha, ao perceber como parecemos um bando de doidos agora."
"Eu olho de volta e vejo o TJ sozinho na entrada, olhando para o panda, com suas patas unidas."
"Novamente, o que parece ser um silêncio muito longo parece se prolongar até que–"
"Injy abre a porta um pouco."
inj "— Quer saber... por que você só não me diz onde tá e eu dou uma olhada?"
t "— Ah! Ah, sim, hum..."
"TJ parece surpreso, como se só agora estivesse considerando essa ideia."
t "— É o quarto à esquerda, no final do corredor."
"TJ aponta para a porta em um ângulo." # at an angle = em um ângulo ?
t "— No armário, no cantinho de trás. Talvez esteja em uma caixa."
"A expressão facial do Injy reflete a minha enquanto franzo a testa."
"Uma caixa em um armário, que ficou lá por mais de uma década?"
inj "— Certo, vou dar uma olhada."
hide Injy with dissolve 
"Injy desaparece atrás da porta e eu ouço a fechadura se encaixando."
"Ficamos ali em silêncio por um tempo até que Carl o quebra."
show Carl Rejected with dis
c "— Cara, ele tá ligando pra polícia."
t "— Não ele não tá."
c "— A gente parece um bando de doido! A gente deveria ir embora."
t "— Não até ele voltar."
c "— Acho que vou vomitar."
ju "— Acho que tecnicamente não tem problema a menos que ele nos mande ir embora."
j "— Ele disse que vai procurar. Não faz mal nenhum só esperar pela resposta dele."
"Vejo o Carl batendo os cascos na calçada, olhando em volta nervoso."
"Me pergunto se ele usou muita maconha, ou algo assim."
m "— Por que você acha que tá no armário?"
t "— Ele usava uma caixa de sapatos ali como um local para suas caças ao tesouro antes. Você lembra."
"Eu vagamente lembro, agora que ele mencionou, mas estou surpreso que o TJ lembra."
"Ele era ainda mais novo."
show Injy at farleft with dissolve
"Então a porta abre e o Injy aparece."
"Sua expressão facial está completamente diferente agora."
"É uma de espanto, e incrédula, mas é o que está em suas patas que chama a minha atenção."
play music "loneliness.ogg" fadein 5.0
show Carl Surprised with dis
show Jenna Surprisedhips with dis
"É uma caixa de sapatos de cor verde-azulado, velha, desgastada e rasgada nos cantos." # torn = rasgada ?
"Fico boquiaberto."
"Injy fica parado ali por um momento, segurando a caixa."
inj "— É... isso? Não é meu, e tem um pedaço de papel dentro."
"As patas do TJ tremem enquanto ele estende as mãos para pegar a caixa, levantando a tampa para olhar dentro."
inj "— Tava no lugar que você falou. Eu nunca vi isso antes."
"Sinto meu estômago se revirar, mais espantado do que qualquer coisa por ele ter encontrado algo."
m "— Você não usa aquele armário?"
"É uma pergunta um tanto estranha, mas eu quero saber como caralho ele talvez não percebeu isso."
"Injy discorda com a cabeça."
inj "— Não, não uso. É basicamente um depósito agora. Eu acho que abri ele algumas vezes pra colocar algumas caixas na prateleira, mas eu realmente não me lembro..."
m "— Você não olhou dentro quando você se mudou?"
"Injy olha para mim, assim como o TJ, por cima do ombro."
"Acho que agora sou eu que estou parecendo a pessoa doida."
inj "— Bem, eu realmente não consigo me lembrar. Foi há alguns anos atrás."
inj "— Minha família me ajudou na mudança, então talvez eles pensaram que era meu quando viram?"
"Eu quero perguntar mais, mas mordo o lábio, não querendo parecer tão frustrado e desconfiado quanto estou."
inj "— É sem dúvida algo que eu poderia não ter percebido. Eu encontrei algumas coisas da última família no vão entre a fundação e o piso."
j "— Quem morava aqui antes de você, se não for incômodo perguntar?"
"Injy se encosta na porta, seus braços cruzados, parecendo muito mais relaxado agora."
inj "— Era a família que vocês estão falando, eu acho? Os Bronsons?"
t "— Sim."
"TJ ainda está olhando para a caixa, sem ter tirado o bilhete."
inj "— Aham, a mulher que morava aqui se mudou logo depois do que aconteceu, mas depois a irmã dela se mudou pra cá."
inj "— Ela me contou sobre o que aconteceu quando eu comprei o lugar."
"Injy olha para a caixa que o TJ ainda está segurando."
inj "— Você sabe o que ele deixou pra vocês? Como você sabia que deveria encontrar isso?" # How did you know to find it ?
t "— É uma... uma antiga gincana que encontramos. Estava escrito para virmos aqui."
inj "— Tipo, algo que ele deixou pra trás?"
t "— É."
inj "— Nossa... bem eu sinto muito pelo que aconteceu com seu amigo. Vocês deviam ser crianças na época?"
"Ninguém diz nada, então eu concordo com a cabeça para ele."
inj "— Me desculpa... também por ter suspeitado tanto quando vocês apareceram. Achei que eu tinha flagrado alguém tentando invadir aqui uns dias atrás."
inj "— Todo cuidado é pouco."
show Julian with dis
ju "— Não se preocupa, é totalmente compreensível."
"Injy concorda com a cabeça, e então se vira ao TJ." # then shifts around ?
inj "— Eu não quero me intrometer mas... o que tá escrito? Eu não li já que não quero me meter nem nada."
t "— Hum."
"TJ levanta a tampa novamente, e então enfia a mão para retirar o pedaço de papel."
"É idêntico aos outros que vimos."
"Injy pega a caixa do lince para que ele possa usar as duas patas para desdobrar o bilhete."
stop music fadeout 5.0
"Então ele começa a ler."
hide Injy
hide Jenna
hide TJ
hide Julian
hide Carl
with dissolve
"\"Espero que todos estejam se divertindo dessa vez,\""
"\"Logo vocês vão saber o que o Chase fez,\""
"\"Descubram, é mamão com açúcar,\""
"\"Se não conseguirem, perto do desenho do Carl no lago é só buscar.\""
"Fica silencioso por um tempo, o único som é o vento suavemente passando pelas árvores."
"Então ouço um som de engasgo e olho para trás bem a tempo de ver o Carl vomitando em alguns arbustos."
stop background fadeout 3.0

scene bg motelfull with fade
"TJ está estranhamente calmo enquanto nos sentamos no quarto do hotel."
"Já se passou cerca de meia hora desde que encontramos o último bilhete."
"Depois que o Carl vomitou todo o almoço nos arbustos, o Julian o levou de volta para casa e tivemos que interromper a gincana."
"O TJ quer que todos nós estejamos lá durante isso."
"O Julian ainda está conosco e eu continuo me perguntando quando caralho ele vai ir embora."
"Ele acabou de entrar no nosso grupinho hoje e o TJ fica agindo como se ele precisasse fazer parte disso por algum motivo."
"Ele mal conhecia o Sydney."
"Mas isso não importa realmente."
"Tudo isso é tão ridículo."
"É tão óbvio que o Sydney não teve nada a ver com essa \"gincana\"."
"Alguém tá colocando a porra desses bilhetes, e essa pessoa tem algo contra mim."
"Me sento com as costas apoiadas na cabeceira da cama, olhando para minhas pernas enquanto o TJ tenta defender tudo isso."
play music "quiet.ogg" fadein 3.0
show TJ Neutral at center with dissolve
t "— Se isso realmente tá te incomodando Chase então você não precisa vir..."
"Meu pelo se arrepia de irritação um pouco."
m "— Cê tá insistindo pra que todo mundo vá, por que não eu?"
"Me forço a não desviar o olhar para o Julian."
t "— Eu quero que você venha sim, mas você tá tão irritado... eu nunca te vi desse jeito."
show Jenna at left with dissolve
j "— Ah eu já, todos nós já. O Chase só tá agindo como o mesmo de antes agora."
"Jenna está sentada no canto com seu notebook como sempre, sorrindo."
"Me deixa puto pra cacete."
m "— Escuta, quem quer que seja que tá escrevendo isso tem algo contra mim. Olha o que o último disse!"
t "— O Sydney escreveu e ele meio que sempre te provocava. É a cara dele."
"Fico calado, desviando o olhar com raiva."
j "— O que você acha que as pistas tão insinuando sobre você, Chase?"
"Penso por um momento, mas é difícil com toda a raiva que continua ameaçando vir à tona."
m "— E–Eu não sei. Eu só não gosto do tom disso e honestamente..."
"Tento pensar na forma correta de expressar o que vou dizer."
m "— Se você me respeitasse você entenderia e pararia com essa caça idiota."
"Fica silêncio por um momento, então o Julian se levanta."
show Julian Confused at right behind TJ with dissolve
ju "— Ei, eu já vou indo."
ju "— Me avisem o que vocês decidirem fazer amanhã. Eu tenho o dia inteiro de folga."
show TJ with dis
t "— Ah! Ok, mano. Muito obrigado por ter vindo com a gente!"
"TJ dá ao cervo um abraço parceiro e eu tento evitar minha irritação." # side hug = abraço parceiro?
hide Julian with dissolve
show TJ Neutral with dis
"Quando o Julian sai pela porta, o TJ senta no pé da cama, olhando para mim."
t "— Eu completamente te respeito Chase, mas eu realmente acho que tudo isso é do Sydney. Ele só tá te provocando."
"Não digo nada, escolhendo olhar para a parede, me sentindo mais incomodado com as minhas próprias emoções do que qualquer outra coisa."
"Eu não me sinto como eu mesmo nem um pouco."
j "— Eu sei que te perguntei hoje de manhã, mas se você acha que isso é obra de outra pessoa, quem poderia ser?"
"Jenna cruza os braços, olhando para mim séria."
"Fico sentado em silêncio por um momento, refletindo se devo ou não contar a eles."
"Eu decido que preciso, já que nenhum dos outros parece estar percebendo."
m "— Eu acho que é o Flynn."
show Jenna Annoyed with dis
j "— Quê?"
m "— Eu acho que é o Flynn... e o Carl. Eles tão fazendo tudo isso."
j "— Não é possível que você tá falando sério."
m "— E quem mais seria!? Foi o Carl quem encontrou o primeiro bilhete. Eu acho que o Flynn deu pra ele."
"A expressão nos rostos da Jenna e do TJ me faz desviar o olhar novamente."
"Eu tô enlouquecendo?"
t "— Chase, isso é..."
m "— Maluquice, eu sei. Mas você viu como o Carl tava agindo hoje, o quão nervoso ele tava. Ele até vomitou!"
j "— O Carl faz isso às vezes."
m "— Ugh."
"Deslizo minhas pernas para fora da cama e deixo elas ficarem na lateral, totalmente de frente para a parede agora." # QUÊ????
t "— Eu sei como o Flynn tava lá no rio, mas até ele não faria isso."
"Olho de volta para o TJ com um olhar firme." # glare = firme ?
m "— E aquelas mensagens que ele tá te mandando?"
t "— Quê–"
show TJ Surprised with dis
"A pata do TJ vai direto ao seu bolso, uma expressão de choque em seu rosto."
"Jenna olha entre nós."
j "— Quê?"
m "— O Flynn enviou uma mensagem pro TJ xingando ele. Eu acho que ele tava te mandando mensagens esse tempo todo."
"O TJ está calado, apenas me encarando."
j "— TJ, isso é verdade?"
show TJ Neutral with dis
"TJ olha para o chão por um momento antes de finalmente levantar o olhar, sua voz estranhamente calma."
t "— É, bem, ele tá bravo. É claro que ele estaria. Mas ele não tem nenhum motivo pra tá escrevendo essa gincana. O Flynn nunca faria isso."
m "— Você tem certeza disso?"
"TJ me olha firme de volta, e agora eu percebo que deixei ele irritado." # glare = firme ?
t "— Sim."
j "— Por que ele faria isso em primeiro lugar?"
"Eu não preciso pensar muito nessa pergunta."
m "— Pra machucar o TJ, pra arruinar a nossa amizade inventando mentiras sobre mim, pra ser um completo cuzão – você escolhe."
t "— Isso é totalmente ridículo."
"Não digo nada, escolhendo olhar para a parede."
"Jenna olha entre nós novamente e discorda com a cabeça."
j "— Beleza, já deu. Nenhum dos dois tão agindo como vocês mesmos então eu acho que é melhor dormirmos. Beleza?"
stop music fadeout 5.0
m "— ... Tanto faz."
"Deslizo para a cama do meu lado, ainda olhando para a parede, ouvindo enquanto o TJ se levanta e vai para o banheiro."
"Jenna continua a digitar em seu computador."
"Fico deitado em silêncio, decidindo que terei que fazer algo para dar um basta nisso."

scene bg black with slow_dissolve
"Sair furtivamente do quarto do hotel é provavelmente a parte mais difícil."
"Eu sei que se eles me pegarem em qualquer momento, é o fim."
"Por volta das 3 da manhã, eu saio da cama, ouvindo os roncos do TJ e observando a forma imóvel de Jenna enrolada na cama à minha frente."
"Silenciosamente, procuro na minha bolsa minhas chaves, então saio pela porta à noite." # bag = bolsa ?
scene bg parkinglotnight with dissolve
play background "crickets.ogg" fadein 5.0
"Ranjo os dentes enquanto meu carro liga, imaginando o TJ ou a Jenna puxando as cortinas e me vendo sentado no carro."
"Eu tenho desculpas; tô doente, tive que dirigir até o pronto-socorro, ou até que não conseguia dormir e queria um lanche em algum lugar."
"Todos são suspeitas, mas devem ser suficientes para me cobrir se as coisas forem de arrasta."
stop background fadeout 3.0
scene bg highwaynight with dissolve
play music "reckoning.ogg" fadein 1.0
"Dirijo pela estrada silenciosa, o ambiente em minha volta quase apagado já que a lua se pôs."
"Levo um momento até encontrar a via que me levará à costa."
scene bg lakeemmanight with dissolve
"Quando encontro, vejo uma luz laranja solitária ofuscando no meio do estacionamento."
"Eu estaciono longe dela na beira do estacionamento. Tá escuro aqui."
"Fico sentado no carro por um tempo, me perguntando que eu tô fazendo, me perguntando que porra eu vou fazer."
"Mas algo me move, um sentimento de que se eu não fazer isso, então o resto da minha vida será arruinado."
"Eu não posso deixar isso acontecer."
"Eu abro a porta e saio rapidamente."
"Pego meu celular e ligo a luz, encontrando a pequena trilha de terra que leva à escuridão profunda."
"O ar está fresco e consigo sentir o cheiro do lago."
play background "lakesounds.ogg" fadein 3.0
"Rapidamente também consigo ouvi-lo, os suaves, desolados sons das ondas passando contra o fino litoral."
"É calmo, mas ao mesmo tempo me deixa aterrorizado, e por um momento eu sinto que o lago é um ser vivo gigantesco."
"Ele me consome com sua presença; algo gigante, onisciente."
"Sabe que estou aqui."
"Eu me arrepio e me forço a continuar."
"Encontro o litoral e a areia seca se move sob meus pés enquanto viro à direita e sigo a costa." # take a right = viro à direita
"Tento ignorar os sons do lago, a sensação de que está me observando, me seduzindo para ele."
stop background fadeout 5.0
"Finalmente, me deparo com a rocha que estou procurando."
"Aquela na qual o Carl costumava esculpir seus desenhos."
"É claro que seria algo que o Carl usou."
"Aquele gordo arrombado do caralho."
"Me ajoelho ao lado dela, movendo a luz do meu celular até encontrar os desenhos."
"Olho para o Super Lobo esculpido na rocha, olhando fixamente... então vejo um reflexo acima dele."
"Movo a luz do celular para cima para ver o que é–"
"Eu me espanto e não consigo evitar que um grito áspero escape de minha garganta." # gasp = espanto ?
"Uma tarântula está ali, me encarando de volta, seu conjunto de olhos brilhando em meio à escuridão."
"Eu tropeço na areia e caio, sentando com força e fazendo com que meus dentes se batam."
"Eu me levanto rapidamente."
"Olho em volta por uma pedra e rapidamente encontro uma."
"Quando me viro de volta e levanto a luz, a aranha sumiu."
"Olho em volta por um tempo, caso ela só tenha se movido em volta, talvez no chão mais perto de mim."
"Porém não vejo nada, e jogo a pedra no lago, xingando essa coisa horrível."
"Então me ajoelho e olho para o local entre o solo rochoso e a rocha."
"Demora um pouco e tenho que me aproximar bastante, olhando mais fundo na fenda e então–"
"Há um reflexo do que parece ser metal."
"Eu começo a cavar, primeiro com minhas próprias mãos, e então com a ajuda de uma pedra plana que estava por perto."
"Estou suando e ofegando quando consigo puxar o objeto."
"Parece uma lancheira antiga."
"Eu a ilumino e mal consigo enxergar o que parece ser um dragão desenhado."
"Eu a abro e tiro o bilhete."
"Eu leio."
"Em um ataque de raiva eu rasgo a coisa idiota no meio, jogando-o no chão."
m "— Seu fodido!"
"Eu murmuro entre os dentes, então pego o pedaço de papel que tirei de um dos cadernos da Jenna, junto com uma caneta." # hiss = murmuro ?
"Escrevo por um momento, usando a lancheira antiga como uma superfície plana."
"Quando termino, coloco-o na caixa, então enfio a caixa na fenda, cobrindo-a com a terra solta que movi." # loose = solta ?
"Eu coloco tudo, então me levanto."
"Pensando duas vezes, pego o bilhete rasgado e o coloco no bolso."
"Então caminho de volta para a costa e pela trilha, ignorando o que parece ser o brilho dos olhos das tarântulas em toda minha volta... talvez seja apenas as estrelas."
scene bg black with dissolve
stop music fadeout 15.0
"Não lembro muito da viagem de volta, nem de estacionar no hotel."
"Quando me dei conta, estava em pé ao lado da cama, olhando para o TJ, observando-o dormir."
window hide
scene bg black with slow_dissolve

jump tjsaturday