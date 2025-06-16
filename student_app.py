import streamlit as st
import re # Import regex for email and phone number validation

def student_registration_form():
    """
    Creates a Streamlit web application for school student registration.
    """
    st.set_page_config(page_title="Student Registration", layout="centered")

    st.title("🏫 School Student Registration Form")
    st.markdown("---") # A horizontal line for separation

    # Initialize session state for success/error messages
    # This helps messages persist or clear correctly across reruns
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    if 'success_message' not in st.session_state:
        st.session_state.success_message = ""
    if 'error_message' not in st.session_state:
        st.session_state.error_message = ""

    # Using st.form for grouping inputs and handling submission
    # This automatically handles input state management for the form
    with st.form(key='student_reg_form', clear_on_submit=False):
        st.subheader("Student Details")

        # Input for Student Name
        student_name = st.text_input("Full Name of Student", placeholder="e.g., Alice Smith")
        # Input for Student ID
        student_id = st.text_input("Student ID", placeholder="e.g., S2025001")

        # Selectbox for Grade/Class
        grades = ["Select Grade", "Kindergarten", "1st Grade", "2nd Grade", "3rd Grade",
                  "4th Grade", "5th Grade", "6th Grade", "7th Grade", "8th Grade",
                  "9th Grade", "10th Grade", "11th Grade", "12th Grade"]
        grade = st.selectbox("Grade/Class", grades)

        st.subheader("Parent/Guardian Contact Information")

        # Input for Parent/Guardian Email
        parent_email = st.text_input("Parent/Guardian Email", placeholder="e.g., parent@example.com")
        # Input for Emergency Contact Number
        emergency_contact = st.text_input("Emergency Contact Number", placeholder="e.g., 123-456-7890")

        # Submit button for the form
        submit_button = st.form_submit_button(label='Register Student')

        # Logic to execute when the submit button is pressed
        if submit_button:
            # Reset messages
            st.session_state.success_message = ""
            st.session_state.error_message = ""
            st.session_state.form_submitted = True # Indicate form was attempted

            errors = []

            # --- Validation Logic ---
            if not student_name.strip():
                errors.append("Student Name is required.")

            if not student_id.strip():
                errors.append("Student ID is required.")
            elif not re.match(r"^[A-Za-z0-9]+$", student_id.strip()):
                errors.append("Student ID can only contain letters and numbers.")

            if grade == "Select Grade":
                errors.append("Please select a Grade/Class.")

            email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not parent_email.strip():
                errors.append("Parent/Guardian Email is required.")
            elif not re.match(email_regex, parent_email.strip()):
                errors.append("Please enter a valid email address for parent/guardian.")

            # Phone number regex allows digits and optional hyphens, 10 digits total
            phone_regex = r"^\d{3}-?\d{3}-?\d{4}$"
            if not emergency_contact.strip():
                errors.append("Emergency Contact Number is required.")
            elif not re.match(phone_regex, emergency_contact.strip()):
                errors.append("Please enter a valid 10-digit phone number (e.g., 123-456-7890 or 1234567890).")

            if errors:
                st.session_state.error_message = "Please correct the following errors:\n" + "\n".join([f"- {e}" for e in errors])
            else:
                st.session_state.success_message = "Student details submitted successfully!"
                # In a real application, you would process or save this data here
                st.write("---")
                st.subheader("Submitted Data (for demonstration):")
                st.json({
                    "Student Name": student_name,
                    "Student ID": student_id,
                    "Grade": grade,
                    "Parent Email": parent_email,
                    "Emergency Contact": emergency_contact
                })
                # Clear form fields after successful submission (if desired, remove clear_on_submit=False from form)
                # For this example, we keep values for review, but in real app you might want to clear.

    # Display messages after the form, based on session state
    if st.session_state.success_message:
        st.success(st.session_state.success_message)
    if st.session_state.error_message:
        # st.error displays the message with a red background
        st.error(st.session_state.error_message)


# Run the Streamlit application
if __name__ == '__main__':
    student_registration_form()
