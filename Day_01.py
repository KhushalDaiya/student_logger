import streamlit as st

st.header("We will add their mobile number and email")

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email address")
    phone = st.text_input("Enter your phone number")

    if st.button("Submit"):
        if name and email and phone:
            st.session_state.submitted = True  
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.phone = phone
        else:
            st.warning("Please fill all the fields before submitting.")

else:
    st.success(f"Hello {st.session_state.name}, Welcome to our page!")
    st.write(f"**Email:** {st.session_state.email}")
    st.write(f"**Phone:** {st.session_state.phone}")
    st.info("We sent you an email with login details.")
    
    if st.button("Go Back"):
        st.session_state.submitted = False
