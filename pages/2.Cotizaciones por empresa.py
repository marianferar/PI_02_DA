import streamlit as st

st.title('Cotizaciones por empresa 📊  ')  
st.markdown('***')

st.subheader('''✅ Acá podrás obtener la información de la empresa particular que quieras ver considerando los años 2020 a 2023. Este criterio se basa en tener cierta perspectiva de cómo puede influir una crisis mundial, como lo fue la pandemia por COVID19, en las acciones de las empresas.''')

st.markdown('''Elige una empresa''')
if st.button('Amazon'):
        st.image('data\pamazon.png')
        st.write('En el mes de junio del año 2020 hubo un gran aumento de cotización, momento en que empezó el confinamiento mundial.')
        st.write('Desde marzo de 2022 el precio hizo un fuerte retroceso. Si te dedicas al trading, es un buen momento para comprar y en cuanto aumente, venderlas.')
if st.button('Apple'):
        st.image('data\papple.png')
        st.write('Desde junio 2020 se dio un gran aumento, de casi 50% en la cotización. Desde esa fecha, el valor continúa en alza.')
if st.button('Chevron'):
        st.image('data\chevron.png')
        st.write('Esta compañía tuvo una disminución de precios durante el año 2020.')
        st.write('Sin embargo, desde diciembre de 2021 se ha dado un crecimiento.')
if st.button('Google'):
        st.image('data\google.png')
        st.write('Se puede ver como entre junio y septiembre de 2021 se dio un pico máximo, de casi 140USD por acción.')
        st.write('Sin embargo, desde diciembre 2021 se ha dado un descendo en el valor.')
if st.button('Microsoft'):
        st.image('data\microsoft.png')
        st.write('Se puede ver un crecimiento sostenido a lo largo de estos años, con un valor máximo de casi 350USD por acción.')
if st.button('Walmart'):
        st.image('data\walmart.png')
        st.write('En esta compañía es más notorio el crecimiento sostenido y progresivo, más lento que las demás.')

st.title('''Otro aspecto importante a considerar es el pago de dividendos... ''')
st.subheader('Esto significa que las empresas comparten un porcentaje de sus ganancias totales con todas las personas accionistas.')

st.write('👇 Acá una tabla resumen con esta información:')
st.image('images\dividendos.png')  

st.write('Esto significa que _APPLE_ es la empresa que más dividendos ha pagado en los últimos 23 años.')
st.write('Luego le siguen _CHEVRON_ _WALMART_ y _MICROSOFT_.')
st.write('_AMAZON_ y _GOOGLE_ no abonaron dividendos en estos 23 años... ¿lo harán más adelante? Por ahora no podemos responder esto.')





    


