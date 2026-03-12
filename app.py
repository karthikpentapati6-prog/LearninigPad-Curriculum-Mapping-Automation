import streamlit as st
import pandas as pd
import time
import io

# Page Configuration
st.set_page_config(page_title="Curriculum Mapping Automation", layout="wide")

st.title("📚 Curriculum Mapping Automation")
st.markdown("Automate the mapping of school curricula to the CBSE content library using semantic search on audio scripts.")

# --- Step 1: Upload School Curriculum ---
st.header("Step 1: Upload School Curriculum")
st.write("Upload the school's lesson file. The system will extract topic names and descriptions.")

col1, col2 = st.columns(2)
with col1:
    grade = st.selectbox("Select Grade", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
with col2:
    subject = st.selectbox("Select Subject", ["Science", "Mathematics", "English", "Social Studies", "Hindi"])

# Accept Excel, PDF, Word formats per PRD
uploaded_file = st.file_uploader("Upload Curriculum File", type=["xlsx", "xls", "pdf", "docx", "csv"])

if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    # Mock Topic Extraction
    st.subheader("Review Extracted Topics")
    st.write("Here are the topics extracted from the uploaded document:")
    
    # Dummy data representing extracted topics from the school file
    mock_extracted_topics = pd.DataFrame({
        "School Topic Name": ["Understanding how plants make food", "Basics of Motion", "Advanced Quantum Mechanics"],
        "Description": ["Detailed look at how plants use sunlight.", "Introduction to speed and force.", "Deep dive into quantum states."]
    })
    st.dataframe(mock_extracted_topics, use_container_width=True)
    
    st.divider()

    # --- Step 2: System Searches Content Library ---
    st.header("Step 2: Semantic AI Search")
    st.write("The system will now compare the extracted school topics against our CBSE audio scripts using AI/semantic matching.")
    
    if st.button("Run AI Curriculum Mapping", type="primary"):
        with st.spinner("Searching CBSE content library via audio scripts... understanding meaning, not just keywords..."):
            # Simulating backend API call / Vector DB search time
            time.sleep(3) 
            
        # --- Step 3: View Mapping Results ---
        st.header("Step 3: View Mapping Results")
        
        # Mock Results Data matching PRD columns
        results_data = {
            "School Topic": [
                "Understanding how plants make food", 
                "Basics of Motion", 
                "Advanced Quantum Mechanics"
            ],
            "Mapped CBSE Content Path": [
                "CBSE-Grade 10-Science-Lesson 3-Photosynthesis-ModelA",
                "CBSE-Grade 9-Science-Lesson 8-Newton's Laws-ModelB",
                "NO MATCH FOUND" # Flagging topics where no suitable content is found
            ],
            "Confidence Score": [
                "High (92%)", 
                "Medium (65%)", 
                "Low (12%)"
            ],
            "Audio Script Snippet": [
                "...the exact process of photosynthesis where plants create food using sunlight...",
                "...understanding how objects in motion behave when force is applied...",
                "N/A"
            ]
        }
        
        df_results = pd.DataFrame(results_data)
        
        # Color coding function for Confidence Scores
        def style_confidence(val):
            if "High" in val:
                return 'color: #2e7d32; font-weight: bold' # Green
            elif "Medium" in val:
                return 'color: #f57c00; font-weight: bold' # Orange
            else:
                return 'color: #d32f2f; font-weight: bold' # Red

        # Apply styling
        styled_df = df_results.style.map(style_confidence, subset=['Confidence Score'])
        st.dataframe(styled_df, use_container_width=True)
        
        st.info("💡 **Note:** 'High' indicates a strong match. 'Medium' indicates a partial match. 'Low' indicates a weak match requiring manual review.")

        st.divider()

        # --- Step 4: Export ---
        st.header("Step 4: Export Mapping")
        st.write("Download the final mapping for the Content/Ops team.")
        
        # Convert DataFrame to CSV for download
        csv = df_results.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="⬇️ Download Final Mapping as CSV",
            data=csv,
            file_name=f'curriculum_mapping_{grade}_{subject}.csv',
            mime='text/csv',
        )