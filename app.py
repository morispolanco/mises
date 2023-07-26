import streamlit as st
import requests

headers = {
    'x-api-key': 'sec_u3PpS7lPyGd7LC0WIMyjZBNqPt4mY1KG',
    "Content-Type": "application/json",
}

def send_message(message):
    data = {
        'sourceId': "cha_MXNXXxxmY5jOvfqXaMNzY",
        'messages': [
            {
                'role': "user",
                'content': message,
            }
        ]
    }

    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['content']
    else:
        return f'Error (Código {response.status_code}): {response.text}'

def main():
    st.title("Obras completas de Mises")


    user_input = st.text_input("Tu pregunta:")

    if st.button("Enviar"):
        st.write("Tú:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
