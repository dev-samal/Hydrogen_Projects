import pandas as pd
import streamlit as st
import altair as at

h2 = pd.read_csv("H2Projects.csv")
h2.info()

st.title(":orange[H2 Projects Around the World]")
st.write("**:green[Funding and infrastructure area among the many limiting factors for countries to invest in projects to generate hydrogen power as an alternate energy source for manufacturing, automotive, etc. industries.]**")
st.write("Make a selection to see which parts of globe are interested in such projects, planned spread over the future years, or project progress")

tab1,tab2,tab3 = st.tabs(['Quick Glance at H2 Interest','Carbon Capture','Explore Specifics by Project Name'])

#Make filters

# selectEndUseValues = ['End Use'].values.tolist()
# selectEndUseFilter = st.sidebar.selectbox('Carbon Capture Distriution by Industry',
#                                          selectEndUseValues)


#yVar = st.sidebar.selectbox('What would you like to y-variable to be' ,x_axis_cols)
with tab1:
###VISUALS
    st.sidebar.header('Make Selections')

    x_axis_cols = cols = h2.drop(columns=['Latitude','Longitude','Carbon Capture','Country','End Use','Electricty Used Color(Feedstock)','Country Full Name','Project Name','Technology Category','Production Technology','Type of Electricity Used for Production','Hydrogen Product','IEA zero-carbon estimated normalized capacity']).columns.values.tolist()

    xVar = st.sidebar.selectbox('Select to view project count by',
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
        title="Project Count and Interest in H2 Production"
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
 # Violin plot
    CO2Plot = at.Chart(h2).transform_density(
    'Date Online',
    as_=['Date Online', 'density'],    
    groupby=['Carbon Capture']
).mark_area(orient='horizontal').encode(
    y=xVar,
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
    spacing=50
)  
CO2Plot


#for Tab 3 as a raw data tab to simply explore at a Project Name level
with tab3:
    #countryProj_count = h2.groupby(['Country Full Name'])['Country Full Name'].count().reset_index(name='Projects')
    h2
    #countryProj_count



