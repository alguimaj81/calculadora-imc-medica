import streamlit as st

# Título e cabeçalho
st.set_page_config(page_title="IMC Médica", page_icon="🩺", layout="centered")
st.title("🩺 Calculadora Médica de IMC e Peso Corporal")
st.markdown("**Ferramenta simples para auxiliar seus atendimentos**")

# Entradas do paciente
col1, col2 = st.columns(2)
with col1:
    peso = st.number_input("Peso (kg)", min_value=1.0, value=70.0, step=0.1)
with col2:
    altura_cm = st.number_input("Altura (cm)", min_value=50, value=170, step=1)

idade = st.number_input("Idade (anos)", min_value=1, value=30, step=1)
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

# Botão calcular
if st.button("Calcular IMC e Peso Ideal", type="primary"):
    # Cálculos
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Baixo peso"
        cor = "🔴"
    elif imc < 25:
        classificacao = "Peso normal"
        cor = "🟢"
    elif imc < 30:
        classificacao = "Sobrepeso"
        cor = "🟡"
    elif imc < 35:
        classificacao = "Obesidade grau 1"
        cor = "🟠"
    elif imc < 40:
        classificacao = "Obesidade grau 2"
        cor = "🔴"
    else:
        classificacao = "Obesidade grau 3"
        cor = "🔴"
    
    # Peso ideal aproximado (fórmula simples Lorentz)
    if sexo == "Masculino":
        peso_ideal = altura_cm - 100 - ((altura_cm - 150) / 4)
    else:
        peso_ideal = altura_cm - 100 - ((altura_cm - 150) / 2.5)
    
    # Mostrar resultados
    st.success(f"**IMC = {imc:.2f}** {cor} {classificacao}")
    
    st.info(f"""
    **Peso ideal aproximado:** {peso_ideal:.1f} kg  
    **Diferença atual:** {peso - peso_ideal:.1f} kg
    """)
    
    st.markdown("---")
    st.markdown("**Mensagem para o paciente (copie e cole):**")
    st.code(f"""
Olá! Seu IMC é {imc:.1f} ({classificacao}).
Seu peso ideal aproximado é {peso_ideal:.1f} kg.
Vamos conversar sobre hábitos saudáveis? 😊
    """, language=None)

# Rodapé
st.caption("🚨 Esta é uma ferramenta de apoio. Não substitui avaliação médica profissional.")
