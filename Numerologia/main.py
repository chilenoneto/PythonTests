import unicodedata

class Alfabeto:
    def __init__(self):
        self.letras_valores = {}
        letra_actual = 'A'
        valor_actual = 1

        for i in range(26):
            self.letras_valores[letra_actual] = valor_actual
            letra_actual = chr(ord(letra_actual) + 1)

            if letra_actual == 'J':
                valor_actual = 1
            else:
                valor_actual += 1

    def valor(self, letra):
        letra_mayuscula = letra.upper()

        if letra_mayuscula in self.letras_valores:
            return self.letras_valores[letra_mayuscula]
        else:
            raise ValueError("La letra no pertenece al alfabeto.")

    def calcular_valor_total(self, cadena):
        valor_total = 0

        for letra in cadena:
            if letra.isalpha():
                valor_total += self.valor(letra)

        while valor_total >= 10:
            suma_digitos = sum(int(digito) for digito in str(valor_total))
            valor_total = suma_digitos

        return valor_total

    def obtener_significado(self, valor, idioma):
        significados = {
            1: {
                'español': "El número 1 representa el liderazgo, la independencia y la individualidad. \n Las personas con este número tienden a ser emprendedoras y tener una personalidad fuerte y ambiciosa. \nSin embargo, pueden volverse dominantes y egocéntricas en exceso.",
                'inglés': "Number 1 represents leadership, independence, and individuality. \nIndividuals with this number tend to be enterprising and have a strong and ambitious personality. \nHowever, they can become overly dominant and egocentric.",
                'portugués': "O número 1 representa liderança, independência e individualidade. \nIndivíduos com esse número tendem a ser empreendedores e ter uma personalidade forte e ambiciosa. \nNo entanto, eles podem se tornar excessivamente dominantes e egocêntricos."
            },
            2: {
                'español': "El número 2 simboliza la cooperación, la diplomacia y la armonía. \n Las personas con este número son pacíficas, amigables y equilibradas, y tienden a buscar relaciones armoniosas. \nNo obstante, pueden ser indecisas y dependientes de los demás.",
                'inglés': "Number 2 symbolizes cooperation, diplomacy, and harmony. \nIndividuals with this number are peaceful, friendly, and balanced, and tend to seek harmonious relationships. \nHowever, they can be indecisive and dependent on others.",
                'portugués': "O número 2 simboliza cooperação, diplomacia e harmonia. \nIndivíduos com esse número são pacíficos, amigáveis e equilibrados, e tendem a buscar relacionamentos harmoniosos. \nNo entanto, podem ser indecisos e dependentes dos outros."
            },
            3: {
                'español': "El número 3 representa la expresión creativa, la comunicación y la sociabilidad. \nAquellos con este número son extrovertidos, carismáticos y tienen una mente creativa. \nSin embargo, pueden ser superficiales y dispersos en sus objetivos.",
                'inglés': "Number 3 represents creative expression, communication, and sociability. \nThose with this number are extroverted, charismatic, and have a creative mind. \nHowever, they can be superficial and scattered in their goals.",
                'portugués': "O número 3 representa expressão criativa, comunicação e sociabilidade. \nAqueles com esse número são extrovertidos, carismáticos e têm uma mente criativa. \nNo entanto, podem ser superficiais e dispersos em seus objetivos."
            },
            4: {
                'español': "El número 4 simboliza la estabilidad, la organización y el trabajo duro. \nLas personas con este número son prácticas, disciplinadas y tienen una fuerte ética laboral. \nSin embargo, pueden ser inflexibles y demasiado rígidas en sus creencias.",
                'inglés': "Number 4 symbolizes stability, organization, and hard work. \nIndividuals with this number are practical, disciplined, and have a strong work ethic. \nHowever, they can be inflexible and too rigid in their beliefs.",
                'portugués': "O número 4 simboliza estabilidade, organização e trabalho duro. \nIndivíduos com esse número são práticos, disciplinados e têm uma forte ética de trabalho. \nNo entanto, podem ser inflexíveis e muito rígidos em suas crenças."
            },
            5: {
                'español': "El número 5 representa la libertad, la aventura y la versatilidad. \nAquellos con este número son inquietos, curiosos y buscan experiencias nuevas y emocionantes. \nSin embargo, pueden ser irresponsables e impacientes en la toma de decisiones.",
                'inglés': "Number 5 represents freedom, adventure, and versatility. \nThose with this number are restless, curious, and seek new and exciting experiences. \nHowever, they can be irresponsible and impatient in decision-making.",
                'portugués': "O número 5 representa liberdade, aventura e versatilidade. A\nqueles com esse número são inquietos, curiosos e buscam experiências novas e emocionantes. \nNo entanto, podem ser irresponsáveis e impacientes na tomada de decisões."
            },
            6: {
                'español': "El número 6 simboliza el amor, el hogar y la responsabilidad. \nLas personas con este número son compasivas, familiares y tienden a cuidar y apoyar a los demás. \nSin embargo, pueden volverse posesivas y sobreprotectoras.",
                'inglés': "Number 6 symbolizes love, home, and responsibility. \nIndividuals with this number are compassionate, family-oriented, and tend to care for and support others. \nHowever, they can become possessive and overprotective.",
                'portugués': "O número 6 simboliza amor, lar e responsabilidade. \nIndivíduos com esse número são compassivos, voltados para a família e tendem a cuidar e apoiar os outros. \nNo entanto, podem se tornar possessivos e superprotetores."
            },
            7: {
                'español': "El número 7 representa la sabiduría, la espiritualidad y la introspección. \nAquellos con este número son introspectivos, místicos y buscan el conocimiento profundo. \nSin embargo, pueden volverse aislados y distantes emocionalmente.",
                'inglés': "Number 7 represents wisdom, spirituality, and introspection. \nThose with this number are introspective, mystical, and seek deep knowledge. \nHowever, they can become isolated and emotionally distant.",
                'portugués': "O número 7 representa sabedoria, espiritualidade e introspecção. \nAqueles com esse número são introspectivos, místicos e buscam conhecimento profundo. \nNo entanto, podem se tornar isolados e emocionalmente distantes."
            },
            8: {
                'español': "El número 8 simboliza el éxito, el poder y la abundancia material. \nAquellos con este número son ambiciosos, emprendedores y orientados hacia el logro y la riqueza. \nSin embargo, pueden volverse materialistas y obsesionados con el poder.",
                'inglés': "Number 8 symbolizes success, power, and material abundance. \nThose with this number are ambitious, entrepreneurial, and oriented towards achievement and wealth. \nHowever, they can become materialistic and obsessed with power.",
                'portugués': "O número 8 simboliza sucesso, poder e abundância material. \nAqueles com esse número são ambiciosos, empreendedores e orientados para a conquista e a riqueza. \nNo entanto, podem se tornar materialistas e obcecados pelo poder."
            },
            9: {
                'español': "El número 9 representa la compasión, la generosidad y el humanitarismo. \nAquellos con este número son altruistas, empáticos y tienen un fuerte sentido de la justicia social. \nSin embargo, pueden ser emocionalmente inestables y tener dificultades para establecer límites.",
                'inglés': "Number 9 represents compassion, generosity, and humanitarianism. \nThose with this number are altruistic, empathetic, and have a strong sense of social justice. \nHowever, they can be emotionally unstable and have difficulties in setting boundaries.",
                'portugués': "O número 9 representa compaixão, generosidade e humanitarismo. \nAqueles com esse número são altruístas, empáticos e têm um forte senso de justiça social. \nNo entanto, podem ser emocionalmente instáveis e ter dificuldades em estabelecer limites."
            }
        }

        return significados.get(valor, {}).get(idioma, "No se encontró un significado para el número en el idioma seleccionado.")

alfabeto = Alfabeto()

idioma = input("Seleccione el idioma (1: español, 2: inglés, 3: portugués): ")

if idioma == "1":
    idioma = "español"
    palabra_salir = "salir"
    pregunta_nombre = f"Ingrese un nombre completo ('{palabra_salir}' para finalizar): "
elif idioma == "2":
    idioma = "inglés"
    palabra_salir = "exit"
    pregunta_nombre = f"Enter a full name ('{palabra_salir}' to exit): "
elif idioma == "3":
    idioma = "portugués"
    palabra_salir = "sair"
    pregunta_nombre = f"Digite um nome completo ('{palabra_salir}' para sair): "
else:
    print("Opción no válida. Por favor, seleccione 1 para español, 2 para inglés o 3 para portugués.")

while True:
    nombre_completo = input(pregunta_nombre)

    if nombre_completo.lower() == palabra_salir:
        break

    # Reemplazar los caracteres acentuados por sus equivalentes sin acento
    nombre_completo = unicodedata.normalize('NFKD', nombre_completo).encode('ASCII', 'ignore').decode('utf-8')

    valor_total = alfabeto.calcular_valor_total(nombre_completo)
    significado = alfabeto.obtener_significado(valor_total, idioma)

    if idioma == "español":
        print("El valor total del nombre es:", valor_total)
        print("Significado según numerología:\n", significado)
    elif idioma == "inglés":
        print("The total value of the name is:", valor_total)
        print("Meaning according to numerology:\n", significado)
    elif idioma == "portugués":
        print("O valor total do nome é:", valor_total)
        print("Significado de acordo com a numerologia:\n", significado)
    print()
