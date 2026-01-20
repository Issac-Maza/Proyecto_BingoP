import random
import string
import os

# ==============================================================================
# 1. REPOSITORIO MAESTRO UNIFICADO (COMPATIBILIDAD TOTAL)
# ==============================================================================
REPOSITORIO_MASTER = {
    'SP': [
        'CASA', 'PERRO', 'GATO', 'SOL', 'LUNA', 'MAR', 'CIELO', 'TIERRA', 
        'AGUA', 'FUEGO', 'AIRE', 'NUBE', 'LLUVIA', 'NIEVE', 'VIENTO', 
        'RAYO', 'TRUENO', 'OLA', 'RIO', 'LAGO', 'MONTAÑA', 'FLOR', 'ARBOL', 
        'LIBRO', 'SILLA', 'MESA', 'LAPIZ', 'PAPEL', 'COMPUTADORA', 'TELEFONO',
        'VIDA', 'TIEMPO', 'DIA', 'AÑO', 'HOMBRE', 'MUJER', 'NIÑO', 'MUNDO', 'PAIS',
        'CIUDAD', 'TRABAJO', 'FAMILIA', 'AMIGO', 'PERSONA', 'GRUPO', 'LUGAR', 'MANO',
        'PROBLEMA', 'PUERTA', 'VENTANA', 'PALABRA', 'HISTORIA', 'NOCHE', 'ESCUELA',
        'ESTRELLA', 'CAMPO', 'LUZ', 'BLANCO', 'NEGRO', 'ROJO', 'AZUL', 'VERDE',
        'GRANDE', 'PEQUEÑO', 'NUEVO', 'VIEJO', 'BUENO', 'MALO', 'ALTO', 'BAJO', 'LARGO', 'CORTO',
        'HACER', 'DAR', 'TENER', 'DECIR', 'VER', 'SABER', 'PODER', 'QUERER', 'VENIR', 'PENSAR',
        'SALIR', 'LLEGAR', 'PASAR', 'PONER', 'TOMAR', 'HABLAR', 'SEGUIR', 'LLEVAR', 'DEJAR',
        'SENTIR', 'ENCONTRAR', 'LLAMAR', 'VIVIR', 'CREER', 'CONOCER', 'PARECER', 'EMPEZAR', 'BUSCAR',
        'COMER', 'BEBER', 'DORMIR', 'CORRER', 'CAMINAR', 'ESCRIBIR', 'LEER', 'JUGAR', 'CANTAR',
        'COMPRAR', 'VENDER', 'TRABAJAR', 'ESTUDIAR', 'APRENDER', 'ENSEÑAR', 'ABRIR', 'CERRAR',
        'ESPERAR', 'RECORDAR', 'OLVIDAR', 'GANAR', 'PERDER', 'AMAR', 'ODIAR', 'NOMBRE', 'FORMA',
        'PARTE', 'CASO', 'VEZ', 'HORA', 'FINAL', 'MANERA', 'PREGUNTA', 'SISTEMA', 'MOMENTO',
        'NUMERO', 'CABEZA', 'OJO', 'CALLE', 'HIJO', 'PADRE', 'MADRE', 'NIÑA', 'GENTE', 'GOBIERNO',
        'BOSQUE', 'COLOR', 'AMARILLO', 'MEJOR', 'PRIMERO', 'ULTIMO', 'MISMO', 'OTRO', 'QUEDAR',
        'ENTRAR', 'BAILAR', 'SUBIR', 'BAJAR', 'NACER', 'MORIR', 'TODO', 'CADA', 'MUERTE', 'AMOR',
        'RAZON', 'MUCHO', 'POCO', 'SIEMPRE', 'NUNCA', 'BIEN', 'MAL', 'AQUI', 'ALLI',
        'AHORA', 'DESPUES', 'ANTES', 'HOY', 'MAÑANA', 'AYER', 'TARDE', 'TEMPRANO', 'DENTRO', 'FUERA',
        'ARRIBA', 'ABAJO', 'CERCA', 'LEJOS', 'JUNTO', 'SOLO', 'MUY', 'MAS', 'MENOS', 'TANTO',
        'NADA', 'ALGO', 'CUAL', 'CUANDO', 'DONDE', 'COMO', 'PORQUE'
    ],
    'EN': [
        'HOUSE', 'DOG', 'CAT', 'SUN', 'MOON', 'SEA', 'SKY', 'EARTH', 
        'WATER', 'FIRE', 'AIR', 'CLOUD', 'RAIN', 'SNOW', 'WIND', 
        'THUNDER', 'STORM', 'WAVE', 'RIVER', 'LAKE', 'MOUNTAIN', 'FLOWER', 
        'TREE', 'BOOK', 'CHAIR', 'TABLE', 'PEN', 'PAPER', 'COMPUTER', 'PHONE',
        'TIME', 'PERSON', 'YEAR', 'WAY', 'DAY', 'THING', 'MAN', 'WORLD', 'LIFE', 'HAND',
        'PART', 'CHILD', 'EYE', 'WOMAN', 'PLACE', 'WORK', 'WEEK', 'CASE', 'POINT', 'GOVERNMENT',
        'COMPANY', 'NUMBER', 'GROUP', 'PROBLEM', 'FACT', 'ROOM', 'MONEY', 'STORY', 'FAMILY',
        'LOT', 'RIGHT', 'STUDY', 'WORD', 'BUSINESS', 'ISSUE', 'SIDE', 'KIND', 'HEAD',
        'SERVICE', 'FRIEND', 'FATHER', 'POWER', 'HOUR', 'GAME', 'LINE', 'END', 'MEMBER',
        'LAW', 'CAR', 'CITY', 'COMMUNITY', 'NAME', 'PRESIDENT', 'TEAM', 'MINUTE', 'IDEA', 'BODY',
        'INFORMATION', 'BACK', 'PARENT', 'FACE', 'LEVEL', 'OFFICE', 'DOOR', 'HEALTH', 'ART', 'WAR',
        'FIELD', 'FOREST', 'LIGHT', 'COLOR', 'WHITE', 'BLACK', 'RED',
        'BLUE', 'GREEN', 'YELLOW', 'BIG', 'SMALL', 'NEW', 'OLD', 'GOOD', 'BAD', 'GREAT',
        'HIGH', 'LOW', 'LONG', 'SHORT', 'FIRST', 'LAST', 'SAME', 'DIFFERENT', 'EARLY', 'LATE',
        'MAKE', 'GIVE', 'TAKE', 'COME', 'THINK', 'SEE', 'WANT', 'USE', 'FIND', 'TELL',
        'ASK', 'SEEM', 'FEEL', 'LEAVE', 'CALL', 'TRY', 'KEEP', 'LET', 'BEGIN',
        'HELP', 'SHOW', 'HEAR', 'PLAY', 'RUN', 'MOVE', 'LIVE', 'BELIEVE', 'BRING', 'HAPPEN',
        'WRITE', 'SIT', 'STAND', 'LOSE', 'PAY', 'MEET', 'INCLUDE', 'CONTINUE', 'LEARN', 'CHANGE',
        'LEAD', 'UNDERSTAND', 'WATCH', 'FOLLOW', 'STOP', 'CREATE', 'SPEAK', 'READ', 'ALLOW', 'ADD',
        'SPEND', 'GROW', 'OPEN', 'WALK', 'WIN', 'OFFER', 'REMEMBER', 'LOVE', 'CONSIDER', 'APPEAR',
        'BUY', 'WAIT', 'SERVE', 'DIE', 'SEND', 'EXPECT', 'BUILD', 'STAY', 'FALL', 'CUT',
        'REACH', 'KILL', 'RAISE', 'PASS', 'SELL', 'REQUIRE', 'REPORT', 'DECIDE', 'PULL', 'RETURN'
    ],
    'PT': [
        'CASA', 'CAO', 'GATO', 'SOL', 'LUA', 'MAR', 'CEU', 'TERRA', 
        'AGUA', 'FOGO', 'AR', 'NUVEM', 'CHUVA', 'NEVE', 'VENTO', 
        'RAIO', 'TROVAO', 'ONDA', 'RIO', 'LAGO', 'MONTANHA', 'FLOR', 
        'ARVORE', 'LIVRO', 'CADEIRA', 'MESA', 'CANETA', 'PAPEL', 'COMPUTADOR',
        'TEMPO', 'PESSOA', 'ANO', 'VEZ', 'DIA', 'COISA', 'HOMEM', 'MUNDO', 'VIDA', 'MAO',
        'PARTE', 'CRIANÇA', 'OLHO', 'MULHER', 'LUGAR', 'TRABALHO', 'SEMANA', 'CASO', 'PONTO', 'GOVERNO',
        'EMPRESA', 'NUMERO', 'GRUPO', 'PROBLEMA', 'FATO', 'SALA', 'DINHEIRO', 'HISTORIA', 'FAMILIA',
        'MUITO', 'DIREITO', 'ESTUDO', 'PALAVRA', 'NEGOCIO', 'QUESTAO', 'LADO', 'TIPO', 'CABEÇA',
        'SERVIÇO', 'AMIGO', 'PAI', 'PODER', 'HORA', 'JOGO', 'LINHA', 'FIM', 'MEMBRO',
        'LEI', 'CARRO', 'CIDADE', 'COMUNIDADE', 'NOME', 'PRESIDENTE', 'EQUIPE', 'MINUTO', 'IDEIA', 'CORPO',
        'INFORMAÇAO', 'COSTAS', 'MAE', 'ROSTO', 'NIVEL', 'ESCRITORIO', 'PORTA', 'SAUDE', 'ARTE', 'GUERRA',
        'CACHORRO', 'ESTRELA', 'CAMPO', 'FLORESTA', 'LUZ', 'COR', 'BRANCO', 'PRETO', 'VERMELHO',
        'AZUL', 'VERDE', 'AMARELO', 'GRANDE', 'PEQUENO', 'NOVO', 'VELHO', 'BOM', 'MAU', 'MELHOR',
        'ALTO', 'BAIXO', 'LONGO', 'CURTO', 'PRIMEIRO', 'ULTIMO', 'MESMO', 'OUTRO', 'CEDO', 'TARDE',
        'FAZER', 'DAR', 'TER', 'DIZER', 'VER', 'SABER', 'QUERER', 'VIR', 'PENSAR',
        'SAIR', 'CHEGAR', 'PASSAR', 'FICAR', 'POR', 'TOMAR', 'FALAR', 'SEGUIR', 'LEVAR', 'DEIXAR',
        'SENTIR', 'ENCONTRAR', 'CHAMAR', 'VIVER', 'ACREDITAR', 'CONHECER', 'PARECER', 'COMEÇAR', 'PROCURAR',
        'COMER', 'BEBER', 'DORMIR', 'CORRER', 'ANDAR', 'ESCREVER', 'LER', 'JOGAR', 'CANTAR', 'DANÇAR',
        'COMPRAR', 'VENDER', 'TRABALHAR', 'ESTUDAR', 'APRENDER', 'ENSINAR', 'ABRIR', 'FECHAR', 'ESPERAR',
        'LEMBRAR', 'ESQUECER', 'GANHAR', 'PERDER', 'AMAR', 'ODIAR', 'MORTE', 'AMOR', 'RAZAO', 'FORMA',
        'MANEIRA', 'SISTEMA', 'MOMENTO', 'RUA', 'FILHO', 'FILHA', 'POVO', 'BOSQUE', 'ENTRAR', 'SUBIR'
    ],
    'DT': [
        'HUIS', 'HOND', 'KAT', 'ZON', 'MAAN', 'ZEE', 'HEMEL', 'AARDE', 
        'WATER', 'VUUR', 'LUCHT', 'WOLK', 'REGEN', 'SNEEUW', 'WIND', 
        'DONDER', 'STORM', 'GOLF', 'RIVIER', 'MEER', 'BERG', 'BLOEM',
        'TIJD', 'PERSOON', 'JAAR', 'KEER', 'DAG', 'DING', 'MAN', 'WERELD', 'LEVEN', 'HAND',
        'DEEL', 'KIND', 'OOG', 'VROUW', 'PLAATS', 'WERK', 'WEEK', 'GEVAL', 'PUNT', 'REGERING',
        'BEDRIJF', 'NUMMER', 'GROEP', 'PROBLEEM', 'FEIT', 'KAMER', 'GELD', 'VERHAAL', 'FAMILIE',
        'VEEL', 'RECHT', 'STUDIE', 'BOEK', 'WOORD', 'ZAAK', 'KWESTIE', 'KANT', 'SOORT', 'HOOFD',
        'DIENST', 'VRIEND', 'VADER', 'MACHT', 'UUR', 'SPEL', 'LIJN', 'EINDE', 'LID',
        'WET', 'AUTO', 'STAD', 'GEMEENSCHAP', 'NAAM', 'PRESIDENT', 'TEAM', 'MINUUT', 'IDEE', 'LICHAAM',
        'INFORMATIE', 'RUG', 'MOEDER', 'GEZICHT', 'NIVEAU', 'KANTOOR', 'DEUR', 'GEZONDHEID', 'KUNST', 'OORLOG',
        'BOOM', 'STER',
        'VELD', 'BOS', 'LICHT', 'KLEUR', 'WIT', 'ZWART', 'ROOD',
        'BLAUW', 'GROEN', 'GEEL', 'GROOT', 'KLEIN', 'NIEUW', 'OUD', 'GOED', 'SLECHT', 'BETER',
        'HOOG', 'LAAG', 'LANG', 'KORT', 'EERSTE', 'LAATSTE', 'ZELFDE', 'ANDER', 'VROEG', 'LAAT',
        'MAKEN', 'GEVEN', 'NEMEN', 'KOMEN', 'DENKEN', 'ZIEN', 'WILLEN', 'GEBRUIKEN', 'VINDEN', 'VERTELLEN',
        'VRAGEN', 'WERKEN', 'LIJKEN', 'VOELEN', 'VERLATEN', 'BELLEN', 'PROBEREN', 'HOUDEN', 'LATEN', 'BEGINNEN',
        'HELPEN', 'TONEN', 'HOREN', 'SPELEN', 'RENNEN', 'BEWEGEN', 'LEVEN', 'GELOVEN', 'BRENGEN', 'GEBEUREN',
        'SCHRIJVEN', 'ZITTEN', 'STAAN', 'VERLIEZEN', 'BETALEN', 'ONTMOETEN', 'OMVATTEN', 'DOORGAAN', 'LEREN',
        'LEIDEN', 'BEGRIJPEN', 'KIJKEN', 'VOLGEN', 'STOPPEN', 'CREEREN', 'SPREKEN', 'LEZEN', 'TOESTAAN',
        'TOEVOEGEN', 'BESTEDEN', 'GROEIEN', 'OPENEN', 'LOPEN', 'WINNEN', 'AANBIEDEN', 'HERINNEREN', 'LIEFDE',
        'DOOD', 'LIEFHEBBEN', 'HATEN', 'REDEN', 'VORM', 'MANIER', 'SYSTEEM', 'MOMENT', 'STRAAT'
    ]
}

def generar_id():
    """Genera un ID alfanumérico aleatorio de 8 caracteres"""
    letras_numeros = string.ascii_uppercase + string.digits
    return ''.join(random.choices(letras_numeros, k=8))

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpiar_pantalla()
        print("=========================================")
        print("   GENERADOR DE CARTONES DE BINGO 3000   ")
        print("=========================================")
        print("Selecciona el idioma de los cartones:")
        print("1. Español (SP)")
        print("2. Inglés (EN)")
        print("3. Portugués (PT)")
        print("4. Holandés (DT)")
        print("5. MIXTO (Generar cartones variados)")
        print("6. Salir")
        
        opcion = input("\nTu elección (1-6): ")
        
        if opcion == '6':
            print("👋 ¡Hasta luego!")
            break

        mapa_idiomas = {'1': 'SP', '2': 'EN', '3': 'PT', '4': 'DT'}
        
        if opcion not in ['1', '2', '3', '4', '5']:
            input("❌ Opción inválida. Presiona Enter para intentar de nuevo...")
            continue

        cantidad_str = input("\n¿Cuántos cartones quieres generar? (Ej: 50, 200): ")
        if not cantidad_str.isdigit():
            input("❌ Debes escribir un número válido. Enter para reiniciar...")
            continue
        
        cantidad = int(cantidad_str)

        nombre_archivo = input("Nombre del archivo (ej: bingo_juego1.txt): ")
        if not nombre_archivo.endswith(".txt"):
            nombre_archivo += ".txt"

        print(f"\n🚀 Generando {cantidad} cartones en '{nombre_archivo}'...")

        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                for i in range(cantidad):
                    
                    # Lógica para elegir idioma
                    if opcion == '5':
                        idioma_actual = random.choice(['SP', 'EN', 'PT', 'DT'])
                    else:
                        idioma_actual = mapa_idiomas[opcion]
                    
                    # Generar ID (Ej: SP-A1B2C3D4)
                    identificador = f"{idioma_actual}-{generar_id()}"

                    # Cantidad de palabras por cartón (Ajustado a reglas del bingo)
                    # SP=24, EN=14, PT=20, DT=10 (Según código BingoP)
                    # Pero para el archivo TXT generamos suficientes palabras
                    # El código BingoP toma las que necesita según la config.
                    # Aquí generamos 24 para asegurar que sirva para SP (el más grande).
                    lista_palabras = REPOSITORIO_MASTER[idioma_actual]
                    
                    # Tomamos hasta 24 palabras si es posible, o todas las disponibles
                    k_palabras = min(len(lista_palabras), 24)
                    seleccion = random.sample(lista_palabras, k_palabras)

                    # Escribir línea
                    linea = f"{identificador} {' '.join(seleccion)}\n"
                    f.write(linea)
            
            print(f"✅ ¡ÉXITO! Archivo guardado.")
        
        except Exception as e:
            print(f"❌ Error al crear archivo: {e}")

        # --- PREGUNTA DEL BUCLE ---
        continuar = input("\n¿Quieres generar otro archivo? (S/N): ").strip().lower()
        if continuar != 's':
            print("👋 ¡Nos vemos!")
            break

if __name__ == "__main__":
    main()