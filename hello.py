import gradio as gr

state = gr.BrowserState("DEFAULT")

def greet(new_name, name_state):
    name_state = new_name
    return "Hello " + new_name + "!", name_state

def fetch_name(name_state):
    return f"{name_state} AAA", name_state  # return to both name_box and local state

def new_btn_click(name_state):
    print(name_state)

main_js = """
(()=>document.querySelectorAll("div.nav-holder").forEach(el => el.style.display = "none"))()
"""

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")

    new_btn = gr.Button("Print Name")
    new_btn.click(fn=new_btn_click, inputs=state, outputs=None)

    # Fixed: Make sure the state is correctly updated when submitting the name
    name.submit(fn=greet, inputs=[name, state], outputs=[output, state])

    demo.load(fn=None, inputs=None, outputs=None, js=main_js)
    
    # On Greet button click, go to /up
    greet_btn.click(None, None, None, js="() => {window.location.href = '/up'}")

with demo.route("/up") as incrementer_demo:
    # New local state for this route
    name_box = gr.Textbox(label="Shared Name")

    # Load the state value when the page loads
    incrementer_demo.load(fetch_name, inputs=state, outputs=[name_box, state])

    new_btn = gr.Button("Print Name")
    new_btn.click(fn=new_btn_click, inputs=state, outputs=None)

demo.launch()