import streamlit as st

def draw_shape(shape_type, color, size=200):
  """
  Draws a basic shape (square, circle, triangle) with the given color and size in Streamlit.

  Args:
      shape_type: String specifying the shape type ("square", "circle", "triangle").
      color: Hexcode string representing the desired color (e.g., "#FF0000" for red).
      size: Optional integer value for the size of the shape (default 200 pixels).
  """
  if shape_type == "square":
    st.write(f"<div style='background-color:{color};width:{size}px;height:{size}px;'></div>", unsafe_allow_html=True)
  elif shape_type == "circle":
    st.write(f"<div style='background-color:{color};width:{size}px;height:{size}px;border-radius:{size//2}px;'></div>", unsafe_allow_html=True)
  elif shape_type == "triangle":
    half_size = size // 2
    top_corner = f"0,{half_size}"
    left_corner = f"{half_size},0"
    right_corner = f"{size},{half_size}"
    st.write(f"<div style='background-color:{color};width:0;height:0;border-left:{half_size}px solid transparent;border-right:{half_size}px solid transparent;border-bottom:{size}px solid {color};'></div>", unsafe_allow_html=True)
    st.write(f"<div style='position:relative;left:{left_corner};top:{top_corner}'>", unsafe_allow_html=True)
    st.write(f"<div style='position:relative;left:{right_corner};top:{top_corner}'>", unsafe_allow_html=True)
  else:
    st.write("Error: Invalid shape type. Supported options are 'square', 'circle', and 'triangle'.")

def display_legend_item(text, color):
  """
  Displays a legend item with colored shape and text in Streamlit.

  Args:
      text: String representing the text to display.
      color: Hexcode string representing the desired color of the shape.
  """

  html = f'<div style="display:flex; align-item: center;"> \
            <div style="background-color:{color};width:20px;height:20px;margin-right:5px;margin-bottom:5px"></div> \
            <span style="margin-right:5px;border-radius:50%;">{text}</span> \
          </div>'
  
  st.write(html,unsafe_allow_html=True)
  
def colored_square(size=15, color="#FF0000"):
  """
  Function to display a colored square in Streamlit.

  Args:
      size: Optional argument for the size of the square (default 15 pixels).
      color: Hexcode string representing the desired color of the square.
  """
  st.write(f"<div style='background-color:{color};width:{size}px;height:{size}px;margin-right:5px;border-radius:2px;'></div>", unsafe_allow_html=True)





