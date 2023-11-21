import streamlit as st
import math

def calcula_orcamento(volume, valor_hora_maquina_total, preco_material, peso_em_gramas):

    # Lógica para calcular o preço com base no volume, taxa da hora da máquina e preço do material
    preco_maquina = valor_hora_maquina_total
    preco_total = (peso_em_gramas*preco_material) + preco_maquina
    return preco_total

def obter_taxa_hora_maquina(impressora):

    # Dados fictícios

    taxas_por_modelo = {

        "Ender 3": 12.0,
        "Ender 3 S1": 13.0,
        "Prusa MK4": 14.5,
        "Ender 5": 13.5
    }
    return taxas_por_modelo.get(impressora, 0.0)

def obter_preco_material(material):

    # Dados fictícios

    precos_por_material = {
        "PLA": 120.0/1000,
        "TPU": 200.0/1000,
        "ABS": 130.0/1000,
        "PETG": 150.0/1000
    }
    return precos_por_material.get(material, 0.0)

def obter_peso_gramas(material,volume):

    #definindo as densidades dos materiais

    densidade_pla  =  1.27
    densidade_tpu  =  1.22
    densidade_abs  =  1.05
    densidade_petg =  1.26

    if material == "PLA":
        peso_em_gramas = volume/densidade_pla

    if material == "TPU":
        peso_em_gramas = volume/densidade_tpu

    if material == "ABS":
        peso_em_gramas = volume/densidade_abs

    if material == "PETG":
        peso_em_gramas = volume/densidade_petg

    return peso_em_gramas

def obter_horas_totais(volume):

    return (volume / 30)
    #se ele insere 0.04cm * 0.02cm * 0.60cm por segundo, *60 por minuto e *60 por hora
    #0.03 cms cubicos por minuto
    #1.73 cms cubicos por hora



def calcula_volume_retangulo(comprimento, largura, altura, preenchimento):
    return (comprimento * largura * altura)*preenchimento

def calcula_volume_cilindro(diametro, altura, preenchimento):
    return (math.pi * (diametro/2)**2 * altura)*preenchimento

def calcula_volume_circulo(diametro, preenchimento):
    return (math.pi * (diametro/2)**2)*preenchimento

def main():
    st.title("Orçamento para Impressão 3D")

    # Seleção da impressora

    impressora_selecionada = st.selectbox("Selecione a impressora:", ["Ender 3", "Ender 3 S1",
                                                                      "Prusa MK4", "Ender 5"])

    # Seleção do material

    material_selecionado = st.selectbox("Selecione o material:", ["PLA", "TPU", "ABS", "PETG"])

    # Selecao do preenchimento

    preenchimento_selecionado = st.selectbox("Selecione o preenchimento:", ["15", "25", "50", "75", "85", "100"])

    preenchimento_selecionado = (float(preenchimento_selecionado))/80

    # Escolha da forma (retângulo, cilindro, círculo ou ambos)

    forma_selecionada = st.radio("Selecione a forma:", ["Retângulo", "Cilindro", "Círculo",
                                                        "Ambos"])

    if forma_selecionada == "Ambos":
        st.subheader("Medidas para o Retângulo:")
        comprimento_retangulo = st.number_input("Comprimento (cm):", min_value=0.1, step=0.1)
        largura_retangulo = st.number_input("Largura (cm):", min_value=0.1, step=0.1)
        altura_retangulo = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        st.subheader("Medidas para o Cilindro:")
        diametro_cilindro = st.number_input("Diametro (cm):", min_value=0.1, step=0.1)
        altura_cilindro = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        st.subheader("Medidas para o Círculo:")
        diametro_circulo = st.number_input("Diametro (cm):", min_value=0.1, step=0.1)

        volume_retangulo = calcula_volume_retangulo(comprimento_retangulo, largura_retangulo, altura_retangulo, preenchimento_selecionado)
        volume_cilindro = calcula_volume_cilindro(diametro_cilindro, altura_cilindro, preenchimento_selecionado)
        volume_circulo = calcula_volume_circulo(diametro_circulo, preenchimento_selecionado)

        # Calcula o volume total considerando os três objetos
        volume_total = volume_retangulo + volume_cilindro + volume_circulo

    elif forma_selecionada == "Retângulo":
        comprimento_retangulo = st.number_input("Comprimento (cm):", min_value=0.1, step=0.1)
        largura_retangulo = st.number_input("Largura (cm):", min_value=0.1, step=0.1)
        altura_retangulo = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o retângulo
        volume_total = calcula_volume_retangulo(comprimento_retangulo, largura_retangulo, altura_retangulo, preenchimento_selecionado)

    elif forma_selecionada == "Cilindro":
        diametro_cilindro = st.number_input("Diametro (cm):", min_value=0.1, step=0.1)
        altura_cilindro = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o cilindro
        volume_total = calcula_volume_cilindro(diametro_cilindro, altura_cilindro, preenchimento_selecionado)


    else:
        diametro_circulo = st.number_input("Diametro (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o círculo
        volume_total = calcula_volume_circulo(diametro_circulo, preenchimento_selecionado)
    

    # Exibe o volume total calculado
    st.write("Volume Total do Objeto:")
    st.write(f"{volume_total:.2f} cm³")

    # Obtém a taxa da hora da máquina com base na impressora selecionada
    taxa_hora_maquina = obter_taxa_hora_maquina(impressora_selecionada)
    valor_hora_maquina_total = (obter_horas_totais(volume_total)*taxa_hora_maquina)

    # Exibe a taxa da hora da máquina
    st.write("Valor total da Hora Maquina:")
    st.write(f"R$ {valor_hora_maquina_total:.2f}")

    # Obtém o preço do material com base no material selecionado
    preco_material = obter_preco_material(material_selecionado)

    #Obtem o peso em gramas
    peso_em_gramas = obter_peso_gramas(material_selecionado,volume_total)
    horas_totais = obter_horas_totais(volume_total)

    # Exibe o preço do material
    st.write("Preço do Material gasto:")
    st.write(f"R$ {peso_em_gramas*preco_material:.2f}")

    # Calcula o preço com base no volume, taxa da hora da máquina e preço do material
    preco = calcula_orcamento(volume_total, valor_hora_maquina_total, preco_material, peso_em_gramas)

    st.write(volume_total, peso_em_gramas)

    preco = math.ceil(preco) + 1
    # Exibe o preço calculado
    st.header("Preço estimado:")
    st.subheader(f"R$ {preco:.2f}")

if __name__ == "__main__":
    main()


