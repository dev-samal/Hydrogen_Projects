import pandas as pd
import streamlit as st
import altair as at

st.set_page_config(layout = "wide")

h2 = pd.read_csv("H2Projects.csv")
h2.info()

st.title(":orange[H2 Projects Around the World]")
st.write("**:blue[Funding and infrastructure area among the many limiting factors for countries to invest in projects to generate hydrogen power as an alternate energy source for manufacturing, automotive, etc. industries.]**")

tab1,tab2,tab3 = st.tabs(['Quick Glance at H2 Interest','Carbon Capture','Explore Specifics by Project Name'])

with tab1:
###VISUALS
    st.sidebar.header('Make Selections')
    st.write(":orange[Make a selection to see which parts of globe are interested in such projects, planned spread over the future years, or project progress]")
    x_axis_cols = cols = h2.drop(columns=['Latitude','Longitude','Carbon Capture','Country','End Use','Electricty Used Color(Feedstock)','Country Full Name','Project Name','Technology Category','Production Technology','Type of Electricity Used for Production','Hydrogen Product','IEA zero-carbon estimated normalized capacity']).columns.values.tolist()

    xVar = st.sidebar.selectbox('Select to Group By for Quick Glance',
                x_axis_cols
                )
# 1)Bar:Select x-axis to see project count summary
    xVar_count = h2.groupby([xVar])[xVar].count().reset_index(name='# Projects Planned/In Progress')
    xVarSelectBar = at.Chart(
        xVar_count).mark_bar().encode(
        x=xVar,
        y='# Projects Planned/In Progress',
        tooltip=['# Projects Planned/In Progress', xVar],
        ).properties(
            height=400, 
            width =700,
            title = "Project Count"
    )
    xVarSelectBar
    st.write('Status grouping summarizes projects plans that countries have discussed in "concept", or "DEMO" & "Feasibility study" indicate varying degrees of active research. Date Online groups by year of when the project will become in true production.')


#2) Map to show project spread and interest in hydrogen production for power
    url_geojson = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
    data_geojson = at.Data(url=url_geojson, format=at.DataFormat(property='features',type='json'))
    points = at.Chart(h2).mark_circle(
    color='goldenrod'
    ).encode(
    latitude='Latitude:Q',
    longitude= 'Longitude:Q',
    size= at.value(100),
    tooltip='Country Full Name'
    ).project(
    "identity",
    reflectX=False,
    reflectY=True
    )      

    world_map1= at.Chart(data_geojson,height=400,width=700).mark_geoshape(
    fill='aliceblue',
    stroke='navy'
    ).project(
    type='identity', reflectY=True).properties(
    ).properties(
        title="Spread and Interest in H2 Production Projects"
    )
    (world_map1 + points)
# world_map= at.Chart(data_geojson).mark_geoshape().encode(
#     color="properties.name:N"
# ).project(
#     type='identity', reflectY=True).properties(
#         height=600,
#         width=700
#     )
with tab2:

    # 3) Visual
    prodProcess = at.Chart(h2).mark_bar().encode(
    y= 'Technology Category',
    color = "Hydrogen Product",
    x='IEA zero-carbon estimated normalized capacity'
    ).properties(
    height= 400,
    width = 500
    )
    prodProcess
    st.write('Technology refers to the chemical process that is used to produce hydrogen that can then be filled into fuel cells to create an emission free power source for automotives, power grid, etc. "Hydrogen Product" refers to the molecules that act as hydrogen "source" for downstream reactions like in a battery.')
    
    #Visual 4
    CO2Capture= at.Chart(h2).transform_density(
    'Date Online',
    as_=['Date Online', 'density'],    
    groupby=['Carbon Capture']
    ).mark_area(orient='horizontal').encode(
    y='Date Online:Q',
    color='Carbon Capture:N',
    x=at.X(
        'density:Q',
        stack='center',
        impute=None,
        title=None,
        axis=at.Axis(labels=False, values=[0],grid=False, ticks=True)        
    ),
    column=at.Column(
        'Carbon Capture:N'
    )
    ).properties(
    width=100
    ).configure_facet(
    spacing=0   
    )
    CO2Capture

    st.write('There is a lot more carbon capture technology build into current year and next 2 years plans than father ahead. This distribution could change once 2023 data is released in a couple more months. One could see how project planning has evolved to includ this very important practice.')

    
    # 5 Visual
    industry2 = at.Chart(h2).mark_bar().encode(
    y='End Use',
    color= 'Carbon Capture',
    x= 'IEA zero-carbon estimated normalized capacity'
    ).properties(
    height= 400,
    width = 700
    )
    # text = industry2.mark_text(
    #       align="left",
    #     baseline="middle",
    #     dx=130,
    #     fontSize= 10,
    # ).encode(text= 'sumCO2:Q')
    industry2

    st.write('These are the industries that commonly use the hydrogen molecules (produced in the previous bar graph) to power manufacturing, refinement of goods or transportation. The chart above shows an estimation of how much CO2 could be reduced per industry globally if they successfully transition to the planned hydrogen projects. During the transition, they are still emitting lots of CO2. Therefore, some industries have planned mechanisms to capture and store their CO2 emission until it can be disposed of properly, indicated by the orange highlights')


    sumCO2 = h2.groupby(by=['End Use'])['IEA zero-carbon estimated normalized capacity'].sum()
    sumCO2
   



#for Tab 3 as a raw data tab to simply explore at a Project Name level
with tab3:
    #countryProj_count = h2.groupby(['Country Full Name'])['Country Full Name'].count().reset_index(name='Projects')
    st.write(':orange[Click on column header to sort ascending to descending]')
    h2
    #countryProj_count



