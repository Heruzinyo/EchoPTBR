
# Arquivos específicos da versão de Android<br><br>Eu também decidi arrumar o posicionamento do ícone original. Também há uma versão do ícone da versão de PC dentro do arquivo PSD, caso você queira usar eu recomendo que você renderize o arquivo PSD do background para que o fundo não fique totalmente preto.

### O jogo usa os mesmos arquivos da versão de PC, você apenas precisa adicionar o préfixo "x-" aos arquivos.
### A versão de android não utiliza os arquivos de texto em sua versão normal, mas sim em sua versão cache. Para gerar a versão cache do arquivo traduzido, no PC coloque o arquivo em sua versão normal e delete a versão cache, e então rode o jogo, depois que ele iniciar (pode demorar um pouco) a versão cache do arquivo será criada.
### Os arquivos AndroidManifest.xml e classes.dex contém a informação sobre a versão do Patch.
### Por algum motivo, após alterar o ícone é necessário o arquivo notification_template_custom_big.xml para que o APK funcione.
### Os arquivos AndroidManifest.xml, classes.dex e notification_template_custom_big.xml foram criados com o Apktool após descompilar o APK do jogo.