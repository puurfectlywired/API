#to communicate with pi over HTTP
from flask import Flask, jsonify
#to communicate with GPIO on pi
from gpiozero import Button, LED

#create the flask app
app = Flask(__name__)

#GPIO pins 18 and 25
button = Button(25)
led = LED(18)

#if there is an HTTP request, run get_status function
@app.route("/status", methods=["GET"]) 

#get_status checks button press/LED status and resturns JSON response
def get_status():

    pressed = button.is_pressed

    if pressed:
        led.on()
    else:
        led.off()
    
    return jsonify({
        "button_pressed": pressed,
        "led_on": pressed
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )