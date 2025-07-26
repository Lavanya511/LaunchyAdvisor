import streamlit as st
import json

def render_dict_as_bullets(d: dict):
    for key, value in d.items():
        if isinstance(value, bool):
            val_str = "✅ Yes" if value else "❌ No"   
        elif value == []:
            val_str = "None"
        else:
            val_str = str(value)
        st.markdown(f"- **{key.capitalize()}:** {val_str}")


st.title("LaunchyAdvisor")

with open("responses.json") as f:
    responses = json.load(f)

query_options = [r["query"] for r in responses]
selected_query = st.selectbox("Select a query to explore expert insights:", query_options)

selected_response = next(r for r in responses if r["query"] == selected_query)

st.subheader("📋 Summary")
st.write(selected_response["summary"])

if selected_response.get("budget"):
    st.subheader("💰 Budget Expert")
    render_dict_as_bullets(selected_response["budget"])

if selected_response.get("legal"):
    st.subheader("⚖️ Legal Expert")
    render_dict_as_bullets(selected_response["legal"])

if selected_response.get("marketing"):
    st.subheader("📈 Marketing Expert")
    render_dict_as_bullets(selected_response["marketing"])

st.subheader("🧠 Critic Feedback")
st.write("\n".join(selected_response.get("critic", {}).get("feedback", [])))

