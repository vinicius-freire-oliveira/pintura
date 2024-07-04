class Pintura:
    def __init__(self, largura_parede1, altura_parede1, largura_parede2, altura_parede2, 
                 largura_parede3, altura_parede3, largura_parede4, altura_parede4, 
                 numero_demaos=2, cobertura_por_galao=40, galao=3.6, lata=18):
        # Inicialização dos atributos da classe com os valores fornecidos
        self.largura_parede1 = largura_parede1
        self.altura_parede1 = altura_parede1
        self.largura_parede2 = largura_parede2
        self.altura_parede2 = altura_parede2
        self.largura_parede3 = largura_parede3
        self.altura_parede3 = altura_parede3
        self.largura_parede4 = largura_parede4
        self.altura_parede4 = altura_parede4
        self.numero_demaos = numero_demaos
        self.cobertura_por_galao = cobertura_por_galao
        self.galao = galao
        self.lata = lata

    def calcular_area_total(self):
        # Método para calcular a área total das paredes a serem pintadas
        area_parede1 = self.largura_parede1 * self.altura_parede1
        area_parede2 = self.largura_parede2 * self.altura_parede2
        area_parede3 = self.largura_parede3 * self.altura_parede3
        area_parede4 = self.largura_parede4 * self.altura_parede4
        area_total = area_parede1 + area_parede2 + area_parede3 + area_parede4
        return area_total

    def calcular_quantidade_tinta(self):
        # Método para calcular a quantidade total de tinta necessária
        area_total = self.calcular_area_total()
        quantidade_tinta = (area_total * self.numero_demaos) / self.cobertura_por_galao
        return quantidade_tinta

    def calcular_numero_galoes(self):
        # Método para calcular o número de galões de 3,6 litros necessários e a sobra
        quantidade_tinta = self.calcular_quantidade_tinta()
        numero_galoes = int(quantidade_tinta / self.galao)
        sobra_galoes = self.galao - (quantidade_tinta % self.galao)
        # Se houver uma sobra maior que 0, adicionamos um galão extra
        if sobra_galoes > 0:
            numero_galoes += 1
        return numero_galoes, sobra_galoes

    def calcular_numero_latas(self):
        # Método para calcular o número de latas de 18 litros necessárias e a sobra
        quantidade_tinta = self.calcular_quantidade_tinta()
        numero_latas = int(quantidade_tinta / self.lata)
        sobra_latas = self.lata - (quantidade_tinta % self.lata)
        # Se houver uma sobra maior que 0, adicionamos uma lata extra
        if sobra_latas > 0:
            numero_latas += 1
        return numero_latas, sobra_latas

# Dados do problema
largura_parede1 = 12.0
altura_parede1 = 5.0
largura_parede2 = 12.0
altura_parede2 = 5.0
largura_parede3 = 15.0
altura_parede3 = 5.0
largura_parede4 = 15.0
altura_parede4 = 5.0
numero_demaos = 2  
cobertura_por_galao = 40
galao = 3.6
lata = 18.0

# Instância da classe Pintura com os dados fornecidos
pintura = Pintura(largura_parede1, altura_parede1, largura_parede2, altura_parede2, 
                  largura_parede3, altura_parede3, largura_parede4, altura_parede4, 
                  numero_demaos, cobertura_por_galao, galao, lata)

# Cálculo do número de galões de 3,6 litros e sobra
numero_galoes, sobra_galoes = pintura.calcular_numero_galoes()

# Cálculo do número de latas de 18 litros e sobra
numero_latas, sobra_latas = pintura.calcular_numero_latas()

# Cálculo do consumo total de tinta
consumo_total = pintura.calcular_quantidade_tinta()

# Exibição dos resultados
print(f"M² da superfície a ser pintada: {pintura.calcular_area_total():.2f} m²")
print(f"Número de demãos: {numero_demaos}")
print(f"M² total a ser pintado com as demãos: {pintura.calcular_area_total() * numero_demaos:.2f} m²")
print(f"Rendimento por galão: {cobertura_por_galao:.2f} m²")
print(f"Consumo total: {consumo_total:.2f} litros")
print(f"Número de galões de 3,6 litros utilizados: {numero_galoes}, sobra: {sobra_galoes:.2f} litros")
print(f"Número de latas de 18 litros utilizadas: {numero_latas}, sobra: {sobra_latas:.2f} litros")
