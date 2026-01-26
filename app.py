import streamlit as st
import random
import pandas as pd
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Bingo_P: Proyecto Final",
    page_icon="🎱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 1. REPOSITORIO MAESTRO-DESAROLLADO POR Paul Alberto Alcivar Zavala
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

# --- CLASES DE LÓGICA --- DESARROLLLADO POR Paul Alberto Alcivar Zavala

class Carton:
    def __init__(self, raw_line, nombre_jugador_default="Desconocido"):
        linea_limpia = raw_line.strip()

        if ',' in linea_limpia:
            partes = linea_limpia.split(',')
            

            if len(partes) >= 3:
                self.id = partes[0].strip()

                self.nombre_jugador = partes[1].strip()

                frase = partes[2].strip().replace('.', '')
                palabras_raw = frase.split()
            else:
                self.id = "ERROR"
                self.nombre_jugador = "Error"
                palabras_raw = []

        else:
            partes = linea_limpia.split()
            self.id = partes[0].strip()

            self.nombre_jugador = nombre_jugador_default
            palabras_raw = partes[1:]


        self.idioma = self.id[:2].upper()
        
  
        self.palabras_lista = [p.upper() for p in palabras_raw]
        

        self.palabras_set = set(self.palabras_lista)
        self.marcadas = set()
        

        self.config = {
            'SP': {'filas': 5, 'cols': 5, 'libre': True, 'max_total': 24},
            'EN': {'filas': 3, 'cols': 5, 'libre': True, 'max_total': 14},
            'PT': {'filas': 4, 'cols': 5, 'libre': False, 'max_total': 20},
            'DT': {'filas': 2, 'cols': 5, 'libre': False, 'max_total': 10}
        }

    def marcar(self, palabra):
        if palabra in self.palabras_set:
            self.marcadas.add(palabra)

    def es_ganador(self):
        return len(self.marcadas) == len(self.palabras_set) and len(self.palabras_set) > 00

class BingoGame:
    def __init__(self):
        self.cartones = []
        self.palabras_cantadas = []
        self.rondas = []
        self.idioma_actual = None
        self.ganadores_ronda = []
        self.juego_terminado = False
        self.palabras_disponibles_sorteo = [] 
        self.jugadores_unicos = set()
        self.ids_registrados = set() # ¡NUEVO! Evita duplicados

    def agregar_cartones(self, contenido_archivo, nombre_jugador_externo):
        nuevos = []
        errores = 0
        duplicados = 0


        for linea in contenido_archivo:
            if linea.strip():
                try:
                    c = Carton(linea, nombre_jugador_externo)
                    
                    if c.idioma in REPOSITORIO_MASTER or True:
                        
                        
                        if c.id not in self.ids_registrados:
                            nuevos.append(c)
                            self.ids_registrados.add(c.id)
                            self.jugadores_unicos.add(c.nombre_jugador) 
                            # ------------------------
                            
                        else:
                            duplicados += 1
                    else:
                        errores += 1
                except:
                    errores += 1
        
        self.cartones.extend(nuevos)
        self.recalcular_rondas()
        # Retornamos 3 valores para control interno
        # Retornamos 3 valores para control interno
        return len(nuevos), errores, duplicados

    def recalcular_rondas(self):
        idiomas_presentes = list(set(c.idioma for c in self.cartones))
        if not self.idioma_actual and idiomas_presentes:
            random.shuffle(idiomas_presentes)
            self.rondas = idiomas_presentes
            self.iniciar_ronda(self.rondas[0])

    def iniciar_ronda(self, idioma):
        self.idioma_actual = idioma
        self.palabras_cantadas = []
        self.ganadores_ronda = []
        self.juego_terminado = False
        
        if idioma in REPOSITORIO_MASTER:
            self.palabras_disponibles_sorteo = REPOSITORIO_MASTER[idioma].copy()
            random.shuffle(self.palabras_disponibles_sorteo)
        else:
            self.palabras_disponibles_sorteo = []

    def extraer_palabra(self):
        if self.palabras_disponibles_sorteo:
            val = self.palabras_disponibles_sorteo.pop(0)
            self.cantar_palabra(val)
            return val
        return None

    def cantar_palabra(self, palabra):
        if not palabra or self.juego_terminado: return
        palabra = palabra.upper().strip()
        
        if palabra not in self.palabras_cantadas:
            self.palabras_cantadas.append(palabra)
        
        activos = [c for c in self.cartones if c.idioma == self.idioma_actual]
        ganadores = []
        
        for c in activos:
            c.marcar(palabra)
            if c.es_ganador():
                ganadores.append(c)
        
        if ganadores:
            self.ganadores_ronda = ganadores
            self.juego_terminado = True

    def siguiente_ronda(self):
        if len(self.rondas) > 1:
            self.rondas.pop(0)
            for c in self.cartones: 
                if c.idioma == self.rondas[0]: c.marcadas = set()
            
            self.iniciar_ronda(self.rondas[0])
            return True
        return False

# --- FRONTEND (STREAMLIT) --- LA CARA - DESAROLLADO POR ISSAC ALEXANDER MAZA Punine

if 'bingo' not in st.session_state:
    st.session_state.bingo = BingoGame()

game = st.session_state.bingo

# SIDEBAR: PANEL DE CONTROL DE DATOS
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055646.png", width=80)
    st.title("Gestión de Cartones")
    
    tab_archivo, tab_manual = st.tabs(["📂 Archivo TXT", "✍️ Manual"])
    
    with tab_archivo:
        uploaded_files = st.file_uploader(
            "Carga Masiva (.txt)", 
            type="txt", 
            accept_multiple_files=True
        )
        if st.button("Procesar Archivos"):
            if uploaded_files:
                total_nuevos = 0
                total_duplicados = 0
                for f in uploaded_files:
                    lines = f.getvalue().decode("utf-8").splitlines()
                    nombre_limpio = f.name.replace(".txt", "")
                    n, e, d = game.agregar_cartones(lines, nombre_limpio)
                    total_nuevos += n
                    total_duplicados += d
                
                if total_nuevos > 0:
                    st.success(f"¡{total_nuevos} cartones añadidos!")
                    time.sleep(1) # Pequeña pausa para leer
                    st.rerun()
                elif total_duplicados > 0:
                    st.warning(f"No se añadieron nuevos: {total_duplicados} repetidos.")
    
    with tab_manual:
        st.caption("Ingresa los datos (ID Palabras...):")
        manual_txt = st.text_area("Pegar cartón aquí", height=150)
        nombre_manual = st.text_input("Nombre del Jugador", value="Jugador_Manual")
        
        if st.button("Cargar Manual"):
            if manual_txt.strip():
                n, e, d = game.agregar_cartones(manual_txt.strip().splitlines(), nombre_manual)
                if n > 0:
                    st.success(f"¡{n} cartón cargado para {nombre_manual}!")
                    st.rerun()
                elif d > 0:
                    st.error("Error: Ese cartón (ID) ya existe.")
                else:
                    st.error("Error en formato o idioma desconocido.")

    st.divider()
    if game.cartones:
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Jugadores", len(game.jugadores_unicos))
        with col_m2:
            st.metric("Cartones", len(game.cartones))
            
        st.write(f"🗣️ **Ronda:** {game.idioma_actual}")
        
        if st.button("⚠️ Reiniciar Sistema", type="primary"):
            st.session_state.bingo = BingoGame()
            st.rerun()

# PANTALLA PRINCIPAL
st.title("🎱 Gran Bingo: Sala de Juego")

if not game.cartones:
    st.info("👋 Para comenzar, carga los cartones usando el menú lateral.")
    with st.expander("ℹ️ Ver Formato de Entrada Requerido"):
        st.code("SP102030 CASA VIDA TIEMPO DIA ...", language="text")
        st.write("Idiomas soportados: SP, EN, PT, DT.")

else:
    col_izq, col_der = st.columns([2, 1])

    with col_izq:
        st.subheader(f"Idioma Actual: {game.idioma_actual}")
        
        # PANTALLA GIGANTE
        if game.palabras_cantadas:
            ultima = game.palabras_cantadas[-1]
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="color: grey;">Palabra Cantada:</h3>
                <h1 style="color: #FF4B4B; font-size: 60px;">{ultima}</h1>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Esperando primera extracción...")

        # CONTROLES
        c1, c2 = st.columns([2, 1])
        with c1:
            restantes = len(game.palabras_disponibles_sorteo)
            btn_txt = "🎲 Extraer Automáticamente" if not game.juego_terminado else "Ronda Finalizada"
            
            if st.button(btn_txt, disabled=game.juego_terminado or restantes == 0, type="primary", use_container_width=True):
                game.extraer_palabra()
                st.rerun()
        
        with c2:
            man_input = st.text_input("Manual", placeholder="Escribir...", label_visibility="collapsed")
            if st.button("Cantar Manual") and man_input:
                 game.cantar_palabra(man_input)
                 st.rerun()

        
        st.caption(f"Palabras restantes en tómbola: {restantes}")
        
        if restantes == 0 and not game.juego_terminado:
             st.error("🚫 ¡Se acabaron las palabras de la tómbola y no hubo ganadores!")

        with st.expander("📜 Historial de esta ronda"):
            st.write(", ".join(game.palabras_cantadas[::-1]))

    # --- PANEL DE PARTICIPANTES ---
    with col_der:
        st.subheader("Estado de Jugadores")
        cartones_activos = [c for c in game.cartones if c.idioma == game.idioma_actual]
        
        if cartones_activos:
            data = []
            for c in cartones_activos:
                estado_txt = "🏆 GANADOR" if c.es_ganador() else "En juego"
                # Usamos el total real del cartón para el progreso
                total = len(c.palabras_set) 
                actual = len(c.marcadas)
                progreso = actual / total if total > 0 else 0
                
                data.append({
                    "Jugador": c.nombre_jugador,
                    "Cartón": c.id,
                    "Estado": estado_txt,
                    "Progreso": progreso
                })
            
            df = pd.DataFrame(data)
            df = df.sort_values(by=["Progreso"], ascending=False)
            
            st.dataframe(
                df, 
                hide_index=True,
                use_container_width=True,
                column_config={
                    "Progreso": st.column_config.ProgressColumn(
                        "Avance", min_value=0, max_value=1, format="%.2f%%"
                    )
                }
            )

    # --- ZONA DE VICTORIA (VISUALIZACIÓN CORREGIDA) ---
    if game.juego_terminado:
        st.divider()
        st.balloons()
        ganadores = game.ganadores_ronda
        
        if len(ganadores) > 1:
            st.warning(f"🔔 ¡EMPATE! Hay {len(ganadores)} ganadores simultáneos.")
        else:
            st.success(f"✨ ¡GANADOR: {ganadores[0].nombre_jugador}!")
            
        cols = st.columns(len(ganadores))
        for idx, winner in enumerate(ganadores):
            with cols[idx]:
                st.info(f"👤 {winner.nombre_jugador}\n🆔 {winner.id}")
                
                cfg = winner.config[winner.idioma]
                palabras = winner.palabras_lista.copy()
                
                # Insertar espacio libre
                centro = (cfg['filas'] * cfg['cols']) // 2
                if cfg['libre'] and len(palabras) >= centro:
                    palabras.insert(centro, "★ LIBRE ★")
                
                # Renderizar Grid - SIN SANGRÍA EN EL STRING PARA EVITAR ERROR DE CÓDIGO
                cells_html = ""
                for p in palabras:
                    es_marcada = (p in winner.marcadas or p == "★ LIBRE ★")
                    bg = "#d4edda" if es_marcada else "#f8f9fa"
                    border = "#155724" if es_marcada else "#ddd"
                    text_color = "#155724" if es_marcada else "#000000"
                    weight = "bold" if es_marcada else "normal"
                    
                    # Generamos cada celda en una sola linea para seguridad
                    cells_html += f"<div style='background:{bg}; border:2px solid {border}; color:{text_color}; font-weight:{weight}; font-size:11px; padding:4px; text-align:center; border-radius:4px; display:flex; align-items:center; justify-content:center; min-height:35px;'>{p}</div>"
                
                # Contenedor final sin sangrías peligrosas
                st.markdown(f"<div style='display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; margin-top:10px;'>{cells_html}</div>", unsafe_allow_html=True)
        
        st.divider()
        if len(game.rondas) > 1:
            if st.button("➡️ Siguiente Ronda (Cambiar Idioma)"):
                game.siguiente_ronda()
                st.rerun()
        else:
            st.success("🏁 Torneo Finalizado.")