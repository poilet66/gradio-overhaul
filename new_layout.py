import gradio as gr

class GradioController():

    initial_role = "hello"

    def contact_us_page(self):

        def handle_btn_click(new_role):
            print(f"Setting role through contact {new_role}")
            return new_role

        with gr.Blocks() as contact_page:
            gr.Markdown("# Contact Us")
            gr.Markdown("You can contact us here: ")

            textbox = gr.Textbox("Enter new role")
            button = gr.Button("Click me")
            button.click(fn=handle_btn_click, inputs=[textbox], outputs=[self.role_state])

    def info_page(self):
        with gr.Blocks() as info_page:
            gr.Markdown("# Information")
            gr.Markdown("Lorem Ipsum")

    def main_page(self, role_state):
        with gr.Blocks() as main_page:
            @gr.render(inputs=role_state)
            def main_page(role):
                if role == "defuser":
                    gr.Markdown("# Defuser")
                elif role == "expert":
                    gr.Markdown("# Expert")
                else:
                    gr.Markdown(f"# {role}")
                
                textbox = gr.Textbox("Enter role here")
                button = gr.Button("Click me")
                button.click(fn=handle_btn_click, inputs=[textbox], outputs=[role_state])

            def handle_btn_click(role_text):
                print(f'Setting role to {role_text}')
                return role_text
        
    def start_gradio(self):    
        with gr.Blocks() as demo:
            self.role_state = gr.BrowserState(self.initial_role)
            with gr.Tab("Contact Us"):
                self.contact_us_page()
            with gr.Tab("Game Window"):
                self.main_page(self.role_state)
            with gr.Tab("Information"):
                self.info_page()

        return demo

if __name__ == "__main__":
    demo = GradioController().start_gradio()
    demo.launch()