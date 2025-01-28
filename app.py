from dotenv import load_dotenv
import POEM_RAG_GENERATOR.chain as chain
import streamlit as st
from streamlit.components.v1 import html

load_dotenv()

def poem_generator_app():
    """ Enhanced Poem Generator App """
    
    # Custom CSS for styling
    st.markdown("""
    <style>
        .poem-output {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            white-space: pre-wrap;
        }
        .title-text {
            color: #2c3e50;
            font-size: 2.5em !important;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    # App header
    st.markdown('<p class="title-text">📜 AI Poetry Composer</p>', unsafe_allow_html=True)
    
    # Sidebar with instructions
    with st.sidebar:
        st.header("🎯 Instructions")
        st.markdown("""
        1. Enter a topic or theme
        2. Click Generate Poem
        3. Enjoy your custom poem!
        """)
        st.markdown("---")
        st.markdown("**Examples:**")
        st.caption("• Sunset over mountains\n• Childhood memories\n• Ocean waves at night")

    # Main form
    with st.form("poem_form"):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            topic = st.text_input(
                "✨ Poem Theme/Topic",
                placeholder="Enter your inspiration (e.g. 'Autumn leaves dancing in the wind')",
                help="Be as descriptive as you like!"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button(
                "🎵 Generate Poem",
                use_container_width=True
            )

    # Handle form submission
    if submitted:
        if not topic:
            st.error("Please enter a topic to generate a poem!")
            st.balloons()
        else:
            with st.spinner("🎨 Crafting your poetic masterpiece..."):
                try:
                    poem = chain.generate_poem(topic)
                    
                    # Display output
                    st.markdown("---")
                    with st.container():
                        st.subheader(f"📖 Poem about *{topic}*")
                        
                        # Poem display with copy button
                        col_a, col_b = st.columns([4, 1])
                        with col_a:
                            with st.expander("View Poem", expanded=True):
                                st.markdown(f'<div class="poem-output">{poem}</div>', 
                                          unsafe_allow_html=True)
                        with col_b:
                            if st.button("📋 Copy", use_container_width=True):
                                st.session_state.copied = True
                                st.write(poem)  # For copying
                                
                    # Success effects
                    st.success("Poem generated successfully!")
                    st.balloons()

                except Exception as e:
                    st.error(f"Failed to generate poem: {str(e)}")
                    st.info("Please try a different topic or description")

    # Reset button
    if st.button("🧹 Clear & Reset", type="secondary"):
        st.session_state.clear()
        st.rerun()

if __name__ == "__main__":
    poem_generator_app()