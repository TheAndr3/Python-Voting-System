class Cadastro:

  def __init__(self):
    self.lista_candidatos = []

  def Cadastro_Candidatos(self):
    #Nesta funcao eu cadastro todos os candidatos num dicionario, logo apos adiciono numa lista.
    self.candidatos = {}
    self.chapa = input("Qual é o nome da chapa: ")
    self.Reitor = input("Digite o nome do reitor: ")
    self.Vice = input("Digite o nome do vice-reitor: ")
    self.candidatos["Reitor"] = self.Reitor
    self.candidatos["Vice-Reitor"] = self.Vice
    self.candidatos["Chapa"] = self.chapa
    self.lista_candidatos.append(self.candidatos)

  def Mostrar_Candidatos(self):
    #Aqui mostro todos os candidatos percorrendo a lista enumerada, podendo ser acessada pelo índice.
    print('Aqui estão as chapas registradas:')
    for indice, candidatos in enumerate(self.lista_candidatos):
      print(f"Índice: {indice}")
      print(f"Chapa: {candidatos['Chapa']}")
      print(f"Reitor: {candidatos['Reitor']}")
      print(f"Vice-Reitor: {candidatos['Vice-Reitor']}")
      print()

  def Alterar_nomes(self):
    #Aqui consigo alterar o nome do reitor ou vice-reitor, um por um.
    try:
      self.indice2 = int(input("Qual é o índice?: "))
      if self.indice2 < len(self.lista_candidatos):
        candidatos = self.lista_candidatos[self.indice2]
        self.escolha = input('Reitor [1] | Vice-Reitor [2]: ')
        if self.escolha == '1':
          self.novo_reitor = input("Qual é o nome do novo Reitor: ")
          candidatos['Reitor'] = self.novo_reitor
        elif self.escolha == '2':
          self.novo_vice = input("Qual é o nome do novo Vice-Reitor: ")
          candidatos['Vice-Reitor'] = self.novo_vice
        else:
          print('Digito invalido')
      else:
        print('Indice inválido')
    except ValueError:
      print('Digito inválido, por favor tente novamente')

  def Excluir_chapa(self):
    #Aqui, utilizando do índice excluo a chapa, mostrando todas.
    try:
      self.indice1 = int(input('Qual o indice da chapa que deseja excluir?: '))
      candidatos = self.lista_candidatos[self.indice1]
      self.lista_candidatos.remove(candidatos)
      print(f"Chapa {'Chapa'} Removida com sucesso")
    except ValueError:
      print('Valor inválido, por favor tente novamente.')

  def salvar_dados(self):
    #Aqui é uma função para uma futura auditoria com todas as chapas registradas.
    try:
      nome_arquivo = input(
        "Digite o nome do arquivo de destino que irá salvar os dados do cadastro: "
      )
      with open(nome_arquivo, 'w') as arquivo:
        #Escrever os dados no arquivo
        arquivo.write("Dados de votação:\n")
        arquivo.write("Lista de candidatos:\n")
        for candidatos in self.lista_candidatos:
          arquivo.write("Chapa: {}\n".format(candidatos['Chapa']))
          arquivo.write("Reitor: {}\n".format(candidatos['Reitor']))
          arquivo.write("Vice-Reitor: {}\n".format(candidatos['Vice-Reitor']))
          arquivo.write("\n")

      print("Dados salvos com sucesso no arquivo {}".format(nome_arquivo))
    except IOError:
      print("Erro ao salvar os dados no arquivo")


class Votação(Cadastro):
  #Nessa classe estou usando dados da primeira classe, portando estou herdando da classe Cadastro, por isso coloquei a classe como parâmetro.

  def __init__(self):
    #Como forma de herança, ocorre um super().__init__
    super().__init__()
    self.modulo1 = []
    self.modulo3 = []
    self.modulo5 = []
    self.modulo7 = []
    self.nulo = []
    self.total = 0
    self.vot_1 = []
    self.vot_2 = []
    self.vot_3 = []
    self.NTD = 0
    self.NTSD = 0
    self.NTST = 0
    self.total = 0
    self.lista_votos = []
    self.NVSD = {}
    self.NVST = {}
    self.NVD = {}
    self.inicial = None

  def eleitores(self):
    #Função que define a quantidade total de cada categoria, ultimo estágio antes de começar o processo de votação.
    self.NTSD = int(input('Número total de servidores docentes votantes: '))
    self.NTST = int(input('Número total de servidores técnicos votantes: '))
    self.NTD = int(input('Número total de discentes votantes: '))
    self.total = self.NTD + self.NTSD + self.NTST

  def ListaDePresenca(self):
    #Quando começa o período de votação, achei necessário o usuário 'assinar' uma lista de presença, para assim ser alocado no modulo que se deve, criei uma lista pra cada modulo
    while True:
      self.inicial = input('Indique a inicial do seu nome: ')
      if self.inicial.upper() in ['A', 'B', 'C', 'D']:
        self.modulo1.append(self.inicial)
        break
      elif self.inicial.upper() in ['E', 'F', 'G', 'H', 'I', 'J']:
        self.modulo3.append(self.inicial)
        break
      elif self.inicial.upper() in ['K', 'L', 'M', 'N', 'O']:
        self.modulo5.append(self.inicial)
        break
      elif self.inicial.upper() in [
          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z'
      ]:
        self.modulo7.append(self.inicial)
        break
      else:
        print('Inicial inválida, por favor digite novamente')

  def Exibir_Resultados(self):
    #Aqui foi mais para teste enquanto testava a aplicação, porém se mostrou útil quando printei o relátorio
    print('Modulo 1:', len(self.modulo1))
    print('Modulo 3:', len(self.modulo3))
    print('Modulo 5:', len(self.modulo5))
    print('Modulo 7:', len(self.modulo7))
    print()

  def Categoria(self):
    #(1 – Docente ; 2 – Servidor Técnico-administrativo; 3–Discente)
    #Criei também uma quarta opção para o usuário poder sair e encerrar o dia, pois há uma chance de ficar preso nessa etapa, caso o numero de votantes disponiveis acabe.
    while True:
      try:
        self.categoria = int(
          input('Indique a sua categoria: \n'
                '[1] – Docente \n'
                '[2] – Servidor Técnico-administrativo \n'
                '[3] – Discente \n'
                '[4] - Saída \n'
                'Digite: '))
        if self.categoria == 1:
          self.vot_1.append(self.categoria)
          if len(self.vot_1) > self.NTSD:
            #Aqui criei um sistema pra sempre verificar se o numero de votantes não ultrapassou o numero maximo que definimos mais cedo.
            self.vot_1.pop()
            print('Quantidade de Docentes insuficiente, tente novamente. \n')
          else:
            break
        elif self.categoria == 2:
          self.vot_2.append(self.categoria)
          if len(self.vot_2) > self.NTST:
            self.vot_2.pop()
            print(
              'Quantidade de Servidores Técnicos Administrativos insuficiente, tente novamente. \n'
            )
          else:
            break
        elif self.categoria == 3:
          self.vot_3.append(self.categoria)
          if len(self.vot_3) > self.NTD:
            self.vot_3.pop()
            print('Quantidade de Discentes insuficente, tente novamente. \n')
          else:
            break
        elif self.categoria == 4:
          self.confirma = input(
            'Tem certeza que quer sair? Se sim, irá automaticamente para o proximo dia: '
          )
          if self.confirma.lower() in ['sim', 's']:
            break
          else:
            print(
              'É aconselhavel sair se não houver mais categorias pra preencher. \n'
            )
        else:
          print('Categoria inválida, por favor digite novamente!\n')
      except ValueError:
        print('Dígito inválido, por favor tente novamente!\n')

    return self.categoria

  def votacao(self, categoria, lista_candidatos):
    #Função principal de votação.
    while True:
      try:
        self.indice = int(input('Qual o índice da chapa que deseja votar: '))
        if self.indice > len(lista_candidatos):
          #Tratamento de erro
          print("Índice inválido! \n")
          return
        voto = lista_candidatos[self.indice]
        #Pego o indice na lista candidatos, que é uma lista de dicionarios, e transformo numa só variavel 'voto'.
        self.lista_votos.append(voto)
        #Adiciono numa lista de votos para futura auditoria
        self.atualizar_votos(categoria, voto['Chapa'])
        #E chamo a função atualizar_votos, dando como argumento a categoria que escolhi antes e especificamente a chave 'Chapa'.
        print(f"Chapa {voto['Chapa']} votada com sucesso \n")
        break
      except ValueError:
        print('Indice da chapa inválido, tente novamente.\n')
      else:
        print('Digito inválido, tente novamente.')

  def atualizar_votos(self, categoria, chapa):
    #Aqui atualizo o numero de votantes de cada categoria na chapa que votou, usando a função acima de votação, uma das partes mais dificeis de desenvolver.
    if categoria == 1:
      if chapa in self.NVSD:
        self.NVSD[chapa] += 1
      else:
        self.NVSD[chapa] = 1

    if categoria == 2:
      if chapa in self.NVST:
        self.NVST[chapa] += 1
      else:
        self.NVST[chapa] = 1

    if categoria == 3:
      if chapa in self.NVD:
        self.NVD[chapa] += 1
      else:
        self.NVD[chapa] = 1

  def Calculo_score(self, chapa):
    #Aqui calculo todos os valores que utilizarei na formula do Score.
    NV = len(self.vot_1) + len(self.vot_2) + len(self.vot_3)
    #Pego o Len das listas de votantes pra definir o numero total
    E_sd = self.NVSD[chapa] / self.NTSD * 1 / 3
    E_st = self.NVST[chapa] / self.NTST * 1 / 3
    E_d = self.NVD[chapa] / self.NTD * 1 / 3
    #Divido a formula em partes para uma melhor vizualização.
    E = (E_sd + E_st + E_d) * NV
    return E

  def Chapa_vencedora(self, lista_candidatos):
    #Aqui defino o ganhador, chamando a função acima Calculo_Score, e utilizando da lista_candidatos da classe Cadastro.
    maior_score = 0
    Chapa_vencedora = None
    for candidato in lista_candidatos:
      chapa = candidato['Chapa']
      #Chamo a função Calculo_score com argumento chapa
      score = self.Calculo_score(chapa)
      if score > maior_score:
        maior_score = score
        Chapa_vencedora = chapa
    if Chapa_vencedora is not None:
      print(
        f"A chapa vencedora é a '{Chapa_vencedora}' com escore {maior_score}.")
    else:
      print("Não há chapas concorrentes.")

  def salvar_dados(self, voto_dia, nulo_dia, dia):
    #Aqui salvo todos os dados para a auditoria, para não se repetir deixei como parametros o voto por dia, voto nulo por dia e o dia para que assim consiga registrar corretamente.
    nome_arquivo = input(
      "Digite o nome do arquivo de destino que irá salvar os dados da votação do dia {}: "
      .format(dia))
    with open(nome_arquivo, 'a') as arquivo:
      arquivo.write("Dados de votação:\n")
      arquivo.write(f'Número de votantes do dia {dia}: {voto_dia} \n')
      arquivo.write(
        'Número de votantes por categoria do dia {}: \n'.format(dia))
      arquivo.write(
        f'Número de Servidores Docentes votantes: {len(self.vot_1)} \n')
      arquivo.write(
        f'Número de Servidores Técnicos votantes: {len(self.vot_2)} \n')
      arquivo.write(f'Número de Discentes votantes: {len(self.vot_3)} \n')
      arquivo.write(f'Número de votos nulo do dia {dia}: {nulo_dia} \n')
      arquivo.write('Número de votos nulo por categoria: \n')
      arquivo.write(
        f'Número de votos nulo dos Servidores Docentes: {nulo_cat_1} \n')
      arquivo.write(
        f'Número de votos nulo dos Servidores Técnicos: {nulo_cat_2} \n')
      arquivo.write(f'Número de votos nulo dos Discentes: {nulo_cat_3} \n')
      arquivo.write('Número de votos em cada chapa dos servidores docentes:\n')
      for chapa, votos in self.NVSD.items():
        arquivo.write(f'Chapa {chapa}: {votos} votos\n')

      arquivo.write(
        '\nNúmero de votos em cada chapa dos servidores técnicos:\n')
      for chapa, votos in self.NVST.items():
        arquivo.write(f'Chapa {chapa}: {votos} votos\n')

      arquivo.write('\nNúmero de votos em cada chapa dos discentes:\n')
      for chapa, votos in self.NVD.items():
        arquivo.write(f'Chapa {chapa}: {votos} votos\n')

    print("Dados do dia {} salvos com sucesso no arquivo {}".format(
      dia, nome_arquivo))


#Criação do menu (Adicionar a exclusão da chapa)
menu = ("[1] - Adicionar os Candidatos.\n"
        "[2] - Alterar os nomes.\n"
        "[3] - Exclusão de alguma chapa.\n"
        "[4] - Mostrar Chapas e Candidatos.\n"
        "[5] - Partir para a votação.\n")

#Transformando as classes em variáveis
votacao = Votação()
cadastro = Cadastro()
#Main 1 - Etapa de Cadastramento
while True:
  try:
    print(menu)
    escolhas = int(input('Escolha um tópico: '))
    if escolhas == 1:
      print()
      cadastro.Cadastro_Candidatos()
      print()
    elif escolhas == 2:
      if len(cadastro.lista_candidatos) > 0:
        #Assim como as funções abaixo, so conseguira entrar se houver no minimo uma chapa registrada.
        print()
        cadastro.Mostrar_Candidatos()
        cadastro.Alterar_nomes()
        print()
      else:
        print('Não há candidatos ainda. \n')
    elif escolhas == 3:
      if len(cadastro.lista_candidatos) > 0:
        print()
        cadastro.Mostrar_Candidatos()
        cadastro.Excluir_chapa()
        print()
      else:
        print('Não há candidatos ainda. \n')
    elif escolhas == 4:
      if len(cadastro.lista_candidatos) > 0:
        print()
        cadastro.Mostrar_Candidatos()
        print()
      else:
        print('Não há candidatos ainda. \n')
    elif escolhas == 5:
      if (len(cadastro.lista_candidatos)) >= 2:
        #Determinei que o progama só passa pra etapa de votação se houver 2 chapas ou mais,
        escolha = input('Certeza que deseja terminar a etapa de Cadastro?: ')
        if escolha.lower() in ['sim', 's']:
          cadastro.salvar_dados()
          print('Primeiro, defina a quantidade dos que irão votar')
          print('-' * 50)
          votacao.eleitores()
          break
      else:
        print('Deve haver pelo menos 2 chapas inscritas na votação. \n')
    else:
      print('Opção inexistente, por favor digite um número válido')
  except ValueError:
    print('Valor inválido, tente novamente.')
    print()

#Main 2 - Etapa da votação
print('Agora começou a etapa de votação!')
print('-' * 50)
#Dados para armazenar
voto_dia1 = 0
nulo_dia1 = 0
voto_dia2 = 0
nulo_dia2 = 0
voto_dia3 = 0
nulo_dia3 = 0
nulo_cat_1 = 0
nulo_cat_2 = 0
nulo_cat_3 = 0
for candidatos in cadastro.lista_candidatos:
  #preenchi os dicionarios NVSD, NVST e NVD com 0 para que não dê um TypeError no futuro (Que estava dando)
  chapa = candidatos["Chapa"]
  votacao.NVSD[chapa] = 0
  votacao.NVST[chapa] = 0
  votacao.NVD[chapa] = 0
#For que vai passando os dias, de 1 a 3.
for dia in range(1, 4):
  print(f"-------- Dia {dia} --------")
  voto = input('Deseja votar neste dia? [Sim]|[Não]: ')
  if voto.lower() in ['não', 'nao', 'n']:
    continue
  elif voto.lower() in ['sim', 's']:
    continuar = False
    while not continuar:
      #Criei uma condição para o While ir rodando, tendo certos aspectos que contradizem e quebram o loop.
      votos = []
      for i in range(votacao.total):
        votacao.ListaDePresenca()
        votacao.Categoria()
        if votacao.categoria == 4:
          continuar = True
          break

        votar = input(
          'Deseja votar em alguma chapa [Sim] Ou anular o voto [Não]:  ')
        if votar.lower() in ['nao', 'n', 'não']:
          if dia == 1:
            nulo_dia1 += 1
            #Condicionais para ir acumulando os valores diários.
            if votacao.categoria == 1:
              nulo_cat_1 += 1
            elif votacao.categoria == 2:
              nulo_cat_2 += 1
            else:
              nulo_cat_3 += 1
          elif dia == 2:
            nulo_dia2 += 1
            if votacao.categoria == 1:
              nulo_cat_1 += 1
            elif votacao.categoria == 2:
              nulo_cat_2 += 1
            else:
              nulo_cat_3 += 1
          elif dia == 3:
            nulo_dia3 += 1
            if votacao.categoria == 1:
              nulo_cat_1 += 1
            elif votacao.categoria == 2:
              nulo_cat_2 += 1
            else:
              nulo_cat_3 += 1

        elif votar.lower() in ['sim', 's']:
          cadastro.Mostrar_Candidatos()
          #Chamei da classe cadastro para mostrar os candidatos para poder saber em qual vai votar.
          votacao.votacao(votacao.categoria, cadastro.lista_candidatos)
          if dia == 1:
            voto_dia1 += 1
          elif dia == 2:
            voto_dia2 += 1
          elif dia == 3:
            voto_dia3 += 1

        #if dia == 1:
        #votacao

        if i < votacao.total - 1:
          confirma = input('Deseja votar novamente neste dia? [Sim]|[Não]: ')
          #Verificação caso o usuario queira passar pra outro dia.

          if confirma.lower() in ['não', 'nao', 'n']:
            if dia == 1:
              votacao.salvar_dados(voto_dia1, nulo_dia1, 1)
              #Salvando os dados para a auditoria com os parametros diários
            elif dia == 2:
              votacao.salvar_dados(voto_dia2, nulo_dia2, 2)
            elif dia == 3:
              votacao.salvar_dados(voto_dia3, nulo_dia2, 3)
            continuar = True
            break

#Relátorio
print('Hora de computador os dados dos 3 dias de votação: \n')
#Criei váriaveis com os prints, para que assim eu consiga organizar melhor os prints e nao fique toda uma confusão.
#------------------------------------------------------------------------
numero_votos = ('Número de votantes por dia: \n'
                f'Número de votantes do dia 1: {voto_dia1} \n'
                f'Número de votantes do dia 2: {voto_dia2} \n'
                f'Número de votantes do dia 3: {voto_dia3} \n')
numero_categoria = (
  'Número de votantes por categoria: \n'
  f'Número de Servidores Docentes votantes: {len(votacao.vot_1)} \n'
  f'Número de Servidores Técnicos votantes: {len(votacao.vot_2)} \n'
  f'Número de Siscentes votantes: {len(votacao.vot_3)} \n')
numero_nulo_dia = ('Número de votos nulo por dia: \n'
                   f'Número de votos nulo do dia 1: {nulo_dia1} \n'
                   f'Número de votos nulo do dia 2: {nulo_dia2} \n'
                   f'Número de votos nulo do dia 3: {nulo_dia3} \n')
numero_nulo_categoria = (
  'Número de votos nulo por categoria: \n'
  f'Número de votos nulo dos Servidores Docentes: {nulo_cat_1} \n'
  f'Número de votos nulo dos Servidores Técnicos: {nulo_cat_2} \n'
  f'Número de votos nulo dos Discentes: {nulo_cat_3} \n')
#-------------------------------------------------------------------------
#Aqui de fato começa os prints do relátorio.
print(numero_votos)
print(numero_categoria)
print(numero_nulo_dia)
print(numero_nulo_categoria)
print('Total de votos de cada urna:')
votacao.Exibir_Resultados()
print('Porcentagem de ausentes de cada categoria:')
print(f'Docentes ausentes: {(((len(votacao.vot_1)/votacao.NTSD)) * 100):.2f}%')
print(
  f'Servidores Técnicos ausentes: {(((len(votacao.vot_2)/votacao.NTST)) * 100):.2f}%'
)
print(f'Discentes ausentes: {(((len(votacao.vot_3)/votacao.NTD)) * 100):.2f}%')

print('Resultados da votação:')
print('Número de votos em cada chapa dos servidores docentes:')
for chapa, votos in votacao.NVSD.items():
  print(f'Chapa {chapa} : {votos} votos')

print('Número de votos em cada chapa dos servidores técnicos:')
for chapa, votos in votacao.NVST.items():
  print(f'Chapa {chapa} : {votos} votos')

print('Número de votos em cada chapa dos discentes:')
for chapa, votos in votacao.NVD.items():
  print(f'Chapa {chapa} : {votos} votos')

print("\nChapa vencedora:")
votacao.Chapa_vencedora(cadastro.lista_candidatos)
