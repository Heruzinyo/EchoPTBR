# Legendas para os créditos da rota do Leo

O vídeo deve ser renderizado no formato: **QuickTime (.mov)** com o Codec de vídeo: **GoPro CineForm** e a Profundidade: **RGBA de 12 bpc + alfa**. Não inclua o áudio!

Depois que o vídeo terminar de ser renderizado, use esses comandos no **[ffmpeg](https://github.com/GyanD/codexffmpeg)**:

`ffmpeg -i original.mov -filter:v alphaextract mask.mov`

`ffmpeg -i original.mov -i mask.mov -filter_complex "hstack" -codec:v vp8 -crf 10 -b:v 50M -auto-alt-ref 0 output.webm`

("original.mov" se refere ao vídeo renderizado).

("-b:v 50M" se refere ao Bitrate, eu deixei 50M para não ficar feio, mas você pode alterar o valor).

O vídeo precisará ser usado com o comando `"sidemask=True"`.

O vídeo está em uma resolução 2x maior que a resolução do jogo para que as legendas fiquem em HD, então é necessário usar o comando `"zoom 0.5"` para que ele fique dentro da resolução do jogo.

Veja o arquivo **Leo_act_2.rpy** para saber como esse vídeo foi utilizado.

Para mais informações leia **[a documentação do Ren'Py para vídeos](https://www.renpy.org/doc/html/movie.html)**.