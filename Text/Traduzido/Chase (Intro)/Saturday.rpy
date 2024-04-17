﻿label saturday:



############################################
stop music fadeout 3.0
scene bg black
with slow_dissolve
play loop "nhysteria.ogg" fadein 20.0
$ renpy.pause(2.0, hard=False)
window show
unk "{cps=22}{font=ui/belligerent.ttf}Eu sabia que você voltaria..."
unk "{cps=15}{font=ui/belligerent.ttf}Vocês todos voltam eventualmente..."
unk "{cps=15}{font=ui/belligerent.ttf}Por que vocês tentam fugir em primeiro lugar...?"
unk "{cps=15}{font=ui/belligerent.ttf}Isso não importa agora..."
scene bg saturday0
with slow_dis
unk "{cps=15}{font=ui/belligerent.ttf}Mesmo estando aqui você vai tentar fugir de novo..."
unk "{cps=15}{font=ui/belligerent.ttf}Apenas pare..."
unk "{cps=15}{font=ui/belligerent.ttf}Porque assim como esta cidade..."
unk "{cps=15}{font=ui/belligerent.ttf}Você só está andando em círculos..."
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
m "— Sim mãe, eu trouxe."  
m "— Não, não eu peguei tudo."
m "— Não, o TJ tá com a gente, a gente foi buscar ele ontem..."
m "— Não eu... Eu te {i}liguei{/i} ontem sim, mas você não atendeu."
m "— Tá. Ok, eu vou tentar ligar de novo na próxima vez."
m "— Então eu... É claro que elas estão limpas!"
m "— Escuta, eu tô dirigindo agora, então-"
m "— É, então eu não deveria estar no celular, né? Eu vou desligar."
m "— Ok, também te amo... tchau."
"Suspiro e finalmente desligo a chamada, deixando o celular no meu colo."
"TJ, ao meu lado no banco do passageiro, se espreguiça para trás e coça a orelha."
t "— Ai, que amorzinha. Já faz um tempo que não vejo sua mãe. Como ela tá?"
"Levanto os ombros."
m "— Tá bem, eu acho. Ela não me diria se não estivesse, de qualquer forma."
"TJ encosta o pé no painel antes de bocejar."
t "— Nossa, parece que estamos dirigindo há diiias."
"Normalmente o TJ não era de reclamar, mas a longa viagem estava obviamente começando a incomodá-lo."
"Honestamente, isso já estava começando a incomodar todos nós."
"Olho para ele."
m "— Tamo quase chegando. Por que você não ouve uma música, ou algo assim?"
t "— Meu celular já descarregou há tipo duas horas. Eu não sabia que demoraria oito horas pra chegar lá."
"Suspiro."
"Mesmo que esse comentário com tom sarcástico tenha sido proposital ou não, ainda me sinto um pouco envergonhado."  
"Tenho que admitir, eu fiz com que nos perdessemos por algumas horas. A Rota 93 é difícil de encontrar, mesmo com o GPS."
"Não é de se admirar que Echo esteja nesse estado."
j "— Você deveria ter trazido um livro, sabe, eles não ficam sem bateria."
"Olho pelo retrovisor e vejo Jenna segurando um livro pesado chamado \"Cognição\"." # Nome do livro traduzido???
"TJ suspira."
t "— Todos meus livros estão no meu celular..."
m "— Por que você não escuta o rádio?"
"TJ começa a tentar achar uma frequência." # Não sei se esse é o termo certo
j "— Nem tenta, só tem música de velho por aqui. Mas eu tenho algumas músicas no meu celular."
j "— Cê tem um cabo P2, Chase?"
m "— Nesse trambolho? Não, mas como eu disse, tamo quase chegando."
"Ter apenas nós três aqui é meio vergonhoso... desequilibradamente."  
"Me pergunto se quando nosso grupinho estiver junto de novo, aquela velha química voltará."
"Só de pensar em ver o Carl, o Flynn e o Leo de novo faz meu coração bater mais forte."
play sound "gps.wav"
"GPS" "— Pegue a saída 127 para Rua Flint."
"Retomo o meu foco para o presente e piso no freio enquanto viro para a ladeira da saída."

scene bg flint with dissolve

t "— Nossa!"
m "— Desculpa! Desculpa..."
# Swerve sound and image change
t "— Chase! Meu deus, presta atenção."
"TJ dá uma risadinha para aliviar o castigo, mas meu rosto fica avermelhado mesmo assim."
m "— Ei, eu e a Jenna saímos três horas do trajeto pra te buscar na CCU, cê poderia ter pego o ônibus." # CCU?
t "— Não, não, eu fico agradecido. É só que eu prefiro que esse não seja o lugar onde eu morra, haha."
"Continuamos pela rua Flint por cerca de quinze minutos em silêncio enquanto eu evito o número cada vez maior de buracos na estrada." # Eu acho que existe um outro termo melhor do que "buracos" mas eu não me lembro agora
"Acho que estamos todos um pouco nervosos agora que estamos nos aproximando do nosso destino."
"Como era de se esperar, não há nenhum outro carro à vista."
j "— Vocês estão empolgados?"
"Olho novamente pelo retrovisor e vejo que Jenna abaixou seu livro, olhando pela janela."
"Na verdade, ainda não pensei muito sobre como me sinto em relação a tudo isso."
menu:
    "— Aham":
            $ Trip_Mood = "good"
            m "— Vai ser ótimo ver todo mundo de novo. Já faz muito tempo que não nos vemos."
    "— Não tanto assim.":
            $ Trip_Mood = "bad"
            m "— Meh, eu acho que vamos continuar de onde paramos."
    "— Eu tô nervoso.":
            $ Trip_Mood = "nervous"
            m "— Sei lá, já faz um tempo que não estamos todos juntos. Você acha que as coisas serão as mesmas?"
j "— Eu tava falando de Echo. Você tá empolgado em voltar?"
m "— Ah."
"Eu realmente não sabia como responder isso."
"Empolgado é a palavra correta?"
"Com certeza é muito estressante."
t "— Desde que possamos ir em uma trilha."
t "— Eu não quero ficar sentado no hotel o dia todo."
j "— Bem, é melhor do que ter uma insolação no deserto. Cê realmente vai fazer uma trilha?"
t "— Ah, tipo, vai ser divertido! Pelo menos eu sei que o Chase vai vir comigo."
"TJ sorri para mim, levantando as sobrancelhas."
"É muito difícil dizer não a um rosto tão entusiasmado... pelo menos por agora."
m "— Sim, sim, claro."
j "— Enfim, parece que você só tá pensando nos garotos, Chase."
j "— ... o Leo, talvez?"
play sound "gps.wav"
"GPS" "— Vire à direita para Rua do Lago Emma."
"Eu ignoro a Jenna, fingindo estar distraído enquanto ajusto o GPS."
"Mais alguns minutos de silêncio se passaram até que a Jenna voltou a falar."
j "— Entãão, essa reportagem que você tá fazendo, do que exatamente é ela?"
"Desvio um pouco para evitar outro buraco."
m "— Um dossiê de notícias."
m "— Se você se lembra teve uma coisa absurda que aconteceu aqui no início de 1900."
m "— Eu li um pouco sobre o assunto e é fudido pra caralho."
t "— Ei, Chase, olha a boca."
m "— Então eu pensei em investigar um pouco mais."
m "— Mas olha, honestamente, eu só preciso fazer algo que pareça bom o suficiente pra ser aprovado."
j "— Bem, isso parece bem divertido. Você vai ter tempo suficiente pra sair? Sei que o Leo fez alguns planos."
"Tudo isso foi ideia do Leo, na verdade." 
"Quando eu lhe disse que iria para Echo nas férias de primavera, ele sugeriu que usássemos isso como desculpa para nos reunirmos."
"Ele disse que não é mais a mesma coisa desde que nós três fomos embora."  
m "— Sim, eu vou ter. Só preciso de algumas filmagens e fotos dos locais antigos e assustadores."
m "— Não deve demorar muito."
"Percebo um reflexo azul e vejo o lago à nossa direita."
"A conversa para um pouco e logo estamos todos fechados em nossos próprios pensamentos."
"Finalmente, fazemos uma curva e começo a ter uma visão da cidade."
"As placas altas e enferrujadas do posto de gasolina e do hotel se destacam sobre o restante da antiga comunidade."
"A Rua do Lago Emma entra à direita da Rua Principal, onde fica o hotel."
"Não demora muito e estamos entrando no estacionamento."

scene bg parkinglotday with dissolve

"Há apenas alguns outros carros no estacionamento."
stop background fadeout 3.0
play sound "engineoff.mp3"
"Eu estaciono na vaga mais próxima da porta e desligo a ignição, aliviado por ter acabado de dirigir."
"Eu relaxo por um momento, esfregando os olhos."
m "— Aaagh. Eu espero que você esteja agradecido, TJ. Nunca mais quero dirigir por tanto tempo assim."
t "— Obrigadoooo, Chase!"
play sound "cardoor.mp3"
"TJ sai do carro, claramente feliz por estar fora."
play music "neutral.ogg"
show TJ Sheepish with dissolve
t "— Aaauuuuugghhh!"
"TJ coloca as patas para trás e se estica dos pés às orelhas, e eu ouço alguns estalos."
t "— Nossa, é muito bom estar fora."
"Eu sorrio enquanto sigo ele e também me espreguiço, embora de forma menos extravagante. É bom ver o TJ voltando ao seu eu feliz."
show Jenna Neutralhips behind TJ at right
with easeinright
j "— Certo, fiz as reservas, então vou fazer o check-in." # Check-in é usado em português comummente?
j "— Vocês dois querem trazer nossas coisas?"
t "— Claro!"
hide Jenna
hide TJ 
with dissolve
"Eu e o TJ vamos até o porta-malas do carro, pegando nossas malas e equipamento de câmera, enquanto a Jenna vai para dentro."

scene bg motelfull with fade

"Fiquei felizmente surpreso."
"Embora seja um pouco úmido, o quarto é espaçoso e em geral limpo, muito mais do que eu esperava de uma cidade como Echo."
"Embora eu tenha vivido na cidade durante a maior parte de minha vida, eu nunca estive no hotel."
show TJ at left with dissolve
t "— Ei, isso é ótimo! E duas camas de casal?"
show Jenna at right with dissolve
j "— É, pensei em pegar um dos quartos mais agradáveis, já que tudo aqui é meio péssimo."
"TJ coloca suas malas na cama."
t "— Então acho que essa será a cama minha e do Chase."
t "— A Jenna pode ficar com a sua, obviamente."
j "— Isso é... gentil de sua parte, TJ. De qualquer forma, toma aqui seus cartões."
"Ela nos entrega nossos cartões de acesso, que eu coloco no bolso de trás."
t "— Então, quando a gente vai comer? Eu tô morrendo de fome!"
"Meu estômago ronca. Não comemos desde o café da manhã e já tá no fim da tarde."
"Pego meu celular, verificando minhas mensagens com o Leo."
m "— O Leo disse que vai comprar sanduíches pra nós da lanchonete."
t "— Você falou-"
m "— Sim, eu falei pra ele pedir pra substituírem pão por alface no seu, TJ."
t "— Boa!"
j "— Beleza, bem, já mandei mensagem pra todo mundo dizendo que estamos aqui. Vamos pelo menos arrumar as malas."
j "— Vai ficar começar a ficar cheio e eu não quero todas as nossas coisas no meio."
hide Jenna
hide TJ
with dissolve
scene bg motelbeds
with fade
"Meia hora depois guardamos todas as nossas coisas nas gavetas do hotel."
"Agora, estou sentado na cama, mexendo no meu equipamento de filmagem enquanto o TJ assiste TV e a Jenna organiza seu trabalho escolar."
t "— Você sabe que tá de férias, né?"
t "— E você já não tá na sua pós? Você deveria relaxar."
j "— É exatamente por isso que preciso estar em dia."
play sound "doorknock.mp3"
"Alguém bate na porta e, como estou mais perto, me levanto para ver quem é."
m "— Deixa que eu vou!"
scene bg moteldoor with dissolve
"Eu olho pelo olho mágico entusiasmado e vejo um boné com um par de chifres muito familiares atravessando ele."
"Sorrio ao destrancar a porta e abri-la."
show Carl at center with dissolve
m "— Carl!"
c "— Chase!"
"Eu bato as patas com ele e o puxo para um abraço." # Bato? = é toque de mão (Linha 343)
"... e imediatamente sinto o cheiro forte de maconha."
"Apesar disso, seu abraço é quente e aconchegante, e sua barriga se aperta contra o meu corpo como um travesseiro através de seu moletom."
"No entanto, há uma robustez subjacente, e sinto seus bíceps se expandirem ao redor dos meus ombros."
"Ele tá malhando?"
"Coloco minhas patas em seus ombros e o afasto, observando-o."
"Ele mudou um pouco desde a última vez que o vi. Ele está definitivamente mais parrudo, e o pelo em seu rosto está um pouco mais desgrenhado."
"Seus olhos estão um pouco vermelhos e sua expressão é um pouco apática, como se ele estivesse sonhando acordado com algum lugar longe daqui."
m "— Ainda usando drogas, é?"
c "— Cê sabe."
"Seu caráter brincalhão diminui um pouco quando ele me dá um sorriso genuíno."
c "— É bom te ver de novo."
"Sinto um calor dentro de mim e sorrio de volta."
m "— Você também."
j "— É o Carl que tá aí?"
hide Carl with dissolve
"Carl e eu voltamos para dentro, com o carneiro permanecendo relaxado enquanto andamos."
scene bg motelfull
show Carl at right with dissolve
show Jenna Smiling at center with easeinleft
c "— Opa Jenna."
j "— Carl! Como você tá?"
c "— Nada mal, apenas vivendo a vida, como se fosse..."
"Parece que ele tá começando a cantar a letra de uma música, mas ele para quando todos nós começamos a olhar para ele com entusiasmo."
"Ele só sorri de volta."
m "— Ahn?"
show TJ behind Jenna at left
with easeinleft
c "— Ei, é o TJ?"
t "— Oi!"
"Embora esteja sorrindo alegremente, TJ está claramente fechando seu nariz." # Fechando?
t "— Continua com seus velhos hábitos, né?"
"Carl levanta os ombros."
"Eu tô começando a me lembrar que isso é algo que ele faz muito. É a sua resposta para quase tudo."
"Fica quieto por um momento, e então eu bato as patas." # Bato?
m "— Então, o que você tem feito, Carl?"
m "— Você não fica online com tanta frequência."
"Carl levanta os ombros."
c "— Ah, cê sabe... só curtindo por aí."
show Jenna Smilinghips with dis
j "— Deve ser meio chato, considerando que aqui é Echo."
c "— Não sair de casa ajuda, haha."
t "— Você conseguiu arranjar um emprego? Sei que fecharam aquele Mercado da Esquina onde você trabalhava."
show Carl Neutral with dis
c "— Ééé, tem sido meio difícil já que quase tudo tá fechando por aqui."
c "— E além disso eu ainda não tenho um carro que possa me levar à Payton."
t "— Ah, é verdade."
t "— Você bateu aquele que seus pais te deram."
show Carl Depressed with dis
"TJ está sorrindo com simpatia, mas Carl se encolhe ainda mais, parecendo melancólico."
show Carl Annoyed with dis
c "— Cara, não mata a minha vibe."
j "— E quanto à faculdade, tá pensando em voltar?"
show Carl Rejected with dis
c "— N-não muito, talvez..."
"Carl está começando a perder aquele olhar distante ao baixar os olhos."
show Jenna Smiling with dis
j "— Você deveria! Você foi por quanto tempo, um semestre?"
j "— Esse tempo não é suficiente pra saber se você realmente não deveria fazer uma faculdade."
j "— As aulas começam a ficar mais fáceis de lidar quando você se acostuma."
c "— É, bem, não era exatamente o trabalho escolar que era o problema."
t "— Você podeeriiia tentar fumar menos maconha, isso pode ajudar."
show Carl Surprised with dis
c "— Q-quê…?"
show Carl Surprised at farright with easeinright
c "— Isso é-era um plano pra me botar em reabilitação, ou algo assim?"
"Carl olha para mim, como se estivesse pedindo ajuda."
m "— Ei, não olha pra mim. Eu tive que lidar com eles pelas últimas dez horas."
c "— É, acho que me esqueci de como eles podem ser meio chatinhos."
t "— É porque a gente se preocupa com você, Carl!"
j "— Bem, tenho certeza de que o Chase tem sentido sua falta desde que você saiu da faculdade."
"Carl e eu estávamos na mesma turma durante toda a escola. Consequentemente, entramos juntos na faculdade."
"Chegamos até a morar juntos durante esse um semestre, o que foi muito divertido. É claro que eu sentia falta dele."
"No entanto, Carl parece bastante impaciente para sair do assunto."
show Carl with dis
c "— Por falar em faculdade, você não foi aceita em Weston, Jenna?"
j "— Aham! Eu vou fazer psicologia experimental. Começo no outono."
c "— Isso é bem legal, parabéns."
"Carl se vira para mim."
c "— E você faz... jornalismo, certo?"
"Ele olha o equipamento, com uma expressão confusa."
c "— O que é tudo isso?"
#pic of cam equipment on bed? # Ficou com deus essa foto
m "— Ah! Sim, um dos motivos pelo qual estou aqui."
m "— Estou fazendo uma reportagem sobre Echo."
c "— Parece que vai ser o melhor filme do ano, Chase." # ? "fell-good"
m "— É isso que você recebe da melhor cidade do século, Carl." # ? "fell-good"
c "— Hehe, é."
"Carl coça seu focinho antes de se virar para o TJ."
c "— E você tá fazendo... o que mesmo?"
c "— Esportes... algo... Olimpíadas bíblicas?"
t "— Treinamento atlético, mas sim, é uma instituição Cristã."
"Carl dá um joinha."
c "— Daora. Então, vamos comer? Tô com uma fome do diabo."
t "— Do diabo é meio extremo, Carl."
t "— Nem mesmo VOCÊ poderia estar com tanta fome assim, hehe."
c "— Mhm, é. Cadê o Leo, ele tá trazendo os sanduíches, certo?"
j "— Ele acabou de me mandar uma mensagem dizendo que tá aqui. Ele tava indo buscar o Flynn."
t "— Então todos nós estaremos aqui! Como nos velhos tempos."
"TJ quase parece aquele lince pequenino de novo, com as orelhas se contorcendo de empolgação." # ? Contorcendo
play sound "doorknock.mp3"
stop music fadeout 2.0
c "— Aah, eles chegaram."
hide Carl
with moveoutright
scene bg motelbeds
with dissolve
"Eu agarro a coberta e observo enquanto Carl dá a volta para abrir a porta." # "moves around the corner"?
"Ouço ela abrir, seguido por uma voz grave e alta do Flynn."
play music "comeover.ogg" fadein 3.0
f "— Ei, por que VOCÊ veio abrir a porta, gordola?"
c "— Pra pegar meus sanduíches, cu de apito. Tô faminto igual um monstro."
c "— Eh... cadê eles?"
f "— O Leo tá com eles... e aí tá ele."
l "— Ei, tá todo mundo aí?"
"Eu sinto meu coração bater mais forte e minha cauda bate na cama quando ouço o barítono agudo do Leo."
"Há um pequeno tumulto antes deles começarem a ir para os cantos, colocando-me frente a frente com o resto dos meus amigos de infância."
show Flynn at center
with dissolve
"Flynn vem primeiro, entrando casualmente, com sua postura solta e relaxada, descontraídamente."
"Diferente do Carl, porém, sua postura relaxada faz com que ele pareça estar pouco se fudendo, ao invés de apenas tentar parecer menor."
"Ele não era um cara tímido, como fica evidente por sua camisa aberta."
f "— E quem tu tá chamando de cu de apito?"
"Flynn dá uma batidinha na cabeça do Carl, que faz um barulho alto, mas Carl continua rindo."
f "— Opa Jenna, TJ, Chase."
"Ele acena para cada um de nós, esfregando suas mãos." # "rubbing his knuckles" ?
hide Flynn
with moveoutleft
show Leo at center
with moveinright
"Imediatamente atrás dele, com os braços em volta de duas grandes sacolas de papel marrom, está Leo."
"Ele sorri por cima das sacolas, examinando a sala com seus olhos junto com suas orelhas altas e retangulares."
"Ele observa a Jenna, depois o TJ, antes de me encontrar."
"Seu rosto não consegue segurar o grande sorriso enquanto ele caminha até a cama em que estou sentado, deixando as duas sacolas."
"Enquanto ele vem parar na minha frente eu estendo minha pata para dar um toque de mão, como fiz com o Carl." # "toque de mão" ?
"Ao invés disso, ele a segura me puxando para um abraço de urso apertado, quase me deixando sem ar."
l "— Chase!"
l "— Cara, que saudade..."
"Assim como o Carl, parece que o Leo ficou maior e mais forte. Ele me levantou sem sequer tentar."
"A tensão que estava sentindo no peito derreteu como um cubo de gelo em uma calçada de Echo."
"Está tudo bem."
"Toda aquela preocupação sobre como ele reagiria foi em vão."
"... Mas o abraço TÁ durando muito tempo já."
"Eu tô sentindo todo mundo olhando pra gente."
j "— E sem mais nem menos ele esquece que existimos."
"Leo finalmente me solta e me dá um tapinha no ombro antes de se virar para cumprimentar a Jenna e o TJ."
hide Leo with dissolve
"Eu me sento trêmulo, me sentindo muito melhor agora que as apresentações já foram feitas."
scene bg motelcouch with dissolve
show Flynn Annoyed at left with dissolve
f "— Porra, deixa o Carl em uma sala por cinco segundos e fica com cheiro de uma sauna de gambás."
f "— A essa altura a maconha já deve tá saindo dos seus poros."
"Flynn comicamente tapa as narinas enquanto abre a janela um pouco."
show Carl Neutral at right with dissolve
"Carl revira os olhos, se inclinando ainda mais e enfiando as patas nos bolsos."
c "— Ai cala a boca. Acho que todos aqui concordam que meu cheiro é muito melhor do que a sua troca de pele." # "shedding" ?
c "— Nada como deixar uma grande pilha de pó de lagarto no sofá para a próxima pessoa."
c "— E só pra te avisar, mano, o comentário sobre gambá foi especista."
f "— E o comentário sobre lagarto não foi?"
show Flynn with dis
"Flynn se vira para mim, ventilando o ar de fora com a mão."
f "— O que é pior, Chase: O cheiro do Carl ou a minha... sujeira?"
show Carl with dis
c "— Ha! Sujeira? Acho que não é bem isso!"
c "— Tenta dizer \"flocos brancos que se soltam de mim a cada passo que dou... exceto quando eu coço meu cu, aí é como se fosse a porra de uma nevasca de pele morta"
c "— ...e alguns deles podem cair na sua boca.\""
c "— É assim que você deveria chamar"
f "— Ei, vocês bolas de pelo, também fazem isso... só que é menos perceptível."
f "— De qualquer forma, tá calor aqui!"
c "— Cê não é sangue frio?"
f "— Alguém diminue a porra do termostato!"
show Carl Neutral with dis
show TJ at center
with dissolve
t "— Alguém diminue o seu linguajar, haha!"
"TJ diz isso a ele como se fosse um professor alegre do fundamental dando uma leve bronca a um aluno para ele não xingar."
f "— ..."
t "— ..."
"Eles se encaram por cerca de cinco segundos, a expressão do Flynn como uma pedra, enquanto TJ perde lentamente o sorriso."
show TJ Sheepish with dis
t "— Uhm..."
f "— Bem, o caralhão de Jesus Cristo, podexá que eu vou diminuir ele." # "Jesus butt-fucking Christ" traduzir melhor
t "— Flynn!"
show Flynn Happy
show Carl 
with dis
"O TJ realmente parece bem chateado, mas o Flynn só agarra ele e o puxa pra um mata-leão, o lince muito mais baixo é facilmente pego pelo lagarto."
f "— Ah, cala boca frescurento, eu tô só brincando!"
"TJ luta hesitantemente contra o aperto."
"Acho que o TJ pensava que teria um pouco de respeito, agora que somos todos adultos."
t "— Ei, ai!"
t "— Vo-você ainda falou!"
"Normalmente eu interviria para ajudar, mas já faz um tempo que não vejo o Flynn e o TJ brigando."
"É engraçado demais pra parar."
f "— Olha, sem pegar leve! Tanto pro seu deus todo-podero-AAGH!" # tá certo isso?
"TJ dá uma cotovelada no estômago do Flynn, tirando vantagem do lagarto por um segundo."
t "— Ha! Viu? Deus trabalha de maneiras misteriosa-AI!"
"Flynn estende a mão e agarra um dos tufos das orelhas do TJ e da um puxão, fazendo com que o felino uive."
c "— Falta! Aspectos das espécies!"
"Aspectos das espécies foi algo que inventamos para tornar nossas brigas um pouco mais justas."
"Envolvia qualquer diferença física distinta entre nossas espécies que pudesse representar uma desvantagem como minha cauda, as orelhas de Jenna, ou os tufos de orelha do TJ."
"Carl era especialmente entusiasmado com isso. Por ser um carneiro, seus chifres eram frequentemente usados como vantagem contra ele." # "leverage "?
j "— TJ! Vem pegar seu sanduíche."
"TJ finalmente se livra das garras do Flynn, alisando seu pelo enquanto tenta parecer o mais digno possível."
t "— Bem, vejo que as coisas não mudaram..."
"Com isso, TJ se dirige à mesa para pegar sua comida."
hide TJ with dissolve
"Não consigo deixar de rir."
m "— Hehe, acho que o TJ ganhou essa por um detalhe técnico." # "technicality"?
c "— Será mesmo? Ele também pode ter tido uma falta."
c "— O Flynn tem uma barriga de lagarto macia, haha."
"Flynn suspira, esfregando o estômago."
f "— Ah, nem tenta me falar sobre maciez, cuzão. Parece que você engoliu uma bola de praia."
c "— Falando nisso, comida!"
stop music fadeout 3.0
scene bg motelbeds with fade
"Todos nós passamos as malas para pegar nossa comida."
"Um sanduíche de frango pra Jenna e o TJ, carne assada pra mim e o Leo, e três hambúrgueres vegetarianos grandes que quase ocupam sua própria sacola pro Carl."
play music "neutral.ogg" fadein 3.0
"Flynn, como sempre, não está comendo nada. Acho que é uma coisa de lagartos."
"Mantenho meu assento na cama enquanto desembrulho o papel alumínio do meu sanduíche."
"O cheiro da carne se espalha, me deixando com água na boca e trazendo algumas memórias com isso."
"Todos nós passávamos muitas noites na antiga lanchonete. Eu me lembro da noite em que eu e Carl nos formamos."
"O Leo nos levou direto do Colégio de Payton pra lanchonete, pulando a festa de formatura que duraria a noite toda pra comer sanduíches e tomar milkshakes."
"Dou uma mordida enorme e um pimentão amarelo escorrega pela outra extremidade, caindo de volta no papel alumínio."
l "— Eitaa! Pega leve, cê vai engasgar."
"De repente, quase caio para o lado quando algo pesado se senta ao meu lado na cama."
show Leo at center with dissolve
"Pego rapidamente um guardanapo e o levo ao focinho, limpando a oleosidade."
m "— {i}Ey{/i}, Leo..."
"Leo ri do meu constrangimento e desembrulha seu sanduíche."
l "— Desculpa se o pão tá meio grudento. O {i}Garrobo{/i} ali demorou um pouco pra entrar no carro."
scene bg motelcouch
show Flynn at left
with dissolve
f "— Ei! Trabalhar na prefeitura é um negócio sério."
f "— Eu não tenho uma empresa familiar da qual eu possa simplesmente sair, como você."
show Carl at right with dissolve
c "— Ei, Flynn. Aposto que consigo comer esse hambúrguer inteiro em um minuto."
f "— ..."
f "— Tu tá me zuando porra? É óbvio que você consegue."
c "— Hahahahaha! É... Mas e quanto a DOIS hambúrgueres?"
scene bg motelbeds
show Leo
with dissolve
l "— Não engasga, Carl."
"Eu decido manter a conversa sobre o trabalho do Leo, já que essa é a razão pela qual ele ainda está aqui."
m "— Os negócios ainda tão indo bem?"
l "— Aham! Payton tá crescendo, assim como o número de clientes."
m "— Acho que foi bom seu pai ter mudado pra Echo, né?"
l "— Com certeza. Aqui tá virando uma cidade fantasma."
l "— Provavelmente será em uma ou duas décadas."
m "— De acordo com alguns padrões, já é."
"Dou outra mordida no meu sanduíche, mordendo outro pimentão."
"Eu tinha me esquecido de como a comida da lanchonete é boa."
scene bg moteltable
show Jenna Smilinghips at left
show TJ Rejected at center
with dissolve
"Percebo que o TJ tá sentado ao lado da Jenna na mesa, beliscando infeliz seu frango enrolado em alface."
"Jenna também parece ter percebido enquanto se inclina para ele."
j "— O que foi, TJ?"
t "— É que... deixa, não importa."
j "— Tem certeza?"
t "— É só a maionese, esqueci que eles colocam em tudo aqui, hehe."
"Jenna levanta o pão do seu sanduíche, inspecionando seu conteúdo."
j "— Hmm, a maionese não chegou a entrar no meu frango. Toma-"
t "— Não, não precisa-"
"Jenna pega o sanduíche do TJ e troca seu frango grelhado."
"Ela arranca a camada de alface com maionese do pão de alface dele antes de colocar o frango."
j "— Pronto! Que tal?"
t "— O-obrigado..."
show TJ Sheepish with dis
"Foi então que o TJ subiu o olhar e viu o Leo e eu olhando para ele. Vejo suas orelhas se abaixarem de vergonha."
t "— Que foi!?"
l "— Hehe, nada TJ, nada."
scene bg motelbeds
show Leo at center
with dissolve
m "— Então seus pais ainda tão deixando você morar na casa aqui em Echo?"
l "— Sim, na verdade tentamos vender ela ano passado, mas é claro que ninguém comprou."
l "— Acho que duas pessoas vieram dar uma olhada, mas foram embora quando viram a cidade."
l "— De qualquer forma, meus pais tão morando em Payton, em uma casa duas vezes maior que a antiga."
m "— Bem, deve ser muito legal morar em sua própria casa."
l "— Meus pais não tão sempre vendo tudo o que eu faço, o que é bom, sabe."
"Leo já terminou seu primeiro sanduíche e agora está desembrulhando o segundo."
"Ele realmente parece que comeria muitos."
m "— Quantas pessoas ainda estão aqui, afinal? Na cidade, quero dizer."
"Leo dá outra mordida e eu ouço a crocância dos pimentões em seu focinho. Ele mastiga pensativamente por um momento antes de engolir."
l "— Hmm, não tenho muita certeza. É claro que eu conheço quase todo mundo aqui, mas a maioria não mora mais aqui."
l "— Quase todo mundo transformou sua antiga casa em um tipo de casa de férias."
m "— Sério, por quê?"
"Não consigo imaginar ninguém vindo aqui para passar férias..."
"... a menos que seus hobbies sejam metanfetamina ou morrer de insolação."
l "— Bem, todos eles têm suas casas antigas aqui, e é barato construir."
l "— E a cidade tá tentando transformar aquele antigo lago em um local pra turismo."
m "— O Lago Emma?"
l "— É. Eles tão instalando docas e tals."
m "— Uhm..."
"O Lago Emma é a antiga represa que fica a poucos minutos da cidade. Quando éramos crianças, brincávamos lá o tempo todo."
"Geralmente era um lugar feio: peixes mortos nas margens, um cheiro horrível e mosquitos por toda parte."
"Contudo, pode ter mudado desde então. Eu não vou lá há... doze anos agora. Nenhum de nós foi."
"Pensar no lago tá fazendo meu estômago embrulhar novamente, tirando meu apetite no processo."
"Já se passou tanto tempo a essa altura, eu preciso aprender a superar as coisas..."
"Na verdade, isso me lembra."
"Os outros estão bastante envolvidos em suas próprias conversas, mas eu abaixo a voz mesmo assim, inclinando-me ao Leo."
m "— Ei, Leo."
l "— Mmmh?"
"Leo se vira para mim. Ele estava no meio de uma mordida enorme e agora está com a metade de um pimentão pendurado no focinho."
"Isso me fez perder a linha de raciocínio por um segundo."
m "— Aaah... bem. É que eu queria filmar o lago um pouco pro meu projeto."
"Leo abaixa a cabeça para tirar o pimentão do focinho, apenas para comê-lo um segundo depois."
"Ele mastiga por um tempo, mas suas orelhas ainda estão apontadas para mim, então continuo."
m "— É meio importante pra história de Echo. Enfim, cê me disse que na segunda todos estarão livres durante o almoço."
"Percebo que pelo posicionamento das orelhas do Leo que ele sabe para onde estou indo, e não tá gostando muito da ideia."
"Eu continuo rapidamente."
m "— É claro que não precisamos fazer isso, mas já faz muito tempo e, se a cidade estiver deixando ele mais bonito, pode ser divertido..."
l "— Escuta, Chase..."
"Sinto meu rosto queimar um pouco sob o pelo."
m "— Desculpa, foi uma ideia idiota..."
l "— Não não, Chase, se dependesse de mim, eu com certeza iria, só que..."
"Leo olha para o Flynn, e eu também olho, vendo que ele ainda está conversando com o Carl."
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "— Não importa o quão rápido tu coma, eu não vou me impressionar caralho."
"Ele está com aquela expressão clássica do Flynn no rosto onde ele fica pressionando os lábios, tentando não sorrir."
c "— E se eu comesse todos os TRÊS?"
f "— Tu já comeu quase tudo do primeiro, então não vale mais, né?"
scene bg motelbeds
show Leo at center
with dissolve
"Olho novamente para o meu sanduíche."
"De repente me sinto muito culpado. Aqui estou eu, de volta depois de três anos, presumindo que sei como todos se sentem." # Here I am = Aqui estou eu?
"Agora estou me sentindo como um impostor."
"Leo percebe, como sempre, e me cutuca com o ombro."
l "— Ei, não se preocupa, não é culpa sua."
"De repente, as orelhas do Leo se levantam, e eu sei que ele de repente teve uma ideia."
"Suas orelhas o tornam facilmente legível, assim como ler as pessoas era fácil pra ele."
"Isso tornou ainda mais impressionante o fato dele ser capaz de perceber o que a maioria de nós estava pensando, considerando minhas orelhas curtas e atarracadas."
"... Ou a ausência delas no Flynn."
l "— Escuta, tem um lugar bacana na beira do rio que na verdade fica bem perto do lago."
l "— Poderíamos almoçar e você poderia ir andando até lá pra fazer sua filmagem!"
"A ideia me faz sentir um pouco melhor."
m "— Beleza, isso poderia ser divertido. E também, esse hotel não tem piscina, então seria muito bom nadar em algum lugar."
l "— Heh, lontras e suas águas. De qualquer forma, vou ter que perguntar pro Flynn, mas eu acho que ele vai ficar de boa com isso."
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "— O que REALMENTE me impressionaria é se tu não comesse o resto."
c "— ..."
c "— Cê é um comédia, Flynn."
"Carl volta a enfiar o próximo hambúrguer na boca enquanto Flynn olha para ele com um leve desgosto."
"Ele de repente percebe que estamos o observando e nos olha de forma estranha, mas isso lentamente se transforma em um sorriso quando ele foca no Leo." # smirk (sorriso) = ?
f "— Parece que tu tá bem feliz, Leo. Diferente de como você tem sido nos últimos três anos."
scene bg motelbeds
show Leo at center
with dissolve
"Fico confuso e franzo a testa olhando para o Leo. Vejo sua expressão mudando e olhando para o Flynn de uma forma que não entendo muito bem."
l "— Bem é claro que eu tô feliz por ver todos nós juntos de novo."
"Olho do Leo para o Flynn, e é muito fácil imaginar um raio de eletricidade entre eles."
scene bg motelcouch
show Flynn at left
show Carl at right
with dissolve
f "— Tu deveria ter visto ele, Chase. Ele passava dias sem sorrir."
c "— Aham, o Leo tem sido meio chato desde que vocês foram."
f "— A Jenna não é uma conselheira? Ei, cê deveria ter uma sessão com o Leo."
scene bg moteltable
show Jenna at left
show TJ Neutral at center
with dissolve
j "— Uhm, eu ainda tô me formando. E eu não vou trabalhar com terapia."
j "— Isso só me deixaria triste."
"O TJ está ocupado tentando segurar seu sanduíche e comê-lo ao mesmo tempo, sem muito sucesso, mas ele também olha para cima." # olha para cima tá correto mas fica estranho
t "— Leo com depressão? É difícil imaginar você NÃO sorrindo. Parecia estar tudo bem com você na internet."
j "— Há algo de errado acontecendo, Leo?"
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