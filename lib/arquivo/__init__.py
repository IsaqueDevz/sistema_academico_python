from validate_docbr import CPF
estudante = []
disciplinas = []
turmasvalidas = []
disciplinasvalidas = []
notas = {}
media = 0
situacaodisciplina = {}


def cadnome():
    while True:
        nome = str(input('Digite o nome do estudante: ')).strip()
        
        if nome.replace(" ", "").isalpha():
            estudante.append(nome)
            break

        else:
            print('O nome não pode conter números ou símbolos! Tente novamente')


def cadmatricula():
    while True:
        matricula = input("Matrícula do estudante: ").upper()

        if len(matricula) == 13:
            estudante.append(matricula)
            break

        else:
            print('A matrícula é inválida! (13 dígitos)')


def cadcurso():
    while True:
        curso = input("Curso do estudante (SIGLA): ").upper()
        
        if curso == 'TIPI' or curso == 'EDF' or curso == 'ADM' or curso == 'MA':
            estudante.append(curso)
            break

        else:
            print('Curso inválido para o ensino médio!')


def cadturma():
    while True:
        turma = input("Turma do estudante: ").upper()

        if estudante[2] == 'TIPI':
            turmasvalidas = ['M08', 'M13', 'M15', 'M10']
            


        elif estudante[2] == 'EDF':
            turmasvalidas = ['M06', 'M05', 'M12', 'M09']

        elif estudante[2] == 'ADM':
            turmasvalidas = ['M01', 'M02', 'M03', 'M04']

        else:
            turmasvalidas = ['M11', 'M17', 'M14', 'M16']

        if turma in turmasvalidas:
            estudante.append(turma)
            break

        else:
            print('Essa sala não pertence ao seu curso! Tente novamente')


def cadcpf():
    validarcpf = CPF()
    while True:
        cpf = input("CPF do estudante (123456789-10): ")

        if validarcpf.validate(cpf):
            estudante.append(cpf)
            break

        else:
            print('CPF inválido!')


def cadastrar_estudante():
    cadnome()
    cadmatricula()
    cadcurso()
    cadturma()
    cadcpf()
    print("Estudante cadastrado!")


def cadastrar_disciplina():
    while True:
        disciplina = input("Nome da disciplina: ").upper()

        if estudante[2] == 'TIPI':
            disciplinasvalidas = ["FILOSOFIA", "SOCIOLOGIA", "GEOGRAFIA", "HISTÓRIA", "ARTE", "EDUCAÇÃO FÍSICA", "LÍNGUA PORTUGUESA E LITERATURA BRASILEIRA", "INGLÊS", 
            "MATEMÁTICA", "FÍSICA", "QUÍMICA", "BIOLOGIA", "ROBÓTICA E SISTEMAS EMBARCADOS", "PROJETOS DE EXTENSÃO", "PROJETO INTEGRADOR", "LÓGICA E TÉCNICAS DE PROGRAMAÇÃO", 
            "FUNDAMENTOS DE TECNOLOGIA DA INFORMAÇÃO", "APLICATIVOS GRÁFICOS PARA WEB", "ANÁLISE E PROJETO DE SISTEMAS", "PROGRAMAÇÃO ORIENTADA A OBJETOS", "PROGRAMAÇÃO WEB I",
            "TECNOLOGIAS DE REDE E INTERNET", "PROGRAMAÇÃO DISPOSITIVOS MÓVEIS", "PROGRAMAÇÃO WEB II",]
            
        elif estudante[2] == 'EDF':
            disciplinasvalidas = ["FILOSOFIA", "SOCIOLOGIA", "GEOGRAFIA", "HISTÓRIA", "ARTE", "EDUCAÇÃO FÍSICA", "LÍNGUA PORTUGUESA E LITERATURA BRASILEIRA", "LPLB",
            "INGLÊS", "MATEMÁTICA", "FÍSICA", "QUÍMICA", "BIOLOGIA", "MATERIAIS DE CONSTRUÇÃO", "INFORMÁTICA APLICADA", "DESENHO TÉCNICO E ARQUITETÔNICO",
            "SEGURANÇA, MEIO AMBIENTE E SAÚDE", "TOPOGRAFIA", "ESTRUTURA ISOSTÁTICA", "PROJETO DE EDIFICAÇÕES I", "MECÂNICA DOS SOLOS", "PROJETO ESTRUTURAL",
            "PROJETO DE INSTALAÇÕES ELÉTRICAS E LÓGICA", "PROJETO DE INSTALAÇÕES HIDRÁULICAS E SANITÁRIAS", "ORÇAMENTO E PLANEJAMENTO DE OBRAS", "PROJETO DE EDIFICAÇÕES II",
            "TECNOLOGIA DAS CONSTRUÇÕES I", "TECNOLOGIA DAS CONSTRUÇÕES II",]

        elif estudante[2] == 'ADM':
            disciplinasvalidas = ["FILOSOFIA", "SOCIOLOGIA", "GEOGRAFIA", "HISTÓRIA", "ARTE", "EDUCAÇÃO FÍSICA", "LÍNGUA PORTUGUESA E LITERATURA BRASILEIRA", "LPLB",
            "INGLÊS", "MATEMÁTICA", "FÍSICA", "QUÍMICA", "BIOLOGIA", "ÉTICA E DIREITO DO CONSUMIDOR", "EMPREENDEDORISMO E DESENVOLVIMENTO DE PROJETOS",
            "COMUNICAÇÃO EMPRESARIAL", "INGLÊS PARA NEGÓCIOS", "INFORMÁTICA", "MATEMÁTICA FINANCEIRA", "ESTATÍSTICA", "CONTABILIDADE GERAL", "FINANÇAS",
            "GESTÃO DE PESSOAS", "ROTINAS E CÁLCULOS TRABALHISTAS", "GESTÃO PÚBLICA", "MARKETING", "LOGÍSTICA", "FUNDAMENTOS DA ECONOMIA",
            "FUNDAMENTOS DA PRODUÇÃO", "FUNDAMENTOS DA ADMINISTRAÇÃO",]

        else:
            disciplinasvalidas = ["FILOSOFIA", "SOCIOLOGIA", "GEOGRAFIA", "HISTÓRIA", "ARTE", "EDUCAÇÃO FÍSICA", "LÍNGUA PORTUGUESA E LITERATURA BRASILEIRA", "INGLÊS", 
            "MATEMÁTICA", "FÍSICA", "QUÍMICA", "BIOLOGIA", "ECOLOGIA APLICADA", "FUNDAMENTOS DE EDUCAÇÃO AMBIENTAL", "ESTATÍSTICA APLICADA",
            "LEGISLAÇÃO E GESTÃO AMBIENTAL", "MICROBIOLOGIA APLICADA", "SOLOS E RECUPERAÇÃO DE ÁREAS DEGRADADAS", "SANEAMENTO AMBIENTAL E SAÚDE PÚBLICA",
            "SISTEMA DE INFORMAÇÕES GEOGRÁFICAS", "CONSERVAÇÃO DA NATUREZA", "INFORMÁTICA APLICADA", "GERENCIAMENTO DE PROJETOS AMBIENTAIS", 
            "HIDROLOGIA, MANEJO E CONSERVAÇÃO DE BACIAS HIDROGRÁFICAS", "DIAGNÓSTICO SOCIOAMBIENTAL", "SEGURANÇA, MEIO AMBIENTE E SAÚDE",]
        

        if disciplina in disciplinasvalidas:
            disciplinas.append(disciplina)
            break
        
        else:
            print('Essa Disciplina é inválida ou pertence a outro curso!')

    print("Disciplina cadastrada!")


def cadastrar_notas():
    for i in disciplinas:
        while True:
            nota = float(input(f'Digite a nota do estudante em {i}: '))

            if 0 <= nota <= 10:
                break
            print('A nota deve estar entre 0 e 10')

        notas[i] = nota

        if nota < 6:
            situacaodisciplina[i] = 'Reprovado'


        elif nota >= 6 and nota < 10:
            situacaodisciplina[i] = 'Aprovado'

        else: 
            situacaodisciplina[i] = 'Aprovado com distinção'

    estudante.append(notas)        
    estudante.append(situacaodisciplina)   


def situacao_estudante():
    reprovadas = 0
    for i in situacaodisciplina.values():
        if i == 'Reprovado':
            reprovadas += 1

    if reprovadas == 0:
        return 'Passou de ano direto'

    if reprovadas <= 2:
        return 'Passou de ano com dependência'

    return 'Retido'


def ficha_estudante():

    print("\n=== FICHA DO ESTUDANTE ===")
    
    for informação in estudante[:5]:
        print(informação, end=' | ')
    print()

    for materia in disciplinas:
        print()
        print(f"{materia}: {notas[materia]} - {situacaodisciplina[materia]}")
        
    print(f'\nSituação final: {situacao_estudante()}')


def listar_disciplinas():

    print("\n=== DISCIPLINAS ===")

    for disciplina in disciplinas:
        print(disciplina)
