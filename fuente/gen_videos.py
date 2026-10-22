# -*- coding: utf-8 -*-
"""Una pagina por video: como esta armado, donde esta el humor,
y las cinco versiones propuestas con las dos pistas separadas."""
import base64, io, json, os, subprocess

DIR = os.path.join(os.path.expanduser("~"), "Desktop", "BRAIN SYRUP", "videos", "LQ")
SITE = u"https://santiagotereso.github.io/brain-syrup/"
LOGO = json.load(io.open("_assets.json", encoding="utf-8"))["logo"]
SAL = "videos"

def tc(s):
    return u"%d:%04.1f" % (int(s) // 60, s % 60)

def frame(path, t, w=480):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", path, "-frames:v", "1",
                        "-vf", "scale=%d:-2" % w, "-q:v", "4", "-f", "image2",
                        "-vcodec", "mjpeg", "-"], capture_output=True)
    return u"data:image/jpeg;base64," + base64.b64encode(r.stdout).decode()

# ---------------------------------------------------------------- los videos
V = []

V.append(dict(
  slug="iphone-1960", n=5, dur=113.1, cortes=53, lineas=32,
  file="An iphone built with 1960s Tech. Guess how big_.mp4",
  titulo=u"An iPhone built with <span class='h1b'>1960s tech</span>",
  corto=u"An iPhone built with 1960s tech",
  tipo=u"Divulgación con gags visuales",
  resumen=u"Una escalada: el celular pasa de la mano al piso de un diner, de ahí a aplastar "
          u"una esquina de Nueva York, después a tapar Manhattan y termina del tamaño de Singapur.",
  beats=[
    ([0.5, 3.0], 0.0, 6.4,
     u"Yo what&rsquo;s up guys? For those who repeatedly asked, we&rsquo;re gonna build an iPhone with 1960s tech.",
     u"El presentador en el living, con el logo entrando arriba a la izquierda.",
     u"La promesa en seis segundos. No hay chiste todavía: hay contrato."),
    ([7.5, 12.5], 6.4, 16.0,
     u"The key idea here is compute versus space&hellip; &mdash;&iquest;What?",
     u"Un hombre de 1960 con un iPhone en la calle. Un forzudo levantando una roca en un supermercado "
     u"con la cara de Zuckerberg recortada al lado. COMPUTE y SPACE con fósforos y cinta métrica, "
     u"y un cubo de vidrio con forzudos apretados adentro.",
     u"El concepto es abstracto y lo resuelve con fuerza bruta: potencia = forzudo, espacio = cuánto lugar ocupa. "
     u"El cubo de forzudos apretados es la metáfora entera en una sola imagen."),
    ([17.5, 21.0], 16.0, 22.6,
     u"The IBM 7090 needed a whole room. It was a pretty impressive machine for that time.",
     u"Archivo en blanco y negro, con el presentador insertado adentro del plano. Cartel 1960 y las specs: "
     u"144 KB, 229.000 operaciones por segundo, 50.000 transistores.",
     u"Dato duro, servido rápido. Es el escalón que hace falta para que lo que viene tenga gracia."),
    ([23.3, 25.5], 22.6, 28.7,
     u"Now today an iPhone 18 fits in your hand and has way more compute. &mdash;Okay.",
     u"Corte a un inodoro. El iPhone está adentro, reproduciendo al presentador, con el cartel "
     u"100,000,000 times faster. Después, un cuadro renacentista con los ojos cerrados.",
     u"<b>El mejor chiste visual del video.</b> La frase es solemne y la imagen es un celular en un inodoro. "
     u"Nadie lo nombra, nadie lo explica, y el &laquo;Okay&raquo; con la cara del cuadro hace de risa enlatada."),
    ([34.0, 38.5], 28.7, 41.4,
     u"Now in 1960 standards, an iPhone would occupy definitely much more space. &mdash;But like, how much more space?",
     u"El celular cae al piso de damero de un diner y empieza a crecer hasta aplastar una esquina de Nueva York "
     u"con gente corriendo. Cartel How much More?",
     u"Acá arranca la escalada, que es la estructura que sostiene todo el medio del video."),
    ([43.5, 51.5], 41.4, 53.3,
     u"Well the answer is 89 square kilometers. Which is&hellip; nope, even bigger than that. It&rsquo;s one and a half Manhattans.",
     u"89 SQUARE KM sobre la ciudad. El celular tapando el cielo entre los edificios. Gente mirando para arriba. "
     u"Manhattan entero desde el aire con el celular encima.",
     u"El <b>&laquo;nope&raquo;</b> es el chiste: se corrige a sí mismo en el aire, como si el número se le "
     u"hubiera quedado corto mientras lo decía. Es el mejor segundo del video."),
    ([57.5, 63.0], 53.3, 66.8,
     u"And if we upgrade to one terabyte, it&rsquo;s the size of Singapore&hellip; what once required a computer "
     u"the size of Godzilla can be done with the size of a sesame seed.",
     u"Singapur explotando bajo el celular. Un Godzilla inflable sobre Ciudad de México que se achica hasta "
     u"quedar del tamaño de una semilla, con un contador: Power vs Size 0% &rarr; 99,9963%.",
     u"La única metáfora del video que se entiende sin audio. El contador subiendo mientras el bicho se "
     u"achica hace el trabajo solo."),
    ([70.5, 77.5], 66.8, 85.0,
     u"in 40 years your phone power should multiply by approximately a million&hellip; There are dozens of objections "
     u"for why it&rsquo;s impossible&hellip; But if you consider quantum computing&hellip;",
     u"Cartel 2060: un tipo de traje marrón sepultado por una avalancha de celulares. Cuatro científicos de "
     u"época en ráfaga, uno por objeción. Un punk con mohawk tipeando en una laptop con QUANTUM COMPUTING en verde.",
     u"El gag es el ritmo: cuatro tomas en cinco segundos, cada una con su cartel. Nadie entiende las leyes y no hace falta. "
     u"Y el contraste final: la ciencia más difícil la explica el personaje menos probable."),
    ([90.0, 96.5], 85.0, 100.0,
     u"&mdash;Is that level of compute beneficial for humanity? &mdash;Yes, man. Don&rsquo;t worry. Absolutely.",
     u"Tres Terminators sentados en sillones de panel de televisión, con público. Corte al presentador tranquilo. "
     u"Cartel KILLER ROBOTS? con una cara de susto de un retrato antiguo.",
     u"<b>El mejor chiste conceptual.</b> La pregunta es sobre si conviene tanta potencia, la imagen son tres robots "
     u"asesinos en un panel de TV, y la respuesta es &laquo;sí, tranquilo&raquo;. El chiste vive entero en el corte."),
    ([108.0], 100.0, 113.1, u"&mdash;",
     u"Archivo en blanco y negro de gente corriendo de un OVNI con SUBSCRIBE en rojo. Cierre con el logo.",
     u"Trece segundos sin diálogo. En el video largo cierra; en un short es tiempo muerto."),
  ],
  humor=[
    u"<b>El chiste nunca está en lo que dice.</b> El texto es siempre información seria en tono de divulgación. "
    u"La gracia la pone la imagen que no corresponde.",
    u"<b>La estructura es una escalada.</b> Cada escalón necesita el anterior, y por eso los shorts que sacan dos "
    u"escalones pegados funcionan mejor que los que sacan uno suelto.",
    u"<b>Se corrige a sí mismo.</b> El &laquo;nope, even bigger than that&raquo; hace que el número parezca descubierto en vivo.",
    u"<b>Los personajes son disfraces de una idea y ninguno habla.</b> El forzudo es la potencia, el punk es la "
    u"computación cuántica. Por eso se recortan y se pegan en cualquier orden.",
  ],
  shorts=[
    (u"El iPhone de 1960 mide una Manhattan y media", [[0.0, 6.4], [41.4, 45.1], [50.9, 53.3]],
     [[0.5, 3.4], [3.6, 6.3], [43.0, 46.5], [50.9, 53.3]], [43.5, 51.5],
     u"La promesa y el remate pegados, sin el medio. Pregunta, número, imagen.",
     u"iPhone con tecnologia de 1960: una Manhattan y media. #brainsyrup #tech"),
    (u"Un celular en el inodoro", [[16.0, 27.6]],
     [[17.2, 20.4], [20.5, 22.5], [22.8, 24.2], [24.2, 27.6]], [17.5, 23.3],
     u"Casi un recorte directo porque ya está bien montado. Entra un segundo más tarde y sale antes del &laquo;Okay&raquo;.",
     u"La computadora de 1960 ocupaba una habitacion entera. #brainsyrup #tech"),
    (u"De Godzilla a una semilla de sésamo", [[59.4, 66.8]],
     [[61.4, 63.5], [63.5, 65.4], [65.6, 66.9]], [63.0],
     u"El más visual de los cinco. Se entiende con el sonido apagado, que es lo que lo hace funcionar en el feed.",
     u"Lo que antes necesitaba una computadora del tamano de Godzilla. #brainsyrup #tech"),
    (u"Las cuatro razones por las que es imposible", [[72.5, 85.0]],
     [[73.3, 74.7], [74.8, 76.2], [76.3, 77.7], [77.8, 79.2], [79.4, 82.4], [82.5, 85.0]], [77.5],
     u"Acá está el montaje rápido: seis tomas sobre una sola tirada de voz, y el punk de remate.",
     u"Hay docenas de razones por las que esto es imposible. #brainsyrup #tech"),
    (u"&iquest;Es bueno para la humanidad?", [[88.9, 93.9]],
     [[88.8, 91.5], [92.4, 93.9], [96.0, 97.2]], [90.0, 96.5],
     u"El chiste vive en el corte: la pregunta sobre los robots, los robots, y la respuesta despreocupada.",
     u"Es bueno para la humanidad? Si, tranquilo. #brainsyrup #ai"),
  ]))

V.append(dict(
  slug="algo", n=4, dur=121.5, cortes=0, lineas=49,
  file="They understand The Internet. Apparently you don't.mp4",
  titulo=u"They understand <span class='h1b'>The Internet</span>",
  corto=u"They understand The Internet",
  tipo=u"Cortometraje animado, sátira",
  resumen=u"El algoritmo como jefe. ALGO, un ejecutivo con cara de sapo, recibe creadores en su oficina "
          u"y los aprueba o los tira por un tubo de gas verde. Es el único de los cinco que no explica nada: actúa.",
  beats=[
    ([0.0, 1.3], 0.0, 5.0,
     u"You&rsquo;re uninteresting. Boring. Don&rsquo;t you get it? &mdash;Can you explain? &mdash;No. Next.",
     u"Primer plano de ALGO, un ejecutivo gordo con cara de sapo. El cartel BORING en letras doradas "
     u"tapa su cara. Tres botones sobre el escritorio: rojo, amarillo, verde.",
     u"<b>Cinco segundos y ya entendés todo.</b> No hay narrador, no hay explicación. El mejor arranque "
     u"de los cinco videos."),
    ([7.8, 15.6], 5.0, 13.0,
     u"Meet Algo, your boss. &mdash;I specialize in ancient Japan. &mdash;Well, they all look the same.",
     u"Cartel MEET ALGO entre humo. Una chica flaca de vestido negro entre jarrones chinos, presentando su trabajo.",
     u"El remate llega antes de que termines de escuchar la frase de ella. Es la estructura de todo el corto: "
     u"alguien se esfuerza, ALGO lo descarta en cuatro palabras."),
    ([18.2, 22.1], 13.0, 24.0,
     u"Show your talents, will you? &mdash;Oh, yes, I&rsquo;m sorry. &mdash;And maybe the camera higher. Yeah, yeah, all that.",
     u"Ella se baja el escote mientras él mira sin mirar. ALGO señala con el dedo.",
     u"El chiste más incómodo del corto y el más preciso: no dice nada explícito, lo dice todo con "
     u"un gesto y un &laquo;yeah, yeah, all that&raquo;."),
    ([33.8, 42.9], 24.0, 39.0,
     u"Watch your tutorial, will you? Get those Chinese parts out of here. We need to have a serious safety conversation.",
     u"Tres oficinistas idénticas entran por una puerta blindada con símbolo de riesgo biológico. "
     u"Un caño escupe gas verde. Las siluetas se disuelven detrás del vidrio.",
     u"El corto pasa de la comedia de oficina al horror sin cambiar de tono. Nadie reacciona."),
    ([45.5, 52.0], 39.0, 56.0,
     u"New button is just great, isn&rsquo;t it? &mdash;Yes, sir. &mdash;Need to talk about something. I like this guy. "
     u"&mdash;Colombians. What are they up to?",
     u"ALGO festeja el botón nuevo. En una pantalla aparece un conspiranoico con los ojos desorbitados "
     u"gritando frente a un micrófono, rodeado de recortes.",
     u"&laquo;I like this guy&raquo; dicho sobre el personaje más delirante del corto es la tesis entera del video."),
    ([58.5, 66.3], 56.0, 72.0,
     u"&hellip;the detector node will start beatboxing. It has proven an increase in engagement of 0.18% in users "
     u"16 to 17 and a half. And if you break it down further by session length, the data actually compounds.",
     u"Un hombre altisimo y flaquísimo, con cartel &laquo;Parker Pivotson, Founder&raquo;, explicando con "
     u"total convicción. Dos mujeres sosteniendo un panel lleno de gráficos sin sentido.",
     u"La jerga de producto llevada al absurdo con la cara más seria posible. El 0,18% en usuarios "
     u"&laquo;de 16 a 17 y medio&raquo; es el detalle que lo hace."),
    ([75.5, 84.0], 72.0, 88.0,
     u"&mdash;I just want to thank you guys for such a unique opportunity. &mdash;You got him recorded? &mdash;Yeah. "
     u"&mdash;What about your things? All good? &mdash;Yeah. &mdash;Family? &mdash;Yeah.",
     u"Los guardaespaldas con anteojos negros. Un chico de buzo violeta en el pasillo. Silencios largos entre frases.",
     u"La conversación social más vacía posible, grabada &laquo;por las dudas&raquo;. El timing de los "
     u"silencios es el chiste."),
    ([89.0, 104.0], 88.0, 104.0,
     u"&mdash;Look, I kind of gotta&hellip; &mdash;Yeah. &mdash;I&rsquo;ll leave you to it. &mdash;Damn, that was long. "
     u"Where is my Colombia guy?",
     u"Dos guardaespaldas apuntando a cámara. El chico del buzo violeta mirando para arriba. "
     u"Un cartel SUBSCRIBE aparece en medio de la escena.",
     u"El SUBSCRIBE metido adentro de la ficción, como un objeto más de la oficina."),
    ([93.0, 97.0], 104.0, 112.0,
     u"The Colombian situation, it&rsquo;s bigger than any of us. Once you see it, there&rsquo;s no going back. "
     u"They don&rsquo;t want you to know how deep this goes, but I found the pattern.",
     u"El conspiranoico a pleno, gritando en su estudio lleno de papeles y chinches.",
     u"Veinte segundos de delirio sin información. Es el personaje que ALGO aprobó."),
    ([106.0, 111.0], 112.0, 121.5,
     u"Hey, nobody reads those long texts. Don&rsquo;t you know that? Everyone&rsquo;s gone by now.",
     u"Cartelones dorados: A SINGLE DAY PRODUCES 500 YEARS OF SOCIAL MEDIA CONTENT. You only consume 0.00005%. "
     u"Un cubo de partículas doradas que se deshace. DECIDED BY HIM, sobre ALGO encogiéndose de hombros.",
     u"<b>El remate del corto y el único momento con dato.</b> Y rompe la cuarta pared: te dice que vos "
     u"tampoco estás leyendo esto."),
  ],
  humor=[
    u"<b>Nadie explica nada.</b> Es el único de los cinco que es ficción pura. Por eso cada pedazo "
    u"funciona solo, sin contexto: es el material más fácil de cortar de todo el canal.",
    u"<b>El timing es de comedia de oficina.</b> Los silencios incomodos valen tanto como las frases. "
    u"Cortar justo después del silencio, no antes.",
    u"<b>La violencia nunca se nombra.</b> El gas verde, las siluetas, el &laquo;you got him recorded?&raquo;. "
    u"Todo pasa en el fondo del plano mientras alguien habla de otra cosa.",
    u"<b>Tiene un dato guardado para el final.</b> Las placas de los 500 años y el 0,00005% son el único "
    u"momento informativo, y llegan cuando ya te ganaron.",
  ],
  shorts=[
    (u"Tu jefe es el algoritmo", [[0.0, 5.2]], [[0.0, 1.2], [1.2, 2.6], [3.3, 4.4], [4.6, 5.3]], [0.0, 7.8],
     u"Los primeros cinco segundos tal cual están. No se puede mejorar un arranque así.",
     u"Tu jefe es el algoritmo. #brainsyrup #animation"),
    (u"Se ven todos iguales", [[9.5, 23.5]], [[9.5, 13.0], [13.2, 16.0], [17.5, 20.0], [20.5, 23.5]], [15.6, 18.2],
     u"La presentación de ella, el descarte en cuatro palabras y el pedido incómodo, pegados.",
     u"Me especializo en Japon antiguo. #brainsyrup #animation"),
    (u"0,18% de engagement", [[55.5, 68.0]], [[56.5, 59.0], [59.2, 62.5], [63.0, 66.3], [66.5, 68.0]], [58.5, 66.3],
     u"La jerga de producto con cara seria. Funciona sola porque no necesita saber quién es nadie.",
     u"Un aumento del 0,18% en usuarios de 16 a 17 y medio. #brainsyrup #animation"),
    (u"El gas verde", [[24.0, 33.0]], [[33.5, 36.0], [36.2, 39.0], [41.5, 44.0], [48.0, 50.5]], [33.8, 42.9],
     u"Acá cruzo pistas a propósito: la voz de la charla de seguridad sobre la imagen del tubo de gas, "
     u"que en el corto vienen separadas.",
     u"Tenemos que tener una conversacion seria sobre seguridad. #brainsyrup #animation"),
    (u"500 años de contenido por día", [[112.0, 119.5]],
     [[97.0, 99.5], [105.0, 108.0], [108.2, 111.0], [111.2, 113.5]], [106.0, 111.0],
     u"El dato al final, con el conspiranoico de entrada para que el remate pegue más fuerte.",
     u"Un solo dia produce 500 anos de contenido. Vos consumis el 0,00005%. #brainsyrup"),
  ]))

V.append(dict(
  slug="super-seniors", n=3, dur=269.9, cortes=0, lineas=41,
  file="SUPER SENIORS. Bizarre animation. You've never felt THIS young.mp4",
  titulo=u"SUPER <span class='h1b'>SENIORS</span>",
  corto=u"SUPER SENIORS",
  tipo=u"Cortometraje animado, acción",
  resumen=u"Un geriátrico llamado Lake Decline. Los robots domésticos se rebelan y atacan. Los viejos "
          u"resultan tener superpoderes, y cada superpoder es una dolencia de la vejez.",
  beats=[
    ([0.0, 11.6], 0.0, 12.0,
     u"Now the question everybody&rsquo;s asking: how fast can they fold your laundry? &mdash;She is beautiful. "
     u"&mdash;Um, the television is in that direction.",
     u"Una presentadora de noticias en un televisor viejo. Un abuelo mirando para el lado equivocado.",
     u"Dos chistes en diez segundos y ninguno se explica: la pregunta estupida de la TV, y el viejo "
     u"enamorado de una pared."),
    ([14.5, 24.0], 12.0, 34.0,
     u"I don&rsquo;t like it, and I&rsquo;m changing your channel. &mdash;Not on my watch.",
     u"Una mano temblorosa estirandose hacia el control remoto sobre un mantel floreado. Lentes que se "
     u"encienden en rojo. Una enfermera gritando.",
     u"El duelo por el control remoto filmado como un western. La escalada visual es toda la gracia."),
    ([37.7, 46.4], 34.0, 62.0,
     u"We have a visitor. &mdash;Timothy, you came back. That takes courage. &mdash;Um, I&rsquo;m actually Floyd, "
     u"and that&rsquo;s my grandpa. &mdash;Floyd, I can hear you.",
     u"Un chico pelirrojo con anteojos cuadrados en la puerta. Los viejos lo confunden con otro.",
     u"El malentendido se sostiene porque nadie lo corrige del todo. &laquo;Floyd, I can hear you&raquo; "
     u"dicho por alguien que claramente no escucha nada."),
    ([69.6, 78.3], 62.0, 90.0,
     u"To the underground bunker. &mdash;Robots are refusing domestic work and attacking humans.",
     u"Robots rojos doblando ropa, y después destrozando un barrio suburbano. Pantallas con una mosca gigante.",
     u"El giro de género: de comedia de geriátrico a película de acción, sin transición."),
    ([84.0, 101.0], 90.0, 120.0,
     u"We&rsquo;ve seen this kind of evil before. It&rsquo;s El Mosca. He must be stopped. "
     u"&mdash;Um, excuse me, can you tell me what&rsquo;s happening?",
     u"El villano es una mosca con traje. Un cartel: Lake Decline Retirement Home. Una central nuclear "
     u"al fondo del paisaje.",
     u"El villano se llama El Mosca y nadie lo discute. El chico sigue preguntando qué pasa y nadie le contesta."),
    ([104.0, 118.0], 120.0, 140.0,
     u"There&rsquo;s a secret about our residents. Their elder challenges have turned into superpowers. "
     u"Indestructible muscle stiffness. Unlimited skin deployment. Telekinetic disorientation. Time trouble. Immortality.",
     u"Cada viejo demuestra su poder: uno rígido como una tabla, una abuela estirando su propia piel "
     u"como una capa, otra levitando cosas sin querer, uno que se teletransporta por confusión.",
     u"<b>El mejor pedazo del corto.</b> Cada superpoder es una dolencia real de la vejez, dicha con nombre "
     u"de cómic. Se entiende sin audio y se puede cortar en cinco piezas distintas."),
    ([139.0, 166.0], 140.0, 200.0, u"&mdash;",
     u"La abuela voladora con la capa de piel. El viejo rígido usado como ariete contra los robots. "
     u"Un sillón de ruedas volando por los aires.",
     u"Un minuto entero de acción sin diálogo. Material libre para cualquier short que necesite imágenes."),
    ([190.0, 205.0], 200.0, 215.0,
     u"Not so fast, Super Seniors. &mdash;Rocko, attack. &mdash;You got it.",
     u"La mosca gigante en primer plano, con dientes. El chico señalando.",
     u"El villano habla como villano de dibujo animado de los ochenta, que es exactamente el punto."),
    ([198.0, 220.0], 215.0, 240.0,
     u"&mdash;Sorcery! &mdash;Look at what you&rsquo;ve done, you super fools! This is not over!",
     u"Una abuela rompiendo un robot de una patada en el aire. Otra haciendo volar un plato.",
     u"&laquo;Sorcery!&raquo; dicho por un viejo que vio a alguien usar una computadora."),
    ([222.0, 240.0], 240.0, 269.9,
     u"Thanks. Um, I just want to say, I&rsquo;m really proud of my grandpa.",
     u"El chico en el pasto, de la mano del abuelo. Un buzón. El logo SUPER SENIORS en estilo cómic. "
     u"Después, placas del festival y del making of.",
     u"El final sincero después de cuatro minutos de robots. Funciona porque no se burla."),
  ],
  humor=[
    u"<b>Cada superpoder es una dolencia.</b> Rigidez muscular indestructible, piel ilimitada, "
    u"desorientación telequinética. Es la idea entera del corto y la que mejor viaja sola.",
    u"<b>Nadie le explica nada al chico.</b> Pregunta tres veces qué está pasando y siempre le contestan otra cosa.",
    u"<b>El tono de los viejos nunca cambia.</b> Hablan igual de una invasión robótica que del canal de televisión.",
    u"<b>Ojo con la marca de agua.</b> Todo el video tiene el laurel del festival arriba a la derecha, "
    u"y en 9:16 va a quedar adentro del cuadro. Para los shorts conviene un master limpio o encuadrar hacia la izquierda.",
  ],
  shorts=[
    (u"Sus dolencias son superpoderes", [[102.5, 120.0]],
     [[103.0, 106.0], [106.2, 109.5], [109.7, 112.5], [112.7, 115.5], [115.7, 120.0]], [104.0, 118.0],
     u"El pedazo más fuerte del corto y el que mejor funciona solo. Cinco poderes, cinco tomas, sin contexto.",
     u"Rigidez muscular indestructible. #brainsyrup #animation"),
    (u"&iquest;Qué tan rápido doblan la ropa?", [[0.0, 6.0]],
     [[0.0, 2.8], [3.0, 5.0], [69.6, 72.5]], [0.0, 69.6],
     u"La pregunta de la presentadora sobre la imagen de los robots doblando ropa, que en el corto llegan "
     u"un minuto después. Cruzar las pistas es lo que arma el chiste.",
     u"La pregunta que todos se hacen. #brainsyrup #animation #robots"),
    (u"Timothy, volviste", [[34.0, 48.5]], [[36.5, 40.0], [40.2, 43.5], [43.7, 46.5], [46.7, 48.5]], [37.7, 46.4],
     u"El malentendido completo, con el remate del abuelo que escucha todo.",
     u"Timothy, volviste. Eso toma coraje. #brainsyrup #animation"),
    (u"Se llama El Mosca", [[85.0, 100.0]], [[78.0, 81.0], [84.0, 87.0], [87.2, 90.5], [96.0, 100.0]], [84.0, 101.0],
     u"La revelación del villano con las imágenes de los robots destruyendo el barrio.",
     u"Hemos visto este tipo de maldad antes. #brainsyrup #animation"),
    (u"Estoy orgulloso de mi abuelo", [[240.0, 248.0]],
     [[222.0, 225.0], [233.0, 236.0], [240.0, 244.0], [244.2, 248.0]], [222.0, 240.0],
     u"El cierre. Es el único de los cinco que no busca risa, y por eso conviene tenerlo.",
     u"Estoy muy orgulloso de mi abuelo. #brainsyrup #animation"),
  ]))

V.append(dict(
  slug="miedo", n=2, dur=563.8, cortes=0, lineas=103,
  file="Why Are People Afraid of This_.mp4",
  titulo=u"Why Are People <span class='h1b'>Afraid of This?</span>",
  corto=u"Why Are People Afraid of This?",
  tipo=u"Ensayo con personajes",
  resumen=u"Nueve minutos sobre el miedo, con el presentador, un extraterrestre de plastilina llamado Greg "
          u"y una ardilla. Pasa de la lista de fobias absurdas a la idea del &laquo;yo imaginario&raquo; y "
          u"termina en una diatriba contra la preocupación.",
  beats=[
    ([0.0, 14.0], 0.0, 30.0,
     u"Hey, something I need to tell you. &mdash;Sure, yeah. Tell me&hellip; &mdash;Um, I mean, that works for like "
     u"a &laquo;can you trust your insect girlfriend&raquo; episode.",
     u"Una cena romántica. La chica se saca la cara y abajo hay un insecto mecánico. Cartel FEAR, "
     u"WHAT IS IT REALLY?",
     u"Abre con un sketch de terror y lo desarma enseguida con un comentario de producción. El canal "
     u"se ríe de su propio recurso antes de que lo hagas vos."),
    ([49.0, 56.0], 30.0, 82.0,
     u"It seems that when we say fear, we actually refer to multiple things. Scares. Panic. Paralysis. "
     u"Paranoia. And our special guest of today, worry.",
     u"Un restaurante elegante donde todo se va deshaciendo. Una señora con cámara. Una neurona gigante.",
     u"La enumeración con imágenes distintas para cada palabra. Es el formato que más se repite en el video."),
    ([84.0, 112.0], 82.0, 110.0,
     u"You can fear almost anything. Really? &mdash;Beards. Balloons. Belly buttons. Flutes. Jello. Bald people. "
     u"Paper. Work. And knees.",
     u"Una lista de fobias con su nombre técnico en pantalla: Pogonophobia sobre una barba gigante, "
     u"Papyrophobia sobre un Godzilla hecho de papel.",
     u"<b>El mejor pedazo para cortar de todo el video.</b> Nueve imágenes en veinte segundos, cada una con "
     u"su palabra. Es una lista, y las listas viajan solas."),
    ([105.0, 112.0], 110.0, 125.0,
     u"No, but really. Knees? How can you fear knees? &mdash;All people are different. You&rsquo;re afraid of duct tape. "
     u"&mdash;I&rsquo;m not.",
     u"Greg, el extraterrestre verde, discutiendo con el presentador.",
     u"El remate de la lista: el que se burla resulta tener la fobia más rara. Y lo niega."),
    ([161.0, 196.0], 125.0, 200.0,
     u"Fear is a brain signal telling us something is wrong&hellip; Fight or flight. And a special third participant. Freeze.",
     u"Una ardilla con paracaídas. Una cueva. Una explosión. El presentador comiendo semillas con dientes de ardilla.",
     u"La parte más didáctica. Visualmente generosa pero conceptualmente conocida: es la que menos "
     u"material de short deja."),
    ([189.0, 231.0], 200.0, 240.0,
     u"Introducing the imaginary you. &mdash;Hey! &mdash;Okay, sorry, sorry. Now close your eyes and think of a "
     u"person you know. Add another one from your memory who never met the first. Now place them somewhere impossible.",
     u"Cartel THE IMAGINARY YOU. Dos personas corriendo por un paisaje de hielo irreal. Aunt Celine en un gimnasio.",
     u"<b>El único momento interactivo del video.</b> Te pide que cierres los ojos y hagas algo. "
     u"Eso en un short es oro: obliga a quedarse."),
    ([224.0, 245.0], 240.0, 290.0,
     u"Supermarket guy should have been nicer. &mdash;Imagination is a superpower. Allison imagines her future "
     u"as a respected&hellip; &mdash;Who did this horrendous abomination? &mdash;Sorry, it&rsquo;s just that you&rsquo;re too gassy.",
     u"Allison, arquitecta imaginaria. Un edificio borroso. Una oficina.",
     u"El chiste de la flatulencia metido en medio de una explicación de psicología, sin aviso."),
    ([287.0, 329.0], 290.0, 345.0,
     u"England needed Harry Kane&hellip; Your imaginary you can be shared with many people. A collective imagination, "
     u"which makes the fear even worse.",
     u"El Mundial de Qatar 2022. Un pub en Birmingham. Hinchas ingleses. Un cristal rojo que dice "
     u"&laquo;we are better than France&raquo;.",
     u"El ejemplo más arriesgado y el mejor: el penal de Harry Kane como caso de imaginación colectiva."),
    ([343.0, 350.0], 345.0, 360.0,
     u"Now, to explain the subconscious, Harry Kane. Hey, Harry. &mdash;Mmm, I think you&rsquo;re muted. You&rsquo;re muted.",
     u"Una videollamada con el presentador, Greg y un recuadro.",
     u"<b>El chiste más compartible del video.</b> Todo el mundo vivió esa escena."),
    ([371.0, 420.0], 360.0, 440.0,
     u"Dulce de leche makes me sad&hellip; What is normalization? Any repeated experience as a child shapes your "
     u"definition of normal&hellip; See your fear as an investment. You don&rsquo;t fear the worst scenario. "
     u"You fear what you are used to fear.",
     u"Greg comiendo helado. Una familia de picnic con conos de tránsito en la cabeza. Un cartel: "
     u"YOU ARE USED TO FEAR.",
     u"Los conos de tránsito en la cabeza explican normalización mejor que la definición."),
    ([434.0, 470.0], 440.0, 480.0,
     u"Worry is a combination of logic and fear&hellip; You never worry at the right time. If a problem has a solution, "
     u"don&rsquo;t worry. If a problem has no solution, then don&rsquo;t worry.",
     u"Un hombre corriendo dentro de una rueda de hamster industrial. WORRY e INACTION dándose la mano. "
     u"Un auto en llamas.",
     u"<b>La frase más citable del canal.</b> Es un proverbio, está bien dicho y dura doce segundos."),
    ([463.0, 500.0], 480.0, 563.8,
     u"By all means, destroy worry, murder worry, and annihilate worry&hellip; Yes, fear can be a good thing. "
     u"Especially when we learn to face what we are scared of&hellip; because you can rewrite your story.",
     u"Un ejército de mercenarios ochentosos. Una mujer haciendo cerámica. Un hombre con la cabeza "
     u"metida en una cortina. Al final: I am not Harry Kane, and I do not approve this message.",
     u"Cierra con el descargo legal como chiste. El último minuto es el más emotivo y el menos cortable."),
  ],
  humor=[
    u"<b>Hay dos registros y el video salta entre ellos.</b> La explicación seria la lleva el presentador; "
    u"Greg, el extraterrestre, interrumpe con lo absurdo. Para un short conviene llevarse los dos, nunca uno solo.",
    u"<b>Las listas son lo más cortable.</b> Las fobias, los tipos de miedo, los tres estados. "
    u"Cada una es un short sin tocar nada.",
    u"<b>El video se ríe de sí mismo.</b> El sketch de la novia insecto lo desarma el propio personaje "
    u"a los quince segundos.",
    u"<b>Tiene una frase hecha adentro.</b> Lo de que si el problema tiene solución no te preocupes y si no "
    u"la tiene tampoco es un proverbio viejo, pero dicho ahí funciona como remate.",
  ],
  shorts=[
    (u"Se le puede tener miedo a cualquier cosa", [[82.0, 106.0]],
     [[82.0, 86.0], [86.5, 90.0], [90.5, 94.0], [94.5, 98.0], [98.5, 102.0], [102.2, 106.0]], [84.0, 112.0],
     u"La lista de fobias completa. Es el short más obvio del video y el que más lejos va a llegar.",
     u"Barbas. Globos. Ombligos. Flautas. Gelatina. Rodillas. #brainsyrup #miedo"),
    (u"Creo que estás muteado", [[342.0, 352.0]], [[343.0, 346.5], [346.7, 350.0], [350.2, 352.5]], [343.0],
     u"Diez segundos, un chiste universal, y no necesita nada del resto del video.",
     u"Para explicar el subconsciente, Harry Kane. #brainsyrup #miedo"),
    (u"Si tiene solución, no te preocupes", [[437.0, 452.0]],
     [[434.0, 438.0], [438.2, 442.0], [442.2, 446.0], [446.2, 452.0]], [434.0, 470.0],
     u"El proverbio con las imágenes de la rueda de hamster y el auto en llamas.",
     u"Si un problema tiene solucion, no te preocupes. Si no la tiene, tampoco. #brainsyrup"),
    (u"Cerrá los ojos", [[195.0, 215.0]], [[189.0, 193.0], [196.0, 200.0], [205.0, 210.0], [210.2, 215.0]], [189.0, 231.0],
     u"El ejercicio de imaginación. Es el único pedazo que le pide algo al que mira, y eso retiene.",
     u"Cerra los ojos y pensa en alguien que conozcas. #brainsyrup #miedo"),
    (u"El tipo del supermercado", [[222.0, 232.0]], [[224.0, 227.0], [227.2, 230.0], [230.2, 233.0]], [224.0, 245.0],
     u"El corte más corto de los cinco. Funciona por lo inesperado de la frase.",
     u"El tipo del supermercado deberia haber sido mas amable. #brainsyrup"),
  ]))

V.append(dict(
  slug="gravedad", n=1, dur=702.9, cortes=0, lineas=121,
  file="Gravity undo_ Most will last under a minute.mp4",
  titulo=u"Gravity <span class='h1b'>undo</span>",
  corto=u"Gravity undo",
  tipo=u"Ensayo con personajes",
  resumen=u"Casi doce minutos sobre qué pasaría si la gravedad desapareciera. El más largo y el más "
          u"estructurado: va de la ley de Newton a una extinción masiva, y termina con una buzo científica "
          u"como última humana viva.",
  beats=[
    ([0.0, 24.0], 0.0, 20.0,
     u"Gravity. A law that is certainly easy to take for granted. &mdash;Mmm, I&rsquo;m not sure I agree with you "
     u"there, man. I appreciate gravity, like, every morning.",
     u"Cartel GRAVITY, OR THE LACK OF IT. Un hombre cayendo en un campo. Un perro flotando sobre una ciudad.",
     u"Greg contradice al presentador en la segunda línea. La dinámica de los dos queda establecida enseguida."),
    ([32.0, 40.0], 20.0, 50.0,
     u"If there was a knob that controlled gravity, just the smallest tweak would disrupt all life on Earth&hellip; "
     u"&mdash;Um, weird.",
     u"Una perilla metálica que va de MIN a MAX con el 100% marcado. Gente flotando en círculo sobre un patio. "
     u"Una mujer flotando entre los techos.",
     u"La perilla es el recurso central del video: convierte una ley física en algo que se puede tocar."),
    ([39.0, 47.0], 39.0, 53.0,
     u"Now the question in everyone&rsquo;s mind, who dies first? &mdash;Who dies last?",
     u"Dos preguntas en pantalla, una detrás de la otra.",
     u"<b>Las dos preguntas que sostienen once minutos.</b> Todo el video es la respuesta a esas dos líneas, "
     u"y por eso son el mejor arranque para un short."),
    ([56.0, 104.0], 53.0, 130.0,
     u"Newton&rsquo;s law of universal gravitation&hellip; every mass attracts every other mass. The object with more "
     u"mass pulls harder&hellip; The human body is a direct consequence of gravity.",
     u"Un sumo flotando en el espacio en posición de loto. Una pila de sumos. Cuerpos humanos deformados "
     u"por distintas gravedades.",
     u"La masa explicada con sumos. Es literal, es tonto, y se entiende al instante."),
    ([144.0, 176.0], 130.0, 195.0,
     u"Every flying animal is pushing air away to move&hellip; without air, you cannot actually push yourself in any "
     u"direction. Unless, uh, force propels you into motion. &mdash;This is great science.",
     u"Un perro saliendo despedido de la puerta de un avión. Un astronauta a la deriva. Pantallas de cálculos.",
     u"El cálculo de que el viaje duraría 970 millones de años, rematado con el &laquo;this is great science&raquo; "
     u"de Greg, que es el comentario del espectador."),
    ([150.0, 166.0], 195.0, 230.0,
     u"The first five seconds, pressure collapses. You try to breathe, but there&rsquo;s nothing pushing the air in. "
     u"That 15 seconds, even if there&rsquo;s air in your lungs, it&rsquo;s useless.",
     u"Unos pulmones con rayos. Un hombre de amarillo tirado en el piso. Un cartel BREATHLESS LEAGUE con "
     u"un sello TOO SLOW sobre una fila de cuerpos.",
     u"La cuenta regresiva por segundos. Es el recurso que mejor retiene de todo el video."),
    ([166.0, 188.0], 230.0, 290.0,
     u"&mdash;I mean, who dies like that? &mdash;Just wasn&rsquo;t a big fan of his. &mdash;But perhaps unexpectedly, "
     u"suffocation is not the fastest cause of death. Inertia is.",
     u"Un motociclista en el bosque. Un hombre sin remera con NO RAGRETS tatuado en el pecho.",
     u"El chiste de Greg sobre el muerto, dicho al pasar, es el tipo de línea que el canal deja caer "
     u"sin subrayar."),
    ([223.0, 232.0], 290.0, 330.0,
     u"And what can kill you faster than inertia? &mdash;Muscle memory. Humans spend years fine-tuning their "
     u"movements against gravity.",
     u"Mujer con una pantalla de CIRCLE y otra de SQUARE a los costados.",
     u"Prepara el único momento participativo del video."),
    ([223.0, 232.0], 330.0, 360.0,
     u"With one hand, draw a circle. With the other, draw a square. Easy, right? Now try to do the circle "
     u"and square at the same time.",
     u"La mujer dibujando en el aire con las dos manos.",
     u"<b>El pedazo más interactivo del canal.</b> Te hace intentar algo que vas a fallar. Para un short, "
     u"eso es retención garantizada y comentarios."),
    ([304.0, 344.0], 360.0, 420.0,
     u"Time to put the teaching to test. Who will be our candidate for the fastest death?&hellip; It seems we&rsquo;ve "
     u"found ourselves a candidate.",
     u"Un cartel SEARCHING sobre una pared de caras. Un cartel navideño CANDIDATE FOUND. Un hombre "
     u"trabajando con un martillo en un taller.",
     u"El formato de concurso aplicado a elegir quién muere primero. El cartel de Navidad es gratuito y por eso funciona."),
    ([368.0, 420.0], 420.0, 500.0,
     u"At one minute, the rate of survival remains relatively high. At ten minutes, it&rsquo;s a different scenario&hellip; "
     u"Sixteen minutes of no gravity, plus gravity coming back.",
     u"Cartel 60% HUMANITY DEAD, 1 MINUTE. Un perro con flotadores. Un monje con marmotas. Un avión "
     u"partido en el aire.",
     u"La escalada por tiempo, con los contadores en pantalla. El mismo recurso que el video del iPhone, "
     u"pero con muertos."),
    ([484.0, 520.0], 500.0, 560.0,
     u"&mdash;this is gonna get, like, pretty ugly, right? &mdash;Well, yes, but we might have a solution. "
     u"With Happy Place, I can be happy and terrified at the same time.",
     u"Un presentador tipo Apple con camisa azul. Un cerebro rosa con una ventanita de conejos. "
     u"Un picnic con Greg mientras el mundo se destruye detrás.",
     u"La parodia de keynote metida en medio del apocalipsis. Es el chiste más construido del video."),
    ([536.0, 568.0], 560.0, 620.0,
     u"The thing deadlier than falling objects is atmospheric pressure waves&hellip; The next hours are a mass "
     u"extinction event, with one exception. A subsea scientific diver.",
     u"Un contenedor volando contra un edificio. Megatsunamis sobre una ciudad. Una buzo con casco "
     u"entre escombros.",
     u"Acá el video se pone serio de verdad y el cambio de tono se nota."),
    ([560.0, 596.0], 620.0, 660.0,
     u"In 1966, a hose disconnection accident exposed NASA technician Jim LeBlanc to 14 seconds of near vacuum. "
     u"He later said that he felt the saliva in his mouth boiling before losing consciousness.",
     u"Un brazo robótico con un vaso de agua. Una cámara de vacío. Un técnico de los sesenta "
     u"frente a una consola.",
     u"<b>El dato real que nadie conoce.</b> Es el único momento del video que da miedo de verdad, "
     u"y no necesita ningún chiste."),
    ([600.0, 660.0], 660.0, 702.9,
     u"She spent 12 lovely days drinking emergency hydration canisters, going to the bathroom, and even spent "
     u"time reading. Until her oxygen ran out&hellip; the next time you are falling through an unusually long set "
     u"of stairs, just remember: it&rsquo;s not gravity&rsquo;s fault.",
     u"Una lata japonesa de hidratación de emergencia. Un conejo flotando. Greg y el presentador en un jardín. "
     u"Un hombre cayendo por una escalera.",
     u"Mata a la última humana con una frase amable y después cierra con un chiste de escalera. "
     u"Es el cambio de tono más brusco de los cinco videos."),
  ],
  humor=[
    u"<b>Es el más largo y el que peor se corta.</b> Casi todo depende del escalón anterior. "
    u"Los shorts que funcionan son los que tienen pregunta y respuesta adentro del mismo tramo.",
    u"<b>Greg es el espectador.</b> Cuando dice &laquo;this is great science&raquo; o pregunta quién muere así, "
    u"está diciendo lo que vos pensaste. Sacarlo deja al presentador solo y el tono se pone didáctico.",
    u"<b>Los contadores en pantalla son el motor.</b> Cinco segundos, quince segundos, un minuto, diez, "
    u"dieciseis. Cada número es una promesa de que falta algo peor.",
    u"<b>Tiene un dato real guardado.</b> Lo de Jim LeBlanc en 1966 y la saliva hirviendo es verdad, "
    u"y es el único momento del canal donde el miedo no es un chiste.",
  ],
  shorts=[
    (u"&iquest;Quién muere primero?", [[39.0, 53.0]], [[32.0, 36.0], [39.5, 43.0], [43.5, 47.0], [47.5, 53.0]], [32.0, 39.0],
     u"Las dos preguntas que sostienen el video entero, con la perilla de gravedad.",
     u"Si la gravedad desapareciera, quien muere primero? #brainsyrup #ciencia"),
    (u"Dibujá un círculo y un cuadrado", [[223.0, 243.0]],
     [[223.0, 227.0], [227.2, 231.0], [231.2, 236.0], [236.2, 243.0]], [223.0, 232.0],
     u"El único pedazo del canal que le pide al que mira que haga algo. Para comentarios no hay nada mejor.",
     u"Con una mano dibuja un circulo. Con la otra, un cuadrado. #brainsyrup #ciencia"),
    (u"La saliva le hirvió en la boca", [[607.0, 633.0]],
     [[560.0, 564.0], [564.2, 568.0], [568.2, 572.0], [572.2, 578.0]], [560.0, 568.0],
     u"El dato de 1966. No tiene chiste y no lo necesita: es el único pedazo del canal que da miedo de verdad.",
     u"En 1966 un tecnico de la NASA estuvo 14 segundos en vacio. #brainsyrup #ciencia"),
    (u"Los primeros quince segundos", [[195.0, 220.0]],
     [[150.0, 154.0], [154.2, 158.0], [158.2, 162.0], [162.2, 166.0], [166.2, 172.0]], [150.0, 166.0],
     u"La cuenta regresiva: cinco segundos, quince segundos. El recurso que mejor retiene del video.",
     u"Los primeros cinco segundos sin gravedad. #brainsyrup #ciencia"),
    (u"No es culpa de la gravedad", [[676.0, 690.0]], [[660.0, 664.0], [664.2, 668.0], [668.2, 672.0]], [660.0],
     u"El chiste de cierre, solo. Nueve segundos y no necesita nada de lo anterior.",
     u"La proxima vez que te caigas por una escalera. #brainsyrup #ciencia"),
  ]))

# ---------------------------------------------------------------- render
CSS = u'''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{color-scheme:dark;
  --bg:#0F1418;--panel:#161D23;--panel2:#111920;--line:#242E36;--line2:#38454F;
  --ink:#E7EDF2;--ink2:#AFBCC7;--dim:#7A8995;--teal:#2DD4BF;--teal-soft:#122E2C;
  --blue:#93B4FD;--warn:#E9B949;
  --ui:"Inter","Segoe UI",system-ui,-apple-system,Helvetica,Arial,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:15px;line-height:1.55}
.app{max-width:1600px;margin:0 auto;padding-block:20px 64px;padding-left:20px;padding-right:20px}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
header{display:flex;align-items:center;gap:22px;flex-wrap:wrap;padding-bottom:20px;border-bottom:1px solid var(--line)}
.logo{flex:none;width:88px;height:88px;border-radius:50%;display:block}
header>.id{min-width:0}
h1{margin:0;font-size:clamp(30px,4.2vw,46px);font-weight:800;letter-spacing:-.03em;line-height:1.02}
.h1b{color:var(--teal)}
.kicker{font-size:12.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin:0 0 10px}
.nav{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
.tab{text-decoration:none;border:1px solid var(--line2);color:var(--dim);font-size:13.5px;font-weight:600;padding:8px 16px;border-radius:999px;white-space:nowrap}
.tab:hover{color:var(--ink);border-color:var(--teal)}
.tab.on{background:var(--teal);border-color:var(--teal);color:#06211E}
h2{font-size:21px;letter-spacing:-.015em;font-weight:700;margin:44px 0 16px;display:flex;align-items:center;gap:14px}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
.ficha{display:flex;flex-wrap:wrap;border:1px solid var(--line);border-radius:10px;background:var(--panel);overflow:hidden;margin-top:14px}
.ficha div{flex:1;min-width:150px;padding:14px 18px;border-right:1px solid var(--line)}
.ficha div:last-child{border-right:0}
.ficha span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.ficha b{display:block;font-size:20px;font-weight:800;margin-top:3px}
.intro{font-size:17px;color:var(--ink2);margin:16px 0 0;max-width:86ch}
.beat{display:grid;grid-template-columns:minmax(0,440px) minmax(0,1fr);gap:20px;padding:20px 0;border-bottom:1px solid var(--line);align-items:start}
.caps{display:flex;gap:6px;flex-wrap:wrap}
.caps img{width:100%;max-width:212px;border-radius:7px;display:block;border:1px solid var(--line)}
.short .caps img{max-width:200px}
.txt p{margin:0 0 8px;max-width:86ch}
.t{font-size:12.5px;color:var(--warn);letter-spacing:.04em}
.voz{font-size:17px;line-height:1.45;color:var(--ink)}
.img,.por{font-size:14px;color:var(--ink2)}
.img b,.por b{color:var(--ink);font-weight:600}
.short{padding:20px;border:1px solid var(--line);border-radius:12px;background:var(--panel);margin-bottom:14px}
.short h3{margin:0 0 12px;font-size:19px;font-weight:700;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.num{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--teal);color:#06211E;font-size:13px;font-weight:800}
.dur{margin-left:auto;font-size:13px;color:var(--teal)}
.nota{font-size:14.5px;color:var(--ink2);margin:12px 0 10px;max-width:86ch}
.pistas{display:flex;gap:22px;flex-wrap:wrap;margin-bottom:8px}
.pistas>div{min-width:0}
.lbl{display:block;font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:4px}
code{font-family:var(--mono);font-size:12.5px;background:var(--panel2);border:1px solid var(--line);
  border-radius:5px;padding:2px 7px;color:var(--teal);white-space:nowrap;display:inline-block;margin:0 2px 3px 0}
.pistas>div:last-child code{color:var(--blue)}
.cap{font-size:13.5px;color:var(--ink2);margin:10px 0 0}
pre{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:16px;overflow-x:auto;
  font-family:var(--mono);font-size:12.5px;color:var(--ink2);line-height:1.5}
.nota-g{padding:22px 26px;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:10px;background:var(--panel)}
.nota-g p{margin:0;font-size:18px;line-height:1.5;max-width:86ch}
.nota-g p+p{margin-top:12px}
.hl{color:var(--teal);font-weight:700}
ul{margin:10px 0 0;padding-left:20px}
li{margin-bottom:9px;color:var(--ink2);max-width:86ch}
li b{color:var(--ink)}
.vidlist{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:16px;margin-top:16px}
.vcard{display:block;text-decoration:none;color:inherit;background:var(--panel);border:1px solid var(--line);
  border-radius:12px;overflow:hidden}
.vcard:hover{border-color:var(--teal)}
.vcard img{width:100%;display:block;aspect-ratio:16/9;object-fit:cover}
.vcard .b{padding:14px 16px}
.vcard .n{font-size:11.5px;font-weight:700;letter-spacing:.08em;color:var(--dim)}
.vcard .ti{font-size:17px;font-weight:700;letter-spacing:-.01em;margin:3px 0 6px}
.vcard .me{font-family:var(--mono);font-size:12px;color:var(--teal)}
.vcard p{margin:8px 0 0;font-size:13.5px;color:var(--ink2)}
@media(max-width:820px){.beat{grid-template-columns:minmax(0,1fr)}}
</style>
'''

def nav(activa):
    its = [(u"Objetivo", u""), (u"Seguimiento", u"seguimiento/"), (u"Videos", u"videos/"), (u"Picadora", u"picadora/"), (u"Cuentas", u"cuentas/"), (u"Mejor call to action", u"cta/"), (u"Posteos", u"posteos/"), (u"Material de estudio", u"referencias/")]
    out = [u'  <nav class="nav">']
    for nm, sub in its:
        on = u" on" if nm == activa else u""
        ac = u' aria-current="page"' if nm == activa else u""
        out.append(u'    <a class="tab%s" href="%s%s"%s>%s</a>' % (on, SITE, sub, ac, nm))
    out.append(u"  </nav>")
    return chr(10).join(out)

def plan_json(v):
    d = {"video": v["file"], "shorts": []}
    for titulo, voz, imagen, caps, nota, cap in v["shorts"]:
        t = titulo.replace(u"&iquest;", u"¿").replace(u"&eacute;", u"e").replace(u"&aacute;", u"a")
        d["shorts"].append({"title": t, "cap": cap,
                            "voz": [[round(a, 2), round(b, 2)] for a, b in voz],
                            "imagen": [[round(a, 2), round(b, 2)] for a, b in imagen]})
    return json.dumps(d, ensure_ascii=False, indent=1)

if not os.path.isdir(SAL):
    os.makedirs(SAL)

tarjetas = u""
for v in V:
    path = os.path.join(DIR, v["file"])
    tiempos = sorted(set([t for b in v["beats"] for t in b[0]] +
                         [t for sh in v["shorts"] for t in sh[3]]))
    print(u"%-14s %d capturas" % (v["slug"], len(tiempos)))
    IM = dict((t, frame(path, t)) for t in tiempos)
    img = lambda t: u'<img src="%s" alt="Captura en %s">' % (IM[t], tc(t))

    beats = u""
    for caps, a, b, voz, imagen, por in v["beats"]:
        beats += (u'<article class="beat">\n  <div class="caps">%s</div>\n  <div class="txt">\n'
                  u'    <p class="t mono">%s &ndash; %s</p>\n    <p class="voz">&laquo;%s&raquo;</p>\n'
                  u'    <p class="img"><b>En pantalla.</b> %s</p>\n'
                  u'    <p class="por"><b>Por qu&eacute; funciona.</b> %s</p>\n  </div>\n</article>\n'
                  % (u"".join(img(c) for c in caps), tc(a), tc(b), voz, imagen, por))

    shorts = u""
    for i, (titulo, voz, imagen, caps, nota, cap) in enumerate(v["shorts"]):
        dur = sum(y - x for x, y in imagen)
        shorts += (u'<article class="short">\n  <h3><span class="num">%02d</span> %s '
                   u'<span class="dur mono">%.1f s</span></h3>\n  <div class="caps">%s</div>\n'
                   u'  <p class="nota">%s</p>\n  <div class="pistas">\n'
                   u'    <div><span class="lbl">Voz</span>%s</div>\n'
                   u'    <div><span class="lbl">Imagen</span>%s</div>\n  </div>\n'
                   u'  <p class="cap"><span class="lbl">Caption</span>%s</p>\n</article>\n'
                   % (i + 1, titulo, dur, u"".join(img(c) for c in caps), nota,
                      u" ".join(u'<code>%s&ndash;%s</code>' % (tc(x), tc(y)) for x, y in voz),
                      u" ".join(u'<code>%s&ndash;%s</code>' % (tc(x), tc(y)) for x, y in imagen), cap))

    pag = (u"<title>%s</title>\n" % v["corto"]) + CSS + u'''
<div class="app">
<header>
  <img class="logo" src="%(logo)s" alt="Logo de Brain Syrup">
  <div class="id">
    <p class="kicker">Video %(n)02d &middot; %(tipo)s</p>
    <h1>%(titulo)s</h1>
  </div>
%(nav)s
</header>

<div class="ficha">
  <div><span>Duraci&oacute;n</span><b class="mono">%(dur)s</b></div>
  <div><span>L&iacute;neas de di&aacute;logo</span><b class="mono">%(lineas)d</b></div>
  <div><span>Versiones propuestas</span><b class="mono">%(nsh)d</b></div>
  <div><span>Material de short</span><b class="mono">%(tot).0f s</b></div>
</div>
<p class="intro">%(resumen)s</p>

<h2>C&oacute;mo est&aacute; armado</h2>
%(beats)s

<h2>D&oacute;nde est&aacute; el humor</h2>
<ul>%(humor)s</ul>

<h2>Las cinco versiones</h2>
%(shorts)s

<h2>El plan, para pegar en la Picadora</h2>
<pre>%(plan)s</pre>

<h2>Lo que no pude leer</h2>
<div class="nota-g">
  <p>Veo los cuadros y leo los subt&iacute;tulos, pero <span class="hl">no escucho</span>: no s&eacute; d&oacute;nde
    hay una pausa, un &eacute;nfasis o un golpe de sonido. Los cortes entran y salen sobre las l&iacute;neas de
    di&aacute;logo, as&iacute; que si alguno te queda abrupto es por ah&iacute;.</p>
</div>
</div>
''' % dict(logo=LOGO, n=v["n"], tipo=v["tipo"], titulo=v["titulo"], nav=nav(u"Videos"),
           dur=u"%d:%02d" % (int(v["dur"]) // 60, int(v["dur"]) % 60), lineas=v["lineas"],
           nsh=len(v["shorts"]),
           tot=sum(sum(y - x for x, y in sh[2]) for sh in v["shorts"]),
           resumen=v["resumen"], beats=beats,
           humor=u"".join(u"<li>%s</li>" % h for h in v["humor"]), shorts=shorts,
           plan=plan_json(v).replace(u"&", u"&amp;").replace(u"<", u"&lt;"))

    d = os.path.join(SAL, v["slug"])
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(pag)
    print(u"   %s/index.html  %d KB" % (v["slug"], len(pag) // 1024))

    v["thumb"] = IM[v["beats"][0][0][0]]
    tarjetas += (u'<a class="vcard" href="%svideos/%s/">\n  <img src="%s" alt="">\n  <div class="b">\n'
                 u'    <p class="n">VIDEO %02d</p>\n    <p class="ti">%s</p>\n'
                 u'    <p class="me">%d:%02d &middot; %d versiones &middot; %.0f s de material</p>\n'
                 u'    <p>%s</p>\n  </div>\n</a>\n'
                 % (SITE, v["slug"], v["thumb"], v["n"], v["corto"],
                    int(v["dur"]) // 60, int(v["dur"]) % 60, len(v["shorts"]),
                    sum(sum(y - x for x, y in sh[2]) for sh in v["shorts"]), v["tipo"]))

INDEX = u"<title>Videos</title>\n" + CSS + u'''
<div class="app">
<header>
  <img class="logo" src="%(logo)s" alt="Logo de Brain Syrup">
  <div class="id">
    <p class="kicker">Videos</p>
    <h1>Brain Syrup <span class="h1b">YouTube Channel</span></h1>
  </div>
%(nav)s
</header>

<p class="intro">Cada video le&iacute;do cuadro por cuadro: c&oacute;mo est&aacute; armado, d&oacute;nde est&aacute;
el humor y cinco versiones de short con la imagen y la voz separadas. Los planes se pegan en la Picadora.</p>

<h2>Los cinco</h2>
<div class="vidlist">
%(cards)s</div>

<h2>Lo que sale de ac&aacute;</h2>
<div class="nota-g">
  <p><span class="hl">25 versiones</span> entre los cinco videos. Con cinco publicaciones por semana,
    es material para cinco semanas sin volver a filmar nada.</p>
  <p>Los que mejor viajan solos son los dos cortos animados: no explican nada, as&iacute; que cualquier
    pedazo se entiende sin contexto.</p>
</div>
</div>
''' % dict(logo=LOGO, nav=nav(u"Videos"), cards=tarjetas)
io.open(os.path.join(SAL, "index.html"), "w", encoding="utf-8").write(INDEX)
print(u"indice %d KB" % (len(INDEX) // 1024))
