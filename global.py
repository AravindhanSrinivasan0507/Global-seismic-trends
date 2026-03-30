
import pymysql
import sqlalchemy as sqlalchemy

connection = pymysql.connect(
        host="localhost",        # or your server IP
        user="root",
        password="Aravindhan@0507",
        database="earthquakes",
        cursorclass=pymysql.cursors.DictCursor
    )

import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Aravindhan@0507@localhost/earthquakes")


import sqlalchemy as sa

engine = sa.create_engine(
    "mysql+pymysql://root:Aravindhan%400507@localhost/earthquakes"
)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Dictionary of queries (already defined in your code)
queries = {
    "1. Top 10 strongest earthquakes":"""
    SELECT id, country, mag, place, time
    FROM quake_data
    ORDER BY mag DESC
    LIMIT 10;
    """,
    "2. Top 10 deepest earthquakes" : """
    SELECT id, country, depth_km, place, time
    FROM quake_data
    ORDER BY depth_km DESC
    LIMIT 10;
    """,
    "3. Shallow earthquakes < 50 km and mag > 7.5" : """
    SELECT id, country, mag, depth_km, place, time
    FROM quake_data
    WHERE depth_km < 50 AND mag > 7.5;
    """,
    "5. Average magnitude per magnitude type" : """
    SELECT magType, AVG(mag) AS avg_mag
    FROM quake_data
    GROUP BY magType;
    """,
    "6. Year with most earthquakes" : """
    SELECT year, COUNT(*) AS quake_count
    FROM quake_data
    GROUP BY year
    ORDER BY quake_count DESC
    LIMIT 1;
    """,
    "7. Month with highest number of earthquakes" : """
    SELECT month, COUNT(*) AS quake_count
    FROM quake_data
    GROUP BY month
    ORDER BY quake_count DESC
    LIMIT 1;
    """,
    "8. Day of week with most earthquakes" : """
    SELECT day_of_week, COUNT(*) AS quake_count
    FROM quake_data
    GROUP BY day_of_week
    ORDER BY quake_count DESC;
    """,
    "9. Count of earthquakes per hour of day" : """
    SELECT HOUR(time) AS hour_of_day, COUNT(*) AS quake_count
    FROM quake_data
    GROUP BY hour_of_day
    ORDER BY quake_count DESC;
    """,
    "10. Most active reporting network" : """
    SELECT net, COUNT(*) AS quake_count
    FROM quake_data
    GROUP BY net
    ORDER BY quake_count DESC
    LIMIT 1;
    """,
    "11. Reviewed vs automatic earthquakes" : """
    SELECT status, COUNT(*) AS count
    FROM quake_data
    GROUP BY status;
    """,
    "12. Count by earthquake type" : """
    SELECT type, COUNT(*) AS count
    FROM quake_data
    GROUP BY type;
    """,
    "13. Number of earthquakes by data type" : """
    SELECT types, COUNT(*) AS count
    FROM quake_data
    GROUP BY types;
    """,
    "14. Events with high station coverage" : """
    SELECT id, country, nst, mag, place
    FROM quake_data
    WHERE nst > 50;
    """,
    "15. Number of tsunamis triggered per year":"""
    SELECT year, COUNT(*) AS tsunami_count
    FROM quake_data
    WHERE tsunami = 1
    GROUP BY year;
    """,
    "16. Top 5 countries with highest avg magnitude (past 10 years)":"""
    SELECT country, AVG(mag) AS avg_mag
    FROM quake_data
    WHERE year >= YEAR(CURDATE()) - 10
    GROUP BY country
    ORDER BY avg_mag DESC
    LIMIT 5;
    """,
    "17. Countries with both shallow and deep earthquakes in same month":"""
    SELECT DISTINCT country, year, month
    FROM quake_data
    GROUP BY country, year, month
    HAVING SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) > 0
       AND SUM(CASE WHEN depth_km > 300 THEN 1 ELSE 0 END) > 0;
    """,
    "18. Year-over-year growth rate in total earthquakes": """
    SELECT year,
           COUNT(*) AS quake_count,
           (COUNT(*) - LAG(COUNT(*)) OVER (ORDER BY year)) / 
           LAG(COUNT(*)) OVER (ORDER BY year) * 100 AS growth_rate
    FROM quake_data
    GROUP BY year
    ORDER BY year;
    """,
    "19. Top 3 seismically active regions":"""
    SELECT country, COUNT(*) AS quake_count, AVG(mag) AS avg_mag
    FROM quake_data
    GROUP BY country
    ORDER BY quake_count DESC, avg_mag DESC
    LIMIT 3;
    """,
    "20. Avg depth within ±5° latitude of equator":"""
    SELECT country, AVG(depth_km) AS avg_depth
    FROM quake_data
    WHERE latitude BETWEEN -5 AND 5
    GROUP BY country;
    """,
    "21. Countries with highest shallow-to-deep ratio": """
    SELECT country,
           SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) /
           NULLIF(SUM(CASE WHEN depth_km >= 50 THEN 1 ELSE 0 END),0) AS shallow_deep_ratio
    FROM quake_data
    GROUP BY country
    ORDER BY shallow_deep_ratio DESC;
    """,
    "22. Avg magnitude difference between tsunami vs non-tsunami":"""
    SELECT AVG(CASE WHEN tsunami = 1 THEN mag END) -
           AVG(CASE WHEN tsunami = 0 THEN mag END) AS mag_diff
    FROM quake_data;
    """,
    "23. Events with lowest reliability": """
    SELECT id, country, gap, rms, mag, place
    FROM quake_data
    ORDER BY (gap + rms) DESC
    LIMIT 20;
    """,
    "24. Consecutive earthquakes within 50 km & 1 hour":"""
    SELECT a.id AS quake1, b.id AS quake2, a.time, b.time, a.place, b.place
    FROM quake_data a
    JOIN quake_data b
      ON a.id <> b.id
     AND ABS(TIMESTAMPDIFF(MINUTE, a.time, b.time)) <= 60
     AND ST_Distance_Sphere(POINT(a.longitude, a.latitude), POINT(b.longitude, b.latitude)) <= 50000;
    """,
    "25. Regions with highest frequency of deep-focus quakes":"""
    SELECT country, COUNT(*) AS deep_quakes
    FROM quake_data
    WHERE depth_km > 300
    GROUP BY country
    ORDER BY deep_quakes DESC
    LIMIT 10;
    """
}


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.markdown(
    "<h1 style='text-align: center; color: white;'>🌍 Earthquake Data Analysis</h1>",
    unsafe_allow_html=True
)

import streamlit as st

st.markdown(
    "<p style='color:red; font-size:18px;'>Select any problem statement:</p>",
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/030/637/247/large_2x/cracks-road-after-earthquake-damage-free-photo.jpg");
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        background-size: 100% 100%;   /* Stretch to fill without cropping */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Target selectbox label specifically */
    div[data-testid="stSelectbox"] label {
        color: white !important;   /* Change label text color */
        font-size: 26px !important;   /* Adjust font size */
        font-weight: bold !important; /* Make it bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Selectbox with styled label
task = st.selectbox(label="Choose task number", options=list(queries.keys()))



if st.button("Run Query"):
    query = queries[task]
    df = pd.read_sql(query, engine)
    st.markdown(
    f"<h3 style='color: white;'>Results for: {task}</h3>",
    unsafe_allow_html=True
)
    st.dataframe(df, use_container_width=True)

    # Visualization logic for each query
    if task == "1. Top 10 strongest earthquakes":
        st.pyplot(df.plot(kind="bar", x="place", y="mag", color="red", legend=False,
                          title="Top 10 Strongest Earthquakes (Matplotlib)").figure)
        st.plotly_chart(px.bar(df, x="place", y="mag", color="country", title=task), use_container_width=True)

    elif task == "2. Top 10 deepest earthquakes":
        st.pyplot(df.plot(kind="bar", x="place", y="depth_km", color="blue", legend=False,
                          title="Top 10 Deepest Earthquakes (Matplotlib)").figure)
        st.plotly_chart(px.bar(df, x="place", y="depth_km", color="country", title=task), use_container_width=True)

    elif task == "3. Shallow earthquakes < 50 km and mag > 7.5":
        st.plotly_chart(px.scatter(df, x="depth_km", y="mag", color="country", hover_data=["place"], title=task), use_container_width=True)

    elif task == "5. Average magnitude per magnitude type":
        st.plotly_chart(px.bar(df, x="magType", y="avg_mag", color="avg_mag", title=task), use_container_width=True)

    elif task == "6. Year with most earthquakes":
        st.plotly_chart(px.bar(df, x="year", y="quake_count", title=task), use_container_width=True)

    elif task == "7. Month with highest number of earthquakes":
        st.plotly_chart(px.bar(df, x="month", y="quake_count", title=task), use_container_width=True)

    elif task == "8. Day of week with most earthquakes":
        st.plotly_chart(px.bar(df, x="day_of_week", y="quake_count", color="quake_count", title=task), use_container_width=True)

    elif task == "9. Count of earthquakes per hour of day":
        st.plotly_chart(px.line(df, x="hour_of_day", y="quake_count", markers=True, title=task), use_container_width=True)

    elif task == "10. Most active reporting network":
        st.plotly_chart(px.bar(df, x="net", y="quake_count", title=task), use_container_width=True)

    elif task == "11. Reviewed vs automatic earthquakes":
        st.plotly_chart(px.pie(df, names="status", values="count", title=task), use_container_width=True)

    elif task == "12. Count by earthquake type":
        st.plotly_chart(px.pie(df, names="type", values="count", title=task), use_container_width=True)

    elif task == "13. Number of earthquakes by data type":
        st.plotly_chart(px.bar(df, x="types", y="count", title=task), use_container_width=True)

    elif task == "14. Events with high station coverage":
        st.plotly_chart(px.scatter(df, x="nst", y="mag", color="country", hover_data=["place"], title=task), use_container_width=True)

    elif task == "15. Number of tsunamis triggered per year":
        st.plotly_chart(px.line(df, x="year", y="tsunami_count", markers=True, title=task), use_container_width=True)

    elif task == "16. Top 5 countries with highest avg magnitude (past 10 years)":
        st.plotly_chart(px.bar(df, x="country", y="avg_mag", color="avg_mag", title=task), use_container_width=True)

    elif task == "17. Countries with both shallow and deep earthquakes in same month":
        st.plotly_chart(px.scatter(df, x="month", y="year", color="country", title=task), use_container_width=True)

    elif task == "18. Year-over-year growth rate in total earthquakes":
        st.plotly_chart(px.line(df, x="year", y="quake_count", markers=True, title="Yearly Earthquake Counts"), use_container_width=True)
        st.plotly_chart(px.line(df, x="year", y="growth_rate", markers=True, title="Growth Rate (%)"), use_container_width=True)

    elif task == "19. Top 3 seismically active regions":
        st.plotly_chart(px.bar(df, x="country", y="quake_count", color="avg_mag", title=task), use_container_width=True)

    elif task == "20. Avg depth within ±5° latitude of equator":
        st.plotly_chart(px.bar(df, x="country", y="avg_depth", title=task), use_container_width=True)

    elif task == "21. Countries with highest shallow-to-deep ratio":
        st.plotly_chart(px.bar(df, x="country", y="shallow_deep_ratio", title=task), use_container_width=True)

    elif task == "22. Avg magnitude difference between tsunami vs non-tsunami":
        st.write("Magnitude difference:", df["mag_diff"].iloc[0])

    elif task == "23. Events with lowest reliability":
        st.plotly_chart(px.scatter(df, x="gap", y="rms", size="mag", color="country", hover_data=["place"], title=task), use_container_width=True)

    elif task == "24. Consecutive earthquakes within 50 km & 1 hour":
        st.plotly_chart(px.scatter(df, x="time", y="quake1", color="quake2", hover_data=["place"], title=task), use_container_width=True)

    elif task == "25. Regions with highest frequency of deep-focus quakes":
        st.plotly_chart(px.bar(df, x="country", y="deep_quakes", title=task), use_container_width=True)

    else:
        st.info("No visualization defined for this query yet.")


