import streamlit as st 

from pathlib import Path
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from sqlalchemy import create_engine
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

##llm model
from langchain_groq import ChatGroq
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    st.info("Please add the api key")
llm=ChatGroq(groq_api_key=api_key,model_name="openai/gpt-oss-120b",streaming=True)


st.set_page_config(page_title="Langchain:chat wtih sql db")
st.title("Langchain: chat with sql db")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

##RADIO

radio_opt=["use sqlite3 db","connect to your sql db"]


selected_opt=st.sidebar.radio(label="choose the db to work with",options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide MY SQL hostname")
    mysql_user=st.sidebar.text_input("MY SQL User")
    mysql_password=st.sidebar.text_input("MY SQL password",type="password")
    mysql_db=st.sidebar.text_input("MY SQL DB")
    
else:
    db_uri=LOCALDB
    


if not db_uri:
    st.info("Please enter the DB information")
    st.stop()

    


@st.cache_resource(ttl=3600)
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    
    if db_uri==LOCALDB:
        dbfilepath=(Path(__file__).parent/"student.db").absolute()
        print(dbfilepath)
        
        creator=lambda: sqlite3.connect(f"file:{dbfilepath}?mode=rw",uri=True)
        return SQLDatabase(create_engine(f"sqlite://",creator=creator))
        
    
    elif db_uri==MYSQL:
        if not (mysql_db and mysql_host and mysql_user and mysql_password):
            st.error("Please provide all connection details")
            st.stop()
            
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
            
    
if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else :
    db=configure_db(db_uri)



##toolkit

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type="tool-calling"
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"]=[{"role":"assistant","content":"How can i help you?"}]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from the DB")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        streamlitcallback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlitcallback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)