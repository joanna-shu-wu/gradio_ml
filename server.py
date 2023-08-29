import joblib

import gradio as gr
import pandas as pd

price_predictor = joblib.load('models/model-v1.joblib')

carat_input = gr.Number(label="Carat")

shape_input = gr.Dropdown(
    ['Round', 'Princess', 'Emerald', 'Asscher', 'Cushion', 'Radiant', 'Oval', 
     'Pear', 'Marquise'], 
     label="Shape"
)

cut_input = gr.Dropdown(
    ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'], 
    label="Cut"
)

color_input = gr.Dropdown(
    ['D', 'E', 'F', 'G', 'H', 'I', 'J'], 
    label="Color"
)

clarity_input = gr.Dropdown(
    ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], 
    label="Clarity"
)
report_input = gr.Dropdown(['GIA', 'IGI', 'HRD', 'AGS'], label="Report")
type_input = gr.Dropdown(['Natural', 'Lab Grown'], label="Type")

model_output = gr.Label(label="Predicted Price")

def predict_price(carat, shape, cut, color, clarity, report, type):
    sample = {
        'carat': carat,
        'shape': shape,
        'cut': cut,
        'color': color,
        'clarity': clarity,
        'report': report,
        'type': type,
    }
    data_point = pd.DataFrame([sample])
    prediction = price_predictor.predict(data_point).tolist()
    return prediction[0]

demo = gr.Interface(fn=predict_price,
                    inputs=[carat_input, shape_input, cut_input, color_input, 
                            clarity_input, report_input, type_input],
                    outputs=model_output,
                    title="Diamond Price Predictor",
                    description="This API allows you to predict the price of a diamond given its attributes",
                    flagging_options=["Incorrect", "Correct"])

demo.queue(concurrency_count=3)
demo.launch(share=True)