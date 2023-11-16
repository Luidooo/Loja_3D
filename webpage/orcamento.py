import streamlit as st
import math

def calcula_orcamento(volume, taxa_hora_maquina, preco_material):

    # Lógica para calcular o preço com base no volume, taxa da hora da máquina e preço do material

    preco_maquina = taxa_hora_maquina * (volume / 1000)  # Convertendo para litros
    preco_total = (preco_material*volume) + preco_maquina
    return preco_total

def obter_taxa_hora_maquina(impressora):

    # Dados fictícios

    taxas_por_modelo = {
        "Ender 3": 5.0,
        "Ender 3 S1": 6.0,
        "Prusa MK4": 7.5,
        "Ender 5": 5.5
    }
    return taxas_por_modelo.get(impressora, 0.0)

def obter_preco_material(material):

    # Dados fictícios

    precos_por_material = {
        "PLA": 120.0/1000,
        "TPU": 150.0/1000,
        "ABS": 100.0/1000,
        "PETG": 130.0/1000
    }
    return precos_por_material.get(material, 0.0)

def calcula_volume_retangulo(comprimento, largura, altura):
    return comprimento * largura * altura

def calcula_volume_cilindro(raio, altura):
    return math.pi * raio**2 * altura

def calcula_volume_circulo(raio):
    return math.pi * raio**2

def main():
    st.title("Orçamento para Impressão 3D")

    # Seleção da impressora

    impressora_selecionada = st.selectbox("Selecione a impressora:", ["Ender 3", "Ender 3 S1", "Prusa MK4", "Ender 5"])

    # Seleção do material

    material_selecionado = st.selectbox("Selecione o material:", ["PLA", "TPU", "ABS", "PETG"])

    # Escolha da forma (retângulo, cilindro, círculo ou ambos)

    forma_selecionada = st.radio("Selecione a forma:", ["Retângulo", "Cilindro", "Círculo", "Ambos"])

    if forma_selecionada == "Ambos":
        st.subheader("Medidas para o Retângulo:")
        comprimento_retangulo = st.number_input("Comprimento (cm):", min_value=0.1, step=0.1)
        largura_retangulo = st.number_input("Largura (cm):", min_value=0.1, step=0.1)
        altura_retangulo = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        st.subheader("Medidas para o Cilindro:")
        raio_cilindro = st.number_input("Raio (cm):", min_value=0.1, step=0.1)
        altura_cilindro = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        st.subheader("Medidas para o Círculo:")
        raio_circulo = st.number_input("Raio (cm):", min_value=0.1, step=0.1)

        volume_retangulo = calcula_volume_retangulo(comprimento_retangulo, largura_retangulo, altura_retangulo)
        volume_cilindro = calcula_volume_cilindro(raio_cilindro, altura_cilindro)
        volume_circulo = calcula_volume_circulo(raio_circulo)

        # Calcula o volume total considerando os três objetos
        volume_total = volume_retangulo + volume_cilindro + volume_circulo
    elif forma_selecionada == "Retângulo":
        comprimento_retangulo = st.number_input("Comprimento (cm):", min_value=0.1, step=0.1)
        largura_retangulo = st.number_input("Largura (cm):", min_value=0.1, step=0.1)
        altura_retangulo = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o retângulo
        volume_total = calcula_volume_retangulo(comprimento_retangulo, largura_retangulo, altura_retangulo)
    elif forma_selecionada == "Cilindro":
        raio_cilindro = st.number_input("Raio (cm):", min_value=0.1, step=0.1)
        altura_cilindro = st.number_input("Altura (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o cilindro
        volume_total = calcula_volume_cilindro(raio_cilindro, altura_cilindro)
    else:
        raio_circulo = st.number_input("Raio (cm):", min_value=0.1, step=0.1)

        # Calcula o volume apenas para o círculo
        volume_total = calcula_volume_circulo(raio_circulo)

    # Exibe o volume total calculado
    st.subheader("Volume Total do Objeto:")
    st.write(f"{volume_total:.2f} cm³")

    # Obtém a taxa da hora da máquina com base na impressora selecionada
    taxa_hora_maquina = obter_taxa_hora_maquina(impressora_selecionada)

    # Exibe a taxa da hora da máquina
    st.subheader("Taxa da Hora da Máquina:")
    st.write(f"R$ {taxa_hora_maquina:.2f} por cm³")

    # Obtém o preço do material com base no material selecionado
    preco_material = obter_preco_material(material_selecionado)

    # Exibe o preço do material
    st.subheader("Preço do Material:")
    st.write(f"R$ {preco_material:.2f} por cm³")

    # Calcula o preço com base no volume, taxa da hora da máquina e preço do material
    preco = calcula_orcamento(volume_total, taxa_hora_maquina, preco_material)

    # Exibe o preço calculado
    st.subheader("Preço estimado:")
    st.write(f"R$ {preco:.2f}")

if __name__ == "__main__":
    main()

