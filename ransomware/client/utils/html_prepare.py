
import os
import webbrowser



def write_message():
    text = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <div class="container">
        <div class="image-container"></div>
        <div class="headlinetext">Gotcha</div>
        <div class="arrow">
            <svg class="arrows">
            <path class="a1" d="M0 0 L30 32 L60 0"></path>
            <path class="a2" d="M0 20 L30 52 L60 20"></path>
            <path class="a3" d="M0 40 L30 72 L60 40"></path>
            </svg>
        </div>
        <div class="instructions">
            <h1>INSTRUCTIONS</h1>
            <ol>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            </ol>
        </div>
        </div>
    </body>
    <style>
        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }
        .container {
        width: 100%;
        min-height: 100vh;
        background-color: black;
        }

        .image-container {
        width: 100%;
        min-height: 60vh;
        height: 70vh;
        background-image: url("./res/depositphotos_117893952-stock-photo-hacker-with-mask.jpg");
        }
        .headlinetext {
        margin-top: 2%;
        font-size: 80px;
        text-align: center;
        color: red;
        }
        .arrow {
        width: 3%;
        height: 70px;
        margin: 0 auto;
        }

        .arrows {
        width: 60px;
        height: 75px;
        position: absolute;
        left: 50%;
        margin-left: -30px;
        bottom: 20px;
        }

        .arrows path {
        stroke: red;
        fill: transparent;
        stroke-width: 4px;
        animation: arrow 2s infinite;
        -webkit-animation: arrow 2s infinite;
        }

        @keyframes arrow {
        0% {
            opacity: 0;
        }
        40% {
            opacity: 1;
        }
        80% {
            opacity: 0;
        }
        100% {
            opacity: 0;
        }
        }

        @-webkit-keyframes arrow /*Safari and Chrome*/ {
        0% {
            opacity: 0;
        }
        40% {
            opacity: 1;
        }
        80% {
            opacity: 0;
        }
        100% {
            opacity: 0;
        }
        }

        .arrows path.a1 {
        animation-delay: -1s;
        -webkit-animation-delay: -1s; /* Safari 和 Chrome */
        }

        .arrows path.a2 {
        animation-delay: -0.5s;
        -webkit-animation-delay: -0.5s; /* Safari 和 Chrome */
        }

        .arrows path.a3 {
        animation-delay: 0s;
        -webkit-animation-delay: 0s; /* Safari 和 Chrome */
        }

        .instructions h1 {
        margin-top: 10%;
        color: green;
        text-align: center;
        font-size: 60px;
        }

        .instructions ol {
        margin-top: 2%;
        padding-bottom: 5%;
        }

        .instructions ol li {
        color: green;
        text-align: center;
        font-size: 32px;
        margin-top: 12px;
        }
    </style>
    </html>


    '''

    file = open("message.html","wb")
    file.write(text.encode())
    file.close()

    webbrowser.open('message.html')